from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains


def print_tag_info(html_tag: WebElement):
    print(f"tag_name = {html_tag.tag_name}, tag_id = {html_tag.id}, text = {html_tag.text}")

# ======== Choose a browser for using: Firefox or Chrome
driver = webdriver.Firefox()
# driver = webdriver.Chrome()

# ======== Navigate browser to a specific website
driver.get("https://www.google.com/")

# ======== BROWSER INTERACTION
# 3.7. Cookies
print("\n\n3.7. Cookies")

# Add data to cookies of this visited website
cookie = {'name' : '1111111', 'value' : '222222222'}
driver.add_cookie(cookie)

time.sleep(2)
# Get saved cookies from this visited website
get_saved_cookies = driver.get_cookies()

print("get_saved_cookies = ", get_saved_cookies)

# ======== Sleep 10s before closing this browser
time.sleep(10)
driver.close()
