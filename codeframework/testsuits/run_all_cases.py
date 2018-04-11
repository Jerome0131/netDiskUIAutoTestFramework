# coding:utf-8

import unittest
import time,os,datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from codeframework.tools.html_test_runner import HTMLTestRunner
from codeframework.baseoperation.browser_engine import BrowserEngine
from codeframework.baseoperation.base_page import BasePage
from resources.config import config


def get_all_cases(cases_path):
    testunit = unittest.TestSuite()
    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(cases_path, pattern='test_*.py', top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit



if __name__ == "__main__":
    BrowserEngine.get_instance().driver = BrowserEngine.get_driver()
    # 执行测试用例集并生成报告
    all_cases_name = get_all_cases(config.CASES_PATH)
    #取前面时间加入到测试报告文件名中
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    filename = os.path.join(config.REPORT_PATH, "result" + now + ".html")
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='Report_title', description='Report_description')
    runner.run(all_cases_name)
    BasePage(BrowserEngine.get_instance().driver).quit_browser()

    BrowserEngine.get_instance().driver = BrowserEngine.get_driver()
    BasePage(BrowserEngine.get_instance().driver).open_url()
    BasePage(BrowserEngine.get_instance().driver).quit_browser()

