from common.base import Base

class RegisterPage(Base):

    email_loc = ("id","id_email")
    email_loc_div = ("xpath","//*[@id='id_email']/..")
    password_loc = ("id","id_password")
    password_loc_div = ("xpath","//*[@id='id_password']/..")
    btn_loc = ("id","jsEmailRegBtn")

    back_index_loc = ("class name","index-font")
    login_link_loc = ("css selector",".form-p>a")

    success_loc = ("css selector","body>h1")



    def input_email(self, text):
        """输入邮箱"""
        self.send(self.email_loc, text)

    def input_password(self, text):
        """输入密码"""
        self.send(self.password_loc, text)

    def click_register_btn(self):
        """点击注册按钮"""
        self.click(self.btn_loc)

    def register_success_text(self):
        """获取注册成功的文本"""
        return self.get_text(self.success_loc)

    def get_email(self):
        """获取邮箱class属性"""
        return self.get_attribute(self.email_loc_div,"class")

    def get_password(self):
        """获取密码框class属性"""
        return self.get_attribute(self.password_loc_div,"class")

    def clear_email(self):
        """清空邮箱输入框"""
        return self.clear(self.email_loc)

    def clear_password(self):
        """清空密码框"""
        return self.clear(self.password_loc)

    def get_email_loc(self,attr=""):
        """获取邮箱输入框value属性"""
        return self.get_attribute(self.email_loc,attr)

    def get_password_loc(self,attr="type"):
        """获取密码框type属性"""
        return self.get_attribute(self.password_loc,attr)

    def get_link_href(self,xpath_loc):
        """获取a标签的href属性"""
        href_loc = ("xpath", xpath_loc)
        return self.get_attribute(href_loc,"href")



