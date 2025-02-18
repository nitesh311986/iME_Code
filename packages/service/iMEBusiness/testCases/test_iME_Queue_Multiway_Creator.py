import re
import logging
import pytest
from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.iME_Queue_Multiway_Creator import iME_Queue_Multiway_Creator
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=21)
@pytest.mark.order(21)
class Test_Ime_Queue_Multiway(BaseTest):

    @pytest.mark.smoke
    def test_iME_Multiway_Create(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)

        self.iMEqueueMultiway = iME_Queue_Multiway_Creator(self.driver, environment)
        self.iMEqueueMultiway.test_create_multiway()
        self.iMEqueueMultiway.fetch_over_all_history_of_interview()
