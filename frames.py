import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
# We cannot directly select the required elements if the frames are present.
# first select the frame and select the reqd elements inside that frame.
driver.switch_to.frame("packageListFrame") # first select the frame and then downward... perform actions.
time.sleep(3)
driver.find_element_by_link_text("org.openqa.selenium").click() # select elements of first frame

# now we are at first frame . To switch to second or other frame, first we need to go back to main page
time.sleep(3)
driver.switch_to.default_content()  # switch back to first frame
time.sleep(3)
driver.switch_to.frame("classFrame") # select second frame
time.sleep(2)
driver.find_element_by_link_text("org.openqa.selenium.grid.distributor.config").click() # select elements of second frame.

