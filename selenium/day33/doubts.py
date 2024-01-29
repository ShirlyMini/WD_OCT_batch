from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
import os


service_obj=Service("E:\selenium\drivers\chromedriver.exe")
ops= webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
# ops.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=ops)
# driver.get("https://demoqa.com/select-menu")
# driver.implicitly_wait(5)
# act=ActionChains(driver)
# driver.find_element(By.XPATH,"//*[@id='withOptGroup']/div[1]/div[2]/div").click()
# list=driver.find_elements(By.XPATH,"//*[@id='withOptGroup']/div[2]/div/div[2]/div/div")#unable to select
# print(len(list))
# for i in list:
#     act.key_down(Keys.ARROW_DOWN).perform()
#     if 'Group 2, option 2' in i.text:
#         print("clicked.....")
#         i.click()
#     # i.click()
#
# sleep(10)

#####################################################333
act=ActionChains(driver)
driver.get("https://demoqa.com/slider")
ele=driver.find_element(By.XPATH,"//*[@id='sliderContainer']/div[1]/span/input")
print(ele.get_attribute("value"))
# act.drag_and_drop_by_offset(ele,100,0)
# driver.execute_script("$(arguments[0]).val('100').change()",ele)--changes not happening
# driver.execute_script("arguments[0].set-attribute('value', '77')",ele)---not work
#arguments[0].set-attribute("value", "77")"

for i in range(10):
    ele.send_keys(Keys.ARROW_RIGHT)# it will increase one value
print(ele.get_attribute("value"))
for i in range(10):
    ele.send_keys(Keys.ARROW_LEFT)# it will increase one value
print(ele.get_attribute("value"))
sleep(10)

#####################################################333


# driver.get("https://demoqa.com/resizable")
#
# act=ActionChains(driver)
# driver.execute_script("window.scrollBy(0, 300)","")
# sleep(10)
# ele=driver.find_element(By.XPATH,"//*[@id='resizableBoxWithRestriction']/span")
#
# print(ele.location)
# ele1=driver.find_element(By.XPATH,"//div[@class='constraint-area']")
# print(ele1.location)
#
#
# act.drag_and_drop_by_offset(ele,300,100).perform()
# print(ele.location)
# sleep(10)

# driver.get("https://demoqa.com/droppable")
#
# driver.execute_script("window.scrollBy(0, 250)","")
#
#
# driver.find_element(By.ID,"droppableExample-tab-accept").click()
# act=ActionChains(driver)
# s1=driver.find_element(By.XPATH,"//div[@id='droppableContainer']/div[1]/div[2]/div[1]/div[1]/div[1]")
# d1=driver.find_element(By.XPATH,"//div[@id='droppableContainer']/div[1]/div[2]/div[1]/div[2]")
# # driver.execute_script("arguments[0].scrollIntoView();", d1)
# sleep(5)
# act.drag_and_drop(s1,d1).perform()
# print(driver.find_element(By.XPATH,"//div[@id='droppableExample-tabpane-accept']/div[1]/div[2]/p").text)
# sleep(20)