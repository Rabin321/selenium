from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
# upload files same as others.
driver.find_element_by_xpath("//input[@id='RESULT_FileUpload-10']").send_keys("F:\sl.png")
