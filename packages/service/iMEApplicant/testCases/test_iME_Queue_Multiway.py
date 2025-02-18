import pytest
import logging
from iMEApplicant.Config.config import TestData
from iMEApplicant.pageObjects.iME_Queue_Multiway import iME_Queue_MultiWay
from iMEApplicant.pageObjects.LoginPage import LoginPage
from iMEApplicant.testCases.test_Base import BaseTest
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)




# @pytest.mark.run(order=10)
@pytest.mark.order(10)
class Test_iME_Queue(BaseTest):

    def test_accepts_rejects_interview(self, wait_for_page_load,environment):
        wait_for_page_load()
        self.loginPage = LoginPage(self.driver,environment)
        message = self.loginPage.do_login(TestData.UserName, TestData.Password)
        log.logger.info(
            "Applicant logged In successfully in to the system after verifying dashboard message" + str(message))

        self.iMEQueue = iME_Queue_MultiWay(self.driver,environment)
        self.iMEQueue.click_on_iME_Queue_icon()
        self.iMEQueue.view_multiway_video()
        self.iMEQueue.view_multiway_webinar()
