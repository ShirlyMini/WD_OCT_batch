from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

###################################################################doubt
driver.get("https://demoqa.com/tool-tips")
driver.maximize_window()
###################################################################doubt

act = ActionChains(driver)

tool_tip_elm1=driver.find_element(By.ID, "toolTipButton")
tool_tip_elm2 =driver.find_element(By.ID, "toolTipTextField")

act.move_to_element(tool_tip_elm1).perform()
print(driver.find_element(By.ID, 'buttonToolTip').text)
sleep(10)

act.move_to_element(tool_tip_elm2).perform()
act.scroll_to_element(driver.find_element(By.ID, 'textFieldToolTip')).perform()
print(driver.find_element(By.ID, 'textFieldToolTip').text)
sleep(20)
###################################################################################
# driver.get("https://www.bedbathandbeyond.com/")
# driver.maximize_window()
# sleep(10)
#
# act=ActionChains(driver)
# elm1=driver.find_element(By.XPATH, "//a[contains(@data-tid,'TN:Bedding') and text()='Bedding']")
# act.move_to_element(elm1).perform()
# sleep(5)
# elm2=driver.find_element(By.XPATH, "//a[contains(@data-tid,'TN:Bedding:QueenMattress') and text()='Queen Mattress']")
# act.move_to_element(elm2).click().perform()
# sleep(5)
# print(driver.title)

#######################################################3
driver.quit()