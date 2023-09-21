import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service("D:\\selenium\\chromedriver.exe"))
driver.maximize_window()
driver.get("https://google.com/")
time.sleep(3)
search = driver.find_element(By.NAME, "q")
action = webdriver.ActionChains(driver)
time.sleep(3)
action.move_to_element(search).click().send_keys("send_keys", Keys.ENTER).perform()
time.sleep(3)
