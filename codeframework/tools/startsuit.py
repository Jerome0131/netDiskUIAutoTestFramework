# coding:utf-8
import time
import unittest
import os
from codeframework.baseoperation.base_page import BasePage
from codeframework.baseoperation.browser_engine import BrowserEngine
from codeframework.tools import html_test_runner
from resources.config import config


class StartSuit(object):
    """
    启动类，主要功能：
    1.唯一的创建driver入口
    2.加载所有的casesuit，并生成html的测试报告
    3.退出浏览器的方法，作为测试结束

    testsuits包中所有的测试套件，都需要使用此工具类
    """
    @staticmethod
    def init_driver(url=config.URL, implicitly_wait_time=config.IMPLICITLY_WAIT_TIME):
        # 唯一创建driver入口
        BrowserEngine.get_instance().driver = BrowserEngine.get_driver()
        BasePage(BrowserEngine.get_instance().driver).open_url(url=config.URL, implicitly_wait_time=config.IMPLICITLY_WAIT_TIME)

    @staticmethod
    def get_test_suite(cases_path, pattern='test_*.py', top_level_dir=None):
        test_suite = unittest.TestSuite()
        # discover 方法定义
        discover = unittest.defaultTestLoader.discover(cases_path, pattern, top_level_dir)
        # discover 方法筛选出来的用例，循环添加到测试套件中
        for test_cases in discover:
            for test_case in test_cases:
                test_suite.addTests(test_case)
                print(test_case)
        return test_suite

    @staticmethod
    def init_report_run(test_suite, current_file_path, report_title="", report_description=""):
        # 如果report目录不存在，则创建一个
        if not os.path.exists(config.REPORT_PATH):
            os.makedirs(config.REPORT_PATH)

        filename = os.path.join(config.REPORT_PATH, os.path.basename(os.path.splitext(os.path.realpath(current_file_path))[0]) + ".html")
        fp = open(filename, 'wb')
        runner = html_test_runner.HTMLTestRunner(stream=fp, title=report_title, description=report_description)
        runner.run(test_suite)
        fp.close()

    @staticmethod
    def quit_browser():
        BasePage(BrowserEngine.get_instance().driver).quit_browser()
