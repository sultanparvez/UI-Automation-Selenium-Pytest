from selenium.common.exceptions import NoSuchElementException
from Locators.HomePageLocators import HomePageLocators

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def is_login_successful(self):
        try:
            element = HomePageLocators.get_title_element(self.driver)
            if element is None:
                raise NoSuchElementException(f"Login Failed")
            return True
        except NoSuchElementException:
            return False

    def logout(self):
        HomePageLocators.get_menu_element(self.driver).click()
        HomePageLocators.get_logout_button_element(self.driver).click()
