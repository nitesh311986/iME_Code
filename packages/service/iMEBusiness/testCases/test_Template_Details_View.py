import re
import logging

import pytest

from iMEBusiness.Config.Config import TestData
from iMEBusiness.pageObjects.TemplatePage import Template_Details
from iMEBusiness.pageObjects.LoginPage import LoginPage
from iMEBusiness.testCases.test_Base import BaseTest
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=12)
@pytest.mark.order(12)
class Test_Template(BaseTest):

    def test_read_template_minimum_requirement_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver, environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        self.templateDetails = Template_Details(self.driver, environment)
        self.templateDetails.click_on_template_icon()
        self.templateDetails.fetch_minimum_requirement()
        self.templateDetails.filter_minimum_requirement_via_filter_box()
        self.templateDetails.filter_minimum_requirement_via_search_box()

    def test_read_template_question_set_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.templateDetails = Template_Details(self.driver, environment)
        self.templateDetails.fetch_question_set()
        self.templateDetails.filter_question_set_via_filter_box()
        self.templateDetails.filter_question_set_via_search_box()

    def test_read_template_multimedia_details(self, wait_for_page_load, environment):
        wait_for_page_load()
        self.templateDetails = Template_Details(self.driver, environment)
        # self.templateDetails.fetch_multimedia_details()
        # self.templateDetails.filter_multimedia_via_filter_box()
        # self.templateDetails.filter_multimedia_via_search_box()
