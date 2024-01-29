from time import sleep #sleep(20)
# import time #time.sleep(20)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


service_obj=Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.implicitly_wait(10)

wait_obj=WebDriverWait(driver, 20, poll_frequency=5, ignored_exceptions=[Exception])
# wait_obj=WebDriverWait(driver, 20)


# sleep(20)
driver.find_element(By.XPATH,'//span[text()="Cab Rental"]').click()
wait_obj.until(expected_conditions.title_is("Ryde: Car Rentals, Mini Buses, Bus Rentals & Tempo Traveller on Rent"))
# wait_obj.until(expected_conditions.invisibility_of_element_located())
# wait_obj.until(expected_conditions.alert_is_present())

wait_obj.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'FDHTIaTiPRDb75lTmJwh')))
print(driver.title)

print(driver.find_element(By.CLASS_NAME,'FDHTIaTiPRDb75lTmJwh').is_displayed())
