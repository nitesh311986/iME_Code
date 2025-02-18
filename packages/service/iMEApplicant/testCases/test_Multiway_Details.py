import pytest
import logging
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.Multiway_Details import Multiway_Details
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.testCases.test_Base import BaseTest
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=11)
@pytest.mark.order(11)
class Test_Multiway_Details(BaseTest):

    def test_fetch_list_of_multiway_interview(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver,environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        log.logger.info(
            "Applicant logged In successfully in to the system after verifying dashboard message" + str(message))

        self.multiWay = Multiway_Details(self.driver,environment)
        self.multiWay.click_on_multiWay_interview_icon()
        self.multiWay.fetch_multiway_interviews_details()

    def test_filter_multiway_interviews(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.multiWay = Multiway_Details(self.driver,environment)
        self.multiWay.filter_the_multiway_interview_via_designation()
        self.multiWay.filter_the_multiway_interview_via_company()
        self.multiWay.filter_the_multiway_interview_via_status()

    def test_fetch_details_of_individual_interview(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.multiWay = Multiway_Details(self.driver,environment)
        # self.multiWay.fetch_details_of_individual_interview()
