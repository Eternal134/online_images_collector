from concurrent.futures.thread import ThreadPoolExecutor
import threading


class CpuThreadPool:
    """cpu型线程池，运算密集型
    """
    
    executor = ThreadPoolExecutor(1)
    
    @classmethod
    def submitTaskNoneResult(cls, function, *args):
        """提交不需要返回结果的异步任务

        Args:
            function (_type_): 函数名
            args (_type_): 参数
        """
        
        cls.executor.submit(function, *args)