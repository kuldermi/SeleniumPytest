from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@value = 'radio1']").click()
driver.find_element(By.CSS_SELECTOR, "#autocomplete").click()
time.sleep(2)