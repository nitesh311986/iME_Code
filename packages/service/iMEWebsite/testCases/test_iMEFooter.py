import pytest
import logging
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.iMEFooterPage import ImeFooter
from iMEWebsite.testCases.test_Base import BaseTest

log = Logger(__name__, logging.INFO)



# @pytest.mark.run(order=8)
@pytest.mark.order(8)
class Test_ImeFooter(BaseTest):


    def test_iMe_Footer(self,wait_for_page_load, environment):
        wait_for_page_load()
        self.iMEFooter = ImeFooter(self.driver, environment)
        self.iMEFooter.verify_links()
