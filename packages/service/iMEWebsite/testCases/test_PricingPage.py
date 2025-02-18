import logging

import pytest

from iMEWebsite.testCases.test_Base import BaseTest
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.PricingPage import PricingPage

log = Logger(__name__, logging.INFO)



# @pytest.mark.run(order=3)
@pytest.mark.order(3)
class Test_Pricing(BaseTest):

    def test_pricing_of_countries(self,wait_for_page_load, environment):
        wait_for_page_load()
        self.pricing = PricingPage(self.driver, environment)
        self.pricing.verify_pricing_of_countries()
