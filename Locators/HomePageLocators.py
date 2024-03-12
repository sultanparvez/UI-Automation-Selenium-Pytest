from selenium.webdriver.common.by import By

class HomePageLocators:
    title_locator = "title"
    menu_locator = "bm-burger-button"
    logout_button_locator = "a[id*='logout']"

    @classmethod
    def get_title_element(cls, driver):
        return driver.find_element(By.CLASS_NAME, cls.title_locator)

    @classmethod
    def get_menu_element(cls, driver):
        return driver.find_element(By.CLASS_NAME, cls.menu_locator)

    @classmethod
    def get_logout_button_element(cls, driver):
        return driver.find_element(By.CSS_SELECTOR, cls.logout_button_locator)