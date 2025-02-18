import pytest
import logging
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.iME_Queue_Page import iME_Queue
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.testCases.test_Base import BaseTest
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=3)
@pytest.mark.order(3)
class Test_iME_Queue(BaseTest):

    def test_search_function_of_ime_queue(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver,environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        log.logger.info(
            "Applicant logged In successfully in to the system after verifying dashboard message" + str(message))

        self.iMEQueue = iME_Queue(self.driver,environment)
        self.iMEQueue.click_on_iME_Queue_icon()
        self.iMEQueue.fetch_interviews_details_via_service()
        self.iMEQueue.fetch_interviews_details_via_company()
        self.iMEQueue.fetch_interviews_details_via_designation()

    def test_fetch_details_of_individual_interview(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.iMEQueue = iME_Queue(self.driver,environment)
        self.iMEQueue.view_details_of_individual_interview()

    def test_verify_status_of_interview(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.iMEQueue = iME_Queue(self.driver,environment)
        # self.iMEQueue.verify_status_of_accepted_interview()


