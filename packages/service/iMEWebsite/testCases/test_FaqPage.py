import pytest
import logging
from iMEWebsite.testCases.test_Base import BaseTest
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.FaqPage import Faq


log = Logger(__name__, logging.INFO)



# @pytest.mark.run(order=7)
@pytest.mark.order(7)
class Test_FAQ(BaseTest):


    def test_faq(self,wait_for_page_load, environment):
        wait_for_page_load()
        self.faq = Faq(self.driver, environment)
        self.faq.click_on_faq()
