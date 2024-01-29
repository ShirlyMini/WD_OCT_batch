from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPageObject:

    # locators of loginpage
    id_email="Email"
    id_password="Password"
    xpath_submit="//button[contains(text(),'Log in')]"
    xpath_logout="//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver=driver

    def SetUsername(self, email):
        self.driver.find_element(By.ID, self.id_email).clear()
        self.driver.find_element(By.ID, self.id_email).send_keys(email)

    def SetPassword(self, pswd):
        self.driver.find_element(By.ID, self.id_password).clear()
        self.driver.find_element(By.ID, self.id_password).send_keys(pswd)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.xpath_submit).click()

    def VerifyTitle(self):
        return self.driver.title == "Dashboard / nopCommerce administration"

    def ClickLogout(self):
        self.driver.find_element(By.XPATH, self.xpath_logout).click()

