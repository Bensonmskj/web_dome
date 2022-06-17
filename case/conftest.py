import pytest
from selenium import webdriver
from pages.register_page import RegisterPage
from common.connect_mysql import DbConnect,dbinfo
from pages.login_page import LoginPage
from pages.usersfeedback_page import UsersFeedbackPage


@pytest.fixture(scope="session", name="driver")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    url = "http://49.235.92.12:8200"
    return url

@pytest.fixture(scope="session")
def base_url1():
    url1 = "https://test-kc.meishakeji.com"
    return url1

@pytest.fixture(scope="session")
def registerPage(driver,base_url):
    register = RegisterPage(driver, base_url)
    return register

@pytest.fixture(scope="session")
def db():
    '''db实例化'''
    _db = DbConnect(dbinfo,database="online")
    yield _db
    _db.close()

@pytest.fixture(scope="session")
def loginPage(driver,base_url):
    loginPage = LoginPage(driver,base_url)
    return loginPage

@pytest.fixture(scope="session")
def usersfeedback(driver,base_url):
    usersfeedback = UsersFeedbackPage(driver,base_url)
    return usersfeedback

from pages.users_userinfo_page import UsersUserInfo

@pytest.fixture(scope="session")
def logindriver(driver,loginPage,base_url):
    '''用户先登录'''
    loginPage.open("/users/login/")
    loginPage.input_email("102@qq.com")
    loginPage.input_password("123456")
    loginPage.click_btn()
    return driver

@pytest.fixture(scope="session")
def userinfo(logindriver,base_url):
    '''个人信息'''
    userinfo = UsersUserInfo(logindriver,base_url)
    return userinfo

