import time
import logging
from selenium.webdriver.common.by import By
from iMEWebsite.pageObjects.BasePage import BasePage
from iMEWebsite.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class ExploreFooter(BasePage):
    imeCaresLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[3]/div[2]/div[1]/p/a")
    imeDistributorsLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[3]/div[2]/div[2]/p/a")
    imeInterviewHubLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[3]/div[2]/div[3]/p/a")



    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def verify_links(self):
        time.sleep(2)
        iMECare = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[3]/div[2]/div[1]/p/a")
        self.de_scroll_into_view(iMECare)
        time.sleep(1)
        self.de_click(self.imeCaresLink)
        log.logger.info("User Clicks On iME Cares Link")
        time.sleep(2)
        imeCaresURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(imeCaresURL))
        # assert imeCaresURL == "https://reservation-sack-316416.framer.app/ime-cares"
        if self.environment == "stage":
            assert imeCaresURL == "https://reservation-sack-316416.framer.app/ime-cares"
        elif self.environment == "UTA":
            assert imeCaresURL == "https://i-me.tech/ime-cares"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)


        imeDistributors = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[3]/div[2]/div[2]/p/a")
        self.de_scroll_into_view(imeDistributors)
        time.sleep(1)
        self.de_click(self.imeDistributorsLink)
        log.logger.info("User Clicks On iME Distributors  Link")
        time.sleep(2)
        imeDistributorsURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(imeDistributorsURL))
        # assert imeDistributorsURL == "https://reservation-sack-316416.framer.app/distributors"
        if self.environment == "stage":
            assert imeDistributorsURL == "https://reservation-sack-316416.framer.app/distributors"
        elif self.environment == "UTA":
            assert imeDistributorsURL == "https://i-me.tech/distributors"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)

        imeInterviewHub = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[3]/div[2]/div[3]/p/a")
        self.de_scroll_into_view(imeInterviewHub)
        time.sleep(2)
        self.de_click(self.imeInterviewHubLink)
        log.logger.info("User Clicks On iME InterviewHub  Link")
        time.sleep(3)
        # Wait for the new tab to open
        time.sleep(2)  # Adjust the sleep time as needed

        # Get the current window handles
        windows = self.driver.window_handles

        # Switch to the new tab (the last one)
        self.driver.switch_to.window(windows[-1])

        # Fetch the URL of the new tab
        imeInterviewHubURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(imeInterviewHubURL))

        # Close the new tab
        self.driver.close()

        # Switch back to the original tab
        self.driver.switch_to.window(windows[0])

        if self.environment == "stage":
            assert imeInterviewHubURL == "https://app.i-me.tech/ime-hub"
        elif self.environment == "UTA":
            assert imeInterviewHubURL == "https://app.i-me.tech/ime-hub"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)