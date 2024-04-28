from selenium.webdriver.common.by import By


class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

    # LOCALIZADORES
    edit_your_account_information_xpath = "//a[contains(text(),'Edit your account information')]"

    # METODOS
    def validate_displayed_edit_your_account_information(self):
        self.driver.find_element(By.XPATH, self.edit_your_account_information_xpath).is_displayed()
        return True
