import pytest
import logging
from iMEWebsite.testCases.test_Base import BaseTest
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.BlogPage import BlogPage

log = Logger(__name__, logging.INFO)



# @pytest.mark.run(order=4)
@pytest.mark.order(4)
class Test_BlogLinks(BaseTest,):
    @pytest.mark.smoke
    def test_blog_links(self,wait_for_page_load, environment):
        wait_for_page_load()
        self.blog = BlogPage(self.driver, environment)
        self.blog.test_links_of_blog()
