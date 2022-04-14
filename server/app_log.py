import logging


class ImgDetectLogger:
    """图片检测日志
    """
    
    # 文件路径
    FILENAME = 'log_file/detect_logger.log'
    # 日期格式
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    
    
    
    @classmethod
    def staticLog(cls, 
                  keywords: str, 
                  total: int, 
                  detected: int, 
                  skipped: int, 
                  failed: int,
                  consuming: float):
        """数据统计日志

        Args:
            keywords (str): 关键描述信息
            total (int): 总数
            detected (int): 检测总数
            skipped (int): 跳过总数
            failed: 失败数
            consuming: 耗时，单位s
        """
        logger = logging.getLogger('ImgDetectLogger')
        logger.setLevel(logging.NOTSET)
        # 设置日志格式
        log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        STATIC_MESSAGE = f" {keywords}: " + \
                f'耗时：{consuming}秒, ' +\
                f'目标总量: {total}, ' +\
                f'成功检测: {detected} | {round(detected/total, 2)*100}%, '+\
                f'无需检测跳过: {skipped} | {round(skipped/total, 2)*100}%, '+\
                f'检测失败: {failed} | {round(failed/total, 2)*100}%, '
        # 设置日志处理方法
        # 输出到文件
        fileHandler = logging.FileHandler(filename=cls.FILENAME, encoding='UTF-8')
        fileHandler.setLevel(logging.INFO)
        fileHandler.setFormatter(log_formatter)
        
        logger.addHandler(fileHandler)
        logger.info(STATIC_MESSAGE)
        # logging.basicConfig(filename=cls.FILENAME, level=logging.INFO, format=LOG_FORMAT, datefmt=cls.DATE_FORMAT, filemode='w')
        # logging.warning(STATIC_MESSAGE)