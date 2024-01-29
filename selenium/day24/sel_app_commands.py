from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
if driver.current_url=="https://www.facebook.com/":
    print("current url is same as expected")
print(driver.page_source)




driver.close()