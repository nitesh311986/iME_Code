import pytest
import logging
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.Marketing import Marketing
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.testCases.test_Base import BaseTest
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=6)
@pytest.mark.order(6)
class Test_Marketing(BaseTest):

    def test_search_function_of_marketing(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver,environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        log.logger.info(
            "Applicant logged In successfully in to the system after verifying dashboard message" + str(message))

        self.marketing = Marketing(self.driver,environment)
        self.marketing.click_on_oneWay_interview_icon()
        self.marketing.fetch_interviews_details_via_company()
        self.marketing.fetch_interviews_details_via_designation()
        self.marketing.view_details_of_interview()
