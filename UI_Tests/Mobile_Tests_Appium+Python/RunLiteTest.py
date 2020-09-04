#!/usr/bin/python

from RunLiteLogin import*
from appium import webdriver
import unittest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import RunLiteSelectors
import RunLiteDetails


class RunLiteAppTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['appium-version'] = '1.17'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['udid'] = '2d159657'
        desired_caps['app'] = os.path.abspath(
            '/home/anton/1.ANTON/Documents/1Work/1.QA/Test-Automation/Mobile_Tests_Appium+Python/run-lite.apk')
        self.wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        self.wd.implicitly_wait(10)

    def tearDown(self):
        self.wd.quit()

    # def test_register(self):
        # create_new = RunLiteLoginClass(self.wd)
        # create_new.auth(self.wd)

    def test_login_user_fail(self):
        error_login = RunLiteLoginClass(self.wd)
        error_login.login_failure(self.wd)

        button_displayed = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.enter_button)))
        self.assertTrue(button_displayed.is_displayed())

    def test_login_user_success(self):
        success_login = RunLiteLoginClass(self.wd)
        success_login.login_success(self.wd)

    def test_create_cashier(self):
        success_login = RunLiteLoginClass(self.wd)
        success_login.login_success(self.wd)

        cashier_sum = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.enter_sum)))
        cashier_sum.send_keys(RunLiteDetails.sum_amount)

        cashier_open = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.open_cashier)))
        cashier_open.click()

        confirm_cashier_open = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.cashier_open_confirm)))
        confirm_cashier_open.click()

        self.wd.implicitly_wait(5)

        check_cashier_open = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.assert_cashier_open)))
        self.assertTrue(check_cashier_open.is_displayed())

        self.wd.implicitly_wait(5)

    def test_operation_prihod(self):
        success_login = RunLiteLoginClass(self.wd)
        success_login.login_success(self.wd)

        open_profile = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.user_profile)))
        open_profile.click()

        open_management = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.management_tab)))
        open_management.click()

        open_menu_main = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.main_menu_open)))
        open_menu_main.click()

        self.wd.implicitly_wait(3)
        click_prihod = self.wd.find_element_by_accessibility_id(RunLiteSelectors.new_prihod)
        click_prihod.click()

        add_prihod = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.prihod_add_new)))
        add_prihod.click()

        choose_sklad = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.sklad_click)))
        choose_sklad.click()

        osnovnoi_sklad = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.main_sklad)))
        osnovnoi_sklad.click()

        click_dalee = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.next_btn)))
        click_dalee.click()

        pick_category = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.category_choose)))
        pick_category.click()

        click_category = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.category_new)))
        click_category.click()

        click_sub_category = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.sub_cat_click)))
        click_sub_category.click()

        choose_sub_cat = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.new_sub)))
        choose_sub_cat.click()

        click_choose_product = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.pick_product)))
        click_choose_product.click()

        next_again = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.more_next)))
        next_again.click()

        set_quantity = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.quantity)))
        set_quantity.send_keys(RunLiteDetails.test_quantity)

        set_price = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.price)))
        set_price.send_keys(RunLiteDetails.cost)

        supply = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.supplier)))
        supply.click()

        pick_supplier = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.postavshik)))
        pick_supplier.click()

        ready_btn = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.click_ready)))
        ready_btn.click()

        ok_added = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.added_prihod)))
        ok_added.click()

        check_prihod_added = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.assert_prihod)))
        self.assertTrue(check_prihod_added.is_displayed())

    def test_operation_rashod(self):
        success_login = RunLiteLoginClass(self.wd)
        success_login.login_success(self.wd)

        click_category = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.category_pick)))
        click_category.click()

        click_sub_cat = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.sub_kat)))
        click_sub_cat.click()

        add_to_cart = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.cart_add)))
        add_to_cart.click()

        self.wd.implicitly_wait(5)
        in_cart = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.cart_go)))
        in_cart.click()

        sell_product = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.sell_it)))
        sell_product.click()

        sell_confirm = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.sell_alert)))
        sell_confirm.click()

        check_rashod_added = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.category_pick)))
        self.assertTrue(check_rashod_added.is_displayed())

    def test_close_cashier(self):
        success_login = RunLiteLoginClass(self.wd)
        success_login.login_success(self.wd)

        open_op = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.cashier_operations)))
        open_op.click()

        close_cash_click = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.close_cash)))
        close_cash_click.click()

        enter_amount = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.add_amount)))
        enter_amount.send_keys(RunLiteDetails.cashier_num)

        conf_cash_close = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.close_cash_confirm)))
        conf_cash_close.click()

        cash_closed_alert = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.cashier_is_closed)))
        cash_closed_alert.click()

        cash_closed_check = WebDriverWait(self.wd, 12).until(
            EC.presence_of_element_located((By.XPATH, RunLiteSelectors.assert_cash_is_closed)))
        self.assertTrue(cash_closed_check.is_displayed())
