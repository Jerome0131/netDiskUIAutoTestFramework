# coding=utf-8

from unittest import TestCase
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from codeframework.tools.logger import Logger
from codeframework.baseoperation.element_finder import ElementFinder
from resources.config import config

logger = Logger("BasePage")


class BasePage(object):
    """
    定一个基类，所有的页面都需要继承此类，会在此类中，封装selenium很大一部分操作页面操作方法
    注意：
    1.所有页面创建的时候，都需要继承与此类
    2.此类中的driver仅仅是变量，在所有页面创建的时候，需要先使用browser_engine.py打开页面，之后方可使用本类中封装的方法
    3.用以上的方法来确保前后操作driver的一致性（重要！）
    """

    def __init__(self, driver):
        self.driver = driver
        self._element_finder = ElementFinder()
        self._test_case = TestCase()

    # 查找元素
    def _element_find(self, locator, first_only, required, tag=None):
        if isinstance(locator, str):
            elements = self._element_finder.find(self.driver, locator, tag)
            if required and len(elements) == 0:
                raise ValueError("Element locator '" + locator + "' did not match any elements.")
            if first_only:
                if len(elements) == 0: return None
                return elements[0]
        elif isinstance(locator, WebElement):
            elements = locator
        # do some other stuff here like deal with list of webelements
        # ... or raise locator/element specific error if required
        return elements

    # 获取元素的文本
    def _get_text(self, locator):
        element = self._element_find(locator, True, True)
        if element is not None:
            return element.text
        return None

    # 获取元素的值
    def _get_value(self, locator, tag=None):
        element = self._element_find(locator, True, False, tag)
        return element.get_attribute('value') if element is not None else None

    # 获取元素的属性
    def _get_element_attribute(self, locator, attribute_name, tag=None):
        element = self._element_find(locator, True, False, tag)
        return element.get_attribute(attribute_name)

    # 判断元素是否存在
    def _is_element_present(self, locator, tag=None):
        element = self._element_find(locator, True, False, tag=tag)
        if element is not None:
            return True
        return False

    # 打开url操作
    def open_url(self, url=config.URL, implicitly_wait_time=config.IMPLICITLY_WAIT_TIME):
        self.driver.get(url);
        logger.info("open url '%s'" % url)
        self.driver.maximize_window()
        self.set_implicitly_wait_time(implicitly_wait_time)

    # 设置浏览器隐式等待时间
    def set_implicitly_wait_time(self, implicitly_wait_time=config.IMPLICITLY_WAIT_TIME):
        self.driver.implicitly_wait(implicitly_wait_time)
        logger.info("set implicitly wait time %s" % implicitly_wait_time)

    # 退出浏览器操作
    def quit_browser(self):
        self.driver.quit()
        logger.info("quit browser")

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("forward operation")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("back operation")

    # 校验方法----------------------------------------------------------------------------------------------------------

    # 验证元素包含文本
    def element_should_contain(self, locator, expected, message=''):
        logger.info("Verifying element '%s' contains text '%s'." %(locator, expected))
        actual = self._get_text(locator)
        if not message:
            message = "Element '%s' should have contained text '%s' but its text was '%s'." % (locator, expected, actual)
        self._test_case.assertIn(expected, actual, message)

    # 验证元素不包含文本
    def element_should_not_contain(self, locator, expected, message=''):
        logger.info("Verifying element '%s' does not contain text '%s'." %(locator, expected))
        actual = self._get_text(locator)
        if not message:
            message = "Element '%s' should not contain text '%s' but it did." % (locator, expected)
        self._test_case.assertNotIn(expected, actual, message)

    # 验证元素的文本
    def element_text_should_be(self, locator, expected, message=''):
        logger.info("Verifying element '%s' contains exactly text '%s'." % (locator, expected))
        actual = self._get_text(locator)
        message = "The text of element '%s' should have been '%s' but in fact it was '%s'." % (locator, expected, actual)
        self._test_case.assertEqual(expected, actual, message)

    # 验证元素的属性值
    def element_attribute_should_be(self, locator, attribute_name, expected, tag=None, message=''):
        logger.info("Verifying element '%s' contains exactly attribute text '%s'." % (locator, expected))
        actual = self._get_element_attribute(locator, attribute_name, tag)
        message = "The attribute text of element '%s' should have been '%s' but in fact it was '%s'." % (locator, expected, actual)
        self._test_case.assertEqual(expected, actual, message)

    # 验证页面包含某元素
    def page_should_contain_element(self, locator, tag=None, message=''):
        if not self._is_element_present(locator, tag):
            if not message:
                message = "Page should have contained element '%s' but did not" % locator
            raise AssertionError(message)
        logger.info("Current page contains element '%s'." % locator)

    # 验证页面不包含某元素
    def page_should_not_contain_element(self, locator, tag=None, message=''):
        if self._is_element_present(locator, tag):
            if not message:
                message = "Page should not have contained element '%s'" % locator
            raise AssertionError(message)
        logger.info("Current page does not contain element '%s'." % locator)


    # 点击方法----------------------------------------------------------------------------------------------------------

    # 点击元素
    def click_element(self, locator):
        logger.info("Clicking element '%s'." % locator)
        self._element_find(locator, True, True).click()

    # 点击按钮
    def click_button(self, locator):
        logger.info("Clicking button '%s'." % locator)
        element = self._element_find(locator, True, False, 'input')
        if element is None:
            element = self._element_find(locator, True, True, 'button')
        element.click()

    # 文本输入方法------------------------------------------------------------------------------------------------------

    # 文本框输入
    def input_text(self, locator, text):
        logger.info("Typing text '%s' into text field '%s'" % (text, locator))
        element = self._element_find(locator, True, True)
        element.clear()
        element.send_keys(text)

    # 显式等待方法------------------------------------------------------------------------------------------------------

    # 等待元素加载
    def wait_until_page_contains_element(self, locator, tag=None, error=None, timeout=config.TIMEOUT):
        if not error:
            error = "Element '%s' did not appear in '%s's." % (locator, timeout)
        try:
            WebDriverWait(self.driver, timeout).until(self._is_element_present(locator, tag=tag))
            logger.info("Wait page contains element '%s'." % locator)
        except TimeoutException:
            raise AssertionError(error)

    # 等待元素消失
    def wait_until_page_does_not_contains_element(self, locator, tag=None, error=None, timeout=config.TIMEOUT):
        if not error:
            error = "Element '%s' did not disappear in %s" % (locator, timeout)
        try:
            WebDriverWait(self.driver, timeout).until_not(self._is_element_present(locator, tag=tag))
            logger.info("Wait page does not contains element '%s'" % locator)
        except TimeoutException:
            raise AssertionError(error)


