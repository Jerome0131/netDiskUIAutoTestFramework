# coding=utf-8

import configparser
import os.path
from resources.config import config
from selenium import webdriver
from codeframework.tools.logger import Logger

# 初始化日志对象logger
logger = Logger("BrowserEngine")

class BrowserEngine(object):

    def __init__(self):
        """
        # 读取配置文件config.ini
        # config = configparser.ConfigParser()
        # configfile_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath('.'), '../..')), 'resources/config/config.ini')
        # config.read(configfile_path, 'utf-8')

        # 获取浏览器类型
        # browser = config.get("browserType", "browser")
        # logger.info("选择的浏览器是%s." % browser)
        """
        browser = config.BROWSER

        if browser == "Chrome":
            self.driver = webdriver.Chrome(config.CHROME_DRIVER_PATH)
            logger.info("打开谷歌浏览器")
        elif browser == "IE":
            self.driver = webdriver.Ie(config.IE_DRIVER_PATH)
            logger.info("打开IE浏览器")
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(None, None, 30, None, None, config.FIREFOX_DRIVER_PATH)
            logger.info("打开火狐浏览器")

    def get_driver(self):
        return self.driver
