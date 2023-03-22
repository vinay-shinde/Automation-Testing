from selenium import webdriver
import time
#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\VINAY\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()


driver.get("https://rahulshettyacademy.com/client")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
time.sleep(2)
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@1234")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Hello@1234")
time.sleep(2)
#driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()









