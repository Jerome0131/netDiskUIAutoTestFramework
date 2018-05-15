# coding=utf-8

import unittest
from codeframework.pageobjects.page_object_tools import page_objects_tools


class TestLoginCase002(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_login_case_3(self):
        try:
            page_objects_tools.login_page_keywords.verify_login_page_elements()
            page_objects_tools.login_page_keywords.input_username_and_password("lhf", "123qwe")
            page_objects_tools.login_page_keywords.click_login_button()
            page_objects_tools.index_page_keywords.verify_index_page_elements()
            page_objects_tools.index_page_keywords.click_user_image()
            page_objects_tools.index_page_keywords.click_logout_button()
            page_objects_tools.login_page_keywords.verify_login_page_elements()
        except AssertionError as e:
            page_objects_tools.login_page_keywords.take_screenshot(__file__)
            raise AssertionError(e)

    def test_login_case_4(self):
        try:
            page_objects_tools.login_page_keywords.verify_login_page_elements()
            page_objects_tools.login_page_keywords.input_username_and_password("lhf", "123qwe")
            page_objects_tools.login_page_keywords.click_login_button()
            page_objects_tools.index_page_keywords.verify_index_page_elements()
            page_objects_tools.index_page_keywords.click_user_image()
            page_objects_tools.index_page_keywords.click_logout_button()
            page_objects_tools.login_page_keywords.verify_login_page_elements()
        except AssertionError as e:
            page_objects_tools.login_page_keywords.take_screenshot(__file__)
            raise AssertionError(e)
