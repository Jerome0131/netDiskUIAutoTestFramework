# coding:utf-8

from codeframework.testsuits import login_suite
from codeframework.testsuits import createfile_suit
from codeframework.testsuits import upload_suite


if __name__ == "__main__":
    # 执行登录功能测试套件
    # login_suite.execute_login_suite()

    # 执行新建文件功能测试套件
    # createfile_suit.execute_createfile_suite()

    # 执行上传文件功能测试套件
    upload_suite.execute_upload_suite()


