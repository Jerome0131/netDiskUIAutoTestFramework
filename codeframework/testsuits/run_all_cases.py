# coding:utf-8

import unittest

from codeframework.tools.startsuit import StartSuit
from resources.config import config


def get_all_cases(cases_path):
    testunit = unittest.TestSuite()
    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(cases_path, pattern='test_*.py', top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


if __name__ == "__main__":
    # 执行测试用例集并生成报告
    all_cases_name = get_all_cases(config.CASES_PATH)
    testrunner = StartSuit()
    testrunner.init_driver()
    testrunner.init_report_run(all_cases_name)
    testrunner.quit_browser()
