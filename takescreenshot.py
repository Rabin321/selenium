from selenium import webdriver

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")

# 2 ways to capture screenshot.
# driver.save_screenshot("F:\Projectselenium\ss.png") # save screenshot in this  location. This way acceps all format like .jpg, .png, etc...
driver.get_screenshot_as_file("F:\Projectselenium\ssway2.png") # this accepts only .png format.
