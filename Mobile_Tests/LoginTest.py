#!/usr/bin/python


from appium import webdriver
import time
import unittest
import os


class LoginTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['appium-version'] = '1.17'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['app'] = os.path.abspath('/home/anton/1.ANTON/Documents/1Work/1.QA/Test-Automation/Mobile_Tests/AUT.apk')

        self.wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        self.wd.implicitly_wait(30)

    def tearDown(self):
        self.wd.quit()

    def test_login_fail(self):
        self.wd.find_element_by_id("com.example.mkim.aut:id/email").send_keys("")
        self.wd.find_element_by_id("com.example.mkim.aut:id/email").send_keys("")
        click_btn = self.wd.find_element_by_id("com.example.mkim.aut:id/email_sign_in_button")
        click_btn.click()

        self.assertTrue(click_btn.is_displayed())


if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
        unittest.TextTestRunner(verbosity=2).run(suite)
