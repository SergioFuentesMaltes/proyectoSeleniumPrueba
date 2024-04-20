from behave import given, when, then
from selenium import webdriver
import time


@given('I have a web browser open')
def step_given_i_have_a_web_browser_open(context):
    context.browser = webdriver.Chrome()

@when('I navigate to "{url}"')
def step_when_i_navigate_to_url(context, url):
    context.browser.get(url)
    time.sleep(3)

@then('The demoqa home page is displayed')
def step_then_the_demoqa_home_page_is_displayed(context):
    assert "DEMOQA" in context.browser.title



