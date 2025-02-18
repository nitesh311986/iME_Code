import re
import logging

import pytest

from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.Multimedia_create import Multimedia_Create
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=6)
@pytest.mark.order(6)
class Test_Multimedia_Creation(BaseTest):

    def test_add_multimedia(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)

        self.multimediaCreate = Multimedia_Create(self.driver, environment)
        self.multimediaCreate.click_on_template_icon()
        self.multimediaCreate.add_multimedia()
