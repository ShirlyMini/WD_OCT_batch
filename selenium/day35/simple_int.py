from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://cleartax.in/s/simple-compound-interest-calculator")
driver.maximize_window()

Int_typ="Simple Interest"
Principal_Amount="10000"
Rate="10"
Period_unit="Years"
Period_option="3"

int_type_drp=Select(driver.find_element(By.ID, "a"))
int_type_drp.select_by_visible_text(Int_typ)

driver.find_element(By.ID, "c").clear()
driver.find_element(By.ID, "c").send_keys(Principal_Amount)

driver.find_element(By.ID, "d").clear()
driver.find_element(By.ID, "d").send_keys(Rate)

int_type_drp=Select(driver.find_element(By.ID, "f"))
int_type_drp.select_by_visible_text(Period_unit)

driver.find_element(By.ID, "e").clear()
driver.find_element(By.ID, "e").send_keys(Period_option)

total_val=driver.find_element(By.XPATH, "//label[text()='Total Value']/following-sibling::span").text
print(total_val)