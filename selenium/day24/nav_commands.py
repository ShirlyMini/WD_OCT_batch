from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

service_obj=Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.linkedin.com/learning-login/")
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
driver.refresh()
print(driver.title)# geek
sleep(2)
driver.back()
print(driver.title)# linked
sleep(2)
driver.forward()
print(driver.title)# geek
sleep(2)

