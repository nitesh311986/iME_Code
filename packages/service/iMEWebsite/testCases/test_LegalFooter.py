import logging

import pytest

from iMEWebsite.testCases.test_Base import BaseTest
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.legalFooter import LegalFooter

log = Logger(__name__, logging.INFO)



# @pytest.mark.run(order=11)
@pytest.mark.order(11)
class Test_LegalFooter(BaseTest):

    def test_legal_footer(self ,wait_for_page_load, environment):
        wait_for_page_load()
        self.legalFooter = LegalFooter(self.driver, environment)
        self.legalFooter.verify_links()
