import re
import logging
import pytest
from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.iME_Video_Transcription import Ime_Queue_Video_Transcription
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=22)
@pytest.mark.order(22)
class Test_Ime_Queue_Video_Transcription(BaseTest):

    def test_fetch_video_transcription_(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)

        self.iMEqueueTranscription = Ime_Queue_Video_Transcription(self.driver, environment)
        self.iMEqueueTranscription.fetch_video_transcription()
