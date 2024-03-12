from selenium.webdriver.common.by import By

class LoginPageLocators:
    username_field_locator = "//input[@data-test='username']"
    password_field_locator = "input[data-test=password]"
    login_button_locator = "input[type='submit']"

    @classmethod
    def get_username_field_element(cls, driver):
        return driver.find_element(By.XPATH, cls.username_field_locator)

    @classmethod
    def get_password_field_element(cls, driver):
        return driver.find_element(By.CSS_SELECTOR, cls.password_field_locator)

    @classmethod
    def get_login_button_element(cls, driver):
        return driver.find_element(By.CSS_SELECTOR, cls.login_button_locator)
