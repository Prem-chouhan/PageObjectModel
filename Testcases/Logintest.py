import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
import time

sys.path.insert(0, '/home/admin-1/PycharmProjects/pageobjectmodel')
from PageObjects.LoginPage import LoginPage


class LoginTest(unittest.TestCase):
    baseURL = "https://www.linkedin.com/home"
    username = "wankhadechetan281@gmail.com"
    password = "Chetan@95"

    driver = webdriver.Firefox()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)

    def test_Login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Security Verification | LinkedIn", self.driver.title, "Title didn't Match")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/admin-1/PycharmProjects/pageobjectmodel/reports"))
