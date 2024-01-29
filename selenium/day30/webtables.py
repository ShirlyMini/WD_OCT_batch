# row & col

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
driver.implicitly_wait(10)

row = len(driver.find_elements(By.XPATH, "//tbody/tr"))
col = len(driver.find_elements(By.XPATH, "//thead/tr/th"))
print(f"row:{row} col:{col}")

# # read specifc row
# for c in range(1,col+1):
#     print(driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[2]/td[{c}]").text)

# # read specifc col
# for r in range(1,row+1):
#     print(driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{r}]/td[1]").text)

# for r in range(1,row+1):
#     for c in range(1,col+1):
#         print(driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{r}]/td[{c}]").text, end="\t")
#     print("\n")

for r in range(1,row+1):
    company = driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{r}]/td[1]").text
    if "SAL Steel" in company:
        for c in range(1,col+1):
            print(driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{r}]/td[{c}]").text, end="\t")
        break


driver.quit()
