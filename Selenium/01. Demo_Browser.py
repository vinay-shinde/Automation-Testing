from selenium import webdriver
import time
#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
service_obj = Service("C:\\Users\\VINAY\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

#-- Firefox
# service_obj = Service("/Users/rahulshetty/documents/geckodriver")
# driver = webdriver.Firefox(service=service_obj)

#-- Edge
# service_obj = Service("/Users/rahulshetty/documents/msedgedriver")
# driver = webdriver.Edge(service=service_obj)

driver.maximize_window()


driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
time.sleep(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.back()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.close()
