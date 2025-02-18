import pytest
import logging
from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.Application_Requirement import Application_Requirement_Create
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=4)
@pytest.mark.order(4)
class Test_Application_Requirement_Creation(BaseTest):

    def test_add_application_requirement_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        self.applicationRq = Application_Requirement_Create(self.driver, environment)
        self.applicationRq.click_on_template_icon()
        self.applicationRq.add_application_requirement()
