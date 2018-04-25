# coding:utf-8

from codeframework.tools.startsuit import StartSuit
from resources.config import cases_path_conf


def execute_login_suite():
    # 执行登录功能测试套件
    StartSuit.execute_funcution_suite(cases_path_conf.Login_CASES_PATH, __file__, "登录功能测试套件")

