from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.remote.webelement import WebElement


def print_tag_info(html_tag: WebElement):
    print(f"tag_name = {html_tag.tag_name}, tag_id = {html_tag.id}, text = {html_tag.text}")

# ======== Choose a browser for using: Firefox or Chrome
driver = webdriver.Firefox()
# driver = webdriver.Chrome()

# ======== Navigate browser to a specific website
current_directory_path = os.path.dirname(os.path.realpath(__file__))
html_file_path = "file://" + os.path.join(current_directory_path, "html/navigating.html")
driver.get(html_file_path)

# ======== BROWSER INTERACTION
# 3.1. INTERACTING WITH THE PAGE
print("\n\n3.1. INTERACTING WITH THE PAGE")

password_input_1 = driver.find_element(By.ID, "passwd-id")
password_input_2 = driver.find_element(By.NAME, "passwd")
password_input_3 = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
password_input_4 = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")

print("\npassword_input_1")
print_tag_info(password_input_1)
print("\npassword_input_2")
print_tag_info(password_input_2)
print("\npassword_input_3")
print_tag_info(password_input_3)
print("\npassword_input_4")
print_tag_info(password_input_4)

# Type some text and keys into <input> for password
password_input_1.send_keys("password_input_1 ")
password_input_2.send_keys("password_input_2 ")
password_input_3.send_keys("password_input_3 ")
# continue type text and keys to move pointer to first or last of the text line
password_input_4.send_keys("password_input_4 ", Keys.ARROW_UP, Keys.ARROW_DOWN, Keys.ARROW_UP)

# Sleep 3s before clearing all text
time.sleep(3)
password_input_2.clear()

# ======== Sleep 10s before closing this browser
time.sleep(10)
driver.close()
