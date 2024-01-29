import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.edge.service import Service as edge_service


# test suite
# test cases
def setUpModule():
    print("LOGIN USING setUpModule from ts1")

def tearDownModule():
    print("LOGOUT USING tearDownModule from ts1")


class test_suite1(unittest.TestCase):
    def setUp(self):
        print("LOGIN USING setUp")

    def tearDown(self):
        print("LOGOUT USING tearDown")

    @classmethod
    def setUpClass(cls):
        print("LOGIN USING setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("LOGOUT USING tearDownClass")
    # @unittest.SkipTest
    # @unittest.skip("Skipping test case 1")
    @unittest.skipIf(True, "Skipped because condition is true")
    def test_case1(self):
        print("this is first test case from ts1")
        # driver = webdriver.Chrome(service=chrome_service(r"E:\selenium\drivers\chromedriver.exe"))
        # driver.get("https://www.selenium.dev/documentation/webdriver/browsers/")
        # print(driver.title)
        # self.assertEqual("Supported Browsers | Selenium", driver.title, "title not same")

    def test_case2(self):
        print("this is sec test case from ts1")
        # driver = webdriver.Edge(service=edge_service(r"E:\selenium\drivers\msedgedriver.exe"))
        # print(driver)
        # self.assertIsNotNone(driver, "driver should not be none")

if __name__=="__main__":
    unittest.main()