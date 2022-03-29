import shortuuid
from selenium import webdriver

from response import Response

print("spdier文件被加载了")

defaultHeader = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

""" 设置webdriver启动参数 """
options = webdriver.ChromeOptions()
# 不加载图片, 提升速度
options.add_argument('blink-settings=imagesEnabled=false')
# 不打开ui
options.add_argument('--headless')

# 启动webdriver
browser = webdriver.Chrome(chrome_options=options)

class Item:
    
    def __init__(self, src: str="", alt: str="") -> None:
        self.id = shortuuid.uuid()
        self.src = src
        self.alt = alt
        

def crawl(url: str, cookies: dict = {}, headers: dict = defaultHeader):
    """爬取网页上的图片链接

    Args:
        url (str): 指定网址
        cookies (dict): cookies
        headers (dict, optional): 请求头设置. Defaults to defaultHeader.

    Returns:
        list: 页面上的所有图片链接
    """
    
    response = Response()
    
    try:
        browser.get(url)
    except:
        response.code = -1
        response.msg = "请输入正确的链接"
    elements = browser.find_elements_by_tag_name('img')
    originalItems = []
    for e in elements:
        try:
            newItem = Item(e.get_attribute('src'), e.get_attribute('alt'))
            originalItems.append(newItem)
        except:
            print('没有获取到img元素的src属性')
            continue
    processedItems = pipeline(originalItems)
    
    itemsDict = [item.__dict__ for item in processedItems]
    
    response.data = itemsDict
    return response.__dict__


def pipeline(imageItems: list) -> list:
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
            
        # 如果url不是已http开头，则在url前补上http
        if isNeedSuppleHttp(url):
            url = 'http:' + url
            
        result.append(item)
        
    return result


if __name__ == "__main__":
    print("主程序启动")