import logging

import pytest

from iMEBusiness.Utilities.customLogger import Logger
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.pageObjects.Digital_Content_View import Digital_Content_View
from iMEBusiness.Config.Config import TestData

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=11)
@pytest.mark.order(11)
class Test_Digital_Content_View(BaseTest):

    def test_read_overall_digital_content_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)

        self.digitalContent = Digital_Content_View(self.driver, environment)
        self.digitalContent.click_on_digital_content_icon()
        self.digitalContent.fetch_digital_content_details()

    def test_view_details_of_each_document(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.digitalContent = Digital_Content_View(self.driver, environment)
        # self.digitalContent.test_fetch_details_of_each_document()

    def test_delete_individual_items(self, wait_for_page_load, environment):
        self.digitalContent = Digital_Content_View(self.driver, environment)
        self.digitalContent.test_delete_individual_item()
        self.digitalContent.test_delete_bulk_item()
