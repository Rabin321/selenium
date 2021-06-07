from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# double click garna lai .double_click use garney.

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()
driver.find_element_by_xpath("//input[@id='field1']").clear() # .clear() clears the default written text/value.
driver.find_element_by_xpath("//input[@id='field1']").send_keys("kllf")

clickvariable = driver.find_element_by_xpath("//button[normalize-space()='Copy Text']")
actions = ActionChains(driver)

actions.double_click(clickvariable).perform()