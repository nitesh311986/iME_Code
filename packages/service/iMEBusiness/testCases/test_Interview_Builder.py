import re
import logging
import pytest
from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.Interview_Builder import Interview_Builder
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=7)
@pytest.mark.order(7)
class Test_Interview_Builder(BaseTest):

    def test_build_recruitment_interview(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)

        self.interviewBuilder = Interview_Builder(self.driver, environment)
        self.interviewBuilder.click_on_interview_builder_icon()
        self.interviewBuilder.create_interview_for_recruitment()
        self.interviewBuilder.create_interview_for_award()
        self.interviewBuilder.create_interview_for_marketing()
        self.interviewBuilder.create_interview_for_learning()
        self.interviewBuilder.create_interview_for_audition()
        self.interviewBuilder.create_interview_for_admission()
