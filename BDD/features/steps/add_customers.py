from time import sleep

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@then(u': click customer module')
def step_impl(context):
    sleep(2)
    context.driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Customers')]").click()

@then(u': verify customer items')
def step_impl(context):
    sleep(2)
    lst = context.driver.find_elements(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Customers')]/parent::a/following-sibling::ul/li/a/p")
    for l in lst:
        print(l.text)

@then(u': click sales module')
def step_impl(context):
    sleep(2)
    context.driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Sales')]").click()

@then(u': verify sales items')
def step_impl(context):
    sleep(2)
    lst = context.driver.find_elements(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Sales')]/parent::a/following-sibling::ul/li/a/p")
    for l in lst:
        print(l.text)
