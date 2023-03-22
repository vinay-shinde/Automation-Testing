from selenium import webdriver
import time
#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Users\\VINAY\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()


driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(2)

# ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
time.sleep(2)
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
time.sleep(2)
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
# CSS -  tagname[attribute='value'] -> //input[@type='submit'],  #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#Static Dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(2)
dropdown.select_by_index(0)
#dropdown.select_by_value()


driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("helloagain")
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()















