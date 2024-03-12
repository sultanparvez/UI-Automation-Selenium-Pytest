from Locators.LoginPageLocators import LoginPageLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        LoginPageLocators.get_username_field_element(self.driver).clear()
        LoginPageLocators.get_username_field_element(self.driver).send_keys(username)

    def enter_password(self, password):
        LoginPageLocators.get_password_field_element(self.driver).send_keys(password)

    def click_login(self):
        LoginPageLocators.get_login_button_element(self.driver).click()
