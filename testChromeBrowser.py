import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


CHAR_OVERLOAD_NUM = 1024
USERNAME = 'JReyno'
PW = 'sqdH5O@97:F4Pr'
C_USERNAME = '谢谢'
C_PW = '谢谢你很多@气。气7'

class testChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("https://qaie.printercloud.com/admin/index.php")

    def test_login_page_overload(self):
        overloadstring='家' * CHAR_OVERLOAD_NUM

        loginUser = self.driver.find_element_by_id('relogin_user')
        loginUser.send_keys(overloadstring)

        loginPW = self.driver.find_element_by_id('relogin_password')
        loginPW.send_keys(overloadstring)
        loginPW.send_keys(Keys.RETURN)
        print(loginUser.get_attribute('class'))

        self.driver.refresh()

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'relogin_user')))

    def test_login_page_blank(self):
        loginBtn = self.driver.find_element_by_id("admin-login-btn")
        loginBtn.click()

        self.driver.refresh()

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'relogin_user')))

    #  throws an error due to login box not moving according to scaling of browser window
    def test_resize_screen(self):
        loginDiv = self.driver.find_element_by_id('loginmenu')
        curCoords = loginDiv.location

        self.driver.set_window_size(600, 700)
        self.assertNotEqual(curCoords, loginDiv.location)

    def test_lost_password(self):
        pwlink = self.driver.find_element_by_id('forgot-password')
        pwlink.click()

        self.assertNotEqual("https://qaie.printercloud.com/admin/index.php", self.driver.current_url)

    def test_valid_user(self):
        loginUser = self.driver.find_element_by_id('relogin_user')
        loginPW =  self.driver.find_element_by_id('relogin_password')
        loginUser.send_keys(USERNAME)
        loginPW.send_keys('passwordThatsReallyGood')
        loginPW.send_keys(Keys.RETURN)

        self.driver.refresh()

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'relogin_user')))

    def test_valid_password(self):
        loginUser = self.driver.find_element_by_id('relogin_user')
        loginPW = self.driver.find_element_by_id('relogin_password')
        loginUser.send_keys('JLeno')
        loginPW.send_keys(PW)
        loginPW.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'relogin_user')))

    def test_valid_credentials(self):
        loginUser = self.driver.find_element_by_id('relogin_user')
        loginPW = self.driver.find_element_by_id('relogin_password')
        loginUser.send_keys(USERNAME)
        loginPW.send_keys(PW)
        loginPW.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.ID, 'relogin_user')))

    def test_invalid_then_valid_return(self):
        loginUser = self.driver.find_element_by_id('relogin_user')
        loginPW = self.driver.find_element_by_id('relogin_password')
        loginUser.send_keys(USERNAME)
        loginPW.send_keys('sqdH50@97:F4Pr')
        loginPW.send_keys(Keys.RETURN)

        self.driver.refresh()  # This is done to ensure driver doesn't get ahead of itself.

        loginUser = self.driver.find_element_by_id('relogin_user')
        loginPW = self.driver.find_element_by_id('relogin_password')
        loginUser.send_keys(USERNAME)
        loginPW.send_keys(PW)
        loginPW.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.ID, 'relogin_user')))

    def test_invalid_then_valid_click(self):
        loginUser = self.driver.find_element_by_id('relogin_user')
        loginPW = self.driver.find_element_by_id('relogin_password')
        loginBtn = self.driver.find_element_by_id("admin-login-btn")
        loginUser.send_keys(USERNAME)
        loginPW.send_keys('sqdH50@97:F4Pr')
        loginBtn.click()

        self.driver.refresh()  # This is done to ensure driver doesn't get ahead of itself.

        loginUser = self.driver.find_element_by_id('relogin_user')
        loginPW = self.driver.find_element_by_id('relogin_password')
        loginBtn = self.driver.find_element_by_id("admin-login-btn")
        loginUser.send_keys(USERNAME)
        loginPW.send_keys(PW)
        loginBtn.click()

        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.ID, 'relogin_user')))

    # Note: Accepts chinese user, but does not allow login even when copied and pasted manually
    def test_valid_c_credentials(self):
        loginUser = self.driver.find_element_by_id('relogin_user')
        loginPW = self.driver.find_element_by_id('relogin_password')
        loginUser.send_keys(C_USERNAME)
        loginPW.send_keys(C_PW)
        loginPW.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.ID, 'relogin_user')))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

