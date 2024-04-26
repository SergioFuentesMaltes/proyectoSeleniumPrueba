from behave import *
from selenium.webdriver.common.by import By
from utils.BrowserSetup import browserSetup


@given(u'I got navigated to the homepage')
def step_impl(context):
    browserSetup(context)


@when(u'I enter valid product name "iPhone" in the search box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='search']/input").send_keys("iPhone")


@when(u'I click on the search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='search']/span/button").click()


@then(u'I should see "iPhone" in the search results')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//a[contains(text(),'iPhone')]").is_displayed()


@when(u'I enter invalid product name "xyz" in the search box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='search']/input").send_keys("xyz")


@then(u'Proper error message should be displayed')
def step_impl(context):
    expected_message = "There is no product that matches the search criteria."
    actual_message = context.driver.find_element(By.XPATH,
                                                 "//p[text()='There is no product that matches the search criteria.']").text
    assert expected_message == actual_message


@when(u'I dont enter any product name in the search box')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='search']/span/button").click()
