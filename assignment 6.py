import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service("D:\\selenium\\chromedriver.exe"))
driver.maximize_window()
driver.get("https://google.com/")
time.sleep(3)

searchBtn = driver.find_element(By.LINK_TEXT, "साइन इन")
webdriver.ActionChains(driver).double_click(searchBtn).perform()

time.sleep(8)
