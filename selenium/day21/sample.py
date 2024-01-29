from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# s=Service(r"C:Users/veenu/Documents/chromedriver-win64/chromedriver.exe")
#=Service("E:\selenium\drivers\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get("https://www.google.com")
browser.maximize_window()