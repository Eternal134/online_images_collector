import requests
from lxml import etree
from selenium import webdriver

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

def crawl(url: str, cookies: dict = {}, headers: dict = defaultHeader):
    """爬取网页上的图片链接

    Args:
        url (str): 指定网址
        cookies (dict): cookies
        headers (dict, optional): 请求头设置. Defaults to defaultHeader.

    Returns:
        list: 页面上的所有图片链接
    """
    
    session = requests.Session()
    # 设置请求头
    session.headers = headers
    # 设置cookies
    for key, value in cookies.items():
        session.cookies.set(key, value)
    # response = session.get(url)
    # html = etree.HTML(response.text)
    # originalImageUrls = html.xpath("//img/@src")
    
    browser.get(url)
    elements = browser.find_elements_by_tag_name('img')
    originalImageUrls = []
    for e in elements:
        try:
            originalImageUrls.append(e.get_attribute('src'))
        except:
            print('没有获取到img元素的src属性')
            continue
    processedImageUrls = pipeline(originalImageUrls)
    
    return {'urls': processedImageUrls}


def pipeline(imageUrls: list):
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
    imageUrls = list(set(imageUrls))
    # 新建一个容器用于保存结果
    result = []
    for index, url in enumerate(imageUrls):
        # 如果url不可用，不会添加到结果集中
        if not isAvailable(url):
            continue
            
        # 如果url不是已http开头，则在url前补上http
        if isNeedSuppleHttp(url):
            url = 'http:' + url
            
        result.append(url)
        
    return result


if __name__ == "__main__":
    print("主程序启动")