#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from selenium import webdriver
from Bombardir_PageObject import *


# Test Bombardir football site - simple positive test case


class CheckBombardir(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(MainPageDetails.bomDriver)
        self.driver.get(MainPageDetails.bomURL)

    def test_simpleBombardirTest(self):
        bombardir = BombardirTest(self.driver)
        bombardir.click_main_menu(self.driver)
        self.assertIn(MainPageDetails.bomAssert, self.driver.current_url)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
            unittest.main()
