import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


# test suite
# test cases
def setUpModule():
    print("LOGIN USING setUpModule from ts2")


def tearDownModule():
    print("LOGOUT USING tearDownModule from ts2")


class test_suite2(unittest.TestCase):
    def test_case3(self):
        print("this is first test case from ts2")
        # driver = webdriver.Firefox(service=Service(r"E:\selenium\drivers\geckodriver.exe"))
        # driver.get("https://www.selenium.dev/documentation/webdriver/browsers/")
        # print(driver.title)
        # self.assertEqual("Supported Browsers | Selenium", driver.title, "title not same")

if __name__=="__main__":
    unittest.main()