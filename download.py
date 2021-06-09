from selenium import webdriver
from selenium.webdriver.common.keys import Keys
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf") # disable the pop up while clickig on download. # "text/plain,application/pdf" ==> mime type
fp.set_preference("browser.download.manager.showWhenStarting", True)
fp.set_preference("browser.download.dir", "D:\ new" )
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe", firefox_profile=fp) # , firefox_profile=fp ==> This means fp  will be execute in that whole websites.
driver.get("http://demo.automationtesting.in/FileDownload.html")
# driver.find_element_by_xpath("//a[@type='button']").click()

driver.find_element_by_xpath("//textarea[@id='textbox']").send_keys("Download selinium")
driver.find_element_by_xpath("//button[@id='createTxt']").click() # generate file
driver.find_element_by_xpath("//a[@id='link-to-download']").click() # download