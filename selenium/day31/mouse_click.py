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
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()


act = ActionChains(driver)
act.context_click(driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")).context_click(driver.find_element(By.XPATH, "//span[text()='Copy']")).perform()
alrt = driver.switch_to.alert
print(alrt.text)
alrt.accept()

act.double_click(driver.find_element(By.XPATH, "//button[contains(text(),'Double-Click')]")).perform()
sleep(5)
alrt = driver.switch_to.alert
print(alrt.text)
alrt.accept()