# coding=utf-8

import configparser
import os.path
from selenium import webdriver

from codeframework.tools.logger import Logger

# 初始化日志对象logger
logger = Logger("BrowserEngine")
# 获取driver所在路径
driver_path = os.path.abspath(os.path.join(os.path.abspath('.'), '../..')) + '/resources/driver'
# 获取chromeDriver所在路径
chrome_driver_path = os.path.join(driver_path, 'chromedriver.exe')
# 获取ieDriver所在路径
ie_driver_path = os.path.join(driver_path, 'IEDriverServer.exe')
# 获取geckodriver所在路径
firefox_driver_path = os.path.join(driver_path, 'geckodriver.exe')


class BrowserEngine(object):

    def __init__(self):
        # 读取配置文件
        config = configparser.ConfigParser()
        configfile_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath('.'), '../..')), 'resources/config/config.ini')
        config.read(configfile_path, 'utf-8')

        # 获取浏览器类型
        browser = config.get("browserType", "browser")
        logger.info("选择的浏览器是%s." % browser)

        if browser == "Chrome":
            self.driver = webdriver.Chrome(chrome_driver_path)
            logger.info("打开谷歌浏览器")
        elif browser == "IE":
            self.driver = webdriver.Ie(ie_driver_path)
            logger.info("打开火狐浏览器")
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(None, None, 30, None, None, firefox_driver_path)
            logger.info("打开火狐浏览器")

    def get_driver(self):
        return self.driver