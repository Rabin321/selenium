from selenium import webdriver

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")

driver.get("https://www.ambition.edu.np/")
# capture all the cookies created by browser
capcookies = driver.get_cookies()
print(capcookies)
print(len(capcookies))

# adding new cookies to the browser.

addcookies = {'name': 'MyOwncookie', 'value': '0987654'}
driver.add_cookie(addcookies) # adding cookie

# Again capturing cookie after adding new cookie.
capcookies = driver.get_cookies()
print(capcookies)
print(len(capcookies))

#Deleting cookie
driver.delete_cookie('MyOwncookie')
# print after deleting cookie
capcookies = driver.get_cookies()
print(capcookies)
print(len(capcookies))

# delete all cookies from the browser
driver.delete_all_cookies()
capcookies = driver.get_cookies()
print(capcookies)
print(len(capcookies))
