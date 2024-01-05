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
current_directory_path = os.path.dirname(os.path.realpath(__file__))
html_file_path = "file://" + os.path.join(current_directory_path, "html/alert.html")
driver.get(html_file_path)

# ======== BROWSER INTERACTION
# 3.5. POPUP DIALOGS
print("\n\n3.5. POPUP DIALOGS")

# Trigger the alert by clicking the button
driver.find_element(By.TAG_NAME, "button").click()

# Switch to the alert and perform actions
alert = driver.switch_to.alert
print("Alert Text:", alert.text)


# ======== Sleep 10s before closing this browser
time.sleep(10)
driver.close()
