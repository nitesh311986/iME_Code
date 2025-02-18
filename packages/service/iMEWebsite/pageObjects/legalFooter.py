import time
import logging
from selenium.webdriver.common.by import By
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.BasePage import BasePage

log = Logger(__name__, logging.INFO)


class LegalFooter(BasePage):
    acceptableUserLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[5]/div[2]/div[1]/p/a")
    cookiesLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[5]/div[2]/div[2]/p/a")
    distributionTeamLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[5]/div[2]/div[3]/p/a")
    privacyLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[5]/div[2]/div[4]/p/a")
    termsOfServicesLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[5]/div[2]/div[5]/p/a")
    userNoticeLink = (By.XPATH, "//div[@class='framer-wpxq5f']/div[5]/div[2]/div[6]/p/a")


    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)


    def verify_links(self):
        time.sleep(2)
        acceptableUser = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[5]/div[2]/div[1]/p/a")
        self.de_scroll_into_view(acceptableUser)
        time.sleep(1)
        self.de_click(self.acceptableUserLink)
        log.logger.info("User Clicks On Acceptable User  Link")
        time.sleep(2)
        acceptableUserURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(acceptableUserURL))
        # assert acceptableUserURL == "https://reservation-sack-316416.framer.app/acceptable-use-policy"
        if self.environment == "stage":
            assert acceptableUserURL == "https://reservation-sack-316416.framer.app/acceptable-use-policy"
        elif self.environment == "UTA":
            assert acceptableUserURL == "https://i-me.tech/acceptable-use-policy"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)

        time.sleep(2)
        cookies = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[5]/div[2]/div[2]/p/a")
        self.de_scroll_into_view(cookies)
        time.sleep(1)
        self.de_click(self.cookiesLink)
        log.logger.info("User Clicks On Cookies  Link")
        time.sleep(2)
        cookiesURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(cookiesURL))
        # assert cookiesURL == "https://reservation-sack-316416.framer.app/cookies-policy"
        if self.environment == "stage":
            assert cookiesURL == "https://reservation-sack-316416.framer.app/cookies-policy"
        elif self.environment == "UTA":
            assert cookiesURL == "https://i-me.tech/cookies-policy"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)

        time.sleep(2)
        distributionTeam = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[5]/div[2]/div[3]/p/a")
        self.de_scroll_into_view(distributionTeam)
        time.sleep(1)
        self.de_click(self.distributionTeamLink)
        log.logger.info("User Clicks On DistributionT eam  Link")
        time.sleep(2)
        distributionTeamURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(distributionTeamURL))
        # assert distributionTeamURL == "https://reservation-sack-316416.framer.app/distribution-terms-of-use"
        if self.environment == "stage":
            assert distributionTeamURL == "https://reservation-sack-316416.framer.app/distribution-terms-of-use"
        elif self.environment == "UTA":
            assert distributionTeamURL == "https://i-me.tech/distribution-terms-of-use"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)

        time.sleep(2)
        privacy = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[5]/div[2]/div[4]/p/a")
        self.de_scroll_into_view(privacy)
        time.sleep(1)
        self.de_click(self.privacyLink)
        log.logger.info("User Clicks On Privacy  Link")
        time.sleep(2)
        privacyURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(privacyURL))
        # assert privacyURL == "https://reservation-sack-316416.framer.app/privacy-policy"
        if self.environment == "stage":
            assert privacyURL == "https://reservation-sack-316416.framer.app/privacy-policy"
        elif self.environment == "UTA":
            assert privacyURL == "https://i-me.tech/privacy-policy"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)

        time.sleep(2)
        termsOfServices = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[5]/div[2]/div[5]/p/a")
        self.de_scroll_into_view(termsOfServices)
        time.sleep(1)
        self.de_click(self.termsOfServicesLink)
        log.logger.info("User Clicks On Terms Of Services  Link")
        time.sleep(2)
        termsOfServicesURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(termsOfServicesURL))
        # assert termsOfServicesURL == "https://reservation-sack-316416.framer.app/terms-of-service"
        if self.environment == "stage":
            assert termsOfServicesURL == "https://reservation-sack-316416.framer.app/terms-of-service"
        elif self.environment == "UTA":
            assert termsOfServicesURL == "https://i-me.tech/terms-of-service"  # Adjust this URL as necessary
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)

        time.sleep(2)
        userNotice = self.driver.find_element(By.XPATH, "//div[@class='framer-wpxq5f']/div[5]/div[2]/div[6]/p/a")
        self.de_scroll_into_view(userNotice)
        time.sleep(1)
        self.de_click(self.userNoticeLink)
        log.logger.info("User Clicks On User Notice  Link")
        time.sleep(2)
        userNoticeURL = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(userNoticeURL))
        # assert userNoticeURL == "https://reservation-sack-316416.framer.app/user-notice"
        if self.environment == "stage":
            assert userNoticeURL == "https://reservation-sack-316416.framer.app/user-notice"
        elif self.environment == "UTA":
            assert userNoticeURL == "https://i-me.tech/user-notice"  # Adjust this URL as necessary
        time.sleep(0.5)
        time.sleep(0.5)
        self.driver.back()
        time.sleep(1)