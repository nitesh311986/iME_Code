import time
import logging
from selenium.webdriver.common.by import By
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.BasePage import BasePage

log = Logger(__name__, logging.INFO)


class ImeFooter(BasePage):
    whatWeDoLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[2]/div[2]/div[1]/p/a")
    forWhomLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[2]/div[2]/div[2]/p/a")
    howLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[2]/div[2]/div[3]/p/a")
    pricingLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[2]/div[2]/div[4]/p/a")


    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def verify_links(self):
        time.sleep(2)
        whatWeDo = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[2]/div[2]/div[1]/p/a")
        self.de_scroll_into_view(whatWeDo)
        time.sleep(1)
        self.de_click(self.whatWeDoLink)
        log.logger.info("User Clicks On what we can do? Link")
        time.sleep(2)
        whatWeDoURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(whatWeDoURL))
        # assert whatWeDoURL == "https://reservation-sack-316416.framer.app/about"
        if self.environment == "stage":
            assert whatWeDoURL == "https://reservation-sack-316416.framer.app/about"
        elif self.environment == "UTA":
            assert whatWeDoURL == "https://i-me.tech/about"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)

        forWhom = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[2]/div[2]/div[2]/p/a")
        self.de_scroll_into_view(forWhom)
        time.sleep(1)
        self.de_click(self.forWhomLink)
        log.logger.info("User Clicks On for Whom? Link")
        time.sleep(2)
        forWhomURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(forWhomURL))
        # assert forWhomURL == "https://reservation-sack-316416.framer.app/ime-in-action"
        if self.environment == "stage":
            assert forWhomURL == "https://reservation-sack-316416.framer.app/ime-in-action"
        elif self.environment == "UTA":
            assert forWhomURL == "https://i-me.tech/ime-in-action"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)

        how = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[2]/div[2]/div[3]/p/a")
        self.de_scroll_into_view(how)
        time.sleep(1)
        self.de_click(self.howLink)
        log.logger.info("User Clicks On How? Link")
        time.sleep(2)
        howURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(howURL))
        # assert howURL == "https://reservation-sack-316416.framer.app/contact"
        if self.environment == "stage":
            assert howURL == "https://reservation-sack-316416.framer.app/contact"
        elif self.environment == "UTA":
            assert howURL == "https://i-me.tech/contact"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)

        pricing = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[2]/div[2]/div[4]/p/a")
        self.de_scroll_into_view(pricing)
        time.sleep(1)
        self.de_click(self.pricingLink)
        log.logger.info("User Clicks On Pricing? Link")
        time.sleep(2)
        pricingURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(pricingURL))
        # assert pricingURL == "https://reservation-sack-316416.framer.app/pricing"
        if self.environment == "stage":
            assert pricingURL == "https://reservation-sack-316416.framer.app/pricing"
        elif self.environment == "UTA":
            assert pricingURL == "https://i-me.tech/pricing"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)

