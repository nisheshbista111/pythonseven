import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service("D:\\selenium\\chromedriver.exe"))
driver.maximize_window()
driver.get("https://crossbrowsertesting.github.io/drag-and-drop")
time.sleep(5)

sourceEle = driver.find_element(By.ID, "draggable")
targetEle = driver.find_element(By.ID, "droppable")
targetEleXOffset = targetEle.location.get("x")
targetEleYOffset = targetEle.location.get("y")

webdriver.ActionChains(driver).drag_and_drop_by_offset(sourceEle, targetEleXOffset, targetEleYOffset).perform()

time.sleep(8)

