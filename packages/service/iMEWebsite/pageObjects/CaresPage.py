import time
import logging

from selenium.common import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.Utilities.excelReader import excel_Data
from iMEWebsite.pageObjects.BlogPage import BasePage

log = Logger(__name__, logging.INFO)


class CaresPage(BasePage):
    caresIcon = (By.XPATH, "//div[@class='framer-1id1vs8']/div[1]/div[3]/p")
    careLinks1 = (By.XPATH, "//div[@class='framer-4ky5ba-container']/section/ul/li/div/div[1]")
    firstCarerImage = (By.XPATH, "//div[@class='framer-4ky5ba-container']/section/ul/li/div/div[1]/div/img")
    secondCarerImage = (By.XPATH, "//div[@class='framer-4ky5ba-container']/section/ul/li/div/div[2]/div/img")
    thirdCarerImage = (By.XPATH, "//div[@class='framer-4ky5ba-container']/section/ul/li/div/div[3]/div/img")
    firstCarerLink = (By.XPATH, "//div[@class='framer-1ad3p3n']/div[2]/p[4]/a")
    secondCarerLink = (By.XPATH, "//div[@class='framer-rktmcd']/div[2]/p/a")
    thirdCarerLink = (By.XPATH, "//div[@class='framer-4ky5ba-container']/section/ul/li[1]/div/div[3]/div/img")

    # Social Media On iME Hub
    partnerLink = (By.XPATH, "//div[@class='framer-1roiqcf']/p/a[2]")
    linkedInLink = (By.XPATH, "//div[@class='w-full rounded-lg overflow-hidden mt-6']/div[1]/div[2]/div[1]/a[1]")
    faceBookLink = (By.XPATH, "//div[@class='w-full rounded-lg overflow-hidden mt-6']/div[1]/div[2]/div[1]/a[2]")
    twitterLink = (By.XPATH, "//div[@class='w-full rounded-lg overflow-hidden mt-6']/div[1]/div[2]/div[1]/a[3]")
    instaGramLink = (By.XPATH, "//div[@class='w-full rounded-lg overflow-hidden mt-6']/div[1]/div[2]/div[1]/a[4]")
    youTubeLink = (By.XPATH, "//div[@class='w-full rounded-lg overflow-hidden mt-6']/div[1]/div[2]/div[1]/a[5]")

    def __init__(self, driver, environment):
        self.environment = environment
        super().__int__(driver)

    def verify_cares_links_functionality(self):
        time.sleep(2)
        self.de_click(self.caresIcon)
        time.sleep(1)
        careLinks = self.driver.find_element(By.XPATH,
                                             "//div[@class='framer-4ky5ba-container']/section/ul/li/div/div[1]")
        self.de_scroll_into_view(careLinks)
        time.sleep(1)

        # self.de_click(self.firstCarerImage)
        # time.sleep(2)
        # original_window = self.driver.current_window_handle
        #
        # # Check we don't have other windows open already
        # assert len(self.driver.window_handles) == 1
        # self.de_click(self.firstCarerLink)
        #
        # time.sleep(3)
        #
        # # Loop through until we find a new window handle
        # for window_handle in self.driver.window_handles:
        #     if window_handle != original_window:
        #         self.driver.switch_to.window(window_handle)
        #         break
        #
        #     # Wait for the new tab to finish loading content
        # get_url = self.driver.current_url
        # log.logger.info("User redirects to the sign in page with url == " + str(get_url))
        # self.driver.close()
        # self.driver.switch_to.window(original_window)
        # time.sleep(2)
        # self.driver.refresh()
        # time.sleep(3)
        # # careLinks = self.driver.find_element(By.XPATH, "//div[@class='framer-1wk8zsv']/h2")
        # # self.de_scroll_into_view(careLinks)
        # # time.sleep(1)
        #
        # # Second Carer
        #
        # self.de_click(self.secondCarerImage)
        # time.sleep(1)
        # original_window = self.driver.current_window_handle
        #
        # # Check we don't have other windows open already
        # assert len(self.driver.window_handles) == 1
        # self.de_click(self.secondCarerImage)
        # time.sleep(2)
        #
        # # Loop through until we find a new window handle
        # for window_handle in self.driver.window_handles:
        #     if window_handle != original_window:
        #         self.driver.switch_to.window(window_handle)
        #         break
        #
        #     # Wait for the new tab to finish loading content
        # get_url = self.driver.current_url
        # log.logger.info("User redirects to the sign in page with url == " + str(get_url))
        # self.driver.close()
        # self.driver.switch_to.window(original_window)
        # time.sleep(3)
        # self.driver.refresh()
        # time.sleep(2)

        # # Third Carer
        #
        # self.de_click(self.thirdCarerImage)
        # time.sleep(1)
        # original_window = self.driver.current_window_handle
        #
        # # Check we don't have other windows open already
        # assert len(self.driver.window_handles) == 1
        # self.de_click(self.thirdCarerImage)
        # time.sleep(2)
        #
        # # Loop through until we find a new window handle
        # for window_handle in self.driver.window_handles:
        #     if window_handle != original_window:
        #         self.driver.switch_to.window(window_handle)
        #         break
        #
        #     # Wait for the new tab to finish loading content
        # get_url = self.driver.current_url
        # log.logger.info("User redirects to the sign in page with url == " + str(get_url))
        # self.driver.close()
        # self.driver.switch_to.window(original_window)
        # time.sleep(3)
        # self.driver.refresh()
        # time.sleep(2)

    # def verify_partner_with_us_links_functionality(self):
    #     # partnerLinks = self.driver.find_element(By.XPATH,
    #     #                                         "//div[@class='framer-1roiqcf']/p/a[2]")
    #     # self.de_scroll_into_view(partnerLinks)
    #     # time.sleep(1)
    #     # original_window = self.driver.current_window_handle
    #     #
    #     # # Check we don't have other windows open already
    #     # assert len(self.driver.window_handles) == 1
    #     #
    #     # log.logger.info("User clicks on sign up block")
    #     # self.de_click(self.partnerLink)
    #     # time.sleep(3)
    #     #
    #     # # Loop through until we find a new window handle
    #     # for window_handle in self.driver.window_handles:
    #     #     if window_handle != original_window:
    #     #         self.driver.switch_to.window(window_handle)
    #     #     break
    #     #
    #     # # Wait for the new tab to finish loading content
    #     # time.sleep(5)
    #     # get_url = self.driver.current_url
    #     # log.logger.info("User redirects to the iME Hub page with url == " + str(get_url))
    #     # # social_media_links = {
    #     # #     "LinkedIn": (self.linkedInLink, "https://www.linkedin.com/"),
    #     # #     "Twitter": (self.twitterLink, "https://x.com/"),
    #     # #     "YouTube": (self.youTubeLink, "https://www.youtube.com/"),
    #     # #     "Facebook": (self.faceBookLink, "https://www.facebook.com/"),
    #     # #     "Instagram": (self.instaGramLink, "https://www.instagram.com/")
    #     # #    }
    #     # #
    #     # # for platform, (link, expected_url) in social_media_links.items():
    #     # #     try:
    #     # # Find and click the social media link
    #     #
    #     # original_window = self.driver.current_window_handle
    #     #
    #     # # Ensure only one window is open before clicking
    #     # assert len(self.driver.window_handles) == 1
    #     # self.de_click(self.linkedInLink)
    #     # time.sleep(2)
    #     #
    #     # # Switch to the new window
    #     # new_window_handle = None
    #     # for window_handle1 in self.driver.window_handles:
    #     #     if window_handle1 != original_window:
    #     #         self.driver.switch_to.window(window_handle1)
    #     #         break
    #
    #     #     if new_window_handle:
    #     #         self.driver.switch_to.window(new_window_handle)
    #     #         time.sleep(3)
    #     #         get_current_url = self.driver.current_url
    #     #         log.logger.info(f"User redirects to page with URL == {get_current_url}")
    #     #
    #     #         if expected_url in get_current_url:
    #     #             log.logger.info(f"User Redirects to {platform}")
    #     #         else:
    #     #             log.logger.error(f"User did not redirect to the expected URL for {platform}.")
    #     #             assert False
    #     #
    #     #         self.driver.close()
    #     #         self.driver.switch_to.window(original_window)
    #     #         time.sleep(2)
    #     #     else:
    #     #         log.logger.error(f"Failed to find a new window for {platform}.")
    #     #
    #     # except NoSuchElementException as e:
    #     #     log.logger.error(f"Element not found for {platform}: {e}")
    #     # except TimeoutException as e:
    #     #     log.logger.error(f"Timeout occurred while interacting with {platform}: {e}")
    #     # except WebDriverException as e:
    #     #     log.logger.error(f"WebDriver error occurred while interacting with {platform}: {e}")
    #     # except Exception as e:
    #     #     log.logger.error(f"An unexpected error occurred while interacting with {platform}: {e}")
    #     # finally:
    #     #     # Ensure that the browser window is always returned to the original state
    #     #     try:
    #     #         if len(self.driver.window_handles) > 1:
    #     #             self.driver.switch_to.window(original_window)
    #     #     except Exception as e:
    #     #         log.logger.error(f"An error occurred during final cleanup: {e}")
    #
    #     # log.logger.info("All social media checks are completed.")
    #     # self.driver.close()
    #     # self.driver.switch_to.window(original_window)
    #
    #     # Find the partner link and scroll it into view
    #     # Find the partner link and scroll it into view
    #     partnerLinks = self.driver.find_element(By.XPATH, "//div[@class='framer-1roiqcf']/p/a[2]")
    #     self.de_scroll_into_view(partnerLinks)
    #     time.sleep(1)
    #
    #     # Save the original window handle
    #     original_window = self.driver.current_window_handle
    #
    #     # Before clicking the partner link, log the number of windows open
    #     log.logger.info(f"Number of windows open before clicking partner link: {len(self.driver.window_handles)}")
    #
    #     # Assert that only one window is open before clicking the partner link
    #     assert len(self.driver.window_handles) == 1, "There are multiple windows open before clicking the partner link."
    #
    #     log.logger.info("User clicks on sign up block")
    #     self.de_click(self.partnerLink)
    #     time.sleep(3)
    #
    #     # Wait for the new window to open and switch to it
    #     WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)
    #
    #     # Loop through the window handles and switch to the new window
    #     new_window_handle = None
    #     for window_handle in self.driver.window_handles:
    #         if window_handle != original_window:
    #             new_window_handle = window_handle
    #             break
    #
    #     if new_window_handle:
    #         self.driver.switch_to.window(new_window_handle)
    #     else:
    #         log.logger.error("Failed to find a new window handle.")
    #         return
    #
    #     # Wait for the new window's page to load completely
    #     time.sleep(5)
    #     get_url = self.driver.current_url
    #     log.logger.info("User redirects to the iME Hub page with url == " + str(get_url))
    #
    #     # Log the number of windows after navigating
    #     log.logger.info(f"Number of windows open after navigating to iME Hub: {len(self.driver.window_handles)}")
    #
    #     # Now, switch back to the original window
    #     self.driver.switch_to.window(original_window)
    #
    #     # Click on the LinkedIn social media link and wait for it to open in a new window
    #     linkedin_link_xpath = "//div[@class='w-full rounded-lg overflow-hidden mt-6']/div[1]/div[2]/div[1]/a[1]"
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, linkedin_link_xpath)))
    #
    #     # Once clickable, click the LinkedIn link
    #     self.de_click(self.linkedInLink)
    #     time.sleep(2)
    #
    #     # Wait for the new window to open and switch to it
    #     WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)
    #
    #     # Loop through the window handles and switch to the new window
    #     new_window_handle1 = None
    #     for window_handle1 in self.driver.window_handles:
    #         if window_handle1 != original_window:
    #             new_window_handle1 = window_handle1
    #             break
    #
    #     if new_window_handle1:
    #         self.driver.switch_to.window(new_window_handle1)
    #         log.logger.info(f"Switched to new window: {new_window_handle1}")
    #     else:
    #         log.logger.error("Failed to find a new window handle for LinkedIn.")
    #         return
    #
    #     # Perform further actions on the new window as needed...
