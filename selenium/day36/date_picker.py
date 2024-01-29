from time import sleep
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.save70.com/flights/?campaignid=16568085087&adgroupid=134041419349&lpage=k&lb=skys&gad_source=1&gclid=Cj0KCQiA7OqrBhD9ARIsAK3UXh00P-oj6XQ3qdYZTmmPmlGVdGjLvhnUodahSf3BxOci0MY4bslIzKAaAsJSEALw_wcB")
driver.find_element(By.ID,"flights_depart_date").click()
#pre=driver.find_element(By.XPATH,"//a/span[@class='ui-icon ui-icon-circle-triangle-w']").is_displayed()
#nex=driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
month='September'
sleep(5)
# while True:
#     month_list=[]
#     for we in driver.find_elements(By.XPATH, f"//span[@class='ui-datepicker-month']"):
#         month_list.append(we.text)# collect both month from the container
#
#     if month == month_list[0]:#comparing first grp month()
#         break
#     else:
#         driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div[2]/div/a/span").click()
#
# driver.find_element(By.XPATH, "//div[@class='ui-datepicker-group ui-datepicker-group-first']/table/tbody/tr/td/a[text()='30']").click()
#selecting first group data


while True:
    months = driver.find_elements(By.XPATH, "//span[@class='ui-datepicker-month']")
    print(months)
 # if month!= months:
 #     driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div[2]/div/a/span").click()
 # break
    l1=[]
    for i in months:
        l1.append(i.text)
    print(l1)



    if month!= l1[1]:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div[2]/div/a/span").click()

    elif month==l1[1]:
        break


print("outside of loop")

dates=driver.find_elements(By.XPATH,"//div[@class='ui-datepicker-group ui-datepicker-group-last']/table/tbody/tr/td")
for i in dates:
    if i.text=='21':
        i.click()
        break

sleep(5)
# #break
print(driver.find_element(By.ID,"flights_depart_date").get_attribute("value"))