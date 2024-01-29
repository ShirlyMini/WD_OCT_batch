import pytest
import sys

sys.path.append(r'C:\Users\user\PycharmProjects\pythonProject_WDBatch')
print(sys.path)
from hybrid_framework.PageObjects.login import LoginPageObject
from hybrid_framework.Utilities.readProperty import ReadConfig
from hybrid_framework.Utilities.customLogger import logger

from hybrid_framework.Utilities.xlutility import *


class Test_Suite_001_login():
    path=r".\TestData\LoginData.xlsx"
    sheet="Sheet1"
    # print(getRow(path, sheet))
    # print(getCol(path, sheet))
    data_list=[]
    for i in range(2, getRow(path, sheet)+1):
        # print((ReadValue(path, sheet, i, 1), ReadValue(path, sheet, i, 2),ReadValue(path, sheet, i, 3)))
        data_list.append((ReadValue(path, sheet, i, 1), ReadValue(path, sheet, i, 2),ReadValue(path, sheet, i, 3)))
    print(data_list)
    #[('admin@yourstore.com', 'admin', 'Pass'), ('admin@yourstore.com', 'adm', 'Fail'), ('adm@yourstore.com', 'admin', 'Fail'), ('adm@yourstore.com'
    # , 'adm', 'Fail')]

    @pytest.mark.regression
    @pytest.mark.parametrize('user, pswd, expected', data_list)
    def test_case_102_login_title(self,setup, user, pswd, expected):

        self.User = ReadConfig.GetUsername()
        self.Pswd = ReadConfig.GetPassword()

        self.driver = setup
        self.log = logger()
        self.log.info("Test Case name::test_case_101_login_title")
        login_obj=LoginPageObject(self.driver)
        login_obj.SetUsername(user)
        login_obj.SetPassword(pswd)
        login_obj.ClickLogin()
        self.log.info("Login successful")
        print(login_obj.VerifyTitle())
        if login_obj.VerifyTitle()==True and expected=="Pass":
            self.log.info("test_case_102_login_title {user} {pswd} :: Passed")
            # WriteValue(path, sheet, i, 2)
            assert True
        elif login_obj.VerifyTitle()==False and expected=="Fail":
            self.log.info("test_case_102_login_title {user} {pswd} :: Passed")
            assert True
        else:
            self.log.error("test_case_102_login_title {user} {pswd} :: Failed")
            self.driver.save_screenshot(fr".\ScreenShots\test_case_102_login_title_{user}_{pswd}.png")
            assert False
            # print("Failure!!!")
            # assert False
