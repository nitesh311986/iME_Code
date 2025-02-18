import pytest
import logging
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.testCases.test_Base import BaseTest
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=1)
@pytest.mark.order(1)
class Test_Login(BaseTest):


    def test_get_page_title(self, wait_for_page_load,environment):
        wait_for_page_load()
        log.logger.info("****==Log In Test Case Of Applicant Starts Here==***")
        self.loginpage = LoginPage(self.driver,environment)
        title = self.loginpage.get_lauch_page_title("iME")
        log.logger.info("Verify the title of launching page")
        print(title)
        assert title == "iME"

    def test_login_process(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.loginpage = LoginPage(self.driver,environment)
        log.logger.info("Applicant enters emailId and password and clicks on sign in button")
        message = self.loginpage.do_login(TestData.UserName, TestData.Password)
        assert message == "Dashboard"
