from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from xlutility import *
service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://cleartax.in/s/simple-compound-interest-calculator")
driver.maximize_window()

test_data=r"C:\Users\user\PycharmProjects\pythonProject_WDBatch\selenium\day36\simple_interest.xlsx"

for r in range(2, getRow(test_data, "Sheet1")+1):

    Int_typ=ReadValue(test_data, "Sheet1", r, 5)
    Principal_Amount=ReadValue(test_data, "Sheet1", r, 1)
    Rate=ReadValue(test_data, "Sheet1", r, 2)
    Period_unit=ReadValue(test_data, "Sheet1", r, 4)
    Period_option=ReadValue(test_data, "Sheet1", r, 3)

    int_type_drp=Select(driver.find_element(By.ID, "a"))
    int_type_drp.select_by_visible_text(Int_typ)

    driver.find_element(By.ID, "c").clear()
    driver.find_element(By.ID, "c").send_keys(Principal_Amount)

    driver.find_element(By.ID, "d").clear()
    driver.find_element(By.ID, "d").send_keys(Rate)

    int_type_drp=Select(driver.find_element(By.ID, "f"))
    int_type_drp.select_by_visible_text(Period_unit)

    driver.find_element(By.ID, "e").clear()
    driver.find_element(By.ID, "e").send_keys(Period_option)

    total_val=driver.find_element(By.XPATH, "//label[text()='Total Value']/following-sibling::span").text
    print(total_val)

    WriteValue(test_data, "Sheet1", r, 8,total_val)

    print(float(total_val.strip("₹ ").replace(",", "")))
    excel_total_value=ReadValue(test_data, "Sheet1", r, 6)
    # print(float(excel_total_value))
    if float(total_val.strip("₹ ").replace(",", "")) == float(excel_total_value):
        # print(True)
        WriteValue(test_data, "Sheet1", r, 9, "True")
        FillGreenColor(test_data, "Sheet1", r, 9)

    else:
        # print(False)
        WriteValue(test_data, "Sheet1", r, 9, "False")
        FillRedColor(test_data, "Sheet1", r, 9)