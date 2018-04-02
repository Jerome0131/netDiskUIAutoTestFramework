from codeframework.tools.logger import Logger

logger = Logger(logger="BasePage").getlog()



class BasePage(object):
    """
    定一个基类，所有的页面都需要继承此类，会在此类中，封装selenium很大一部分操作页面操作方法
    注意：
    1.所有页面创建的时候，都需要继承与此类
    2.此类中的driver仅仅是变量，在所有页面创建的时候，需要导入selenium的webdriver，导入后方可使用本类中封装的方法
    3.用以上的方法来确保前后操作driver的一致性（重要！）
    """

    def __init__(self, driver):
        self.driver = driver

    # 退出浏览器操作
    def quit_browser(self):
        self.driver.quit()
        logger.info("浏览器退出成功")

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("当前页前进")

    def back(self):
        self.driver.back()
        logger.info("当前页面后退")