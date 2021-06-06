from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")

link = driver.find_elements(By.TAG_NAME, "a") # this type is used for multiple values.
# link = driver.find_element_by_tag_name("a") # yo garna mildain yo case ma coz we have to show no of links that may be many links.

print("No of links present:", len(link))
#capture all the links.
for list in link:
    print(list.text)

#clicking link Everything is case sensetive in selenium or any web developing or anything.....
# 1. link text
driver.find_element_by_link_text("REGISTER").click()

# 2. partial link text (Partial link text ma link text ko certain character matra vaye pani hunxa)
# driver.find_element_by_partial_link_text("REG").click()
