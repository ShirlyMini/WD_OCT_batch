import pytest

from PageObjects.login import LoginPageObject
from Utilities.readProperty import ReadConfig
from Utilities.customLogger import logger


class Test_Suite_001_login():
    @ pytest.mark.sanity
    @ pytest.mark.regression
    def test_case_101_login_title(self,setup):

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
        print(login_obj.VerifyTitle())
        if login_obj.VerifyTitle()==True:
            self.log.info("test_case_101_login_title :: Passed")
            assert True
        else:
            self.log.error("test_case_101_login_title :: Failed")
            self.driver.save_screenshot(r".\ScreenShots\test_case_101_login_title.png")
            assert False
            # print("Failure!!!")
            # assert False
