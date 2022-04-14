class Item:
    
    """爬取图片数据封装
    """
    def __init__(self, src: str="", alt: str="") -> None:
        
        self.src = src
        self.alt = alt
        # 图片中包含的目标集合
        self.goals = []
        # 是否已经进行过处理
        self.isHandled = False
        
        
class RequestIdItem:
    """ 缓存中requestId键对应的值模型 """
    def __init__(self, srcList: list=[], updateOrder: int=0) -> None:
        self.srcList = srcList
        self.updateOrder = updateOrder
        
        
class ObtainResultData:
    """ 获取结果接口数据模型 """
    def __init__(self, itemList: list=[], updateOrder: int=0) -> None:
        self.itemList = itemList
        self.updateOrder = updateOrder