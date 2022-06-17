from pages.register_page import RegisterPage
import pytest
class TestRegisterPageNew():

    @pytest.fixture(autouse=True)
    def open_register(self,registerPage:RegisterPage):
        '''把打开注册页面写成fixture，并设置autouse=True，让每条用例自动调用'''
        return registerPage.open("/users/register/")

    def test_email_1(self,registerPage:RegisterPage):
        '''注册-输入空的账号和空的密码，点击提交按钮邮箱输入框红色提示（class属性包含errorput）'''
        #打开注册页面
        #registerPage.open("/users/register/")
        registerPage.input_email("")
        registerPage.input_password("")
        registerPage.click_register_btn()
        #实际结果
        actual_result = registerPage.get_email()
        print(actual_result)
        #断言
        assert "errorput" in actual_result

    def test_email_2(self,registerPage):
        '''输入的邮箱格式不对，空的密码，点击提交按钮邮箱输入框红色提示（class属性包含errorput）'''
        # 打开注册页面
        #registerPage.open("/users/register/")
        registerPage.input_email("12345")
        registerPage.input_password("")
        registerPage.click_register_btn()
        # 实际结果
        actual_result = registerPage.get_email()
        print(actual_result)
        # 断言
        assert "errorput" in actual_result

    def test_password_3(self,registerPage):
        '''输入的邮箱格式正确，密码为空，点击提交按钮邮箱输入框红色提示（class属性包含errorput）'''
        # 打开注册页面
        #registerPage.open("/users/register/")
        registerPage.input_email("123456@qq.com")
        registerPage.input_password("")
        registerPage.click_register_btn()
        # 实际结果
        actual_result = registerPage.get_password()
        print(actual_result)
        # 断言
        assert "errorput" in actual_result

    def test_email_4(self,registerPage):
        '''注册-邮箱输入框输入文本：123@qq.com，再清空文本，输入框为空'''
        registerPage.input_email("123@qq.com")
        print("获取到的属性为：",registerPage.get_email_loc(attr="type"))
        assert registerPage.get_email_loc(attr="value") == "123@qq.com"
        registerPage.clear_email()
        print("获取到的数据为：",registerPage.get_email_loc(attr="value"))
        assert registerPage.get_email_loc(attr="value") == ""

    def test_password_5(self,registerPage):
        '''注册-密码框输入文本：123456，显示******'''
        registerPage.input_password("123456")
        #断言输入的密码是否为123456
        assert registerPage.get_password_loc(attr="value") == "123456"
        #断言密码显示是否为******
        assert registerPage.get_password_loc(attr="type") == "password"

    def test_link_6(self,registerPage,base_url):
        '''点击页面回到首页按钮，回到登录页'''
        link = registerPage.get_link_href('//*[@class="index-font"]')
        print(link)
        assert link == base_url + "/"

    def test_link_7(self,registerPage,base_url):
        '''点击logo，回到登录页'''
        link = registerPage.get_link_href('//*[@class="index-logo"]')
        assert link == base_url + "/"

    def test_link_8(self,registerPage,base_url):
        '''点击登录按钮，回到登录页'''
        link = registerPage.get_link_href('//*[@class="fr hd-bar"]/li[2]/a[1]')
        assert link == base_url + "/users/login/"

    def test_link_9(self,registerPage,base_url):
        '''点击立即登录按钮，回到登录页'''
        link = registerPage.get_link_href("//*[text()='[立即登录]']")
        assert link == base_url + "/users/login/"








