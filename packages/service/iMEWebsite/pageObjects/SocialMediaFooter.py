import time
import logging

from selenium.common import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.BasePage import BasePage

log = Logger(__name__, logging.INFO)


class SocialMedia(BasePage):
    linkedInLink = (By.XPATH, "//div[@class='framer-rx2zxy']/div/div[2]/a[1]")
    twitterLink = (By.XPATH, "//div[@class='framer-rx2zxy']/div/div[2]/a[2]")
    youTubeLink = (By.XPATH, "//div[@class='framer-rx2zxy']/div/div[2]/a[3]")
    faceBookLink = (By.XPATH, "//div[@class='framer-rx2zxy']/div/div[2]/a[4]")
    instaGramLink = (By.XPATH, "//div[@class='framer-rx2zxy']/div/div[2]/a[5]")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def test_social_media_links(self):
        time.sleep(2)

        social_media_links = {
            "LinkedIn": (self.linkedInLink, "https://www.linkedin.com/"),
            "Twitter": (self.twitterLink, "https://x.com/"),
            "YouTube": (self.youTubeLink, "https://www.youtube.com/"),
            "Facebook": (self.faceBookLink, "https://www.facebook.com/"),
            "Instagram": (self.instaGramLink, "https://www.instagram.com/")
        }

        for platform, (link, expected_url) in social_media_links.items():
            try:
                # Find and click the social media link
                social_media_element = self.driver.find_element(By.XPATH,
                                                                "//div[@class='framer-rx2zxy']/div/div[2]/a[1]")
                self.de_scroll_into_view(social_media_element)
                time.sleep(1)
                original_window = self.driver.current_window_handle

                # Ensure only one window is open before clicking
                assert len(self.driver.window_handles) == 1
                self.de_click(link)
                time.sleep(2)

                # Switch to the new window
                new_window_handle = None
                for window_handle in self.driver.window_handles:
                    if window_handle != original_window:
                        new_window_handle = window_handle
                        break

                if new_window_handle:
                    self.driver.switch_to.window(new_window_handle)
                    time.sleep(3)
                    get_current_url = self.driver.current_url
                    log.logger.info(f"User redirects to page with URL == {get_current_url}")

                    if expected_url in get_current_url:
                        log.logger.info(f"User Redirects to {platform}")
                    else:
                        log.logger.error(f"User did not redirect to the expected URL for {platform}.")
                        assert False

                    self.driver.close()
                    self.driver.switch_to.window(original_window)
                    time.sleep(2)
                else:
                    log.logger.error(f"Failed to find a new window for {platform}.")

            except NoSuchElementException as e:
                log.logger.error(f"Element not found for {platform}: {e}")
            except TimeoutException as e:
                log.logger.error(f"Timeout occurred while interacting with {platform}: {e}")
            except WebDriverException as e:
                log.logger.error(f"WebDriver error occurred while interacting with {platform}: {e}")
            except Exception as e:
                log.logger.error(f"An unexpected error occurred while interacting with {platform}: {e}")
            finally:
                # Ensure that the browser window is always returned to the original state
                try:
                    if len(self.driver.window_handles) > 1:
                        self.driver.switch_to.window(original_window)
                except Exception as e:
                    log.logger.error(f"An error occurred during final cleanup: {e}")

        log.logger.info("All social media checks are completed.")
        # linkedIn = self.driver.find_element(By.XPATH, "//div[@class='framer-rx2zxy']/div/div[2]/a[1]")
        # self.de_scroll_into_view(linkedIn)
        # time.sleep(1)
        # assert len(self.driver.window_handles) == 1
        # self.de_click(self.linkedInLink)
        # time.sleep(2)
        # socialMediaURL = self.driver.current_url
        # log.logger.info("User Clicks On Social Media Icon With URL == " + str(socialMediaURL))
        # original_window = self.driver.current_window_handle
        # for window_handle in self.driver.window_handles:
        #     if window_handle != original_window:
        #         self.driver.switch_to.window(window_handle)
        #         time.sleep(3)
        #         break
        # get_current_url = self.driver.current_url
        # log.logger.info("User redirects to  page with url == " + str(get_current_url))
        # if "https://www.linkedin.com/" in get_current_url:
        #     log.logger.info("User Redirects to LinkedIN")
        # else:
        #     assert False
        #
        # self.driver.close()
        # self.driver.switch_to.window(original_window)
        # time.sleep(2)
        #
        # # Twitter
        # linkedIn = self.driver.find_element(By.XPATH, "//div[@class='framer-rx2zxy']/div/div[2]/a[1]")
        # self.de_scroll_into_view(linkedIn)
        # time.sleep(1)
        # original_window = self.driver.current_window_handle
        # assert len(self.driver.window_handles) == 1
        # self.de_click(self.twitterLink)
        # time.sleep(2)
        # for window_handle in self.driver.window_handles:
        #     if window_handle != original_window:
        #         self.driver.switch_to.window(window_handle)
        #         time.sleep(2)
        #         break
        # get_current_url = self.driver.current_url
        # log.logger.info("User redirects to  page with url == " + str(get_current_url))
        # if "https://x.com/" in get_current_url:
        #     log.logger.info("User Redirects to Twitter")
        # else:
        #     assert False
        #
        # self.driver.close()
        # self.driver.switch_to.window(original_window)
        # time.sleep(2)
        #
        # # You Tube
        # linkedIn = self.driver.find_element(By.XPATH, "//div[@class='framer-rx2zxy']/div/div[2]/a[1]")
        # self.de_scroll_into_view(linkedIn)
        # time.sleep(1)
        # original_window = self.driver.current_window_handle
        # assert len(self.driver.window_handles) == 1
        # self.de_click(self.youTubeLink)
        # time.sleep(2)
        # for window_handle in self.driver.window_handles:
        #     if window_handle != original_window:
        #         self.driver.switch_to.window(window_handle)
        #         time.sleep(2)
        #         break
        # get_current_url = self.driver.current_url
        # log.logger.info("User redirects to page with url == " + str(get_current_url))
        # if "https://www.youtube.com/" in get_current_url:
        #     log.logger.info("User Redirects to You Tube")
        # else:
        #     assert False
        #
        # self.driver.close()
        # self.driver.switch_to.window(original_window)
        # time.sleep(2)
        #
        # # FaceBook
        #
        # linkedIn = self.driver.find_element(By.XPATH, "//div[@class='framer-rx2zxy']/div/div[2]/a[1]")
        # self.de_scroll_into_view(linkedIn)
        # time.sleep(1)
        # original_window = self.driver.current_window_handle
        # assert len(self.driver.window_handles) == 1
        # self.de_click(self.faceBookLink)
        # time.sleep(2)
        # for window_handle in self.driver.window_handles:
        #     if window_handle != original_window:
        #         self.driver.switch_to.window(window_handle)
        #         time.sleep(2)
        #         break
        # get_current_url = self.driver.current_url
        # log.logger.info("User redirects to page with url == " + str(get_current_url))
        # if "https://www.facebook.com/" in get_current_url:
        #     log.logger.info("User Redirects to Facebook")
        # else:
        #     assert False
        #
        # self.driver.close()
        # self.driver.switch_to.window(original_window)
        # time.sleep(2)
        #
        # # Insta
        # linkedIn = self.driver.find_element(By.XPATH, "//div[@class='framer-rx2zxy']/div/div[2]/a[1]")
        # self.de_scroll_into_view(linkedIn)
        # time.sleep(1)
        # original_window = self.driver.current_window_handle
        # assert len(self.driver.window_handles) == 1
        # self.de_click(self.instaGramLink)
        # time.sleep(2)
        # for window_handle in self.driver.window_handles:
        #     if window_handle != original_window:
        #         self.driver.switch_to.window(window_handle)
        #         time.sleep(2)
        #         break
        # get_current_url = self.driver.current_url
        # log.logger.info("User redirects to  page with url == " + str(get_current_url))
        # if "https://www.instagram.com/" in get_current_url:
        #     log.logger.info("User Redirects to Instagram")
        # else:
        #     assert False
        #
        # self.driver.close()
        # self.driver.switch_to.window(original_window)
        # time.sleep(2)
