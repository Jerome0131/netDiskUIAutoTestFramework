# coding=utf-8

import unittest
import time
from codeframework.baseoperation.browser_engine import BrowserEngine
from codeframework.pageobjects.loginpage.login_page_keywords import LoginPageKeywords


class TestLoginCase002(unittest.TestCase):
    def setUp(self):
        self._login_page_keywords = LoginPageKeywords(BrowserEngine.get_instance().driver)

    def tearDown(self):
        pass

    def test_login_case_3(self):
        self._login_page_keywords.verify_login_page_elements()
        self._login_page_keywords.input_username_and_password("test", "123qwe")
        self._login_page_keywords.click_login_button()
        self._login_page_keywords.verify_login_failed(True)

    def test_login_case_4(self):
        self._login_page_keywords.verify_login_page_elements()
        self._login_page_keywords.input_username_and_password("test1", "123qwe")
        self._login_page_keywords.click_login_button()
        self._login_page_keywords.verify_login_failed(False)

if __name__ == '__main__':
    unittest.main


