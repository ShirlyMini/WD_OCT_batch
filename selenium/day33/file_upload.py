from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
location=os.getcwd()


service_obj=Service("E:\selenium\drivers\chromedriver.exe")
ops= webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
ops.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=ops)

driver.get("https://www.foundit.in/")
driver.find_element(By.XPATH, "//div[contains(text(), 'Upload Resume')]").click()
driver.find_element(By.ID, "file-upload").send_keys(r"C:\Users\user\PycharmProjects\pythonProject_WDBatch\selenium\day33\file-sample_100kB.doc")

