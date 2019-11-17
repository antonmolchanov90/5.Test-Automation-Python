#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from selenium import webdriver
from Bombardir_PageObject import*
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-gpu')


# Test Bombardir football site - simple positive test case

class CheckBombardir(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(MainPageDetails.bomDriver, options=chrome_options)
        self.driver.get(MainPageDetails.bomURL)

    def test_simpleBombardirTest(self):
        bombardir = BombardirTest(self.driver)
        bombardir.click_main_menu(self.driver)
        self.assertIn(MainPageDetails.bomAssert, self.driver.current_url)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
            unittest.main()
