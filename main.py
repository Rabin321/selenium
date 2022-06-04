import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")

driver.get("https://booking.com/")
print(driver.title)

time.sleep(2)
# driver.find_element_by_xpath("//*[name()='path' and contains(@fill,'#fff')]").click()  ## click on logo

driver.find_element_by_xpath("//input[@id='ss']").send_keys("Pokhara") ## textfield
time.sleep(1)
driver.find_element_by_xpath("//span[@class='search_hl_name'][normalize-space()='Pokhara']").click()

time.sleep(1)
driver.find_element_by_css_selector("span[aria-label='7 June 2022'] span[aria-hidden='true']").click() ## 7 checkin caender
time.sleep(1)
driver.find_element_by_css_selector("span[aria-label='4 July 2022'] span[aria-hidden='true']").click() ## 4 check out calender

time.sleep(1)
driver.find_element_by_xpath("//span[contains(@class,'js-sb-submit-text')]").click() ##search
time.sleep(3)

driver.find_element_by_xpath("//body/div[@id='bodyconstraint']/div[@id='bodyconstraint-inner']/div[@id='searchresultsTmpl']/div[@id='basiclayout']/div[@id='right']/div[@id='ajaxsrwrap']/div[@id='search_results_table']/div[@data-component='arp-properties-list']/div[1]").click()  ## see availability
time.sleep(3)
print("before windows")
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
print("before reserve")
# driver.find_element_by_xpath("//button[@id='b_tt_holder_1']").click() ##reserve
time.sleep(1)
print("Not clicked")
time.sleep(5)

# Scroll down till the element is visible

reserve = driver.find_element_by_css_selector(".tt_content")
driver.execute_script("arguments[0].scrollIntoView();", reserve)
print("scrolled")
time.sleep(1)
driver.find_element_by_xpath("//div[@class='tt_content']").click()
time.sleep(2)
driver.find_element_by_xpath("//span[@class='bui-button__text js-reservation-button__text']").click()
time.sleep(10)

