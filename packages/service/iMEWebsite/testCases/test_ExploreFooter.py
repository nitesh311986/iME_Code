import logging

import pytest

from iMEWebsite.testCases.test_Base import BaseTest
from iMEWebsite.pageObjects.exploreFooter import ExploreFooter
from iMEWebsite.Utilities.customLogger import Logger


log = Logger(__name__, logging.INFO)


# @pytest.mark.run(order=9)
@pytest.mark.order(9)
class Test_ExploreFooter(BaseTest):

    def test_explore_footer(self,wait_for_page_load, environment):
        wait_for_page_load()
        self.exploreFooter = ExploreFooter(self.driver, environment)
        self.exploreFooter.verify_links()
