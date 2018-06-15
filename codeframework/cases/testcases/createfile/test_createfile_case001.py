# coding=utf-8

import unittest
from codeframework.tools.pagehandle import pagehandle
from time import sleep

class TestCreatefileCase001(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_createfile_case_1(self):
        try:
            pagehandle.login_page_keywords.input_username_and_password("貔貅1", "123qwe")
            pagehandle.login_page_keywords.click_login_button()
            pagehandle.index_page_keywords.verify_index_page_elements()
            # pagehandle.index_page_keywords.click_person_file()
            pagehandle.index_page_keywords.click_newMenu_button()
            pagehandle.index_page_keywords.verify_create_menu()
            pagehandle.index_page_keywords.click_addfolder_button()
            sleep(20)
        except AssertionError as e:
            pagehandle.login_page_keywords.take_screenshot(__file__)
            raise AssertionError(e)
