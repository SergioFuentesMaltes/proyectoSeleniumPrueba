import time

from behave import given, when, then

from pages.Home_Page import HomePage
from pages.Login_Page import LoginPage
from pages.MyAccount_Page import MyAccountPage
from utils.BrowserSetup import browserSetup
from utils.config import email_adress, password, invalid_email_adress, invalid_password


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



@when(u'I press "Login" button')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_login_button()



@then(u'I should get logged in successfully')
def step_impl(context):
    my_account_page = MyAccountPage(context.driver)
    assert my_account_page.validate_displayed_edit_your_account_information()


@when(u'I enter invalid email address and invalid password into the fields')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.enter_invalid_email_address(invalid_email_adress)
    login_page.enter_invalid_password(invalid_password)
    login_page.click_login_button()



@then(u'I should get an error message')
def step_impl(context):
    login_page = LoginPage(context.driver)
    assert login_page.validate_displayed_error_credentials_message()


@when(u'I enter valid email address and invalid password into the fields')
def step_impl(context):
    print("Inside - I enter valid email address and invalid password into the fields")


@when(u'I dont enter anything in the fields')
def step_impl(context):
    print("Inside - I dont enter anything in the fields")
