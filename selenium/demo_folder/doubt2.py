from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

s=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
time.sleep(20)

driver.find_element(By.XPATH,"//input[@id='fromCity']").send_keys("BLR")
source=driver.find_elements(By.XPATH,"//ul[@role='listbox']/li")
print(len(source))
for i in source:
    print("################################")
    print(i.text)
    print("################################")
    if 'Bengaluru, India' in i.text :
        i.click()
        print("Selected Bengaluru, India")
        break
time.sleep(10)