# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.makemytrip.com/")
# driver.maximize_window()
# sleep(10)
#
# acc_elem=driver.find_element(By.XPATH,'//*[text()="Login or Create Account"]')
# print(acc_elem.is_displayed())
# if acc_elem.is_displayed()==True:
#     acc_elem.click()
# sleep(5)
# btn_elem=driver.find_element(By.XPATH,'//button[@data-cy="continueBtn"]')
# print(btn_elem.is_enabled())
# if btn_elem.is_enabled()==False:
#     driver.find_element(By.ID, 'username').send_keys("912345678")
#     print(btn_elem.is_enabled())
#     if btn_elem.is_enabled()==True:
#         print("elem is enabled")
#         btn_elem.click()
#         #driver.find_element(By.XPATH, '//span[contains(text(),"Continue")]').click()---Not working
#
# # print(driver.find_element(By.XPATH, '//li[@data-cy="oneWayTrip"]').is_selected())
# # driver.find_element(By.XPATH, '//li[@data-cy="roundTrip"]').click()
# # print(driver.find_element(By.XPATH, '//li[@data-cy="oneWayTrip"]').is_selected())
# sleep(10)
#
# driver.close()


from time import sleep
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

service_obj=Service(r"E:\selenium\drivers\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
#
# driver.get("https://www.linkedin.com/learning-login/")
# driver.maximize_window()
# sleep(10)
#
# acc_elem=driver.find_element(By.ID,'auth-id-button')
# print(acc_elem.is_displayed())#true
# print(acc_elem.is_enabled())#false
# if acc_elem.is_enabled()==False:
#     driver.find_element(By.XPATH, "//input[@id='auth-id-input']").send_keys("xyz.gmail.com")
#     print(acc_elem.is_enabled())#true
#     acc_elem.click()
#     print(driver.find_element(By.ID,"auth-email-inline-error").is_displayed())
#     print(driver.find_element(By.ID,"auth-email-inline-error").text)
#
#
# sleep(10)
#
# driver.close()






driver.get("https://www.facebook.com/signup")
driver.maximize_window()
sleep(1)

print(driver.find_element(By.XPATH, '//label[text()="Male"]/following-sibling::input').is_selected())# fAsle
driver.find_element(By.XPATH, '//label[text()="Male"]/following-sibling::input').click()
print(driver.find_element(By.XPATH, '//label[text()="Male"]/following-sibling::input').is_selected())#True
sleep(10)

driver.close()