from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
location=os.getcwd()


service_obj=Service("E:\selenium\drivers\chromedriver.exe")
###################ops object creation
ops= webdriver.ChromeOptions()
preferences={"download.default_directory":location}
ops.add_experimental_option("prefs", preferences)
ops.add_argument("--start-maximized")
ops.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=ops)

driver.get('https://file-examples.com/index.php/sample-documents-download/sample-doc-download/')
driver.find_element(By.XPATH, "//tbody/tr[1]/td/a[text()='Download sample DOC file']").click()
sleep(20)
