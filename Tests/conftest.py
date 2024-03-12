import pytest
from selenium import webdriver
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+ '/../' )
from TestData.TestData import TestData
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session",autouse=True)
def browser():
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj)
    driver.get(TestData.BASE_URL)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()