from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import os
location=os.getcwd()


service_obj=Service("E:\selenium\drivers\msedgedriver.exe")
###################ops object creation
ops= webdriver.EdgeOptions()
preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
ops.add_experimental_option("prefs", preferences)
ops.add_argument("--start-maximized")
ops.add_experimental_option("detach", True)
#ops.add_argument("--proxy-server='127.0.0.1:8080'")
ops.add_extension(r"C:\Users\user\Downloads\ljngjbnaijcbncmcnjfhigebomdlkcjo.crx")
driver = webdriver.Edge(service=service_obj, options=ops)

driver.get('https://file-examples.com/index.php/sample-documents-download/sample-doc-download/')
driver.find_element(By.XPATH, "//tbody/tr[1]/td/a[text()='Download sample DOC file']").click()
sleep(15)
print(driver.window_handles)

driver.switch_to.window(driver.window_handles[1])
sleep(8)
driver.switch_to.frame('wacframe')
driver.find_element(By.XPATH, '//span[text()="Download"]').click()
sleep(20)
