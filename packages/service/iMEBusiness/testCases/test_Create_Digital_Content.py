import logging

import pytest

from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.Digital_Content_Create import Digital_Content_Create
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=9)
@pytest.mark.order(9)
class Test_Create_Digital_Content(BaseTest):

    def test_create_digital_content(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        self.digitalContent = Digital_Content_Create(self.driver, environment)
        self.digitalContent.click_on_digital_content_icon()
        self.digitalContent.create_digital_content_item()
        self.digitalContent.create_digital_content_folder()
        # self.digitalContent.create_item_under_folder()
