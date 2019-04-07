#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#NEGATIVE TEST

#Open browser, enter Facebook
driver = webdriver.Chrome("/opt/chromedriver")
driver.get("https://www.facebook.com")

#Locate elements, pass email & password (both empty), click Log In button
driver.find_element_by_id("email").send_keys("")
driver.find_element_by_id("pass").send_keys("")
driver.find_element_by_id("loginbutton").click()

#Assert successfull login
if driver.title == 'Log into Facebook | Facebook':
 print('Passed')
else:
 print('Error')

#Close browser
driver.quit()
