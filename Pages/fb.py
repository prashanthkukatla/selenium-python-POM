import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

option = Options()
option.add_argument("--disable-notifications")
driver = webdriver.Chrome(options = option)
driver.maximize_window()

driver.get("https://www.facebook.com/")
driver.find_element(By.ID,"email").send_keys("prashanthkukatla20@gmail.com")
driver.find_element(By.ID,"pass").send_keys("pswrd.420")
driver.find_element(By.NAME,"login").click()
driver.find_element(By.XPATH,"//div[@class='x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z'][1]").click()
logout_ele = (By.XPATH,"//div[@class='x1iorvi4 x4uap5 xwib8y2 xkhd6sd']//div[@class='xu06os2 x1ok221b']/span[text()='Log out']")
WebDriverWait(driver,20).until(EC.visibility_of_element_located(logout_ele)).click()
# driver.find_element(By.XPATH,"//div[@class='x1iorvi4 x4uap5 xwib8y2 xkhd6sd']//div[@class='xu06os2 x1ok221b']/span[text()='Log out']").click()
driver.implicitly_wait(2)
print(driver.title)
time.sleep(10)