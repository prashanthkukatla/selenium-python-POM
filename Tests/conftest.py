import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope = "class")
def init_driver(request):

	option = Options()
	option.add_argument("--disable-notifications")
	web_driver = webdriver.Chrome(options = option)
	web_driver.maximize_window()
	request.cls.driver = web_driver

	yield
	web_driver.quit()