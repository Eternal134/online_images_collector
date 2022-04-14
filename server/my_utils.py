import typing
import json


class DictUtil:
    """字典相关工具
    """
    
    @staticmethod
    def objectToDict(object) -> dict:
        """对象转字典，深层转换

        Args:
            object (_type_): 要转换的对象
        """
        return json.loads(json.dumps(object, default=lambda x: x.__dict__, sort_keys=False))