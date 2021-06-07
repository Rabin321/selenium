import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# We should import ActionChains to use mouse funtion.

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")

driver.find_element_by_id("txtUsername").send_keys("Admin")
time.sleep(2)
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

adminhover = driver.find_element_by_xpath("//b[normalize-space()='Admin']")
usermngthover = driver.find_element_by_xpath("//a[normalize-space()='User Management']")
userhover = driver.find_element_by_id("menu_admin_viewSystemUsers")


actions = ActionChains(driver) #  create an object.

actions.move_to_element(adminhover).click().perform()
print("admin")
actions.move_to_element(usermngthover).click().perform()
print("usermng")
actions.move_to_element(userhover).click().perform()
print("user")
# we should use .perform() in case of mouse functions.