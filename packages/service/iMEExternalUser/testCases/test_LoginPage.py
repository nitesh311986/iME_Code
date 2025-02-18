import json
import logging
import pytest
from iMEExternalUser.Config.config import TestData
from iMEExternalUser.testCases.test_Base import BaseTest
from iMEExternalUser.Utilities.customLogger import Logger
from iMEExternalUser.pageObjects.LoginPage import LoginPage

log = Logger(__name__, logging.INFO)



# @pytest.mark.order(1)
class Test_Login(BaseTest):

    @pytest.mark.smoke
    def test_get_page_title(self, wait_for_page_load, environment):
        log.logger.info("****==Log In Test Case Of Applicant Starts Here==***")
        wait_for_page_load()
        self.loginpage = LoginPage(self.driver, environment)
        title = self.loginpage.get_launch_page_title("iME")
        log.logger.info("Verify the title of launching page")
        print(title)
        # assert title == "iME"

    @pytest.mark.smoke
    def test_login_process(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginpage = LoginPage(self.driver, environment)
        log.logger.info("External User enters emailId and password and clicks on sign in button")
        message = self.loginpage.do_login(TestData.UserName, TestData.Password)
        # assert message == "iME Queue"
        # if "Pritesh!" in message:
        #     log.logger.info("External User logged In successfully in to the system ")
        # else:
        #     assert False
