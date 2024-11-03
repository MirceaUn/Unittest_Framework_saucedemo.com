import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CartTests(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()

    def tearDown(self) -> None:
        self.driver.quit()

    def testCurrentURL(self):
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'

    def testDropdownSortAscending(self):
        dropdown = Select(self.driver.find_element(By.CLASS_NAME, 'product_sort_container'))
        dropdown.select_by_visible_text('Price (low to high)')
        web_list_prices = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
        price_list = []
        for price in web_list_prices:
            price_list.append(price.text)

        char = '$'

        for idx, ele in enumerate(price_list):
            price_list[idx] = ele.replace(char, '')

        sorted_price_list = price_list
        price_list.sort()
        assert price_list == sorted_price_list, 'Not sorted ascending'

    def testAddToCart(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        list_1 = self.driver.find_elements(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
        assert len(list_1) == 0

    def testNumberProductsInCart(self):
        self.driver.find_element(By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)').click()
        assert self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == str(1)
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        assert self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == str(3)

    def testCheckProductsInCart(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        self.assertEqual(self.driver.current_url, 'https://www.saucedemo.com/cart.html')
