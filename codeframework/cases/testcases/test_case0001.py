# coding=utf-8

import unittest
from codeframework.baseoperation.base_page import BasePage
from codeframework.baseoperation.browser_engine import BrowserEngine
from codeframework.pageobjects.loginpage.login_page_keywords import LoginPageKeywords


class TestCase0001(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserEngine().get_driver()
        self._base_page = BasePage(self._driver)
        self._login_page_keywords = LoginPageKeywords(self._base_page)
        self._base_page.open_url()

    def tearDown(self):
        self._base_page.quit_browser()

    def test_login(self):
        self._login_page_keywords.verify_login_page_elements()
        self._login_page_keywords.input_username_and_password("linghuiquan", "lhq123456")
        self._login_page_keywords.click_login_button()

if __name__ == '__main__':
    unittest.main


