#!/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# Page Details Class

class MainPageDetails(object):
        bomURL = 'https://bombardir.ru/'
        bomDriver = '/opt/chromedriver'
        bomAssert = 'https://bombardir.ru/france'


# Base Page Class

class BaseClass(object):
    def __init__(self, driver):
        self.driver = driver


# Bombardir Test Class

class BombardirTest(BaseClass):
    def click_main_menu(self, driver):
        bom_rus = WebDriverWait(driver, 100).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '#dropdownMenu01')))
        bom_rus.click()
        bom_eng = WebDriverWait(driver, 100).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '#dropdownMenu04')))
        bom_eng.click()
        bom_spa = WebDriverWait(driver, 100).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '#dropdownMenu05')))
        bom_spa.click()
        bom_ger = WebDriverWait(driver, 100).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '#dropdownMenu06')))
        bom_ger.click()
        bom_ita = WebDriverWait(driver, 100).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '#dropdownMenu07')))
        bom_ita.click()
        bom_fre = WebDriverWait(driver, 100).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '#dropdownMenu08')))
        bom_fre.click()
        driver.implicitly_wait(10)
