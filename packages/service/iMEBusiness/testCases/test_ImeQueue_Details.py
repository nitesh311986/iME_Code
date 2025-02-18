import re
import logging
import pytest
from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.IMEQueue import ImeQueue_Details
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=24)
@pytest.mark.order(24)
class Test_Ime_Queue_View(BaseTest):

    @pytest.mark.smoke
    def test_read_overall_interview_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)

        self.iMEqueueDetails = ImeQueue_Details(self.driver, environment)
        self.iMEqueueDetails.click_on_imeQueue_icon()
        self.iMEqueueDetails.fetch_overall_iMEQueue_details()

    def test_read_interview_position_application(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.iMEqueueDetails = ImeQueue_Details(self.driver, environment)
        self.iMEqueueDetails.fetch_interview_iME_Queue()

    def test_filter_iME_Queue(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.iMEqueueDetails = ImeQueue_Details(self.driver, environment)
        self.iMEqueueDetails.filter_interview_details()
        self.iMEqueueDetails.filter_interview_details_on_status()
        self.iMEqueueDetails.filter_interview_details_by_designation()
