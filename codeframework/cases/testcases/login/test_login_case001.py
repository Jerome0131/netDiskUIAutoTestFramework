# coding=utf-8

import unittest
import time
from codeframework.baseoperation.base_page import BasePage
from codeframework.baseoperation.browser_engine import BrowserEngine
from codeframework.pageobjects.loginpage.login_page_keywords import LoginPageKeywords


class TestLoginCase001(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserEngine().get_driver()
        self._login_page_keywords = LoginPageKeywords(self._driver)
        self._login_page_keywords.open_url()

    def tearDown(self):
        self._login_page_keywords.quit_browser()

    def test_login_case_1(self):
        self._login_page_keywords.verify_login_page_elements()
        self._login_page_keywords.input_username_and_password("test", "123qwe")
        self._login_page_keywords.click_login_button()
        time.sleep(20)
        self._login_page_keywords.verify_login_failed()

    def test_login_case_2(self):
        self._login_page_keywords.verify_login_page_elements()
        self._login_page_keywords.input_username_and_password("test1", "123qwe")
        self._login_page_keywords.click_login_button()
        time.sleep(20)
        self._login_page_keywords.verify_login_failed(False)

if __name__ == '__main__':
    unittest.main


