import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class login_scenario(unittest.TestCase):
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

    # both valid
    def test_login_valid(self):
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        if driver.find_element(By.XPATH, "//p[contains(text(),'SAKSHI WADHWANI')]").is_displayed():
            print("Test Pass-Logged Successfully")
        else:
            print("Test Fail-Report The Issue")

    # both invalid inputs
    def test_log_invalid(self):
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admi")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin12")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        if driver.find_element(By.XPATH,
                               "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/p[1]").is_displayed():
            print("Test Pass-Unable to log with invalid data")
        else:
            print("Test Fail-Report The Issue")

    # without input
    def test_withoutdata(self):
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys()
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys()
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        if driver.find_element(By.CSS_SELECTOR,
                               "div.orangehrm-login-layout div.orangehrm-login-layout-blob div.orangehrm-login-container div.orangehrm-login-slot-wrapper div.orangehrm-login-slot div.orangehrm-login-form form.oxd-form:nth-child(2) div.oxd-form-row:nth-child(2) div.oxd-input-group.oxd-input-field-bottom-space > span.oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message:nth-child(3)").is_displayed():
            print("Test Pass")
        else:
            print("Test Fail")

    # With VEIP
    def test_VEIP(self):
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        if driver.find_element(By.XPATH,
                               "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/p[1]").is_displayed():
            print("Test Pass-Unable to log with invalid data")
        else:
            print("Test Fail-Report The Issue")

    # With VEWP
    def test_VEWP(self):
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Admin")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        if driver.find_element(By.CSS_SELECTOR,
                               "div.orangehrm-login-layout div.orangehrm-login-layout-blob div.orangehrm-login-container div.orangehrm-login-slot-wrapper div.orangehrm-login-slot div.orangehrm-login-form form.oxd-form:nth-child(2) div.oxd-form-row:nth-child(2) div.oxd-input-group.oxd-input-field-bottom-space > span.oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message:nth-child(3)").is_displayed():
            print("Test Pass")
        else:
            print("Test Fail")

    # with wevp
    def test_wevp(self):
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys()
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        if driver.find_element(By.CSS_SELECTOR,
                               "div.orangehrm-login-layout div.orangehrm-login-layout-blob div.orangehrm-login-container div.orangehrm-login-slot-wrapper div.orangehrm-login-slot div.orangehrm-login-form form.oxd-form:nth-child(2) div.oxd-form-row:nth-child(2) div.oxd-input-group.oxd-input-field-bottom-space > span.oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message:nth-child(3)").is_displayed():
            print("Test Pass")
        else:
            print("Test Fail")


    def test_forget_pwd(self):
        driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']").click()
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        if driver.find_element(By.CSS_SELECTOR, "div.orangehrm-forgot-password-container div.orangehrm-forgot-password-wrapper div.orangehrm-card-container form.oxd-form div.oxd-form-row:nth-child(5) div.oxd-input-group.oxd-input-field-bottom-space > span.oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message:nth-child(3)").is_displayed():
            print("Test Pass-Mandatory alert display")
        else:
            print("Test Fail-report issue")
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Test")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        if driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) div.orangehrm-forgot-password-container div.orangehrm-forgot-password-wrapper div.orangehrm-card-container > h6.oxd-text.oxd-text--h6.orangehrm-forgot-password-title:nth-child(1)").is_displayed():
            print("Test Pass-Reset PWD displayed")
        else:
            print("Test Fail-not displayed report issue")


    def TearDown(self):
        driver.close()




if __name__ == '__main__':
    unittest.main()
