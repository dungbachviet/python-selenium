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
html_file_path = "file://" + os.path.join(current_directory_path, "html/locating.html")
driver.get(html_file_path)

# ======== BROWSER INTERACTION
# ============== LOCATING BY ID
# Get a form tag by its ID
# <form id="loginForm">
login_form = driver.find_element(By.ID, 'loginForm')
print("\n\n======= GET <FORM> TAG BY ITS ID")
print("login_form.id = ", login_form.id)
print("login_form.tag_name = ", login_form.tag_name)
print("login_form.text = ", login_form.text)
print("login_form.location = ", login_form.location)


# ============== LOCATING BY NAME ATTRIBUTE
# Get input tag by its name attribute
# <input name="username" type="text" />
username_input = driver.find_element(By.NAME, 'username')
print("\n\n======= GET <INPUT> TAG BY ITS ID")
print("username_input.id = ", username_input.id)
print("username_input.tag_name = ", username_input.tag_name)
print("username_input.text = ", username_input.text)
print("username_input.location = ", username_input.location)


# ============== LOCATING BY XPATH
print("\n\n======= GET <FORM> TAG BY XPATH")
login_form_1 = driver.find_element(By.XPATH, "/html/body/form[1]")
login_form_2 = driver.find_element(By.XPATH, "//form[1]")
login_form_3 = driver.find_element(By.XPATH, "//form[@id='loginForm']")
login_form_4 = driver.find_element(By.XPATH, "//form[input/@name='username']")

print("\nlogin_form_1")
print_tag_info(login_form_1)
print("\nlogin_form_2")
print_tag_info(login_form_2)
print("\nlogin_form_3")
print_tag_info(login_form_3)
print("\nlogin_form_4")
print_tag_info(login_form_4)


print("\n\n======= GET <INPUT> TAG BY XPATH: USERNAME")
username_input_1 = driver.find_element(By.XPATH, "//form[input/@name='username']/input[1]")
username_input_2 = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[1]")
username_input_3 = driver.find_element(By.XPATH, "//input[@name='username']")

print("\nusername_input_1")
print_tag_info(username_input_1)
print("\nusername_input_2")
print_tag_info(username_input_2)
print("\nusername_input_3")
print_tag_info(username_input_3)


print("\n\n======= GET <INPUT> TAG BY XPATH: CLEAR BUTTON")
clear_button_1 = driver.find_element(By.XPATH, "//input[@name='continue'][@type='button']")
clear_button_2 = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[4]")

print("\nclear_button_1")
print_tag_info(clear_button_1)
print("\nclear_button_2")
print_tag_info(clear_button_2)


# ============== LOCATING HYPERLINKS BY LINK TEXT
print("\n\n======= GET <a> TAG BY HYPERLINK TEXT: CONTINUE LINK")

continue_link_1 = driver.find_element(By.LINK_TEXT, 'Text Continue')
continue_link_2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Text Conti')

print("\ncontinue_link_1")
print_tag_info(continue_link_1)
print("\ncontinue_link_2")
print_tag_info(continue_link_2)


# ============== LOCATING BY TAG NAME
print("\n\n======= LOCATING BY TAG NAME")

heading1 = driver.find_element(By.TAG_NAME, 'h1')
print("\nheading1")
print_tag_info(heading1)

# ============== LOCATING BY CLASS NAME
print("\n\n======= LOCATING BY CLASS NAME")

content = driver.find_element(By.CLASS_NAME, 'content')
print("\ncontent")
print_tag_info(content)

# ============== LOCATING BY CSS SELECTORS
print("\n\n======= LOCATING BY CSS SELECTORS")

content = driver.find_element(By.CSS_SELECTOR, 'p.content')
print("\ncontent")
print_tag_info(content)

# ======== Sleep 5s before closing this browser
time.sleep(5)
driver.close()
