import pytest
import sys
from selenium import webdriver
sys.path.append(r'C:\Users\user\PycharmProjects\pythonProject_WDBatch')
print(sys.path)
from hybrid_framework.Utilities.readProperty import ReadConfig


@pytest.fixture()
def setup(browser):
    # print(browser)
    BaseURL = ReadConfig.GetBaseUrl()
    if browser != None:
        if browser.lower() == "chrome":
            from selenium.webdriver.chrome.service import Service
            service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
            driver = webdriver.Chrome(service=service_obj)
        elif browser.lower() == "edge":
            from selenium.webdriver.edge.service import Service
            service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
            driver = webdriver.Edge(service=service_obj)
        elif browser.lower() == "firefox":
            from selenium.webdriver.firefox.service import Service
            service_obj = Service(r"E:\selenium\drivers\geckodriver.exe")
            driver = webdriver.Firefox(service=service_obj)
    else:
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

    driver.get(BaseURL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


def pytest_addoption(parser):  # this will get the values from CLI/hooks
    parser.addoption("--browser")
    # parser.addoption("--number")


@pytest.fixture()
def browser(request):  # this will return browser value to setup method
    #print(request.config.getoption("--browser"))
    return request.config.getoption("--browser")#, request.config.getoption("--number")

def pytest_configure(config):
    config.addinivalue_line("markers", "functionality: functional testing")
    config.addinivalue_line("markers", "regression: regression testing")
    config.addinivalue_line("markers", "sanity: regression testing")