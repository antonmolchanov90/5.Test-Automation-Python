#!/usr/bin/python


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import RunLiteSelectors
import RunLiteDetails


class BaseClass(object):
    def __init__(self, wd):
        self.wd = wd


class RunLiteLoginClass(BaseClass):

    def auth(self, wd):
        create_acc = WebDriverWait(self.wd, 12).until(
             EC.presence_of_element_located((By.XPATH, RunLiteSelectors.account)))
        create_acc.click()

        add_name = WebDriverWait(self.wd, 12).until(
             EC.presence_of_element_located((By.XPATH, RunLiteSelectors.place_name)))
        add_name.send_keys(RunLiteDetails.company)

        phone = WebDriverWait(self.wd, 12).until(
             EC.presence_of_element_located((By.XPATH, RunLiteSelectors.phone_number)))
        phone.send_keys(RunLiteDetails.phone_num)

        shop = WebDriverWait(self.wd, 12).until(
             EC.presence_of_element_located((By.XPATH, RunLiteSelectors.shop_name)))
        shop.send_keys(RunLiteDetails.store_name)

        email = WebDriverWait(self.wd, 12).until(
             EC.presence_of_element_located((By.XPATH, RunLiteSelectors.email_addr)))
        email.send_keys(RunLiteDetails.email_addr)

        user_new = WebDriverWait(self.wd, 12).until(
             EC.presence_of_element_located((By.XPATH, RunLiteSelectors.user_name)))
        user_new.send_keys(RunLiteDetails.user)

        new_password = WebDriverWait(self.wd, 12).until(
             EC.presence_of_element_located((By.XPATH, RunLiteSelectors.new_pass)))
        new_password.send_keys(RunLiteDetails.pwrd)

        repeat_pwrd = WebDriverWait(self.wd, 12).until(
             EC.presence_of_element_located((By.XPATH, RunLiteSelectors.repeat_pass)))
        repeat_pwrd.send_keys(RunLiteDetails.pwrd)

        create_btn = WebDriverWait(self.wd, 12).until(
             EC.presence_of_element_located((By.XPATH, RunLiteSelectors.click_create_acc)))
        create_btn.click()

    def login_failure(self, wd):
        err_name = WebDriverWait(self.wd, 12).until(
             EC.presence_of_element_located((By.XPATH, RunLiteSelectors.username)))
        err_name.send_keys("")

        err_password = WebDriverWait(self.wd, 12).until(
             EC.presence_of_element_located((By.XPATH, RunLiteSelectors.password)))
        err_password.send_keys("")

        err_button = WebDriverWait(self.wd, 12).until(
             EC.presence_of_element_located((By.XPATH, RunLiteSelectors.enter_button)))
        err_button.click()

    def login_success(self, wd):
        name = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.username)))
        name.send_keys(RunLiteDetails.user)

        password = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.password)))
        password.send_keys(RunLiteDetails.pwrd)

        button = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.enter_button)))
        button.click()

        self.wd.implicitly_wait(5)
