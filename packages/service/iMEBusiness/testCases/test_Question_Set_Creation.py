import re
import logging

import pytest

from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.Question_Set import Question_Set_Create
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)

# @pytest.mark.run(order=5)
@pytest.mark.order(5)
class Test_Question_Set_Creation(BaseTest):

    def test_add_question_set_details(self,wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)

        self.questionSetCreate = Question_Set_Create(self.driver, environment)
        self.questionSetCreate.click_on_template_icon()
        # self.questionSetCreate.add_question_set()

    def test_add_question_set_from_list(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.questionSetCreate = Question_Set_Create(self.driver, environment)
        # self.questionSetCreate.add_question_from_list()
