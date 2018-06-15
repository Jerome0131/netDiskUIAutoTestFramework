# coding:utf-8

from codeframework.tools.startsuit import StartSuit
from resources.config import cases_path_conf


def execute_createfile_suite():
    # 执行新建文件功能测试套件
    StartSuit.execute_funcution_suite(cases_path_conf.Createfile_CASES_PATH, __file__, "新建文件功能测试套件")