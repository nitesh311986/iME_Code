import time
import logging

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.BasePage import BasePage

log = Logger(__name__, logging.INFO)


class AboutUsPage(BasePage):
    oneWayVideoLink = (By.XPATH, "//div[@class='framer-1uwivy']/div[1]/div[1]/div/div[1]/p")

    def __init__(self, driver, environment):
        self.environment = environment
        super().__int__(driver)

    def verify_about_us_links(self):
        log.logger.info("****==Verify Function Of Abouts Us Links==***")
        time.sleep(3.5)
        iMeIcon = self.driver.find_element(By.XPATH, "//div[@class='framer-1id1vs8']/div[1]/div[1]/div/div[1]/p")
        self.moveToElement(iMeIcon)
        time.sleep(1)
        log.logger.info("User Clicks On About Us Link")
        about = self.driver.find_element(By.XPATH,
                                         "//div[@role='dialog' and @class='framer-1nhn8ey']/div/div/div[1]/p/a")
        time.sleep(1)
        self.de_action_method(about)
        time.sleep(1)
        aboutUrl = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(aboutUrl))
        if self.environment == "stage":
            assert aboutUrl == "https://reservation-sack-316416.framer.app/about"
        elif self.environment == "UTA":
            assert aboutUrl == "https://i-me.tech/about"  # Adjust this URL as necessary
        self.driver.back()
        time.sleep(1.5)

        # link1 = self.driver.find_element(By.XPATH, "//div[@class='framer-wb98i3']/div[2]/a")
        # self.de_scroll_into_view(link1)
        # time.sleep(1)
        # self.de_click(self.oneWayVideoLink)
        # oneWayInterviewUrl = self.driver.current_url
        # log.logger.info("User will redirect to page with url == " + str(oneWayInterviewUrl))
        # assert oneWayInterviewUrl == "https://i-me.tech/one-way-interviews"
        # self.driver.back()
        # time.sleep(1)

        # iMe Action
        iMeIcon = self.driver.find_element(By.XPATH, "//div[@class='framer-1id1vs8']/div[1]/div[1]/div/div[1]/p")
        self.moveToElement(iMeIcon)
        time.sleep(1)
        log.logger.info("User Clicks On iME Action Link")
        action = self.driver.find_element(By.XPATH,
                                          "//div[@role='dialog' and @class='framer-1nhn8ey']/div/div/div[2]/p/a")
        time.sleep(1)
        self.de_action_method(action)
        time.sleep(1)
        actionUrl = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(actionUrl))
        if self.environment == "stage":
            assert actionUrl == "https://reservation-sack-316416.framer.app/ime-in-action"
        elif self.environment == "UTA":
            assert actionUrl == "https://i-me.tech/ime-in-action"  # Adjust this URL as necessary
        self.driver.back()
        time.sleep(1.5)

        # iME Hub

        iMeIcon = self.driver.find_element(By.XPATH, "//div[@class='framer-1id1vs8']/div[1]/div[1]/div/div[1]/p")
        self.moveToElement(iMeIcon)
        time.sleep(1)
        log.logger.info("User Clicks On iME Action Link")
        demoOnline = self.driver.find_element(By.XPATH,
                                              "//div[@role='dialog' and @class='framer-1nhn8ey']/div/div/div[3]/p/a")
        time.sleep(1)
        self.de_action_method(demoOnline)
        time.sleep(1)
        iMEHUbUrl = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(iMEHUbUrl))
        if self.environment == "stage":
            assert iMEHUbUrl == "https://app.i-me.tech/ime-hub"
        elif self.environment == "UTA":
            assert iMEHUbUrl == "https://app.i-me.tech/ime-hub"  # Adjust this URL as necessary
        self.driver.back()
        time.sleep(1.5)

        # Pricing

        iMeIcon = self.driver.find_element(By.XPATH, "//div[@class='framer-1id1vs8']/div[1]/div[1]/div/div[1]/p")
        self.moveToElement(iMeIcon)
        time.sleep(1)
        log.logger.info("User Clicks On iME Action Link")
        Pricing = self.driver.find_element(By.XPATH,
                                           "//div[@role='dialog' and @class='framer-1nhn8ey']/div/div/div[4]/p/a")
        time.sleep(1)
        self.de_action_method(Pricing)
        time.sleep(1)
        pricingUrl = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(pricingUrl))
        if self.environment == "stage":
            assert pricingUrl == "https://reservation-sack-316416.framer.app/pricing"
        elif self.environment == "UTA":
            assert pricingUrl == "https://i-me.tech/pricing"  # Adjust this URL as necessary
        self.driver.back()
        time.sleep(1.5)
