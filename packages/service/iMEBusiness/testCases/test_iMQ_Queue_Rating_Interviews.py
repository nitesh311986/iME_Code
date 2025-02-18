import re
import logging
import pytest
from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.pageObjects.iME_Queue_RatingPage import RatingPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=23)
@pytest.mark.order(23)
class Test_Rating_Interviews(BaseTest):

    @pytest.mark.demo
    def test_your_rating_feature(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)

        self.rating = RatingPage(self.driver, environment)
        self.rating.test_your_rating()
        self.rating.test_team_rating()

    def test_complete_rating(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.rating = RatingPage(self.driver, environment)
        self.rating.test_complete_rating()

    def test_assign_user_to_interview(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.rating = RatingPage(self.driver, environment)
        # self.rating.test_assign_user_to_interview()

    def test_update_interview_status(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.rating = RatingPage(self.driver, environment)
        self.rating.test_update_status_of_interview()

    def test_multimedia_resubmission_feature(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.rating = RatingPage(self.driver, environment)
        self.rating.test_multimedia_resubmission_feature()
