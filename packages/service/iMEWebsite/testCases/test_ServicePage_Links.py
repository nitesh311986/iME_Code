import logging

import pytest

from iMEWebsite.testCases.test_Base import BaseTest
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.ServicePage import ServicePage

log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=2)
@pytest.mark.order(2)
class Test_Service_Page_Links(BaseTest):

    def test_verify_iMe_action_page_functionsP(self,wait_for_page_load, environment):
        wait_for_page_load()
        self.servicePage = ServicePage(self.driver, environment)
        self.servicePage.verify_iMe_action_scrolling()
        self.servicePage.verify_services_links_functions()
        self.servicePage.verify_strategic_link()
        self.servicePage.verify_contact_and_ime_hub_link()
