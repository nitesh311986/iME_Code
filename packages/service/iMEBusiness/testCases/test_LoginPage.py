import re
import logging
import pytest
from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=1)
@pytest.mark.order(1)
class Test_Login(BaseTest):
    @pytest.mark.smoke
    def test_get_page_title(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        title = self.loginPage.get_launch_page_title("iME")
        assert title == "iME"

    @pytest.mark.smoke
    def test_login_process(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        # //msg = re.split(r"\s+", message)
        # assert message == "Business Profile"
