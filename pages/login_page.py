from common.base import Base

class LoginPage(Base):
    email_loc = ("id","username")
    password_loc = ("id","password_l")
    click_loc = ("id","jsLoginBtn")

    errorliest = ("class name","errorlist")
    login_tips = ("id","jsLoginTips")

    def input_email(self,username):
        '''输入用户名'''
        self.send(self.email_loc,username)

    def input_password(self,password):
        '''输入密码'''
        self.send(self.password_loc,password)

    def click_btn(self):
        '''点击登录'''
        self.click(self.click_loc)

    def get_errorlist(self):
        '''获取errorlist文本'''
        return self.get_text(self.errorliest)

    def get_login_tips(self):
        '''获取登录失败的提示语'''
        tips = self.get_text(self.errorliest)
        if not tips:
            tips = self.get_text(self.login_tips)
        return tips

    def get_login_url(self):
        '''获取登录后的页面url'''
        return self.driver.current_url

