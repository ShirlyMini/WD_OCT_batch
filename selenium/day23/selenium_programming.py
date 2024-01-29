# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://money.rediff.com/gainers")
# driver.maximize_window()
# print(driver.title)
# elems=driver.find_element(By.XPATH, "//table[@class='dataTable']/tbody/tr[10]/following::td")
# print(elems)# first elem
# print(elems.text)
# driver.close()
#################################################################

# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://money.rediff.com/gainers")
# driver.maximize_window()
# print(driver.title)
# elems=driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr[10]/following::td")
# print(elems)
# print(len(elems))
#
# # for i in elems:
# #     print(i.text)
# driver.close()


# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://money.rediff.com/gainers")
# driver.maximize_window()
# print(driver.title)
# elems=driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr[10]/td[1]")
# #print(elems.text)#AttributeError: 'list' object has no attribute 'text'
# print(elems)
# # print(len(elems))
#
# # for i in elems:
# #     print(i.text)
# driver.close()

####################################################################3

# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://money.rediff.com/gainers")
# driver.maximize_window()
# print(driver.title)
# elems=driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr[10]/td[ksmxsx]")
# print(elems)
# print(len(elems))
# driver.close()


# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://money.rediff.com/gainers")
# driver.maximize_window()
# print(driver.title)
# elem=driver.find_element(By.XPATH, "//table[@class='dataTable']/tbody/tr[10]/td[ksmxsx]")
# #selenium.common.exceptions.NoSuchElementException
# print(elem)
# driver.close()


##################################################################3

# clear

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
print(driver.title)
driver.find_element(By.XPATH, "//input[@id='srchword']").send_keys("globlin")
# print(driver.find_element(By.XPATH, "//input[@id='srchword']").text)# will not work
print(driver.find_element(By.XPATH, "//input[@id='srchword']").get_attribute("value"))
driver.find_element(By.XPATH, "//input[@id='srchword']").clear()
driver.find_element(By.XPATH, "//input[@id='srchword']").send_keys("tata")
print(driver.find_element(By.XPATH, "//input[@id='srchword']").get_attribute("value"))
print(driver.find_element(By.XPATH, "//input[@id='srchword']").get_attribute("class"))

driver.close()


# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# print(driver.title)
# driver.find_element(By.XPATH, "//input[@id='email']").send_keys("xyz_gamiul.com")
# # print(driver.find_element(By.XPATH, "//input[@id='srchword']").text)# will not work
# print(driver.find_element(By.XPATH, "//input[@id='email']").get_attribute("value"))
#
# driver.close()