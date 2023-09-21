import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service("D:\\selenium\\chromedriver.exe"))
driver.maximize_window()
driver.get("https://google.com/")
time.sleep(3)

signIn = driver.find_element(By.LINK_TEXT, "साइन इन")
webdriver.ActionChains(driver).click_and_hold(signIn).perform()

time.sleep(5)
