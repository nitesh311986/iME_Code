import pytest
import logging
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.Learning import Learning
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.testCases.test_Base import BaseTest
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=7)
@pytest.mark.order(7)
class Test_Learning(BaseTest):

    def test_search_function_of_learning(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver,environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        log.logger.info(
            "Applicant logged In successfully in to the system after verifying dashboard message" + str(message))

        self.learning = Learning(self.driver,environment)
        self.learning.click_on_oneWay_interview_icon()
        self.learning.fetch_interviews_details_via_company()
        self.learning.fetch_interviews_details_via_designation()
        self.learning.view_details_of_interview()
