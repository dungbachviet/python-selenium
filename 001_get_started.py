from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# ======== Choose a browser for using: Firefox or Chrome
driver = webdriver.Firefox()
# driver = webdriver.Chrome()

# ======== Navigate browser to a specific website
driver.get("http://www.python.org")

# ======== Get title and current URL of this visted website
print("driver = ", driver)
print("driver.title = ", driver.title)
print("driver.current_url = ", driver.current_url)

# Check visited website's title must contain some text
assert "Python" in driver.title

# ======== Get an HTML tag of this visited website by `name` attribute. Ex: <input name="q">
test_element = driver.find_element(By.NAME, "q")

# Remove all content in this tag
test_element.clear()

# Type some text to this tag
test_element.send_keys("pycon")

# Continue typing Enter to this tag
test_element.send_keys(Keys.RETURN)

# Check if the error message ("No results found.") has existed in HTML source of this visited website at this moment
time.sleep(1)  # Sleep 1s for browser driver loads new HTML source of result page
assert "No results found." not in driver.page_source

# ======== Sleep 5s before closing this browser
time.sleep(5)
driver.close()
