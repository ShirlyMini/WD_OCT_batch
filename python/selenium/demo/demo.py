import time

from selenium import webdriver
from selenium.webdriver.edge import service

driver = webdriver.Edge(service=service.Service("E:\selenium\drivers\msedgedriver.exe"))
#driver = webdriver.Chrome(service=service.Service())

time.sleep(10)
driver.get("https://google.com")
print(driver.title)
#driver.close()