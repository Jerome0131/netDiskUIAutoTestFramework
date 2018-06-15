# coding=utf-8

import unittest
from codeframework.tools.pagehandle import PageHandle
from time import sleep


class TestLoginCase001(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_login_case_1(self):
        pagehandle = PageHandle()
        try:
            pagehandle.login_page_keywords.verify_login_page_elements()
            pagehandle.login_page_keywords.input_username_and_password("admin", "123qwe")
            pagehandle.login_page_keywords.click_login_button()
            pagehandle.index_page_keywords.verify_index_page_elements()
            pagehandle.index_page_keywords.click_user_image()
            pagehandle.index_page_keywords.click_logout_button()
        except AssertionError as e:
            pagehandle.login_page_keywords.take_screenshot(__file__)
            raise AssertionError(e)


