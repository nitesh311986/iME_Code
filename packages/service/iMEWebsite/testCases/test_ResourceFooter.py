import pytest
import logging
from iMEWebsite.testCases.test_Base import BaseTest
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.resourceFooter import ResourceFooter

log = Logger(__name__, logging.INFO)



# @pytest.mark.run(order=10)
@pytest.mark.order(10)
class Test_ResourceFooter(BaseTest):


    def test_Resource_Footer(self,wait_for_page_load, environment):
        wait_for_page_load()
        self.resourceFooter = ResourceFooter(self.driver, environment)
        self.resourceFooter.verify_links()
