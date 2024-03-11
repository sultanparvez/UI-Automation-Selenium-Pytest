import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Config.config import TestData


@pytest.fixture(scope="class")
def browser():
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj)
    driver.get(TestData.BASE_URL)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("browser")
class TestLogin:

    def test_login_validation(self, browser):
        login = LoginPage(browser)
        homepage = HomePage(browser)
        login.enter_username(TestData.username)
        login.enter_password(TestData.password)
        login.click_login()
        assert homepage.is_login_successful(), "Login failed"

