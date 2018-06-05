# coding=utf-8

from codeframework.pageobjects.loginpage.login_page_keywords import LoginPageKeywords
from codeframework.pageobjects.indexpage.index_page_keywords import IndexPageKeywords
from codeframework.baseoperation.browser_engine import BrowserEngine


class PageHandle(object):
    def __init__(self):
        self.login_page_keywords = LoginPageKeywords(BrowserEngine.get_instance().driver)
        self.index_page_keywords = IndexPageKeywords(BrowserEngine.get_instance().driver)


pagehandle = PageHandle()
