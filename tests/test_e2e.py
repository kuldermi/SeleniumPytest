import time

from selenium.webdriver.common.by import By
from PythonE2E.utility.BaseClass import BaseClass
import  pytest

@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        self.driver.find_element ( By.XPATH , "//form/div[1]" )
        self.driver.find_element ( By.LINK_TEXT , "Forgot password?" ).click ( )

        self.driver.find_element ( By.CSS_SELECTOR , "form div input[type= 'email']" ).send_keys ( "ka@gmail.com" )
        self.driver.find_element ( By.ID , 'userPassword' ).send_keys ( "abc" )
        self.driver.find_element ( By.CSS_SELECTOR , "div input[id='confirmPassword']" ).send_keys ( "abc" )
        self.driver.find_element ( By.XPATH , "//button[text()= 'Save New Password']" ).click ( )
        time.sleep ( 2 )

