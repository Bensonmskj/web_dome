import pytest

from pages.users_userinfo_page import UsersUserInfo
from time import sleep
class TestUesrsUserInfo():

    @pytest.fixture(autouse=True)
    def open_userinfo(self,userinfo:UsersUserInfo):
        #打开个人中心页
        userinfo.open("/users/userinfo/")

    def test_userinfo_1(self,userinfo:UsersUserInfo):
        '''个人信息-修改昵称为空，点击保存，提示：请输入昵称！'''
        #先清空输入框
        userinfo.nick_name_clear()
        #输入空的昵称
        userinfo.input_nick_name("")
        sleep(1)
        #点击保存按钮
        userinfo.save_btn_click()
        sleep(1)
        #断言
        actual_result = userinfo.get_error_tips()
        assert actual_result == "请输入昵称！"

    @pytest.mark.parametrize("test_input",["yoyo","哲哲"])
    def test_user_iinfo_2(self,userinfo:UsersUserInfo,test_input):
        '''个人信息-修改昵称为：哲哲，点击保存，提示：个人信息修改成功！'''
        # 先清空输入框
        userinfo.nick_name_clear()
        # 输入昵称
        userinfo.input_nick_name(test_input)
        sleep(1)
        # 点击保存按钮
        userinfo.save_btn_click()
        sleep(1)
        # 断言
        actual_result = userinfo.get_dialog_text()
        assert actual_result == "个人信息修改成功！"
        assert userinfo.get_nick_value() == test_input
