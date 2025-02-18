import re
import logging
import pytest
from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.Admission import Admission_Details
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=20)
@pytest.mark.order(20)
class Test_Admission_Interview_View(BaseTest):

    def test_read_overall_interview_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        self.admInterviewDetails = Admission_Details(self.driver, environment)
        self.admInterviewDetails.click_on_admission_icon()
        self.admInterviewDetails.fetch_overall_admission_interviews_details()

    def test_read_interview_position_application(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.admInterviewDetails = Admission_Details(self.driver, environment)
        self.admInterviewDetails.fetch_interview_position_applicant_numbers_for_admission()

    def test_traverse_through_list_of_interview(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.admInterviewDetails = Admission_Details(self.driver, environment)
        self.admInterviewDetails.traverse_admission_interview_list()

    def test_filter_interview_details_status_dd(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.admInterviewDetails = Admission_Details(self.driver, environment)
        self.admInterviewDetails.filter_interview_details()
        self.admInterviewDetails.filter_interview_details_through_search()

    def test_rate_function_of_for_interview(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.admInterviewDetails = Admission_Details(self.driver, environment)
        self.admInterviewDetails.test_your_rating_function()

    def test_multimedia_resubmission(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.admInterviewDetails = Admission_Details(self.driver, environment)
        # self.admInterviewDetails.test_multimedia_resubmission()

    def test_update_interview_status(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.admInterviewDetails = Admission_Details(self.driver, environment)
        self.admInterviewDetails.test_update_interview_status()

    def test_fetch_interview_transcription(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.admInterviewDetails = Admission_Details(self.driver, environment)
        self.admInterviewDetails.fetch_interview_transcript()

    def test_fetch_create_multiway(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.admInterviewDetails = Admission_Details(self.driver, environment)
        # self.admInterviewDetails.test_create_multiway_of_admission()
