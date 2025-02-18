import re
import logging
import pytest
from iMEExternalUser.Config.config import TestData
from iMEExternalUser.testCases.test_Base import BaseTest
from iMEExternalUser.Utilities.customLogger import Logger
from iMEExternalUser.pageObjects.LoginPage import LoginPage
from iMEExternalUser.pageObjects.Notification import Notification_Details

log = Logger(__name__, logging.INFO)


# @pytest.mark.order(3)

class Test_Notification_View(BaseTest):
    @pytest.mark.smoke
    def test_read_notification_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        # assert message == "iME Queue"
        # if "Pritesh!" in message:
        self.notificationDetails = Notification_Details(self.driver, environment)
        self.notificationDetails.click_on_notificationIcon()
        # self.notificationDetails.fetch_notification_details()
        # else:
        #     assert False
