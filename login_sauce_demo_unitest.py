import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTests(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')

    def tearDown(self) -> None:
        self.driver.quit()

    def testWrongCredentials(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('user')
        self.driver.find_element(By.ID, 'password').send_keys('pass')
        self.driver.find_element(By.ID, 'login-button').click()
        error_text_1 = self.driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]').text
        assert error_text_1 == "Epic sadface: Username and password do not match any user in this service", 'Unexpected error message'

    def testSuccesfulLogin(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'

    def testClickLoginNoCredentials(self):
        self.driver.find_element(By.ID, 'login-button').click()
        error_text_1 = self.driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]').text
        assert error_text_1 == "Epic sadface: Username is required", 'Unexpected error message'

    def testGlitchUser(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('performance_glitch_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()
        self.driver.implicitly_wait(10)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'
