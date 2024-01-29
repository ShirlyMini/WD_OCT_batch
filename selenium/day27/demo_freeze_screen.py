from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

sleep(5)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#sleep(10)
wait_ob=WebDriverWait(driver,20)
wait_ob.until(expected_conditions.element_to_be_clickable((By.XPATH,'//span[text()="PIM"]')))
driver.find_element(By.XPATH,'//span[text()="PIM"]').click()
#unable to click on PIM menu option  and inspected elements are not highliting
#driver.find_element(By.XPATH,"//*[@id='app'']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
wait_ob.until(expected_conditions.presence_of_element_located((By.XPATH,'//div[@class="oxd-grid-4 orangehrm-full-width-grid"]/div[6]/div/div[2]/div/div/div[2]/i')))
driver.find_element(By.XPATH,'//div[@class="oxd-grid-4 orangehrm-full-width-grid"]/div[6]/div/div[2]/div/div/div[2]/i').click()

wait_ob.until(expected_conditions.presence_of_all_elements_located((By.XPATH,'//div[@role="listbox"]/div/span')))
# driver.find_element(By.XPATH,'//div[@class="oxd-select-option"]/span[contains(text(),"Account")]').click()
list_of_elem = driver.find_elements(By.XPATH,'//div[@role="listbox"]/div/span')
print(list_of_elem)
for i in list_of_elem:
    print(i.text)

sleep(20)


# import time
#
# s=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get("https://www.save70.com/flights/?campaignid=16568085087&adgroupid=134041419349&lpage=k&lb=skys&gad_source=1&gclid=Cj0KCQiA7OqrBhD9ARIsAK3UXh00P-oj6XQ3qdYZTmmPmlGVdGjLvhnUodahSf3BxOci0MY4bslIzKAaAsJSEALw_wcB")#
# driver.find_element(By.XPATH,"//input[@placeholder='Origin name or code']").click()
# driver.find_element(By.XPATH,"//input[@placeholder='Origin name or code']").send_keys("new")
# #driver.find_element(By.XPATH,"//input[@placeholder='Origin name or code']").send_keys(Keys.ENTER)
# sleep(5)
# ele=driver.find_elements(By.XPATH,"//ul/li[@class='ui-menu-item']/a")
#
# print(len(ele))
# for i in ele:
#     print(i.text)
# time.sleep(10)












# driver.get("https://demo.guru99.com/test/ajax.html")
# #driver.find_element(By.XPATH,"//input[@id='yes']").click()
# # ele =driver.find_elements(By.XPATH,"//label/input[@type='radio']")
# ele =driver.find_elements(By.XPATH,"//div[@class='container']/form/p[1]/label")
# print(len(ele))
# print(ele)
# for i in ele:
#     # print("*****",i.get_attribute("value"))
#     print("*****",i.text)
#
# #for radio button its not working
# #***************************************************************************************
# # ele=driver.find_elements(By.XPATH,"//div[@id='navbar-brand-centered']/ul/li")
# # print(len(ele))
# # for i in ele:
# #     print(i.text)
# #     if i.text=='Selenium':
# #      i.click()
# #     print("Selenium is Clicked")