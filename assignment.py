import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service("D:\\selenium\\chromedriver.exe"))
driver.maximize_window()
driver.get("https://google.com/")
time.sleep(3)
textarea = driver.find_element(By.NAME, 'q')
textarea.send_keys('webdriver')
textarea.send_keys(Keys.ENTER)
time.sleep(8)

webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()

time.sleep(8)
