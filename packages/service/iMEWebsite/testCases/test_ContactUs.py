import logging

import pytest

from iMEWebsite.testCases.test_Base import BaseTest
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.ContactUsPage import ContactUs

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=6)
@pytest.mark.order(6)
class Test_ContactUs(BaseTest):

    def test_contact_us(self,wait_for_page_load, environment):
        wait_for_page_load()
        self.contactUs = ContactUs(self.driver, environment)
        self.contactUs.send_enquiry()
