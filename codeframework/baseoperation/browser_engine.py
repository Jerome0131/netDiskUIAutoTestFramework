import configparser
import os.path
from selenium import webdriver

from codeframework.tools.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):
    """
    根据配置文件config.ini中的浏览器类型和url来打开对应的浏览器和地址
    """
    dir = os.path.dirname(os.path.abspath('.'))  # 获取本py项目的相对路径
    chrome_driver_path = dir + '/resources/chromedriver.exe'  # 取得chromedriver的路径
    ie_driver_path = dir + '/resources/iedriver.exe'  # 取得iedriver的路径

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = configparser.ConfigParser()
        configfile_path = os.path.dirname(os.path.abspath('.')) + '/resources/config/config.ini'
        config.read(configfile_path)

        browser = config.get("browserType", "browser")
        logger.info("选择的浏览器是%s." % browser)
        url = config.get("testServer", "URL")
        logger.info("测试地址：%s" % url)

        if browser == "Chrome":
            driver = webdriver.Chrome()
            logger.info("打开谷歌浏览器")
        elif browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("打开火狐浏览器")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("打开火狐浏览器")

        driver.get(url)
        logger.info("打开网址：%s" % url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver


