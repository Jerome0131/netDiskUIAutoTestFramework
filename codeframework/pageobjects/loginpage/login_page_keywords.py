# coding=utf-8

from codeframework.baseoperation.base_page import BasePage
from resources.config import config
from codeframework.pageobjects.loginpage import login_page_text
from codeframework.pageobjects.loginpage import login_page_location


class LoginPageKeywords(BasePage):
    def verify_login_page_elements(self):
        # 验证登录界面包含企业网盘logo
        self.page_should_contain_element(login_page_location.login_img_logo)
        # 验证登录界面帮助中心的文本
        self.element_text_should_be(login_page_location.login_span_help, login_page_text.login_help_center_text)
        # 验证登录界面当前语种类型的文本
        self.element_text_should_be(login_page_location.login_span_language, login_page_text.login_current_language_text)
        # 验证登录界面欢迎登录的文本
        self.element_text_should_be(login_page_location.login_div_login_title, login_page_text.login_welcome_login_text)
        # 验证登录界面账号框的placeholder属性值
        self.element_attribute_should_be(login_page_location.login_input_username, "placeholder", login_page_text.login_username_placeholder_text)
        # 验证登录界面密码框的placeholder属性值
        self.element_attribute_should_be(login_page_location.login_input_password, "placeholder", login_page_text.login_password_placeholder_text)
        # 验证登录界面中登录按钮的文本
        self.element_text_should_be(login_page_location.login_button_login_btn, login_page_text.login_login_btn_text)
        # 验证登录界面包含下载客户端
        self.page_should_contain_element(login_page_location.login_div_client_title)

    def input_username_and_password(self, username, password):
        # 输入账号
        self.input_text(login_page_location.login_input_username, username)
        # 输入密码
        self.input_text(login_page_location.login_input_password, password)

    def click_login_button(self, implicitly_wait_time=config.IMPLICITLY_WAIT_TIME):
        # 点击登录按钮
        self.click_element(login_page_location.login_button_login_btn)
        # 设置隐式等待时间
        self.set_implicitly_wait_time(implicitly_wait_time)

    def verify_login_failed(self, locker_or_unactiver=True, timeout=config.TIMEOUT):
        # locker_or_unactiver=True表示锁定用户登录
        # locker_or_unactiver=False表示未激活用户登录
        self.wait_until_page_contains_element(login_page_location.login_div_login_error, timeout=timeout)
        if locker_or_unactiver:
            self.element_text_should_be(login_page_location.login_div_login_error, login_page_text.login_error_lock_text)
        else:
            self.element_text_should_be(login_page_location.login_div_login_error, login_page_text.login_error_unactive_text)


