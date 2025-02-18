import pytest
import logging
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.pageObjects.iME_Hub_Stream_History import iMEHUbStreamHistory
from iMEApplicant.testCases.test_Base import BaseTest
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=13)
@pytest.mark.order(13)
class Test_iME_Hub_Stream_View(BaseTest):
    def test_fetch_list_and_details_of_iME_HUb_Stream_History(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        log.logger.info(
            "Applicant logged In successfully in to the system after verifying dashboard message" + str(message))

        self.iMEHubStream = iMEHUbStreamHistory(self.driver, environment)
        self.iMEHubStream.click_on_iME_HUb_icon()
        self.iMEHubStream.view_list_and_details_of_streams_history()

