from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# To click right mouse button we use .context_click.
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
rightbuttonvariable = driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")
actions = ActionChains(driver)

actions.context_click(rightbuttonvariable).perform()

