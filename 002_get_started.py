import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class PythonOrgSearch(unittest.TestCase):
    """Setup Unit Test For A Website"""

    def setUp(self):
        """Setup and open new browser driver before running each test case"""
        self.driver = webdriver.Firefox()

    def test_search_in_python_org_001(self):
        """Test Case 1: Method name should start with prefix of test_ to be valid"""

        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        test_element = driver.find_element(By.NAME, "q")
        test_element.send_keys("pycon")
        test_element.send_keys(Keys.RETURN)

        time.sleep(1)  # Sleep a bit for loading new HTML content
        self.assertNotIn("No results found.", driver.page_source)


    def test_search_in_python_org_002(self):
        """Test Case 2: Method name should start with prefix of test_ to be valid"""

        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        test_element = driver.find_element(By.NAME, "q")
        test_element.send_keys("pycon222")
        test_element.send_keys(Keys.RETURN)

        time.sleep(1)  # Sleep a bit for loading new HTML content
        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        """Close browser after finishing each test case"""
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
