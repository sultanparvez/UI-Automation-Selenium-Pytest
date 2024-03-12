import pytest
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from TestData.TestData import TestData

@pytest.mark.usefixtures()
class TestLogin:

    @pytest.mark.parametrize("username, password", [
        (TestData.username, TestData.password),
        (TestData.username2, TestData.password)
    ])
    def test_login_validation(self, browser, username,password) :
        login_page = LoginPage(browser)
        homepage = HomePage(browser)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        assert homepage.is_login_successful(), "Login failed"
        homepage.logout()


