import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("D:\\selenium\\chromedriver.exe"))
driver.maximize_window()
driver.get("https://demoblaze.com/")

nav_login = driver.find_element(By.ID, 'login2')
nav_login.click()
driver.implicitly_wait(10)

txtbox_username = driver.find_element(By.ID, 'loginusername')
txtbox_username.send_keys('testmorning')
txtbox_password = driver.find_element(By.ID, 'loginpassword')
txtbox_password.send_keys('test123')
login_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
time.sleep(5)
login_button.click()
time.sleep(5)
