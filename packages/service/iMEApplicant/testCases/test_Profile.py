import pytest
import logging
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.ProfilePage import ProfilePage
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.testCases.test_Base import BaseTest
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=2)
@pytest.mark.order(2)
class Test_Profile(BaseTest):

    def test_click_profile_icon(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.loginpage = LoginPage(self.driver,environment)
        log.logger.info("Applicant enters emailId and password and clicks on sign in button")
        message = self.loginpage.do_login(TestData.UserName, TestData.Password)
        print(message)
        log.logger.info(
            "Applicant logged In successfully in to the system after verifying dashboard message" + str(message))

    def test_fill_personal_information(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.profilepage = ProfilePage(self.driver,environment)
        self.profilepage.click_on_profile_icon()
        # self.profilepage.fill_personal_information()

    # def test_fill_about_me_information(self, wait_for_page_load,environment):
    #     wait_for_page_load()
    #     self.profilepage = ProfilePage(self.driver,environment)
    #     log.logger.info("Applicant clicks on profile icon")
    #     self.profilepage.click_on_profile_icon()
    #     log.logger.info("Applicant start filling about me information")
    #     self.profilepage.fill_about_me_information()

    def test_fill_additional_information(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.profilepage = ProfilePage(self.driver,environment)
        self.profilepage.click_on_profile_icon()

        # self.profilepage.fill_additional_information()

    # def test_fill_educational_information(self):
    #     self.profilepage = ProfilePage(self.driver)
    #     log.logger.info("Applicant clicks on profile icon")
    #     self.profilepage.click_on_profile_icon()
    #     log.logger.info("Applicant start filling additional information")
    #     self.profilepage.fill_educational_information()
