import pytest
import logging
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.Recruitments import Recruitment
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.testCases.test_Base import BaseTest
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=4)
@pytest.mark.order(4)
class Test_Recruitment(BaseTest):

    def test_search_function_of_recruitment(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver,environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        log.logger.info(
            "Applicant logged In successfully in to the system after verifying dashboard message" + str(message))

        self.recruitment = Recruitment(self.driver,environment)
        self.recruitment.click_on_oneWay_interview_icon()
        self.recruitment.fetch_interviews_details_via_company()
        self.recruitment.fetch_interviews_details_via_designation()
        self.recruitment.view_details_of_interview()
