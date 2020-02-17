import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import testChromeBrowser

class testFirefox(testChromeBrowser.testChrome):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://qaie.printercloud.com/admin/index.php")


if __name__ == "__main__":
    unittest.main()