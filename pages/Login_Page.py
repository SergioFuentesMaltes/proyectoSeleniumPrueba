from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.BrowserSetup import browserSetup
from utils.config import email_adress



class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # LOCALIZADORES
    email_address_textbox_xpath = "//input[@id='input-email']"
    password_textbox_xpath = "//input[@id='input-password']"
    login_button_xpath = "//input[@class='btn btn-primary']"
    new_costumer_continue_button_xpath = "//a[contains(text(),'Continue')]"
    error_credentials_message_xpath = "//div[text()='Warning: No match for E-Mail Address and/or Password.']"

    # METODOS
    def enter_email_address(self, email_adress):
        self.driver.find_element(By.XPATH, self.email_address_textbox_xpath).send_keys(email_adress)

    def enter_invalid_email_address(self, invalid_email_adress):
        self.driver.find_element(By.XPATH, self.email_address_textbox_xpath).send_keys(invalid_email_adress)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def enter_invalid_password(self, invalid_password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(invalid_password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def validate_displayed_error_credentials_message(self):
        self.driver.find_element(By.XPATH, self.error_credentials_message_xpath).is_displayed()
        return True
