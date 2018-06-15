# coding:utf-8

from codeframework.tools.startsuit import StartSuit
from resources.config import cases_path_conf


def execute_upload_suite():
    # 执行新建文件功能测试套件
    StartSuit.execute_funcution_suite(cases_path_conf.UPLOAD_CASES_PATH, __file__, "上传功能测试套件")