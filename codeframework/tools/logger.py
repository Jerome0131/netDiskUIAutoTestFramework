# coding=utf-8

import logging
import time
import os


class Logger(object):

    def __init__(self, logger_name, c_level=logging.DEBUG, f_level=logging.DEBUG):
        """
        :param logger_name:
        :param c_level:
        :param f_level:
        :return:
        """
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        sh.setLevel(c_level)

        # 设置文件日志
        fh = logging.FileHandler(get_log_name())
        fh.setFormatter(formatter)
        fh.setLevel(f_level)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)


def get_log_name():
        rq = time.strftime('%Y%m%d', time.localtime(time.time()))
        log_path = os.path.abspath(os.path.join(os.getcwd(), '../..')) + '/testresult/testlog/'
        log_name = log_path + rq + '.log'
        if not os.path.exists(log_name):
            f = open(log_name, 'w+')
            f.close()
        return log_name




