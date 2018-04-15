# coding=utf-8

import os
from resources.config import config

# cases所在路径
CASES_PATH = os.path.join(config.PROJECT_PATH, "codeframework/cases")

# testcases所在路径
TESTCASES_PATH = os.path.join(CASES_PATH, "testcases")

# 登录功能测试用例所在路径
Login_CASES_PATH = os.path.join(TESTCASES_PATH, "login")