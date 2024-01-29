from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import string
import random


class addCustomer:
    xpath_customer_menu = "//ul[@role='menu']/li[4]/a/p"
    xpath_customer_item = "//ul[@role='menu']/li[4]/ul/li[1]/a/p"
    xpath_add_button = "//a[@class='btn btn-primary']"
    id_Email = "Email"
    id_pswd = "Password"
    id_firstname="FirstName"
    id_lastname="LastName"
    id_gender_male="Gender_Male"
    id_gender_female="Gender_Female"
    id_dateofbirth = "DateOfBirth"
    id_company="Company"
    id_taxexempt="IsTaxExempt"
    id_newsletter="SelectedNewsletterSubscriptionStoreIds_taglist"
    xpath_newsletter="//input[@aria-describedby='SelectedNewsletterSubscriptionStoreIds_taglist']"
    newsletter_option="Test store 2"
    xpath_option_newsletter = f"//li[contains(text(),'{newsletter_option}')]"
    xpath_customerrole_container= "//input[@aria-describedby='SelectedCustomerRoleIds_taglist']"
    id_customerrole= 'SelectedCustomerRoleIds'
    customerrole_option='Forum Moderators'
    xpath_customerrole = f"//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'{customerrole_option}')]"
    xpath_defaultregisterrole="//span[contains(text(),'Registered')]"
    xpath_deleteregisterrole = "//span[contains(text(),'Registered')]/following-sibling::span"
    id_select_vendor= 'VendorId'
    id_active="Active"
    id_admin_comment="AdminComment"
    xpath_save="//button[@name='save']"
    xpath_alert = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver=driver

    def ClickCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.xpath_customer_menu).click()

    def ClickCustomerOption(self):
        self.driver.find_element(By.XPATH, self.xpath_customer_item).click()

    def ClickAddCustomer(self):
        self.driver.find_element(By.XPATH, self.xpath_add_button).click()

    def SetCustomerEmail(self, email):
        self.driver.find_element(By.ID, self.id_Email).send_keys(email)

    def SetCustomerPassword(self, pswd):
        self.driver.find_element(By.ID, self.id_pswd).send_keys(pswd)

    def SetFirstName(self, name):
        self.driver.find_element(By.ID, self.id_firstname).send_keys(name)

    def SetLastName(self, name):
        self.driver.find_element(By.ID, self.id_lastname).send_keys(name)

    def SetGender(self, gender):
        if gender=="Male":
            self.driver.find_element(By.ID, self.id_gender_male).click()
        elif gender=="Female":
            self.driver.find_element(By.ID, self.id_gender_female).click()
        else:
            self.driver.find_element(By.ID, self.id_gender_male).click()

    def SetDOB(self, dob):
        self.driver.find_element(By.ID, self.id_dateofbirth).send_keys(dob)

    def SetCompany(self, company):
        self.driver.find_element(By.ID, self.id_company).send_keys(company)

    def SetTaxexempt(self, option):
        if option=="Yes":
            self.driver.find_element(By.ID, self.id_taxexempt).click()
        elif option=="No":
            pass

    def SetNewsLetter(self, NL_name):
        self.elem = self.driver.find_element(By.ID, self.id_newsletter)
        self.driver.execute_script("arguments[0].scrollIntoView()", self.elem)

        self.driver.find_element(By.XPATH, self.xpath_newsletter).click()
        self.newsletter_option=NL_name
        self.driver.find_element(By.XPATH, f"//li[contains(text(),'{self.newsletter_option}')]").click()

    def SetCustomerRole(self, role):
        self.customerrole_option = role
        sleep(3)
        if role=="Registered":
            if self.driver.find_element(By.XPATH, self.xpath_defaultregisterrole).is_displayed():
                pass
            elif self.driver.find_element(By.XPATH, self.xpath_defaultregisterrole).is_displayed()==False:
                self.driver.find_element(By.XPATH, self.xpath_customerrole_container).click()
                # self.driver.find_element(By.XPATH, self.xpath_customerrole).click()
                self.driver.find_element(By.XPATH, f"//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'{self.customerrole_option}')]").click()
        if role != "Registered":
            self.driver.find_element(By.XPATH, self.xpath_deleteregisterrole).click()
            self.driver.find_element(By.XPATH, self.xpath_customerrole_container).click()
            # self.driver.find_element(By.XPATH, self.xpath_customerrole).click()
            self.driver.find_element(By.XPATH, f"//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'{self.customerrole_option}')]").click()

    def SetVendor(self, vname):
        self.drp_down=Select(self.driver.find_element(By.ID, self.id_select_vendor))
        self.drp_down.select_by_visible_text(vname)

    def SetActive(self, option):
        if option=="No":
            self.driver.find_element(By.ID, self.id_active).click()
        elif option=="Yes":
            pass

    def SetAdminComment(self):
        msg="this is admin content"
        self.driver.find_element(By.ID, self.id_admin_comment).send_keys(msg)

    def ClickSave(self):
        self.driver.find_element(By.XPATH, self.xpath_save).click()

    def VerifyAlert(self):
        return "customer has been added successfully." in self.driver.find_element(By.XPATH, self.xpath_alert).text

    def random_email_gen(self):
        # print(string.ascii_letters + string.digits)
        # print(random.choice(string.ascii_letters + string.digits))
        email_gen = ""
        for i in range(8):
            email_gen = email_gen + random.choice(string.ascii_letters + string.digits)
        return email_gen