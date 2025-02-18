import pytest
from iMEApplicant.utilities.customLogger import Logger
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.Create_Content_Library import Create_ContentLibrary
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.testCases.test_Base import BaseTest
import logging



log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=12)
@pytest.mark.order(12)
class Test_Create_ContentLibrary(BaseTest):

    def test_create_content_library_function(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver,environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        log.logger.info(
            "Applicant logged In successfully in to the system after verifying dashboard message" + str(message))

        self.c_contentLib = Create_ContentLibrary(self.driver,environment)
        self.c_contentLib.click_on_content_Library()
        self.c_contentLib.create_content_library()