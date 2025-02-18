import pytest
import logging
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.Admission import Admission
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.testCases.test_Base import BaseTest
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=9)
@pytest.mark.order(9)
class Test_Admission(BaseTest):
    @pytest.mark.smoke
    def test_search_function_of_admission(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        log.logger.info(
            "Applicant logged In successfully in to the system after verifying dashboard message" + str(message))

        self.admission = Admission(self.driver, environment)
        self.admission.click_on_oneWay_interview_icon()
        self.admission.fetch_interviews_details_via_company()
        self.admission.fetch_interviews_details_via_designation()
        self.admission.view_details_of_interview()
