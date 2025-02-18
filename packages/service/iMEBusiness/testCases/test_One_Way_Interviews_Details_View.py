import re
import logging

import pytest

from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.One_Way_Interview_Details_View_Page import Interview_Details
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=13)
@pytest.mark.order(13)
class Test_Interview_View(BaseTest):

    def test_read_recruitment_interview_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)

        self.interviewDetails = Interview_Details(self.driver, environment)
        self.interviewDetails.click_on_interview_icon()
        self.interviewDetails.fetch_recruitment_interview_details()

    def test_read_admission_interview_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.interviewDetails = Interview_Details(self.driver, environment)
        self.interviewDetails.fetch_admission_interview_details()

    def test_read_award_interview_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.interviewDetails = Interview_Details(self.driver, environment)
        self.interviewDetails.fetch_award_interview_details()

    def test_read_marketing_interview_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.interviewDetails = Interview_Details(self.driver, environment)
        self.interviewDetails.fetch_marketing_interview_details()

    def test_read_learning_interview_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.interviewDetails = Interview_Details(self.driver, environment)
        self.interviewDetails.fetch_learning_interview_details()

    def test_read_audition_interview_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.interviewDetails = Interview_Details(self.driver, environment)
        self.interviewDetails.fetch_audition_interview_details()


