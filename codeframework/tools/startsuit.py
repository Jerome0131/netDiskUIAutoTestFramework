# coding:utf-8
import time

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
    def init_driver():
        # 唯一创建driver入口
        BrowserEngine.get_instance().driver = BrowserEngine.get_driver()
        BasePage(BrowserEngine.get_instance().driver).open_url()

    @staticmethod
    def init_report_run(casesuit):
        # 取前面时间加入到测试报告文件名中
        now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))

        # 如果report目录不存在，则创建一个
        if not os.path.exists(config.REPORT_PATH):
            os.makedirs(config.REPORT_PATH)

        filename = os.path.join(config.REPORT_PATH, "result" + now + ".html")
        fp = open(filename, 'wb')
        runner = html_test_runner.HTMLTestRunner(stream=fp, title='登录测试', description='测一下会崩溃')
        runner.run(casesuit)
        fp.close()

    @staticmethod
    def quit_browser():
        BasePage(BrowserEngine.get_instance().driver).quit_browser()
