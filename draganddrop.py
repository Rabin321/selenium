from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

dragvar = driver.find_element_by_xpath("//div[@id='box4']")
dgvar = driver.find_element_by_xpath("//div[@id='box3']")
dropvar = driver.find_element_by_xpath("//div[@id='box102']")
drpvar = driver.find_element_by_xpath("//div[@id='box103']")
dpvar = driver.find_element_by_xpath("//div[@id='box106']")

action =  ActionChains(driver)
action.drag_and_drop(dragvar, dropvar).perform()
action.drag_and_drop(dragvar, drpvar).perform()
action.drag_and_drop(dgvar, dpvar).perform()