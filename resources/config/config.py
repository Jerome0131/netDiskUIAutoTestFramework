# coding=utf-8

import os
import time

# 浏览器类型
# BROWSER = "Firefox"
# BROWSER = "IE"
BROWSER = "Chrome"

# 默认打开的URL
URL = "http://192.168.1.247"
# URL = "http://192.168.1.135"

# 默认隐性等待时间（单位：秒）
IMPLICITLY_WAIT_TIME = 5

# 默认超时时间（单位：秒）
TIMEOUT = 20

# 项目所在路径
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

# 日志文件所在路径
LOGGER_PATH = os.path.join(PROJECT_PATH, "testresult/testlog")

# 取当前时间
NOW = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))

# 截屏文件所在路径
SCREENSHOTS_PATH = os.path.join(PROJECT_PATH, "testresult/screenshots/" + NOW)

# report所在路径
REPORT_PATH = os.path.join(PROJECT_PATH, "testresult/report/" + NOW)

# driver所在路径
DRIVER_PATH = os.path.join(PROJECT_PATH, "resources/driver")

# 上传file所在文件夹路径
FILE_PATH = os.path.join(PROJECT_PATH,"resources/file")

# ee.docx所在路径
XLS_File_PATH = os.path.join(FILE_PATH,'ee.docx')

# chromeDriver所在路径
CHROME_DRIVER_PATH = os.path.join(DRIVER_PATH, 'chromedriver.exe')

# ieDriver所在路径
IE_DRIVER_PATH = os.path.join(DRIVER_PATH, 'IEDriverServer.exe')

# geckodriver所在路径
FIREFOX_DRIVER_PATH = os.path.join(DRIVER_PATH, 'geckodriver.exe')


