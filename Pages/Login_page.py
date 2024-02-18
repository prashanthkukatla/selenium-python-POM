import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common import alert



class LoginPage:
	
	def __init__(self,driver):
		
		self.driver = driver
		self.profile_img = "//div[@class='x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z'][1]"
		self.logout_clk = (By.XPATH,"//div[@class='x1iorvi4 x4uap5 xwib8y2 xkhd6sd']//div[@class='xu06os2 x1ok221b']/span[text()='Log out']")
		self.wait =WebDriverWait(self.driver,20)
	
	email_id = "email"
	password_id = "pass"

	def login(self,username,password):
		print(self.driver.title)
		self.driver.find_element(By.ID,self.email_id).send_keys(username)
		self.driver.find_element(By.ID,self.password_id).send_keys(password)
		
	def click(self):
		self.driver.find_element(By.NAME,'login').click()

	def get_text(self):
		titLe= self.driver.title
		print(titLe)
	
	def get(self,url):
		self.driver.get(url)
		
	def logout(self):
		self.driver.find_element(By.XPATH,self.profile_img).click()
		self.wait.until(EC.visibility_of_element_located(self.logout_clk)).click()
		# self.driver.find_element(By.XPATH,self.logout_clk).click()
		self.driver.implicitly_wait(10)
		print(self.driver.title)
		