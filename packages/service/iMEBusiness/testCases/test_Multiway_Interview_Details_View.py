import logging
import pytest
from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.Multiway_Details_View import Multiway_Interview_Details
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=14)
@pytest.mark.order(14)
class Test_Multiway_Interview_View(BaseTest):

    def test_read_multiway_interview_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        # msg = re.split(r"\s+", message)
        # assert msg[0] in "Good Afternoon Nitesh!"
        # assert message == "Business Profile"
        self.mulInterviewDetails = Multiway_Interview_Details(self.driver, environment)
        self.mulInterviewDetails.click_on_interview_icon()
        # self.mulInterviewDetails.view_multiway_invites_details()


    def test_fetch_details_of_video_call_pf_multiway_interview(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.mulInterviewDetails = Multiway_Interview_Details(self.driver, environment)
        self.mulInterviewDetails.view_details_of_video_call_of_multiway_interview()

    def test_fetch_details_of_webinar_of_multiway_interview(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.mulInterviewDetails = Multiway_Interview_Details(self.driver, environment)
        self.mulInterviewDetails.view_details_of_webinar_of_multiway_interview()


