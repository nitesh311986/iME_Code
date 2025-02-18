import pytest
import logging
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.Auditions import Auditions
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.testCases.test_Base import BaseTest
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=8)
@pytest.mark.order(8)
class Test_Auditions(BaseTest):

    def test_search_function_of_auditions(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver,environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        log.logger.info(
            "Applicant logged In successfully in to the system after verifying dashboard message" + str(message))

        self.auditions = Auditions(self.driver,environment)
        self.auditions.click_on_oneWay_interview_icon()
        self.auditions.fetch_interviews_details_via_company()
        self.auditions.fetch_interviews_details_via_designation()
        self.auditions.view_details_of_interview()
