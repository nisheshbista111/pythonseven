import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("D:\\selenium\\chromedriver.exe"))
driver.maximize_window()
driver.get("https://google.com/")
time.sleep(3)

gmailLink = driver.find_element(By.LINK_TEXT, "Gmail")
xOffset = 100
yOffset = 100
webdriver.ActionChains(driver).move_by_offset(xOffset, yOffset).perform()

time.sleep(6)
