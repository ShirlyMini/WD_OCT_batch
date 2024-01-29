# locator- Normal locator,cutomised locator

# locator- ID (unique and fastest), Name, Class, tag, Link text,Partial link text
# customised locator  CSS and Xpath

#<input type="text"
# class="inputtext _55r1 _6luy"
# name="email"
# id="email"
# data-testid="royal_email"
# placeholder="Email address or phone number"
# autofocus="1"
# aria-label="Email address or phone number">
# input, img,table(td tr th), button, a(link ,href)


############################################3
#ID

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
# driver.find_element(By.ID, "email").send_keys("abc.gmail.com")
# driver.find_element(By.ID, "pass").send_keys("abcdef")
# sleep(15)
# driver.close()

#################################################3
# name

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
# driver.find_element(By.NAME, "email").send_keys("abc.gmail.com")
# driver.find_element(By.NAME, "pass").send_keys("abcdef")
# sleep(15)
# driver.close()

#############################################################
#class

# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.geeksforgeeks.org/")
# driver.maximize_window()
# print(driver.title)
# driver.find_element(By.CLASS_NAME, "header-main__signup").click()
# sleep(15)
# driver.close()

#################################################
#tag

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
# driver.find_element(By.NAME, "email").send_keys("abc.gmail.com")
# driver.find_element(By.NAME, "pass").send_keys("abcdef")
# driver.find_element(By.TAG_NAME, "button").click()
# sleep(15)
# driver.close()

############################################################
# link text

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
# # driver.find_element(By.LINK_TEXT, "Forgotten password?").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "password?").click()
# sleep(15)
# driver.close()


#######################################
# links in button form
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.geeksforgeeks.org/")
# driver.maximize_window()
# print(driver.title)
# driver.find_element(By.LINK_TEXT, "Sign In").click()
# # driver.find_element(By.PARTIAL_LINK_TEXT, "password?").click()
# sleep(15)
# driver.close()

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()
print(driver.title)
# driver.find_element(By.LINK_TEXT, "Sign In").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Create new").click()
sleep(15)
driver.close()

