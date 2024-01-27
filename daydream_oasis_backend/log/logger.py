# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/3/5 9:54
import datetime
import logging
import os


class MyLogger:

    def __init__(self, log_to_file=False, file_name='后端.log') -> None:

        MyLogger.log_to_file = log_to_file
        # 创建对应的日志文件
        if log_to_file:
            now_date = datetime.datetime.now()
            cur_dir = os.path.abspath(__file__).rsplit(os.sep, 1)[0]
            log_dir = os.path.join(cur_dir, str(now_date.year), str(
                now_date.month), str(now_date.day))
            if not os.path.isdir(log_dir):
                os.makedirs(log_dir)
            MyLogger.log_file = os.path.join(log_dir, file_name)

    @classmethod
    def get_logger(cls, logger_name='logger'):  # 获取日志器
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)  # 级别降到最低，默认所有日志都会输出
        if cls.log_to_file:
            handler = logging.FileHandler(
                filename=cls.log_file, mode='a', encoding='utf-8')
        else:
            handler = logging.StreamHandler()

        # handler.setLevel(logging.INFO)
        formater = logging.Formatter(
            '%(levelname)s:%(name)s:%(asctime)s:%(process)d:%(thread)d:%(pathname)s:%(lineno)d:%(message)s')
        handler.setFormatter(formater)
        logger.addHandler(handler)

        return logger


logger = MyLogger(log_to_file=False, file_name='blog.log').get_logger('0318-SPACE')

if __name__ == '__main__':
    logger = MyLogger(log_to_file=False, file_name='blog.log').get_logger('0318-SPACE')
    logger.info('hello')
