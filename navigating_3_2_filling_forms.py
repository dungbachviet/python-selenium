from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select



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
# 3.2. FILLING IN FORMS
print("\n\n3.2. FILLING IN FORMS")

# ===== Way1: Using XPath to get select tag
select_tag = driver.find_element(By.XPATH, "//select[@name='cars']")
all_option_tags = select_tag.find_elements(By.TAG_NAME, "option")
for option_tag in all_option_tags:
    print("Value is: %s" % option_tag.get_attribute("value"))
    print("Wait 1s to click other option ...")
    time.sleep(1)
    option_tag.click()

# ===== Way2: Using Select object to interact with <select> tag
time.sleep(2)
select = Select(driver.find_element(By.ID, 'cars'))
# Deselect all options inside <select> tag
select.deselect_all()
# select <option> tag at index 1, 2 (inside of <select> tag)
select.select_by_index(1)
select.select_by_index(2)

# Get all selected options
all_selected_options = select.all_selected_options
print("all_selected_options = ", all_selected_options)

# Get all options (inside <select> tag)
options = select.options
print("all options inside <select> = ", options)

# Click Submit button
time.sleep(2)
driver.find_element(By.ID, "submit").click()
driver.find_element(By.ID, "submit").submit()

# ======== Sleep 10s before closing this browser
time.sleep(10)
driver.close()
