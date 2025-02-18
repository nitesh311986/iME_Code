import re
import logging
import pytest
from iMEExternalUser.pageObjects.LoginPage import LoginPage
from iMEExternalUser.pageObjects.iME_Queue_RatingPage import RatingPage
from iMEExternalUser.testCases.test_Base import BaseTest
from iMEExternalUser.Utilities.customLogger import Logger
from iMEExternalUser.Config.config import TestData

log = Logger(__name__, logging.INFO)



# @pytest.mark.order(2)
class Test_Rating_Interviews(BaseTest):
    @pytest.mark.smoke
    def test_your_rating_feature(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        # assert message == "iME Queue"
        # if "Pritesh!" in message:

        self.rating = RatingPage(self.driver, environment)
        self.rating.test_your_rating()
        log.logger.info("User Is On" + environment)

    @pytest.mark.smoke
    def test_team_rating_feature(self, environment):
        self.rating = RatingPage(self.driver, environment)
        self.rating.test_team_rating()

    @pytest.mark.smoke
    def test_complete_rating_feature(self, environment):
        self.rating = RatingPage(self.driver, environment)
        self.rating.test_complete_rating()
