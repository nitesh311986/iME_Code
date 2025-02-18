import pytest
import logging
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.contentLibrary import contentLibrary
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.testCases.test_Base import BaseTest
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=13)
@pytest.mark.order(13)
class Test_ContentLibrary(BaseTest):

    def test_delete_content_function(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver,environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        log.logger.info(
            "Applicant logged In successfully in to the system after verifying dashboard message" + str(message))

        self.contentLib = contentLibrary(self.driver,environment)
        self.contentLib.click_on_content_Library()
        self.contentLib.fetch_all_details_of_content_library()
        self.contentLib.search_content_library_items_via_document_type()
        self.contentLib.search_content_library_items_via_document_title()

    def test_update_content_library(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.contentLib = contentLibrary(self.driver,environment)
        self.contentLib.update_file_title()
        self.contentLib.delete_files()
