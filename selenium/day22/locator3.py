# xpath - xml path
# traverse bottom to top vice versa

#############################################
# abs xpath


# /html/body/div[2]/div[5]/table/tbody/tr[4]/td[3]

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
# print(driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/table/tbody/tr[4]/td[3]').text)
# sleep(15)
# driver.close()


##################################################################
# relative xpath

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
# print(driver.find_element(By.XPATH, '//*[@id="leftcontainer"]/table/tbody/tr[9]/td[1]').text)
# sleep(15)
# driver.close()


#//li/div/button/i[contains(@class,'gfg-icon_dark-mode')]

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
# driver.find_element(By.XPATH, "//li/div/button/i[contains(@class,'gfg-icon_dark-mode')]").click()
# sleep(15)
# driver.close()


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
print(driver.title)
elems=driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr[10]/following::td")
for i in elems:
    print(i.text)
sleep(1)
driver.close()
