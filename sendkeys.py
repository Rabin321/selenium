import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")

driver.get("https://github.com/")
print(driver.title)
time.sleep(2)

driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
driver.find_element_by_css_selector("#login_field").send_keys("username123")
driver.find_element_by_css_selector(("#password")).send_keys("password1234")
driver.find_element_by_css_selector("input[value='Sign in']").click()



time.sleep(5)
print(driver.title)
