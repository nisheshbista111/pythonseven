import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

    # Navigate to url
driver.get("http://www.google.com")

    # Store 'google search' button web element
gmailLink = driver.find_element(By.LINK_TEXT, "Gmail")

    # Performs mouse move action onto the element
webdriver.ActionChains(driver).move_to_element(gmailLink).perform()

time.sleep(6)
