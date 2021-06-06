from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()
 # scroll garney 3 methods
 # 1. Scroll down by pixels.
# driver.execute_script("window.scrollBy(0,2000)", "")

# 2. Scroll down till the element is visible
# nepalflag = driver.find_element_by_xpath("//img[@alt='Flag of Nepal']")
# driver.execute_script("arguments[0].scrollIntoView();", nepalflag)

# 3. Scroll down page till end

driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")