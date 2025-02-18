import re
import logging
import pytest
from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.Awards import Awards_Details
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


@pytest.mark.run(order=16)
@pytest.mark.order(16)
class Test_Award_Interview_View(BaseTest):
    @pytest.mark.demo
    def test_read_overall_interview_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        self.awInterviewDetails = Awards_Details(self.driver, environment)
        self.awInterviewDetails.click_on_award_icon()
        self.awInterviewDetails.fetch_overall_award_interviews_details()

    def test_read_interview_position_application(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.awInterviewDetails = Awards_Details(self.driver, environment)
        self.awInterviewDetails.fetch_interview_position_applicant_numbers_for_award()

    def test_traverse_through_list_of_interview(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.awInterviewDetails = Awards_Details(self.driver, environment)
        self.awInterviewDetails.traverse_award_interview_list()

    def test_filter_interview_details_status_dd(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.awInterviewDetails = Awards_Details(self.driver, environment)
        self.awInterviewDetails.filter_interview_details()
        self.awInterviewDetails.filter_interview_details_through_search()

    def test_rate_function_of_for_interview(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.awInterviewDetails = Awards_Details(self.driver, environment)
        self.awInterviewDetails.test_your_rating_function()

    def test_multimedia_resubmission(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.awInterviewDetails = Awards_Details(self.driver, environment)
        # self.awInterviewDetails.test_multimedia_resubmission()

    def test_interview_status_update(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.awInterviewDetails = Awards_Details(self.driver, environment)
        self.awInterviewDetails.test_update_interview_status()

    def test_fetch_interview_transcription(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.awInterviewDetails = Awards_Details(self.driver, environment)
        self.awInterviewDetails.fetch_interview_transcript()

    def test_create_multiway(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.awInterviewDetails = Awards_Details(self.driver, environment)
        # self.awInterviewDetails.test_create_multiway_for_award()
