import logging

import pytest

from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.BusinessProfile import BusinessProfilePage
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=2)
@pytest.mark.order(2)
class Test_Business_Profile(BaseTest):

    def test_read_business_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        # msg = re.split(r"\s+", message)
        # assert msg[0] in "Good Afternoon Nitesh!"
        # assert message == "Business Profile"
        self.businessProfile = BusinessProfilePage(self.driver, environment)
        self.businessProfile.click_on_profile_icon()
        self.businessProfile.fetch_business_details()

    def test_read_business_subscription(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.businessProfile = BusinessProfilePage(self.driver, environment)
        self.businessProfile.fetch_subscription_details()

    def test_read_business_user(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.businessProfile = BusinessProfilePage(self.driver, environment)
        self.businessProfile.fetch_user_details()
