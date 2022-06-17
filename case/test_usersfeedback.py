from pages.usersfeedback_page import UsersFeedbackPage
import pytest
from time import sleep

class TestUsersFeedBack():

    @pytest.fixture(autouse=True)
    def open_usersfeedbacki(self,usersfeedback:UsersFeedbackPage):
        #打开反馈页面
        usersfeedback.open("/users/feedbackiframe/")
        #切换到ifranme
        usersfeedback.to_iframe()

    def test_select_1(self,usersfeedback:UsersFeedbackPage):
        '''获取下拉框选项： 改进建议 页面布局 提BUG'''
        all = usersfeedback.all_subject()
        print(all)
        assert all == ["改进建议", "页面布局", "提BUG"]

    def test_select_2(self,usersfeedback:UsersFeedbackPage):
        '''通过value值定位 1、选中页面布局 '''
        usersfeedback.select_subject(value="页面布局")
        assert usersfeedback.selected_subject() == "页面布局"

        '''2、选中改进建议'''
        usersfeedback.select_subject(value="改进建议")
        assert usersfeedback.selected_subject() == "改进建议"

        '''3、选中提BUG'''
        usersfeedback.select_subject(value="提BUG")
        assert usersfeedback.selected_subject() == "提BUG"

    def test_select_3(self,usersfeedback:UsersFeedbackPage):
        '''通过下标值定位 index'''
        usersfeedback.select_subject_index(index=0)
        assert usersfeedback.selected_subject() == "改进建议"

    # @pytest.mark.parametrize("test_input,expect",[(0,"改进建议"), (1,"页面布局"), (2,"提BUG"),])
    # def test_select_4(self,usersfeedback:UsersFeedbackPage,test_input,expectation):
    #     usersfeedback.select_subject_index(test_input)
    #     assert usersfeedback.selected_subject() == expectation

    def test_alert_1(self,usersfeedback:UsersFeedbackPage):
        usersfeedback.select_subject(value="改进建议")
        sleep(2)
        usersfeedback.input_feedback_textarea(text="测试")
        sleep(2)
        usersfeedback.input_feedback_emailarea(text="102@qq.com")
        sleep(2)
        usersfeedback.click_send_button()
        #text = usersfeedback.alert_text()
        text = usersfeedback.get_alert_text()
        #usersfeedback.alert_text()
        #print(usersfeedback.alert_text())
        assert text == "提交成功！"

    #字典类型参数
    @pytest.mark.parametrize("test_input,expected",[
                             [{"subject":"改进建议","textarea":"123","emailarea":"123@qq.com"},"提交成功！"],
                             [{"subject": "提BUG", "textarea": "123", "emailarea": "123@qq.com"}, "提交成功！"],
                             [{"subject": "页面布局", "textarea": "123", "emailarea": "123@qq.com"}, "提交成功！"],
                             ])
    def test_alert_2(self,usersfeedback:UsersFeedbackPage,test_input,expected):
        #反馈类型
        usersfeedback.select_subject(value=test_input["subject"])
        #反馈内容
        usersfeedback.input_feedback_textarea(text=test_input["textarea"])
        #邮箱
        usersfeedback.input_feedback_emailarea(text=test_input["emailarea"])
        #点击send按钮
        usersfeedback.click_send_button()
        #实际结果
        text = usersfeedback.get_alert_text()
        #断言
        assert text == expected
















