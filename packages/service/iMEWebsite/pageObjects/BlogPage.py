import time
import logging
from selenium.webdriver.common.by import By
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.BasePage import BasePage

log = Logger(__name__, logging.INFO)


class BlogPage(BasePage):
    blogIcon = (By.XPATH, "//div[@class='framer-1id1vs8']/div[1]/div[2]/p")
    twitterIcon = (By.XPATH, "//div[@class='framer-1jjplmq']/div[1]/div/div/*[local-name()='svg']")
    facebookIcon = (By.XPATH, "//div[@class='framer-1jjplmq']/div[2]/div/div/*[local-name()='svg']")
    linkedinIcon = (By.XPATH, "//div[@class='framer-1jjplmq']/div[3]/div/div/*[local-name()='svg']")
    backButton = (By.XPATH, "//div[@class='framer-e9z9ob']/div[1]/div/a")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def test_links_of_blog(self):
        time.sleep(2)
        self.de_click(self.blogIcon)
        time.sleep(1)

        # totalBlogs = len(self.driver.find_elements(By.XPATH,
        #                                            "//div[@id='blog-posts']/a/div[2]/div/h5"))
        #
        # for i in range(totalBlogs):
        #     Blogs = []
        #     Blogs = self.driver.find_elements(By.XPATH,
        #                                       "//div[@id='blog-posts']/a/div[2]/div/h5")
        #     Blogs[i].click()
        #     time.sleep(3)
        #     blogURL = self.driver.current_url
        #     log.logger.info("User Clicks On Blog With URL == " + str(blogURL))
        #     original_window = self.driver.current_window_handle
        #     assert len(self.driver.window_handles) == 1
        #     self.de_click(self.twitterIcon)
        #     time.sleep(2)
        #     for window_handle in self.driver.window_handles:
        #         if window_handle != original_window:
        #             self.driver.switch_to.window(window_handle)
        #             time.sleep(2)
        #             break
        #     get_title = self.driver.title
        #     log.logger.info("User redirects to the sign in page with title == " + str(get_title))
        #     if "X" in get_title:
        #         log.logger.info("User Redirects to Twitter")
        #     else:
        #         assert False
        #
        #     self.driver.close()
        #     self.driver.switch_to.window(original_window)
        #     time.sleep(2)
        #
        #     # FaceBook
        #
        #     original_window = self.driver.current_window_handle
        #     assert len(self.driver.window_handles) == 1
        #     self.de_click(self.facebookIcon)
        #     time.sleep(2)
        #     for window_handle in self.driver.window_handles:
        #         if window_handle != original_window:
        #             self.driver.switch_to.window(window_handle)
        #             time.sleep(2)
        #             break
        #     get_title = self.driver.title
        #     log.logger.info("User redirects to the sign in page with title == " + str(get_title))
        #     if "Facebook" in get_title:
        #         log.logger.info("User Redirects to FaceBook")
        #     else:
        #         assert False
        #
        #     self.driver.close()
        #     self.driver.switch_to.window(original_window)
        #     time.sleep(2)
        #
        #     # Linked IN
        #
        #     original_window = self.driver.current_window_handle
        #     assert len(self.driver.window_handles) == 1
        #     self.de_click(self.linkedinIcon)
        #     time.sleep(2)
        #     for window_handle in self.driver.window_handles:
        #         if window_handle != original_window:
        #             self.driver.switch_to.window(window_handle)
        #             time.sleep(2)
        #             break
        #     get_url = self.driver.current_url
        #     log.logger.info("User redirects to the sign in page with title == " + str(get_url))
        #     if "https://www.linkedin.com/" in get_url:
        #         log.logger.info("User Redirects to LinkedIn")
        #     else:
        #         assert False
        #
        #     self.driver.close()
        #     self.driver.switch_to.window(original_window)
        #     time.sleep(1.5)
        #     self.driver.back()
        #
        #     # self.de_click(self.backButton)
        #     time.sleep(3)
