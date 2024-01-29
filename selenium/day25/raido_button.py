from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://demoqa.com/radio-button")
# driver.maximize_window()
#
# driver.find_element(By.XPATH,"//label[contains(text(),'Yes')]").click()
# print(driver.find_element(By.XPATH,"//label[contains(text(),'Yes')]").text)
# print(driver.find_element(By.XPATH,"//label[contains(text(),'Yes')]/preceding-sibling::input").is_selected())
#
# sleep(20)


driver.get("https://www.makemytrip.com/")
driver.maximize_window()
sleep(20)
driver.find_element(By.XPATH,"//li[@data-cy='roundTrip']").click()
print(driver.find_element(By.XPATH,"//li[@data-cy='roundTrip' and @class='selected']").is_displayed())#True
print(driver.find_element(By.XPATH,"//li[@data-cy='roundTrip' and @class='selected']").is_selected())#False# input tag