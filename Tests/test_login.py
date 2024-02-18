from selenium import webdriver

import pytest

from Config.config import BasicData
from Pages.Login_page import LoginPage
from Tests.BaseTest import BaseTest

class TestLogin(BaseTest):
	
	def test_login(self):
		
		
		loginpage = LoginPage(self.driver)
		loginpage.get(BasicData.URL)
		loginpage.login(BasicData.Username,BasicData.Password)
		
	def test_click(self):
		
		loginpage = LoginPage(self.driver)
		loginpage.click()
		
	def test_get_text(self):
		
		loginpage = LoginPage(self.driver)
		loginpage.get_text()
		
		# assert title == BasicData.Title
	
	def test_logout(self):
		
		logout = LoginPage(self.driver)
		logout.logout()