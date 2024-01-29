from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
driver.implicitly_wait(10)
################################################################33
# driver.find_element(By.ID, "tabButton").click()
# driver.find_element(By.ID, "tabButton").click()
#
# print(driver.current_window_handle)
# print(driver.window_handles)#[parent, child, child]
# # parent, child = driver.window_handles
# # print(parent)
# # print(child)
# # driver.switch_to.window(child)
# # print(driver.find_element(By.ID, "sampleHeading").text)
# for handle in driver.window_handles[1:]:
#     driver.switch_to.window(handle)
#     print(driver.find_element(By.ID, "sampleHeading").text)
#     sleep(5)
#     driver.close()# driver
#     # driver.quit()# clean up
# # driver.close()
# #########################################################333333

# driver.find_element(By.ID, "windowButton").click()
# driver.find_element(By.ID, "windowButton").click()
# print(driver.window_handles)
# # parent, child = driver.window_handles
# # driver.switch_to.window(child)
# # print(driver.find_element(By.ID, "sampleHeading").text)
# # driver.quit()
# for handle in driver.window_handles[1:]:
#     driver.switch_to.window(handle)
#     print(driver.find_element(By.ID, "sampleHeading").text)
#     sleep(5)
#     # driver.close()# driver
#     driver.quit()

############################################################3

# driver.find_element(By.ID, "messageWindowButton").click()
# driver.find_element(By.ID, "messageWindowButton").click()
# driver.find_element(By.ID, "messageWindowButton").click()
# print(driver.window_handles)
# for i in driver.window_handles[1:]:
#     driver.switch_to.window(i)
#     sleep(5)
#     driver.close()
# sleep(3)
