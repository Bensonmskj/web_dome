from common.base import Base

class UsersUserInfo(Base):
    nick_name_loc = ("id","nick_name")
    save_btn_loc = ("id","jsEditUserBtn")
    tips_loc = ("class name","error-tips")
    dialog_loc = ("css selector","#jsSuccessTips>.cont")

    def nick_name_clear(self):
        '''清空输入框'''
        self.clear(self.nick_name_loc)

    def input_nick_name(self,nick_name):
        '''输入昵称'''
        self.send(self.nick_name_loc,nick_name)

    def get_nick_value(self):
        '''获取输入的内容'''
        return self.get_attribute(self.nick_name_loc,"value")

    def save_btn_click(self):
        '''点击保存按钮'''
        self.click(self.save_btn_loc)

    def get_error_tips(self):
        '''获取tips报错信息'''
        return self.get_text(self.tips_loc)

    def get_dialog_text(self):
        '''获取dialog文本信息'''
        return self.get_text(self.dialog_loc)



