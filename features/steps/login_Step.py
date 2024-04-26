import time

from behave import given, when, then

from pages.Home_Page import HomePage
from pages.Login_Page import LoginPage
from utils.BrowserSetup import browserSetup
from utils.config import email_adress, password


@given(u'I navigated to login page')
def step_impl(context):
    browserSetup(context)
    home_page = HomePage(context.driver)
    home_page.click_my_account_option()
    home_page.click_login_option()



@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.enter_email_address(email_adress)
    login_page.enter_password(password)
    time.sleep(5)

@when(u'I press "Login" button')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_login_button()
    time.sleep(5)

@then(u'I should get logged in successfully')
def step_impl(context):
    print("Inside - I should get logged in successfully")

@when(u'I enter invalid email address and invalid password into the fields')
def step_impl(context):
    print("Inside - I enter invalid email address and invalid password into the fields")

@then(u'I should get an error message')
def step_impl(context):
    print("Inside - I should get an error message")

@when(u'I enter valid email address and invalid password into the fields')
def step_impl(context):
    print("Inside - I enter valid email address and invalid password into the fields")

@when(u'I dont enter anything in the fields')
def step_impl(context):
    print("Inside - I dont enter anything in the fields")
