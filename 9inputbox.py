from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# finding how many input boxes are present in the webpages

inputboxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print("No of inputboxes are:", len(inputboxes))

# providing value into textboxes

driver.find_element_by_id("RESULT_TextField-1").send_keys("Ram")
driver.find_element_by_id("RESULT_TextField-2").send_keys("rai")
driver.find_element_by_id("RESULT_TextField-3").send_keys("9800981230")
driver.find_element_by_id("RESULT_TextField-4").send_keys("Usa")
driver.find_element_by_id("RESULT_TextField-5").send_keys("Chicago")
driver.find_element_by_id("RESULT_TextField-6").send_keys("hello@gmail.com")

#radio button
status = driver.find_element_by_id("RESULT_RadioButton-7_1").is_selected()
print(status)
driver.find_element_by_xpath("//label[normalize-space()='Male']").click()

#select checkboxes
driver.find_element_by_xpath("//label[normalize-space()='Thursday']").click()
driver.find_element_by_xpath("//label[normalize-space()='Saturday']").click()
statuss = driver.find_element_by_xpath("//label[normalize-space()='Saturday']").is_selected()
print(statuss)
#dropdown
drpdwn = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(drpdwn)

# many approach in selecting options in dropdown menues.
# 1. selection of options in dropdown
drp.select_by_visible_text('Morning')

#  2. select by method
drp.select_by_index(2)

#  3. select by value
drp.select_by_value("Radio-2")

# count no. of options in dropdown
print("no of options are:", len(drp.options))

# capture all the options in dropdown and print them as output
optionlist = drp.options
for option in optionlist:
    print(option.text)


#submit
driver.find_element_by_id("FSsubmit").click()