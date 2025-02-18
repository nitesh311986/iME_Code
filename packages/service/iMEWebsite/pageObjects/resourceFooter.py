import time
import logging
from selenium.webdriver.common.by import By
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.BasePage import BasePage

log = Logger(__name__, logging.INFO)


class ResourceFooter(BasePage):
    blogLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[4]/div[2]/div[1]/p/a")
    contactUsLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[4]/div[2]/div[2]/p/a")
    faqLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[4]/div[2]/div[3]/p/a")
    featureListLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[4]/div[2]/div[4]/p/a")


    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)


    def verify_links(self):
        time.sleep(2)
        Blog = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[4]/div[2]/div[1]/p/a")
        self.de_scroll_into_view(Blog)
        time.sleep(1)
        self.de_click(self.blogLink)
        log.logger.info("User Clicks On Blog Link")
        time.sleep(2)
        blogURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(blogURL))
        # assert blogURL == "https://reservation-sack-316416.framer.app/blog"
        if self.environment == "stage":
            assert blogURL == "https://reservation-sack-316416.framer.app/blog"
        elif self.environment == "UTA":
            assert blogURL == "https://i-me.tech/blog"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)

        contactUs = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[4]/div[2]/div[2]/p/a")
        self.de_scroll_into_view(contactUs)
        time.sleep(1)
        self.de_click(self.contactUsLink)
        log.logger.info("User Clicks On Contact Us Link")
        time.sleep(2)
        contactUsURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(contactUsURL))
        # assert contactUsURL == "https://reservation-sack-316416.framer.app/contact"
        if self.environment == "stage":
            assert contactUsURL == "https://reservation-sack-316416.framer.app/contact"
        elif self.environment == "UTA":
            assert contactUsURL == "https://i-me.tech/contact"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)

        FAQ = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[4]/div[2]/div[3]/p/a")
        self.de_scroll_into_view(FAQ)
        time.sleep(1)
        self.de_click(self.faqLink)
        log.logger.info("User Clicks On FAQ Link")
        time.sleep(2)
        faqURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(faqURL))
        # assert faqURL == "https://reservation-sack-316416.framer.app/faqs"
        if self.environment == "stage":
            assert faqURL == "https://reservation-sack-316416.framer.app/faqs"
        elif self.environment == "UTA":
            assert faqURL == "https://i-me.tech/faqs"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)

        featureLink = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[4]/div[2]/div[4]/p/a")
        self.de_scroll_into_view(featureLink)
        time.sleep(1)
        self.de_click(self.featureListLink)
        log.logger.info("User Clicks On Feature List Link")
        time.sleep(2)
        featureListURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(featureListURL))
        # assert featureListURL == "https://reservation-sack-316416.framer.app/about"
        if self.environment == "stage":
            assert featureListURL == "https://reservation-sack-316416.framer.app/about"
        elif self.environment == "UTA":
            assert featureListURL == "https://i-me.tech/about"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)
