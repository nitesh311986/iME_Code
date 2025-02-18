import logging

import pytest

from iMEWebsite.testCases.test_Base import BaseTest
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.SocialMediaFooter import SocialMedia

log = Logger(__name__, logging.INFO)



# @pytest.mark.run(order=12)
@pytest.mark.order(12)
class Test_SocialMediaFooter(BaseTest):

    def test_social_media_footer(self,wait_for_page_load, environment):
        wait_for_page_load()
        self.socialMediaFooter = SocialMedia(self.driver, environment)
        self.socialMediaFooter.test_social_media_links()
