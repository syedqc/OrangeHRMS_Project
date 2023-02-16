import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class search_scenario(unittest.TestCase):
    def setUp(self):
        global driver
        ch_options = Options()
        ch_options.add_experimental_option("detach", True)
        ch_options.add_argument("--incognito")
        driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe", options=ch_options)
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.implicitly_wait(5)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def test_searchvalid(self):
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("admin")
        Result= driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']").text

        if Result== "Admin":
            print("Test Pass-Search working fine")
        else:
            print("Test Fail-Report issue")

    def test_searchvalid1(self):
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("min")
        Result= driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']").text

        if Result== "Admin":
            print("Test Pass-Search working fine")
        else:
            print("Test Fail-Report issue")

    def tearDown(self) -> None:
        driver.close()
if __name__ == "__main__":
    unittest.main()
