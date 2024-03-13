from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CommonFunctions:
    def __init__(self, driver):
        self.driver = driver
        self.original_window = None

    def window_switching(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != self.original_window:
                self.driver.switch_to.window(window_handle)

    def switch_to_original_window(self):
        if self.original_window:
            self.driver.switch_to.window(self.original_window)
        else:
            raise ValueError("Original window handle is not set.")

    def switch_to_iframe(self, iframe_element):
        self.driver.switch_to.frame(iframe_element)

    def switch_to_default_content(self):
        self.switch_to_default_content(self.driver)