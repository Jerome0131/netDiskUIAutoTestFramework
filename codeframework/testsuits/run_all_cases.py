# coding:utf-8

from codeframework.tools.startsuit import StartSuit
from resources.config import config

if __name__ == "__main__":
    # 执行测试用例集并生成报告
    StartSuit.init_driver()
    test_suite = StartSuit.get_test_suite(config.CASES_PATH)
    StartSuit.init_report_run(test_suite, __file__, "登录测试")
    StartSuit.quit_browser()

