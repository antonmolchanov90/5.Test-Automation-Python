# Public API for testing - https://apidojo-yahoo-finance-v1.p.rapidapi.com

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import unittest
from pyassert import assert_that


class YahooFinanceApi(unittest.TestCase):

    def setUp(self):
        self.response = requests.Response()

    # Market Summary API test
    def test_YaMarketSummary(self):
        self.response = requests.request('get', 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-summary')
        assert_that(self.response.status_code).is_equal_to(401)
        assert_that(self.response.content).contains(b'{"message":"Missing RapidAPI application key. Go to https:\\/\\/docs.rapidapi.com\\/docs\\/keys to learn how to get your API application key."}')

    # Market Movers API test
    def test_MarketMovers(self):
        self.response = requests.request('get', 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-movers')
        assert_that(self.response.status_code).is_equal_to(401)
        assert_that(self.response.ok).is_false()

    # Market Quotes API test
    def test_MarketQuotes(self):
        self.response = requests.request('get', 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-quotes')
        assert_that(self.response.status_code).is_true()
        assert_that(self.response.status_code).is_equal_to(401)

    # Market Charts API test
    def test_MarketCharts(self):
        self.response = requests.request('get', 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts')
        assert_that(self.response.text).is_true()
        assert_that(self.response.headers).contains('Content-Type')

    # Market Auto-Complete API test
    def test_MarketAutoComplete(self):
        self.response = requests.request('get', 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/auto-complete')
        assert_that(self.response.url).equals('https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/auto-complete')
