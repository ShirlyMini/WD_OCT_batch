import pytest
import sys

sys.path.append(r'C:\Users\user\PycharmProjects\pythonProject_WDBatch')
print(sys.path)
from hybrid_framework.PageObjects.login import LoginPageObject
from hybrid_framework.PageObjects.addCustomer import addCustomer
from hybrid_framework.Utilities.readProperty import ReadConfig
from hybrid_framework.Utilities.customLogger import logger

from hybrid_framework.Utilities.xlutility import *

class Test_Suite_003_add_customer():
    @pytest.mark.sanity
    @pytest.mark.functionality
    @pytest.mark.regression
    def test_case_101_add_customer(self,setup):

        self.User = ReadConfig.GetUsername()
        self.Pswd = ReadConfig.GetPassword()

        self.driver = setup
        self.log = logger()
        self.log.info("Test Case name::test_case_101_login_title")
        login_obj=LoginPageObject(self.driver)
        login_obj.SetUsername(self.User)
        login_obj.SetPassword(self.Pswd)
        login_obj.ClickLogin()
        self.log.info("Login successful")

        ac_obj=addCustomer(self.driver)
        ac_obj.ClickCustomerMenu()
        ac_obj.ClickCustomerOption()
        ac_obj.ClickAddCustomer()
        self.log.info("Launced Add customer page")

        ac_obj.SetCustomerEmail(ac_obj.random_email_gen()+"@gmail.com")
        ac_obj.SetCustomerPassword("123456")
        ac_obj.SetFirstName("pooja")
        ac_obj.SetLastName("ravi")
        # option are Female and Male
        ac_obj.SetGender("Female")
        ac_obj.SetDOB("02/10/1998")
        ac_obj.SetCompany("xyz company")
        ac_obj.SetTaxexempt("No")
        # options: Your store name and Test store 2
        ac_obj.SetNewsLetter("Test store 2")
        # options: Registered, Guests, Vendors, Administrators, Forum Moderators
        ac_obj.SetCustomerRole("Registered")
        # Vendor 1, Vendor 2
        ac_obj.SetVendor("Vendor 2")
        ac_obj.SetActive("No")
        ac_obj.SetAdminComment()

        ac_obj.ClickSave()
        self.status = ac_obj.VerifyAlert()
        if self.status==True:
            self.log.info("test_case_101_add_customer :: Passed")
            assert True
        else:
            self.log.error("test_case_101_add_customer :: Failed")
            self.driver.save_screenshot(r".\ScreenShots\test_case_101_add_customer.png")
            assert False


