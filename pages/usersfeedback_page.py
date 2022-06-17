from common.base import Base

class UsersFeedbackPage(Base):

        iframe_loc = ("id","feedback_iframe")
        select_loc = ("name","subject")
        textarea_loc = ("id","mesaage")
        email_loc = ("xpath","//*[@class='form-report']/label[3]/input")
        send_button_loc = ("class name","button")

        def to_iframe(self):
            '''切换到iframe'''
            self.switch_iframe(self.iframe_loc)

        def all_subject(self):
            '''获取所有选项'''
            all = self.select_object(self.select_loc).options #返回List of 元素对象
            all_text = [i.text for i in all]
            return all_text

        def select_subject(self,value=""):
            '''通过vlaue值选中下拉选项'''
            self.select_by_value(self.select_loc,value)

        def select_subject_index(self,index):
            '''通过index选中下拉选项'''
            self.select_by_index(self.select_loc,index)

        def selected_subject(self):
            '''获取被选中的选项'''
            selected = self.select_object(self.select_loc).first_selected_option
            return selected.text

        def input_feedback_textarea(self,text=""):
                '''获取到反馈内容栏'''
                self.send(self.textarea_loc,text)

        def input_feedback_emailarea(self,text=""):
                '''获取到邮箱输入栏'''
                self.send(self.email_loc,text)

        def click_send_button(self):
                '''点击发送按钮'''
                self.click(self.send_button_loc)



