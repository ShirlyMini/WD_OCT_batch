from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests



service_obj=Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

link_elem = driver.find_elements(By.XPATH,"//a")
try:
    for i in link_elem:
        url=i.get_attribute("href")
        status=requests.get(url)
        print(status.status_code)
        if status.status_code>299:
            print("invalid status code for", url)
        else:
            print("valid status code for", url)
except Exception as msg:
    print("No status code for", url, msg)