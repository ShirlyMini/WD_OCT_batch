# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://demoqa.com/alerts")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# driver.find_element(By.ID, "alertButton").click()
# alert_obj=driver.switch_to.alert
# print(alert_obj.text)
# alert_obj.accept()# click ok
# # alert_obj.dismiss()# click cancel


################################################################
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://demoqa.com/alerts")
# driver.maximize_window()
# driver.implicitly_wait(10)
# wait_ob=WebDriverWait(driver,20)
#
#
# driver.find_element(By.ID, "timerAlertButton").click()
# wait_ob.until(expected_conditions.alert_is_present())
# alert_obj=driver.switch_to.alert
# print(alert_obj.text)
# alert_obj.accept()# click ok
# # alert_obj.dismiss()# click cancel

###################################################################
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://demoqa.com/alerts")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
#
# driver.find_element(By.ID, "confirmButton").click()
# alert_obj=driver.switch_to.alert
# print(alert_obj.text)
# # alert_obj.accept()# click ok
# alert_obj.dismiss()# click cancel
# print(driver.find_element(By.XPATH,"//span[@id='confirmResult']").text)

####################################################################
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://demoqa.com/alerts")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# sleep(5)# manual interptuion
# driver.find_element(By.ID, "promtButton").click()
# alert_obj=driver.switch_to.alert
# print(alert_obj.text)
# alert_obj.send_keys("Welcome")
# alert_obj.accept()# click ok
# # alert_obj.dismiss()# click cancel
# print(driver.find_element(By.XPATH,"//span[@id='promptResult']").text)# elm wont be there after alert dismiss

##############################################################
# auth pop up
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import autoit

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/basic_auth")
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()

autoit.win_wait_active("",30)
autoit.send("admin{TAB}")
autoit.send("admin{ENTER}")
sleep(10)
print(driver.find_element(By.ID, "content").is_displayed())
sleep(20)