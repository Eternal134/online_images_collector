import redis
import pickle
from app_models.model import ObtainResultData, RequestIdItem


class RedisServer:
    
    redisHost = 'redis'
    redisPort = '6379'
    pool = redis.ConnectionPool(host=redisHost, port=redisPort)
    r = redis.Redis(connection_pool=pool)
    
    def __init__(self):
        pass
    
    def get(self, key: str):
        
        try:
            value = self.r.get(key)
        except redis.exceptions.ConnectionError  as e:
            raise Exception("连接到redis服务失败")
        if value is None:
            return None
        else:
            return pickle.loads(value)
    
    def set(self, key: str, value):
        
        value_json = pickle.dumps(value)
        self.r.set(key, value_json)
    
    def mget(self, keys: list):
        values = self.r.mget(keys)
        if values is None:
            return None
        else:
            return [pickle.loads(value) for value in values]
        
    
    def saveItemListToRedis(self, requestId: str, itemList: list):
        """将请求id和此次请求对应的结果保存到redis

        Args:
            requestId (str): 请求id
            itemList (list): 结果列表
        """
        srcList = []
        for item in itemList:
            src = item.src
            srcList.append(src)
            # 保存src-item键值对
            self.set(src, item)
        # 取出原有的
        requestIdItem = self.get(requestId)
        if requestIdItem is None:
            requestIdItem = RequestIdItem()
        # 原有的图片链接列表
        currentSrcs = requestIdItem.srcList
        # 添加现在的
        requestIdItem.srcList = srcList if currentSrcs is None else currentSrcs + srcList
        requestIdItem.srcList = list(set(requestIdItem.srcList))
        # 更新顺序+1，代表此数据有更新
        requestIdItem.updateOrder += 1
        # 保存requestId-srcList键值对
        self.set(requestId, requestIdItem)


    def readItemListFormRedis(self, requestId: str) -> ObtainResultData:
        """根据请求id从redis中读取结果

        Args:
            requestId (str): 前端发来的请求id
        """
        requestIdItem = self.get(requestId)
        if requestIdItem is None:
            return ObtainResultData()
        updateOrder = requestIdItem.updateOrder
        # 先从requestIdItem中取出图片地址src，再拿src作为key查缓存，取出item
        itemList = [self.get(src) for src in requestIdItem.srcList]
        return ObtainResultData(itemList, updateOrder)

if __name__ == "__main__":
    redis = RedisServer()
    redis.set('test', 123)
    print(redis.get('test'))