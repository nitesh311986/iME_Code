import pytest
import logging
from iMEApplicant.utilities.customLogger import Logger
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.pageObjects.iME_Hub_View import iMEHUbViewPage
from iMEApplicant.testCases.test_Base import BaseTest

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=14)
@pytest.mark.order(14)
class Test_iME_Hub_View(BaseTest):
    def test_fetch_list_and_details_of_iME_HUb(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver,environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        log.logger.info(
            "Applicant logged In successfully in to the system after verifying dashboard message" + str(message))

        self.iMEHub = iMEHUbViewPage(self.driver,environment)
        self.iMEHub.click_on_iME_HUb_icon()
        self.iMEHub.view_list_and_details_of_streams()
        self.iMEHub.view_list_and_details_of_folder()

    def test_filter_list_of_favourite_stream(self, wait_for_page_load,environment):
        self.iMEHub = iMEHUbViewPage(self.driver,environment)
        self.iMEHub.filter_list_of_favourite_stream()


