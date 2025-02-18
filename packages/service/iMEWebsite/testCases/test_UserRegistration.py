import logging

import pytest

from iMEWebsite.testCases.test_Base import BaseTest
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.UserRegistrationPages import UserRegistration

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=13)
@pytest.mark.order(13)
class Test_User_Registration(BaseTest):

    def test_verify_signIn_signUP(self,wait_for_page_load, environment):
        wait_for_page_load()
        self.registration = UserRegistration(self.driver, environment)
        # title = self.registration.get_launch_page_title("iME | Video Interviews")
        # assert title == "iME | Video Interviews"
        self.registration.verify_sign_in()
