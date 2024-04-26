from selenium import webdriver


def browserSetup(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")
