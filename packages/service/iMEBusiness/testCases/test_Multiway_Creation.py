import logging
import pytest
from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.pageObjects.Multiway_Item_Creation import Multiway_Item_Creation
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=25)
@pytest.mark.order(25)
class Test_Multiway_Creation(BaseTest):

    def test_create_multiway_creation(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        self.mulItemCreation = Multiway_Item_Creation(self.driver, environment)
        self.mulItemCreation.click_on_interview_icon()
        self.mulItemCreation.create_multiway_video_call()
        self.mulItemCreation.create_multiway_webinar()
