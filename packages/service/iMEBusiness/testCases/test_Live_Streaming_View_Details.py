import re
import logging

import pytest

from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.Streaming import Streaming
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=10)
@pytest.mark.order(10)
class Test_Streaming(BaseTest):

    def test_view_live_streaming_list(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)

        self.streaming = Streaming(self.driver, environment)
        self.streaming.click_on_streaming_icon()
        self.streaming.fetch_live_streaming_details()
        # self.streaming.filter_live_stream_list_via_title()
        # self.streaming.view_details_of_individual_live_streaming()
        # self.streaming.update_live_streaming()
        # self.streaming.delete_live_streaming_item()
        # self.streaming.bulk_delete_live_streaming_item()

    def test_view_upload_streaming_list(self, wait_for_page_load, environment):
        self.streaming = Streaming(self.driver, environment)
        # self.streaming.fetch_upload_streaming_details()
        # self.streaming.filter_upload_stream_list_via_title()
        # # self.streaming.view_details_of_individual_upload_streaming()
        # # self.streaming.update_uploads_streaming()
        # self.streaming.delete_upload_streaming_item()
