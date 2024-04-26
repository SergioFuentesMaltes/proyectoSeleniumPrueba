import self
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # LOCALIZADORES

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_xpath = "//a[contains(text(),'Login')]"

    # METODOS
    def click_my_account_option(self):
        self.driver.find_element(By.XPATH, self.my_account_option_xpath).click()

    def click_login_option(self):
        self.driver.find_element(By.XPATH, self.login_option_xpath).click()
