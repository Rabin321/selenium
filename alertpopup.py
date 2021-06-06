import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//button[normalize-space()='Click Me']").click()

# only 2 options in alert box. i.e. ok and cancel

time.sleep(1)

# driver.switch_to.alert.accept() # click on ok
driver.switch_to.alert.dismiss() # click on cancel

