import pytest
import logging

from iMEWebsite.testCases.test_Base import BaseTest
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.AboutUsPage import AboutUsPage

log = Logger(__name__, logging.INFO)



# @pytest.mark.run(order=1)
@pytest.mark.order(1)
class Test_About_Us(BaseTest):
    @pytest.mark.smoke
    def test_verify_signIn_signUP(self,wait_for_page_load, environment):
        wait_for_page_load()
        self.aboutUs = AboutUsPage(self.driver,environment)
        self.aboutUs.verify_about_us_links()
