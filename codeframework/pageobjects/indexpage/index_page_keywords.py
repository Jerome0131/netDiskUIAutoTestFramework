# coding=utf-8


from codeframework.baseoperation.base_page import BasePage
from codeframework.pageobjects.indexpage import index_page_text
from codeframework.pageobjects.indexpage import index_page_location


class IndexPageKeywords(BasePage):

    def verify_index_page_elements(self):
        # 验证前台界面文档访问的文本
        self.element_text_should_be(index_page_location.index_div_document_access,
                                    index_page_text.index_document_access_text)

        # 验证前台界面个人文件的文本
        self.element_text_should_be(index_page_location.index_span_person_file,
                                    index_page_text.index_personal_file_text)

        # 验证前台界面群组文件的文本
        self.element_text_should_be(index_page_location.index_span_group_file, index_page_text.index_group_file_text)

        # 验证前台界面协同文件的文本
        self.element_text_should_be(index_page_location.index_span_coop_file, index_page_text.index_coop_file_text)

        # 验证前台界面回收站的文本
        self.element_text_should_be(index_page_location.index_span_recycle, index_page_text.index_recycle_text)

        # 验证前台界面快捷访问的文本
        self.element_text_should_be(index_page_location.index_div_quick_access, index_page_text.index_quick_access_text)

        # 验证前台界面常用文件的文本
        self.element_text_should_be(index_page_location.index_span_recent, index_page_text.index_active_file_text)

        # 验证前台界面我的收藏的文本
        self.element_text_should_be(index_page_location.index_span_favorite, index_page_text.index_my_favorite_text)

        # 验证前台界面我的订阅的文本
        self.element_text_should_be(index_page_location.index_span_subscribe, index_page_text.index_my_subscribe_text)

        # 验证前台界面标签分类的文本
        self.element_text_should_be(index_page_location.index_span_subscribe, index_page_text.index_my_subscribe_text)

        # 验证前台界面共享管理的文本
        self.element_text_should_be(index_page_location.index_div_share_management,
                                    index_page_text.index_share_management_text)

        # 验证前台界面我的分享的文本
        self.element_text_should_be(index_page_location.index_span_link, index_page_text.index_my_share_text)

        # 验证前台界面收到的分享的文本
        self.element_text_should_be(index_page_location.index_span_receive, index_page_text.index_received_share_text)

    def click_user_image(self):
        # 点击前台界面用户头像
        self.click_element(index_page_location.index_img_user_logo)

        self.focus(index_page_location.index_img_user_logo)

        # 等待操作下拉加载出来
        self.wait_until_page_contains_element(index_page_location.index_menu_ul_xmenu)

    def click_logout_button(self):
        # 验证退出按钮的文本
        self.element_text_should_be(index_page_location.index_menu_span_logout, index_page_text.index_logout_text)

        # 点击退出按钮
        self.click_element(index_page_location.index_menu_span_logout)

    def click_admin_button(self):
        # 验证系统管理按钮的文本
        self.element_text_should_be(index_page_location.index_menu_span_admin,index_page_text.index_admin_text)

        # 点击系统管理按钮
        self.click_element(index_page_location.index_menu_span_admin)

    def click_person_file(self):
        # 点击前台界面个人文件
        self.click_element(index_page_location.index_span_person_file)

    def click_newMenu_button(self):
        #等到页面包含新建按钮
        self.wait_until_page_contains_element(index_page_location.index_span_newMenuBtn)
        #点击前台新建按钮
        self.click_element(index_page_location.index_span_newMenuBtn)

    def verify_create_menu(self):
        #验证新建下来菜单新建文件夹按钮的文本
        self.element_text_should_be(index_page_location.index_menu_span_addfolder,index_page_text.index_addfolder_text)

        #验证新建下来菜单新建Word文档按钮的文本
        self.element_text_should_be(index_page_location.index_menu_span_newword,index_page_text.index_newword_text)

        # 验证新建下来菜单新建excle表格按钮的文本
        self.element_text_should_be(index_page_location.index_menu_span_newexcel, index_page_text.index_newexcel_text)

        # 验证新建下来菜单新建ppt演示按钮的文本
        self.element_text_should_be(index_page_location.index_menu_span_newppt, index_page_text.index_newppt_text)

        # 验证新建下来菜单新建Word文档按钮的文本
        self.element_text_should_be(index_page_location.index_menu_span_newtxt, index_page_text.index_newtxt_text)

    def click_addfolder_button(self):
        # 点击新建文件夹按钮
        self.click_element(index_page_location.index_menu_span_addfolder)

    def uploadfile(self,filepath):
        #上传文件，path是文件路径
        self._element_find(index_page_location.index_div_uploadfile).send_keys(filepath)


