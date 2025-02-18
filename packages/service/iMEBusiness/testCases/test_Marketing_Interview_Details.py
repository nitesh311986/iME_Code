import re
import logging
import pytest
from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.Marketing import Marketing_Details
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=17)
@pytest.mark.order(17)
class Test_Marketing_Interview_View(BaseTest):

    def test_read_overall_interview_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)

        self.marketingInterviewDetails = Marketing_Details(self.driver, environment)
        self.marketingInterviewDetails.click_on_marketing_icon()
        self.marketingInterviewDetails.fetch_overall_marketing_interviews_details()

    def test_read_interview_position_application(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.marketingInterviewDetails = Marketing_Details(self.driver, environment)
        self.marketingInterviewDetails.fetch_interview_position_applicant_numbers_for_marketing()

    def test_traverse_through_list_of_interview(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.marketingInterviewDetails = Marketing_Details(self.driver, environment)
        self.marketingInterviewDetails.traverse_marketing_interview_list()

    def test_filter_interview_details_status_dd(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.marketingInterviewDetails = Marketing_Details(self.driver, environment)
        self.marketingInterviewDetails.filter_interview_details()
        self.marketingInterviewDetails.filter_interview_details_through_search()

    def test_rate_function_of_for_interview(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.marketingInterviewDetails = Marketing_Details(self.driver, environment)
        self.marketingInterviewDetails.test_your_rating_function()

    def test_multimedia_resubmission(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.marketingInterviewDetails = Marketing_Details(self.driver, environment)
        # self.marketingInterviewDetails.test_multimedia_resubmission()

    def test_interview_status_update(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.marketingInterviewDetails = Marketing_Details(self.driver, environment)
        self.marketingInterviewDetails.test_update_interview_status()

    def test_fetch_interview_transcription(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.marketingInterviewDetails = Marketing_Details(self.driver, environment)
        self.marketingInterviewDetails.fetch_interview_transcript()

    def test_create_multiway(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.marketingInterviewDetails = Marketing_Details(self.driver, environment)
        # self.marketingInterviewDetails.test_create_multiway_for_marketing()
