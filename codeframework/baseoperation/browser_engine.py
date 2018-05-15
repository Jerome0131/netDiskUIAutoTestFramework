# coding=utf-8

from resources.config import config
from selenium import webdriver
from codeframework.tools.logger import Logger

# 初始化日志对象logger
logger = Logger("BrowserEngine")


class BrowserEngine(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):  # 是否存在__instance变量
            cls._instance = super(BrowserEngine, cls).__new__(cls, *args)  # 如果不存在，则新建一个类实例
        return cls._instance

    @classmethod
    def get_instance(cls, *args):
        return cls.__new__(cls, *args)

    @staticmethod
    def get_driver():
        browser = config.BROWSER

        if browser == "Chrome":
            driver = webdriver.Chrome(config.CHROME_DRIVER_PATH)
            logger.info("打开谷歌浏览器")
        elif browser == "IE":
            driver = webdriver.Ie(config.IE_DRIVER_PATH)
            logger.info("打开IE浏览器")
        elif browser == "Firefox":
            driver = webdriver.Firefox(None, None, 30, None, None, config.FIREFOX_DRIVER_PATH)
            logger.info("打开火狐浏览器")

        return driver
