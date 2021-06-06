import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")  # open website
driver.find_element_by_xpath(
    "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()  # click on button and it redirects to another window/tab

print(driver.current_window_handle)  # parent open window/tab ko value

handlevalues = driver.window_handles  # returns all the values of opened window/tabs.

for handle in handlevalues:
    driver.switch_to.window(handle)
    print(driver.title)
    time.sleep(3)
    if driver.title == "SeleniumHQ Browser Automation":
        driver.find_element_by_link_text("Downloads").click()


# driver.quit()  # closes all browsers window. but.close() closes only selected/specific window
