from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demoqa.com/checkbox")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"svg.rct-icon.rct-icon-uncheck").click()
# print(driver.find_element(By.CSS_SELECTOR,"svg.rct-icon.rct-icon-uncheck").is_selected())
# print(driver.find_element(By.XPATH,"//input[@id='tree-node-home']/following-sibling::span[@class='rct-checkbox']/*[name()='svg']").click()
# print(driver.find_element(By.XPATH,"//input[@id='tree-node-home']").is_selected())
print(driver.find_element(By.CSS_SELECTOR,"svg.rct-icon.rct-icon-check").is_displayed())

sleep(20)