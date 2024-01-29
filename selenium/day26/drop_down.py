from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.globalsqa.com/samplepagetest/")
driver.maximize_window()
#####################################################################3
# appr1
# driver.find_element(By.ID,"g2599-experienceinyears").click()
# input="10+"
# driver.find_element(By.XPATH,f"//option[text()='{input}']").click()
#
# sleep(20)

#################################################################################3
# appr2

drp_elem = driver.find_element(By.ID,"g2599-experienceinyears")
select_obj = Select(drp_elem)
select_obj.select_by_visible_text("3-5")
select_obj.select_by_index(2)
select_obj.select_by_value('7-10')

sleep(20)