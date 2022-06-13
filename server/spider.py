import time
import torch
from selenium import webdriver
from app_log import ImgDetectLogger
from app_models.model import Item
from redis_server import RedisServer
from thread_pool import CpuThreadPool


""" 设置webdriver启动参数 """
options = webdriver.ChromeOptions()
# 不加载图片, 提升速度
# options.add_argument('blink-settings=imagesEnabled=false')
# 不打开ui
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# 启动webdriver
browser = webdriver.Chrome(chrome_options=options)

# 本地加载yolov5模型
model = torch.hub.load('yolov5', 'yolov5s', source='local')

redisServer = RedisServer()

class Spider:
    
    
    def __init__(self, requestId):
        # 请求id
        self.requestId = requestId
        # 已爬取的网址集合
        self.crawledUrlSet = set()
        # 爬取网址最大数量预设
        self.crawledUrlMax = 30
        # 爬取的图片链接数量
        self.crawledImageSrcCount = 0
        # 最大图片链接量
        self.crawledImageSrcCountMax = 5000
        
    def handleImages(self):
        
        
        """对图片进行后续处理，只会对没有处理结果的图片进行处理

        Args:
            requestId (str): 前端发来的请求id
        """
        # 起始计时
        time1 = time.time()
        
        detected = 0
        skipped = 0
        failed = 0
        
        print('图片处理开始，requestId=' + self.requestId)
        
        requestIdItem = redisServer.get(self.requestId)
        if requestIdItem is None:
            return
        srcs = requestIdItem.srcList
        total = len(srcs)
        if not srcs or len(srcs) == 0:
            return
        items = redisServer.mget(srcs)
        if items is None:
            return
        for item in items:
            # 如果目标还没有进行过处理
            if item and not item.isHandled:
                try:
                    # 进行目标检测
                    yoloResults = model(item.src)
                    # 保存检测结果
                    item.goals = list(set(yoloResults.pandas().xyxy[0]['name']))
                    detected += 1
                except:
                    print("yolov5检测出错，src=" + item.src)
                    failed += 1
                # 标记处理过
                item.isHandled = True
            # 如果处理过，计数
            else:
                skipped += 1
            # 保存处理结果
            redisServer.saveItemListToRedis(self.requestId, [item])
            print(f'requestId={self.requestId} 检测进度：已处理：{detected} 总量：{total}')
        LOG_MSG = f'requestId={self.requestId}'
        # 耗时
        consuming = round(time.time() - time1, 2)
        ImgDetectLogger.staticLog(keywords=LOG_MSG, total=total, detected=detected, skipped=skipped, failed=failed, consuming=consuming)
        print("图片后续处理完成")
        
    
    def crawl(self, url: str, depth: int=0, nextPageLinkText: str=''):
        """爬取网页上的图片链接

        Args:
            url (str): 指定网址
            requestId (str): 请求id
            depth(int): 深度（递归次数）

        Returns:
            list: 页面上的所有图片链接
        """
        
        print('crawl启动')
        # 不能同时指定nextPageLinkText和depthc参数
        if nextPageLinkText!='':
            depth = 0
        
        # 递归终止条件
        if depth < 0 or \
            len(self.crawledUrlSet) >= self.crawledUrlMax or \
                self.crawledImageSrcCount >= self.crawledImageSrcCountMax:
            return
        
        try:
            browser.get(url)
            self.crawledUrlSet.add(url)
        except:
            raise Exception("请输入正确的链接")
        
        while True:
            elements = browser.find_elements_by_tag_name('img')[:(self.crawledImageSrcCountMax-self.crawledImageSrcCount)]
            for e in elements:
                try:
                    imgSrc = e.get_attribute('src')
                    alt = e.get_attribute('alt')
                    try:
                        linkUrl = browser.find_element_by_xpath(f"//*[@alt='{alt}']/ancestor::a").get_attribute('href')
                    except:
                        linkUrl = '' 
                    newItem = Item(imgSrc, alt=alt, webUrl=url, linkUrl=linkUrl)
                    processedItem = self.pipeline([newItem])
                    redisServer.saveItemListToRedis(self.requestId, processedItem)
                    self.crawledImageSrcCount += 1
                except Exception as e:
                    print(str(e))
                    continue
                
            # 开启多线程进行图片处理
            CpuThreadPool.submitTaskNoneResult(self.handleImages)
            
            # 翻页
            if len(nextPageLinkText.strip()) == 0:
                break
            try:
                nextPageButton = browser.find_element_by_link_text(nextPageLinkText)
                if not nextPageButton:
                    break
                else:
                    nextPageButton.click()
            except Exception as e:
                break
        print("图片爬取完成")
        
        if depth == 0:
            return
        # 获取网页上的链接数量
        aTagNum = len(browser.find_elements_by_tag_name('a'))
        for i in range(aTagNum):
            # 由于页面上的链接内容会随刷新而改变，无法固定循环，只能每次重新获取页面上的所有链接
            tags = browser.find_elements_by_tag_name('a')
            _url = tags[i].get_attribute('href')
            # 如果此地址还没有爬过才会去爬
            if _url not in self.crawledUrlSet:
                self.crawl(_url, depth-1)
                
    def pipeline(self, imageItems: list) -> list:
        """管道处理程序，对结果进行处理

        Args:
            imageUrls (list): 爬取的图片链接结果
        """
        def isNeedSuppleHttp(url: str):
            """url字符串是否需要补充http开头

            Args:
                url (str): 需要判断的地址
            """
            if url.startswith('http'):
                return False
            if url.startswith('//'):
                return True
            return False
        
        def isAvailable(url: str):
            """判断url是否可用

            Args:
                url (str): 需要判断的地址
            """
            if url.strip():
                return True
            return False
        
        # 使用set去重
        imageItems = list(set(imageItems))
        # 新建一个容器用于保存结果
        result = []
        for item in imageItems:
            url = item.src
            # 如果url为none，不会添加到结果集中
            if not url:
                continue
            # 如果url不可用，不会添加到结果集中
            if not isAvailable(url):
                continue
                
            # 如果url不是以http开头，则在url前补上http
            if isNeedSuppleHttp(url):
                url = 'http:' + url
                
            result.append(item)
            
        return result