import pytest
import logging
from iMEWebsite.testCases.test_Base import BaseTest
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.CaresPage import CaresPage

log = Logger(__name__, logging.INFO)



# @pytest.mark.run(order=5)
@pytest.mark.order(5)
class Test_CaresPage(BaseTest):

    def test_cares_link(self,wait_for_page_load, environment):
        wait_for_page_load()
        self.care = CaresPage(self.driver, environment)
        self.care.verify_cares_links_functionality()
        # self.care.verify_partner_with_us_links_functionality()
