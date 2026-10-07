import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.helpers import login


@pytest.fixture
def driver():
	service = Service(ChromeDriverManager().install())
	browser = webdriver.Chrome(service=service)
	yield browser
	browser.quit()


@pytest.fixture
def logged_in_driver(driver):
	login(driver)
	return driver
