import time
import logging

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.BlogPage import BasePage

log = Logger(__name__, logging.INFO)


class ServicePage(BasePage):
    recruitmentLink = (By.XPATH, "//div[@class='framer-1iimtv1']/div[2]/div/div/div[2]/a")
    awardLink = (By.XPATH, "//div[@class='framer-1tt7t98']/div[1]/div/div/div[2]/a")
    marketingLink = (By.XPATH, "//div[@class='framer-a7lpk0']/div[1]/div/div/div[2]/a")
    learningLink = (By.XPATH, "//div[@class='framer-1yp8s9k']/div[2]/div/div/div[2]/a")
    auditionLink = (By.XPATH, "//div[@class='framer-mo2sl']/div[2]/div/div/div[2]/a")
    admissionLink = (By.XPATH, "//div[@class='framer-wlwf15']/div[1]/div/div/div[2]/a")
    strategicSection = (By.XPATH, "//div[@class='framer-1h7ntgg']/div/h2")
    contactUsLink = (By.XPATH,"//div[@class='framer-on932q']/div/div[2]/p/a[1]")
    iMEHubLink = (By.XPATH,"//div[@class='framer-on932q']/div/div[2]/p/a[2]")



    def __init__(self, driver, environment):
        self.environment = environment
        super().__int__(driver)

    def verify_iMe_action_scrolling(self):
        log.logger.info("****==Verify Functions Of iME Action Page Behaviour==***")
        time.sleep(2)
        iMeIcon = self.driver.find_element(By.XPATH, "//div[@class='framer-1id1vs8']/div[1]/div[1]/div/div[1]/p")
        self.moveToElement(iMeIcon)
        time.sleep(1)
        log.logger.info("User Clicks On iME Action Link")
        about = self.driver.find_element(By.XPATH,
                                         "//div[@role='dialog' and @class='framer-1nhn8ey']/div/div/div[1]/p/a")
        action = self.driver.find_element(By.XPATH,
                                          "//div[@role='dialog' and @class='framer-1nhn8ey']/div/div/div[2]/p/a")
        time.sleep(1)
        # self.de_click(action)
        self.moveToElement(about)
        time.sleep(0.5)
        self.de_action_method(action)
        time.sleep(0.5)
        actionUrl = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(actionUrl))
        # assert actionUrl == "https://reservation-sack-316416.framer.app/ime-in-action"
        if self.environment == "stage":
            assert actionUrl == "https://reservation-sack-316416.framer.app/ime-in-action"
        elif self.environment == "UTA":
            assert actionUrl == "https://i-me.tech/ime-in-action"  # Adjust this URL as necessary
        time.sleep(1)
        learningLink = self.driver.find_element(By.XPATH, "//div[@class='framer-1yp8s9k']/div[2]/div/div/div[2]/a")
        self.de_scroll_into_view(learningLink)
        time.sleep(0.5)
        recruitmentLink = self.driver.find_element(By.XPATH, "//div[@class='framer-1iimtv1']/div[2]/div/div/div[2]/a")
        self.de_scroll_into_view(recruitmentLink)
        time.sleep(0.5)

        # Verify functionalities of all services links

    def verify_services_links_functions(self):
        log.logger.info("****==Verify Functions Of All Services Links==***")

        # Verify admission Services

        time.sleep(1)
        admissionLink = self.driver.find_element(By.XPATH, "//div[@class='framer-wlwf15']/div[1]/div/div/div[2]/a")
        self.de_scroll_into_view(admissionLink)
        time.sleep(0.5)
        self.de_click(self.admissionLink)
        time.sleep(1)
        admissionLinkUrl = self.driver.current_url
        log.logger.info("User will redirect to admission page with url == " + str(admissionLinkUrl))
        # assert admissionLinkUrl == "https://reservation-sack-316416.framer.app/admissions"
        if self.environment == "stage":
            assert admissionLinkUrl == "https://reservation-sack-316416.framer.app/admissions"
        elif self.environment == "UTA":
            assert admissionLinkUrl == "https://i-me.tech/admissions"  # Adjust this URL as necessary
        time.sleep(2)
        self.driver.back()

        # Verify audition Services

        time.sleep(1)
        auditionLink = self.driver.find_element(By.XPATH, "//div[@class='framer-mo2sl']/div[2]/div/div/div[2]/a")
        self.de_scroll_into_view(auditionLink)
        time.sleep(0.5)
        self.de_click(self.auditionLink)
        time.sleep(1)
        auditionLinkUrl = self.driver.current_url
        log.logger.info("User will redirect to audition page with url == " + str(auditionLinkUrl))
        # assert auditionLinkUrl == "https://reservation-sack-316416.framer.app/auditions"
        if self.environment == "stage":
            assert auditionLinkUrl == "https://reservation-sack-316416.framer.app/auditions"
        elif self.environment == "UTA":
            assert auditionLinkUrl == "https://i-me.tech/auditions"  # Adjust this URL as necessary
        time.sleep(2)
        self.driver.back()

        # Verify award Services

        time.sleep(1)
        awardLink = self.driver.find_element(By.XPATH, "//div[@class='framer-1tt7t98']/div[1]/div/div/div[2]/a")
        self.de_scroll_into_view(awardLink)
        time.sleep(0.5)
        self.de_click(self.awardLink)
        time.sleep(1)
        awardLinkUrl = self.driver.current_url
        log.logger.info("User will redirect to award page with url == " + str(awardLinkUrl))
        # assert awardLinkUrl == "https://reservation-sack-316416.framer.app/awards"
        if self.environment == "stage":
            assert awardLinkUrl == "https://reservation-sack-316416.framer.app/awards"
        elif self.environment == "UTA":
            assert awardLinkUrl == "https://i-me.tech/awards"  # Adjust this URL as necessary
        time.sleep(2)
        self.driver.back()

        # Verify learning Services

        time.sleep(1)
        learningLink = self.driver.find_element(By.XPATH, "//div[@class='framer-1yp8s9k']/div[2]/div/div/div[2]/a")
        self.de_scroll_into_view(learningLink)
        time.sleep(0.5)
        self.de_click(self.learningLink)
        time.sleep(1)
        learningLinkUrl = self.driver.current_url
        log.logger.info("User will redirect to learning page with url == " + str(learningLinkUrl))
        # assert learningLinkUrl == "https://reservation-sack-316416.framer.app/learning"
        if self.environment == "stage":
            assert learningLinkUrl == "https://reservation-sack-316416.framer.app/learning"
        elif self.environment == "UTA":
            assert learningLinkUrl == "https://i-me.tech/learning"  # Adjust this URL as necessary
        time.sleep(2)
        self.driver.back()

        # Verify marketing Services

        time.sleep(1)
        marketingLink = self.driver.find_element(By.XPATH, "//div[@class='framer-a7lpk0']/div[1]/div/div/div[2]/a")
        self.de_scroll_into_view(marketingLink)
        time.sleep(0.5)
        self.de_click(self.marketingLink)
        time.sleep(1)
        marketingLinkUrl = self.driver.current_url
        log.logger.info("User will redirect to marketing page with url == " + str(marketingLinkUrl))
        # assert marketingLinkUrl == "https://reservation-sack-316416.framer.app/marketing"
        if self.environment == "stage":
            assert marketingLinkUrl == "https://reservation-sack-316416.framer.app/marketing"
        elif self.environment == "UTA":
            assert marketingLinkUrl == "https://i-me.tech/marketing"  # Adjust this URL as necessary
        time.sleep(2)
        self.driver.back()

        # Verify Recruitment Service
        time.sleep(1)
        recruitmentLink = self.driver.find_element(By.XPATH, "//div[@class='framer-1iimtv1']/div[2]/div/div/div[2]/a")
        self.de_scroll_into_view(recruitmentLink)
        time.sleep(0.5)
        self.de_click(self.recruitmentLink)
        time.sleep(1)
        recruitmentUrl = self.driver.current_url
        log.logger.info("User will redirect to recruitment page with url == " + str(recruitmentUrl))
        # assert recruitmentUrl == "https://reservation-sack-316416.framer.app/recruitment"
        if self.environment == "stage":
            assert recruitmentUrl == "https://reservation-sack-316416.framer.app/recruitment"
        elif self.environment == "UTA":
            assert recruitmentUrl == "https://i-me.tech/recruitment"  # Adjust this URL as necessary
        time.sleep(2)
        self.driver.back()

    def verify_strategic_link(self):
        log.logger.info("****==Verify Functions Of All Strategic Links==***")

        # Verify admission Services

        time.sleep(2)
        strategicS = self.driver.find_element(By.XPATH, "//div[@class='framer-1h7ntgg']/div/h2")
        self.de_scroll_into_view(strategicS)
        time.sleep(1)

        sLink1 = self.driver.find_element(By.XPATH,
                                          "//div[@class='framer-6lopy6']/div/div/div/div[2]/div/div[2]/a[1]")
        sLink1.click()
        time.sleep(3)
        if self.environment == "stage":
            surveyLink = self.driver.current_url
            log.logger.info("User will redirect to marketing page with url == " + str(surveyLink))
        elif self.environment == "UTA":
            surveyLink = self.driver.current_url
            log.logger.info("User will redirect to marketing page with url == " + str(surveyLink))
        self.driver.back()
        time.sleep(3)

        sLink2 = self.driver.find_element(By.XPATH,
                                          "//div[@class='framer-6lopy6']/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/a")
        sLink2.click()
        time.sleep(3)
        if self.environment == "stage":
            surveyLink = self.driver.current_url
            log.logger.info("User will redirect to marketing page with url == " + str(surveyLink))
        elif self.environment == "UTA":
            surveyLink = self.driver.current_url
            log.logger.info("User will redirect to marketing page with url == " + str(surveyLink))
        self.driver.back()
        time.sleep(3)

        sLink3 = self.driver.find_element(By.XPATH,
                                          "//div[@class='framer-6lopy6']/div[3]/div[1]/div[1]/div[2]/div/div[2]/div/a")
        sLink3.click()
        time.sleep(3)
        if self.environment == "stage":
            surveyLink = self.driver.current_url
            log.logger.info("User will redirect to marketing page with url == " + str(surveyLink))
        elif self.environment == "UTA":
            surveyLink = self.driver.current_url
            log.logger.info("User will redirect to marketing page with url == " + str(surveyLink))
        self.driver.back()
        time.sleep(3)

        sLink4 = self.driver.find_element(By.XPATH,
                                          "//div[@class='framer-6lopy6']/div[4]/div[1]/div[1]/div[2]/div/div[2]/div/a")

        sLink4.click()
        time.sleep(3)
        if self.environment == "stage":
            surveyLink = self.driver.current_url
            log.logger.info("User will redirect to marketing page with url == " + str(surveyLink))
        elif self.environment == "UTA":
            surveyLink = self.driver.current_url
            log.logger.info("User will redirect to marketing page with url == " + str(surveyLink))
        self.driver.back()
        time.sleep(3)

    def verify_contact_and_ime_hub_link(self):
        log.logger.info("****==Verify Functions Of Contact Us and iME Hub Links==***")

        time.sleep(2)
        contactUs = self.driver.find_element(By.XPATH, "//div[@class='framer-on932q']/div/div[2]/p/a[1]")
        self.de_scroll_into_view(contactUs)
        time.sleep(1)
        self.de_click(self.contactUsLink)
        time.sleep(2)
        if self.environment == "stage":
            cStageLink = self.driver.current_url
            log.logger.info("User will redirect to marketing page with url == " + str(cStageLink))
        elif self.environment == "UTA":
            cUatLink = self.driver.current_url
            log.logger.info("User will redirect to marketing page with url == " + str(cUatLink))
        self.driver.back()
        time.sleep(3)

        # Verify iME Hub Link

        # Store the ID of the original window
        original_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        log.logger.info("User clicks on sign up block")
        self.de_click(self.iMEHubLink)
        time.sleep(3)

        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        # Wait for the new tab to finish loading content
        time.sleep(3)
        get_url = self.driver.current_url
        log.logger.info("User redirects to the iME Hub page with url == " + str(get_url))
        # assert get_url == "https://app.i-me.tech/sign-up"
        self.driver.close()
        self.driver.switch_to.window(original_window)
        time.sleep(3)


