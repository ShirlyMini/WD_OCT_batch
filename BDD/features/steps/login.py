from time import sleep

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@given(u': Launch Browser')
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service("E:\selenium\drivers\chromedriver.exe"))


@when(u': Open Nopcommerce page')
def step_impl(context):
    context.driver.get("https://admin-demo.nopcommerce.com/")
    context.driver.maximize_window()


@then(u': verify the presence of logo')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h1")


@then(u': Close Browser')
def step_impl(context):
    context.driver.quit()

@when(u': Enter Username "{user}" and Password "{pswd}"')
def step_impl(context, user, pswd):
    context.driver.find_element(By.ID, "Email").clear()
    context.driver.find_element(By.ID, "Email").send_keys(user)
    context.driver.find_element(By.ID, "Password").clear()
    context.driver.find_element(By.ID, "Password").send_keys(pswd)


@when(u': Click Submit')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    sleep(5)

@then(u': verify the presence of Dashboard Logo')
def step_impl(context):
    if context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Dashboard')]").is_displayed():
        print("Dashboard page launched successfully")
    else:
        assert False


@then(u': Presence of Dashboard Logo verified successfully "{status}"')
def step_impl(context, status):
    if context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Dashboard')]").is_displayed():
        if status=="True":
            print("Dashboard page launched successfully")
            context.driver.quit()
            assert True
        else:
            assert False
    else:
        if status=="False":
            print("Dashborad page not launced...")
            context.driver.quit()
            assert True
        else:
            assert False
