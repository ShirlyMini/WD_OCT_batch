from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import os
location=os.getcwd()


service_obj=Service("E:\selenium\drivers\geckodriver.exe")
###################ops object creation
ops= webdriver.FirefoxOptions()
preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
ops.set_preference("bowser.download.manager.showWhenStarting",False)
ops.set_preference("browser.download.folderList",2)#0-desktop,1-downloadfolder,2-desiredloc
ops.set_preference("browser.download.dir",location)#onlythefolderlistis2
#ops.set_preference("pdfjs.disabled",True)
ops.add_argument("--start-maximized")
# ops.add_argument("--proxy-server='127.0.0.1:8080'")

ops.set_preference("detach", True)
driver = webdriver.Firefox(service=service_obj, options=ops)
driver.install_addon(r"C:\Users\user\Downloads\ljngjbnaijcbncmcnjfhigebomdlkcjo.crx", temporary=True)
driver.get('https://file-examples.com/index.php/sample-documents-download/sample-doc-download/')
driver.find_element(By.XPATH, "//tbody/tr[1]/td/a[text()='Download sample DOC file']").click()

sleep(20)
