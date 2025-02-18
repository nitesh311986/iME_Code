import re
import logging
import pytest
from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.AnalyticsPage import Analytics_Details
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)



class Test_Analytical_Details(BaseTest):

    @pytest.mark.demo
    def test_read_overall_analytical_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        # msg = re.split(r"\s+", message)
        # assert msg[0] in "Good Afternoon Nitesh!"
        # assert message == "Business Profile"
        self.analyticalDetails = Analytics_Details(self.driver, environment)
        # self.analyticalDetails.click_on_analytics_icon()
        # self.analyticalDetails.fetch_overall_interview_details()
