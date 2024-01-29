# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver import ActionChains
#
# ops=webdriver.ChromeOptions()
# # ops.add_argument("--headless")
# # ops.add_argument("--start-maximised")
# # ops.add_argument("--incognito")
# s=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=s, options=ops)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# sleep(10)
# driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# #sleep(10)
# wait_ob=WebDriverWait(driver,10)
# wait_ob.until(expected_conditions.element_to_be_clickable((By.XPATH,"//span[text()='PIM']")))
# driver.find_element(By.XPATH,"//span[text()='PIM']").click()
# sleep(2)
#
# act = ActionChains(driver)
# # driver.find_element(By.XPATH,"//div[@class='oxd-form-row']/div/div[6]/div/div[2]/div/div/div[2]/i").click()
# # elem = driver.find_element(By.XPATH,"//div[@role='listbox']/div/span[contains(text(),'Software Engineer')]")
#
# # driver.execute_script("arguments[0].scrollIntoView()", elem)# browser scroll
#
#
# # act.scroll_to_element(elem).perform()# inside the elem container
#
# elm2=driver.find_element(By.XPATH, "//div[contains(text(),'Cassidy')]")
# # driver.execute_script("arguments[0].scrollIntoView()",elm2)# browser scroll
# act.scroll_to_element(elm2).perform()
# sleep(10)


####################################################################3
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver import ActionChains
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# ###################################################################doubt
# driver.get("https://demoqa.com/tool-tips")
# driver.maximize_window()
# ###################################################################doubt
#
# act = ActionChains(driver)
#
# tool_tip_elm1=driver.find_element(By.ID, "toolTipButton")
# tool_tip_elm2 =driver.find_element(By.ID, "toolTipTextField")
#
# act.move_to_element(tool_tip_elm1).perform()
# print(driver.find_element(By.ID, 'buttonToolTip').text)
# sleep(3)
#
# act.move_to_element(tool_tip_elm2).perform()
# act.scroll_to_element(driver.find_element(By.ID, 'textFieldToolTip')).perform()
#
# # driver.execute_script("arguments[0].scrollIntoView()",driver.find_element(By.ID, 'textFieldToolTip'))
# print(driver.find_element(By.ID, 'textFieldToolTip').text)


# act.scroll_to_element(driver.find_element(By.XPATH, "//div[@id='texToolTopContainer']/a[2]")).perform()
# driver.execute_script("arguments[0].scrollIntoView()",driver.find_element(By.XPATH, "//div[@id='texToolTopContainer']/a[2]"))

# act.scroll_by_amount(0,250).perform()


#################################################################3
#https://www.selenium.dev/documentation/webdriver/actions_api/wheel/

# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver import ActionChains
#
# ops=webdriver.ChromeOptions()
# s=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=s, options=ops)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# sleep(10)
# driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# #sleep(10)
# wait_ob=WebDriverWait(driver,10)
# wait_ob.until(expected_conditions.element_to_be_clickable((By.XPATH,"//span[text()='PIM']")))
# driver.find_element(By.XPATH,"//span[text()='PIM']").click()
# sleep(2)
#
# act = ActionChains(driver)
# elem=driver.find_element(By.XPATH, "//div[contains(text(),'Grace')]")
# # act.scroll_to_element(elem).perform()
# print(elem.location)
# scr_origin=ScrollOrigin.from_element(elem)
# sleep(5)
# act.scroll_from_origin(scr_origin,0,850).perform()
# print(elem.location)
# sleep(10)

########################################################3

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
###################ops object creation
ops= webdriver.ChromeOptions()
ops.add_argument("--incognito")
ops.add_argument("--start-maximized")
ops.add_argument("--headless")
driver = webdriver.Chrome(service=service_obj, options=ops)

###################################################################doubt
driver.get("https://demoqa.com/select-menu")
# driver.maximize_window()
###################################################################doubt

act = ActionChains(driver)
scr_origin = ScrollOrigin.from_element(driver.find_element(By.ID, "cars"))
act.scroll_from_origin(scr_origin, 0,300).perform()

act.key_down(Keys.CONTROL).\
    move_to_element(driver.find_element(By.XPATH, "//*[@id='cars']/option[4]")).click().\
    move_to_element(driver.find_element(By.XPATH, "//*[@id='cars']/option[3]")).click().\
    move_to_element(driver.find_element(By.XPATH, "//*[@id='cars']/option[2]")).click().\
    move_to_element(driver.find_element(By.XPATH, "//*[@id='cars']/option[1]")).click().\
    key_up(Keys.CONTROL).perform()
print(driver.title)
sleep(10)