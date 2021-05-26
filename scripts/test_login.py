import allure
from selenium import webdriver


class TestLoging:
    def test_login_001(self):
        print(1)
        allure.attach("输入", "123", allure.attachment_type.TEXT)
        assert 1
    def test_login_002(self):
        print(2)
        driver = webdriver.Chrome()
        driver.get('http://baidu.com')
        allure.attach("输入", "123", allure.attachment_type.TEXT)
        # allure.attach("截图", driver.get_screenshot_as_png(), allure.attachment_type.PNG)

        assert 1
    def test_login_003(self):
        print(3)
        assert 1
