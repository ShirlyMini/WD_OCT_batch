from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://demoqa.com/dragabble")
driver.maximize_window()

act = ActionChains(driver)
drag_elem=driver.find_element(By.ID, "dragBox")
print(drag_elem.location)#{'x': 375, 'y': 384}

# act.drag_and_drop_by_offset(drag_elem, 200, 0).perform()
# print(drag_elem.location)
#
# act.drag_and_drop_by_offset(drag_elem, -200, 0).perform()
# print(drag_elem.location)

act.drag_and_drop_by_offset(drag_elem, 0, 100).perform()
print(drag_elem.location)
sleep(3)
# driver.execute_script("arguments[0].scrollIntoView()", drag_elem)# scroll until elem found
driver.execute_script("window.scrollBy(0,100)", "")
print(driver.execute_script("return-window.pageYOffset;"))#-100
# print(driver.execute_script("return-window.pageXOffset;"))
sleep(5)
act.drag_and_drop_by_offset(drag_elem, 0, -100).perform()
print(drag_elem.location)

sleep(10)


