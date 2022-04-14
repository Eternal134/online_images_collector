from redis_server import RedisServer
from spider import Spider

from response import Response
from thread_pool import CpuThreadPool

# 连接redis
redisServer = RedisServer()
""" 数据在redis保存的方式：
    requestId - {'srcList': srcList, 'updateOrder': 更新顺序计数} : 请求id与图片地址
    src - Item : 图片链接与对应的数据封装
"""

def trigger(url: str, requestId: str, depth: int):
    """第一次请求，将会运行爬虫去网页爬取图片

    Args:
        url (str): 起始地址
        requestId (str): 请求id
    """
    spider = Spider(requestId)
    # 异步启动爬虫程序
    CpuThreadPool.submitTaskNoneResult(spider.crawl, url, depth)
    return Response(requestId)


def obtainResults(requestId: str):
    """获取结果

    Args:
        requestId (str): 请求Id
    """
    response = Response(requestId)
    obtainResultData = redisServer.readItemListFormRedis(requestId)
    response.data = obtainResultData
    return response