import logging

import pytest

from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.Create_Live_Stream import Create_Live_Stream
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=8)
@pytest.mark.order(8)
class Test_Create_Live_Stream(BaseTest):

    def test_create_live_stream(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        self.liveStream = Create_Live_Stream(self.driver, environment)
        self.liveStream.click_on_streaming_icon()
        self.liveStream.create_live_streaming()
        # self.liveStream.create_folder()
