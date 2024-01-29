from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
location=os.getcwd()


service_obj=Service("E:\selenium\drivers\chromedriver.exe")
ops= webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
# ops.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=ops)

driver.get("https://www.foundit.in/")

print(driver.get_cookies())
print(len(driver.get_cookies()))

#[{'domain': '.foundit.in', 'expiry': 1738298445, 'httpOnly': False, 'name': '_ga_HT3XNW7GHL', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GS1.1.1703738439.1.0.1703738445.54.0.0'},
# {'domain': '.foundit.in', 'expiry': 1703824844, 'httpOnly': False, 'name': '_clsk', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1w8wx67%7C1703738444899%7C1%7C1%7Ct.clarity.ms%2Fcollect'},
# {'domain': '.foundit.in', 'expiry': 1735274444, 'httpOnly': False, 'name': 'ajs_anonymous_id', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%2218caeb988e911d-0554faa00d5792-26001951-100200-18caeb988ea1c2%22'},
# {'domain': '.foundit.in', 'expiry': 1737902443, 'httpOnly': False, 'name': 'cto_bundle', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'MNQSDF9IeTNQa29tQllnOVg4TVBsRyUyRnBFSWZtd3R1b2xVSTlDYktHemVoQmF5TmhGQWElMkYxM1ZkT0c3Vk01ZUVSS1pwejlBMnZvNUNYTEZiZTZzODEwWFVuS2lZVnVIbnJOcnNydHRtOCUyRlprQ2UxSnY2dGg0eVl6TnpzMktGRTZHRU5CVWpCOHljZyUyRnRiRmJxdVZVckJkbUlHZyUzRCUzRA'},
# {'domain': '.foundit.in', 'expiry': 1711514442, 'httpOnly': False, 'name': '_fbp', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'fb.1.1703738442345.308699499'}, {'domain': '.foundit.in', 'expiry': 1703824839, 'httpOnly': False, 'name': '_uetsid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '4034ff00a53b11eeb4086b55d453ddb4'}, {'domain': '.foundit.in', 'expiry': 1735274444, 'httpOnly': False, 'name': '_clck', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '6tt6jl%7C2%7Cfhx%7C0%7C1457'},
# {'domain': '.foundit.in', 'expiry': 1738298439, 'httpOnly': False, 'name': '_ga', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.1.137634877.1703738439'}, {'domain': '.foundit.in', 'expiry': 1737434438, 'httpOnly': False, 'name': '__gpi', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'UID=00000cc75284be98:T=1703738438:RT=1703738438:S=ALNI_May49vmRnELM8SulHfjMQ0RJMYGzQ'},
# {'domain': '.foundit.in', 'expiry': 1735274439, 'httpOnly': False, 'name': 'WZRK_G', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'd3bc5e4d3030445c861410dee40cca2b'}, {'domain': 'www.foundit.in', 'expiry': 1735294239, 'httpOnly': False, 'name': '__rtbh.lid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22dtQpDq7bxaqfWBbpjvcc%22%7D'},
# {'domain': '.foundit.in', 'expiry': 1737434439, 'httpOnly': False, 'name': '_uetvid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '40352b90a53b11ee81625b45a57453ff'},
# {'domain': '.foundit.in', 'expiry': 1737434438, 'httpOnly': False, 'name': '__gads', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ID=b1762e5e44ee7659:T=1703738438:RT=1703738438:S=ALNI_MbLZAcUbwnoPHHjklRDgAFh2rRqGw'},
# {'domain': '.foundit.in', 'expiry': 1735274438, 'httpOnly': False, 'name': 'MSUID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'afe80f46-13a1-4480-98b4-f0f98b3f1695'}, {'domain': '.foundit.in', 'expiry': 1703739639, 'httpOnly': False, 'name': 'WZRK_S_6K9-ZK8-ZZ6Z', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%7B%22p%22%3A1%2C%22s%22%3A1703738438%2C%22t%22%3A1703738439%7D'}, {'domain': '.www.foundit.in', 'expiry': 1704343245, 'httpOnly': False, 'name': 'RT', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '"z=1&dm=www.foundit.in&si=cd805c1a-65fc-42c6-8027-a31cf2306ef9&ss=lqopvdz0&sl=1&tt=c6l&rl=1&ld=c6p"'}, {'domain': '.foundit.in', 'expiry': 1706330438, 'httpOnly': False, 'name': 'NHP', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'true'},
# {'domain': '.foundit.in', 'expiry': 1711514438, 'httpOnly': False, 'name': '_gcl_au', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1.1.821856147.1703738438'}]


#########################################
# add cookie

driver.add_cookie({'name':"mycookie", "value":"12345667"})
print(driver.get_cookies())
print(len(driver.get_cookies()))

for cookie in driver.get_cookies():
    if cookie['name']=="mycookie":
        print(f"name:{cookie['name']}, value:{cookie['value']}")

#delete cookie
driver.delete_cookie("mycookie")
print(driver.get_cookies())
print(len(driver.get_cookies()))

driver.delete_all_cookies()
print(driver.get_cookies())
print(len(driver.get_cookies()))

