from pages.login_page import LoginPage
from time import sleep
import pytest

class TestLogin():
    @pytest.fixture(autouse=True)
    def open_login(self,loginPage:LoginPage):
        return loginPage.open("/users/login/")

    def test_login_success1(self,loginPage):
        '''输入正确用户名，正确密码，点击登录,登录成功'''
        loginPage.input_email("102@qq.com")
        sleep(2)
        loginPage.input_password("123456")
        sleep(2)
        loginPage.click_btn()
        #actual_result = loginPage.get_errorlist()
        actual_result = loginPage.get_login_tips()
        assert actual_result ==''

    def test_login_failed1(self,loginPage):
        '''输入空用户名，空密码，点击登录'''
        loginPage.input_email("")
        sleep(2)
        loginPage.input_password("")
        sleep(2)
        loginPage.click_btn()
        #actual_result = loginPage.get_errorlist()
        actual_result = loginPage.get_login_tips()
        print(actual_result)
        assert actual_result == '这个字段是必须的'

    def test_login_failed2(self,loginPage):
        '''输入错误用户名，正确密码，点击登录，预期： 用户名或密码错误'''
        loginPage.input_email("123")
        loginPage.input_password("123456")
        loginPage.click_btn()
        actual_result = loginPage.get_login_tips()
        assert actual_result == '用户名或密码错误'

    def test_login_failed3(self,loginPage):
        '''输入正确用户名，密码数小于6，点击登录，预期：确保该变量至少包含 6 字符(目前字符数 5)。'''
        loginPage.input_email("102@qq.com")
        loginPage.input_password("12345")
        loginPage.click_btn()
        actual_result = loginPage.get_errorlist()
        assert actual_result == '确保该变量至少包含 6 字符(目前字符数 5)。'

    def test_login_success2(self, loginPage):
        '''输入正确用户名，正确密码，点击登录,登录成功'''
        loginPage.input_email("102@qq.com")
        sleep(2)
        loginPage.input_password("123456")
        sleep(2)
        loginPage.click_btn()
        actual_result = loginPage.get_login_tips()
        assert actual_result != '用户名或密码错误'

    def test_login_success3(self,loginPage,base_url):
        '''输入正确用户名，正确密码，点击登录，根据页面url断言'''
        loginPage.input_email("102@qq.com")
        sleep(2)
        loginPage.input_password("123456")
        sleep(2)
        loginPage.click_btn()
        actual_result = loginPage.get_login_url()
        print(actual_result)
        assert actual_result == base_url + '/'

