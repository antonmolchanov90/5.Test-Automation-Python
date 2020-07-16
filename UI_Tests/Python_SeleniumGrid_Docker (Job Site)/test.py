import unittest
from selenium import webdriver


class TestJobSite(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Remote(
            command_executor='http://192.168.99.100:4444/wd/hub',
            desired_capabilities={
                'browserName': 'firefox',
                'javascriptEnabled': True
            }
        )

        self.driver.get('https://www.job.kg/')

    def test_siteOpened(self):

        assert len(self.driver.find_elements_by_class_name("site-logo-slogan"))

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":

    unittest.main(verbosity=1)
