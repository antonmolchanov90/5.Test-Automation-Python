#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from FacebookLogin_Locators import*
from FacebookLogin_Credentials import*


# POSITIVE CASE - SIMPLE VERIFICATION

# Open browser, enter Facebook
driver = webdriver.Chrome("/home/anton/ANTON/Documents/1.Работа/1.QA/Test-Automation/UI_Tests/Python_Selenium (Facebook LogIn)/chromedriver")
driver.get("https://www.facebook.com")

# Locate elements, pass email & password (both empty), click Log In button
driver.find_element_by_id(email).send_keys(emailAddress)
driver.find_element_by_id(passWord).send_keys(passwordAccess)
driver.find_element_by_id(loginButton).click()

# Assert successful login
if driver.title == 'Facebook':
    print('Passed!')
else:
    print('Failed!')

# Close browser
driver.quit()


# NEGATIVE CASE 1

# Open browser, enter Facebook
driver = webdriver.Chrome("/opt/chromedriver")
driver.get("https://www.facebook.com")

# Locate elements, pass email & password (both empty), click Log In button
driver.find_element_by_id(email).send_keys("")
driver.find_element_by_id(passWord).send_keys("")
driver.find_element_by_id(loginButton).click()

# Assert unsuccessful login
if driver.title == 'Log into Facebook | Facebook':
    print('Passed!')
else:
    print('Failed!')

# Close browser
driver.quit()


# NEGATIVE CASE 2

# Open browser, enter Facebook
driver = webdriver.Chrome("/opt/chromedriver")
driver.get("https://www.facebook.com")

# Locate elements, pass email & password (both empty), click Log In button
driver.find_element_by_id(email).send_keys(emailAddress)
driver.find_element_by_id(passWord).send_keys("")
driver.find_element_by_id(loginButton).click()

# Assert unsuccessful login
if driver.title == 'Log into Facebook | Facebook':
    print('Passed!')
else:
    print('Failed!')

# Close browser
driver.quit()
