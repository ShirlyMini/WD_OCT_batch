# customised loactor
# xpath and css
# css
#######################################################
# tag/id
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# print(driver.title)
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc.gmail.com")
# driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("abcdef")
# sleep(15)
# driver.close()


# tag/class
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.geeksforgeeks.org/")
# driver.maximize_window()
# print(driver.title)
# driver.find_element(By.CSS_SELECTOR, "a.header-main__signup").click()
# sleep(15)
# driver.close()


# tag/attr

# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.geeksforgeeks.org/")
# driver.maximize_window()
# print(driver.title)
# driver.find_element(By.CSS_SELECTOR, "[type=button]").click()
# sleep(15)
# driver.close()

# tag/class/attr

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
print(driver.title)
driver.find_element(By.CSS_SELECTOR, ".header-main__signup[type=button]").click()
sleep(15)
driver.close()








# xpath