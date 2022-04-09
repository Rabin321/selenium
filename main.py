import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")

for i in range (100):
  driver.get("https://github.com/Rabin321")
  print(driver.title)
  driver.get("https://github.com/Rabin321")


