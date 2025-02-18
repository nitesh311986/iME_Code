import time
import logging
from selenium.webdriver.common.by import By
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Analytics_Details(BasePage):
    analyticsIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[3]/a")
    invitesDetails = (By.XPATH,
                      "//div[@id='block-4027b96d-0979-4e60-974e-c054bc9f0d40_caa7bd8a-1baf-4f5e-af25-d3539c7d6a91']/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div/span")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_analytics_icon(self):
        time.sleep(1)
        self.de_click(self.analyticsIcon)
        time.sleep(15)

    def fetch_overall_interview_details(self):
        log.logger.info(
            "!!! == Fetch the analytical details of total  invites, all applications,completed applications , "

            "and failed minimum requirements  == !!!")

        invites = self.get_element_text(self.invitesDetails)
        log.logger.info("length" + str(invites))

        # totalLength = len(self.driver.find_elements(By.XPATH,
        #                                             "//div[@data-automation-id='kpi-actual-value']/span"))
        # log.logger.info("length" + str(totalLength))
        # totalDetails = []
        # totalDetails = self.driver.find_elements(By.XPATH,
        #                                          "//div[@data-automation-id='kpi-actual-value']/span")
        # for i in range(totalLength):
        #     log.logger.info("in loop")
        #     log.logger.info("analytical details of total  invites, all applications,completed applications and failed "
        #                     "minimum requirements == " + str(totalDetails[i].text))
