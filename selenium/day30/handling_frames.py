from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demoqa.com/nestedframes")
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.find_element(By.XPATH, "//div[@id='framesWrapper']/div[1]").text)

################Nested frame###############3
driver.switch_to.frame("frame1")
driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@srcdoc="<p>Child Iframe</p>"]'))
print(driver.find_element(By.XPATH, "//body/p").text)
driver.switch_to.parent_frame()
print(driver.find_element(By.XPATH, "//body").text)
driver.switch_to.default_content()
print(driver.find_element(By.XPATH, "//div[@id='framesWrapper']/div[1]").text)