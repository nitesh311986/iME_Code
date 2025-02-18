import pytest
import logging
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.Awards import Awards
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.testCases.test_Base import BaseTest
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=5)
@pytest.mark.order(5)
class Test_Award(BaseTest):

    def test_search_function_of_awards(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver,environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        log.logger.info(
            "Applicant logged In successfully in to the system after verifying dashboard message" + str(message))

        self.awards = Awards(self.driver,environment)
        self.awards.click_on_oneWay_interview_icon()
        self.awards.fetch_interviews_details_via_company()
        self.awards.fetch_interviews_details_via_designation()
        self.awards.view_details_of_interview()
