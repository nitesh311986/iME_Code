import re
import logging
import pytest
from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.Notification import Notification_Details
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)



class Test_Notification_View(BaseTest):

    def test_read_notification_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)

        self.notificationDetails = Notification_Details(self.driver, environment)
        # self.notificationDetails.click_on_notificationIcon()
        # self.notificationDetails.fetch_notification_details()
