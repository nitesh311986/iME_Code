import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.BasePage import BasePage


log = Logger(__name__, logging.INFO)


class UserRegistration(BasePage):
    signInButton = (By.XPATH, "//div[@class='framer-1id1vs8']/div[2]/div[2]/a")
    signUpButton = (By.XPATH, "//div[@class='framer-1id1vs8']/div[2]/div[1]/a")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def get_launch_page_title(self, title):
        return self.driver.get_title(title)

    def verify_sign_in(self):
        time.sleep(3)
        log.logger.info("****==Verify User Should Redirects To Right Page By Clicking On Sign In Button==***")
        # Store the ID of the original window
        original_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        log.logger.info("User clicks on sign in block")
        self.de_click(self.signInButton)
        time.sleep(3)

        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        # Wait for the new tab to finish loading content
        WebDriverWait(self.driver, 10).until(EC.title_is("iME"))
        get_url = self.driver.current_url
        log.logger.info("User redirects to the sign in page with url == " + str(get_url))
        # assert get_url == "https://app.i-me.tech/sign-in"
        self.driver.close()
        self.driver.switch_to.window(original_window)
        time.sleep(3)

        # Verify sign up functionality

        log.logger.info("****==Verify User Should Redirects To Right Page By Clicking On Sign Up Button==***")
        # Store the ID of the original window
        original_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        log.logger.info("User clicks on sign up block")
        self.de_click(self.signUpButton)
        time.sleep(3)

        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        # Wait for the new tab to finish loading content
        WebDriverWait(self.driver, 10).until(EC.title_is("iME"))
        get_url = self.driver.current_url
        log.logger.info("User redirects to the sign up page with url == " + str(get_url))
        # assert get_url == "https://app.i-me.tech/sign-up"
        self.driver.close()
        self.driver.switch_to.window(original_window)
        time.sleep(3)


