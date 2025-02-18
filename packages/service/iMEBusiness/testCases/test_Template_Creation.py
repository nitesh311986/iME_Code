import re
import logging

import pytest

from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.Template_Create import Template_Create
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=3)
@pytest.mark.order(3)
class Test_Template_Creation(BaseTest):

    def test_add_minimum_requirement_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)

        self.templateCreate = Template_Create(self.driver, environment)
        self.templateCreate.click_on_template_icon()
        self.templateCreate.add_minimum_requirement()
