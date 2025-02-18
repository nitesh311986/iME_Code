import logging
import time
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEApplicant.pageObjects.BasePage import BasePage
from iMEApplicant.utilities.customLogger import Logger


log = Logger(__name__, logging.INFO)


class iMEHUbStreamHistory(BasePage):
    profileIcon = (By.XPATH,
                   "//div[@class='hidden md:flex items-center gap-x-4 lg:gap-x-6']/div/button")
    hubIcon = (By.CSS_SELECTOR,
               "a[class='flex items-center  rounded-md p-3 bg-[#E4E4E7] dark:bg-[#27272A]  hover:bg-[#E4E4E7] hover:dark:bg-[#27272A]']")

    steamIcon = (By.XPATH, "//div[@class='ps-sidebar-container css-1h6ytad']/div[2]/div[1]/nav[1]/ul/a[2]")

    # View List And Details Of Stream
    authorOfLiveStream = (By.XPATH, "//div[@class='space-y-9']/div[1]/div/div/div/div/div/a/div/span/span[1]")
    titleOfLiveStream = (By.XPATH, "//div[@class='space-y-9']/div[1]/div/div/div/div/div/a/div/span/p")
    durationOfLiveStream = (By.XPATH, "//div[@class='space-y-9']/div[1]/div/div/div/div/div/a/div[1]/div[1]")
    accessModeAndViewLiveStream = (By.XPATH, "//div[@class='space-y-9']/div[1]/div/div/div/div/div/a/div[1]/div[2]")
    dateOfLiveStream = (By.XPATH, "//div[@class='space-y-9']/div[1]/div/div/div/div/div/a/div[1]/div[3]")

    firstFavouriteIcon = (By.XPATH, "//div[@class='ps-sidebar-container css-1h6ytad']/nav[3]/ul/a[1]/li/a")
    filterDD = (By.XPATH, "//div[@class='mb-4 relative !w-full md:w-[200px] !ml-0 flex gap-2 items-center']/button")
    streamOptionOfFilterDD = (
        By.XPATH, "//div[@class='mb-4 relative !w-full md:w-[200px] !ml-0 flex gap-2 items-center']/ul/li[2]")
    folderOptionOfFilterDD = (
        By.XPATH, "//div[@class='mb-4 relative !w-full md:w-[200px] !ml-0 flex gap-2 items-center']/ul/li[3]")

    filesOptionOfFilterDD = (
        By.XPATH, "//div[@class='mb-4 relative !w-full md:w-[200px] !ml-0 flex gap-2 items-center']/ul/li[4]")

    noStreamAvailableMessage = (By.XPATH, "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_iME_HUb_icon(self):
        time.sleep(8)
        # self.driver.execute_script("document.getElementById('headlessui-menu-button-:r1:').click()")
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "applicant-profile-switch-button"))
            )
            script = "arguments[0].click();"
            self.driver.execute_script(script, element)
        except TimeoutException:
            print("Element not found or not clickable within the timeout period.")
        time.sleep(1)

        # self.driver.execute_script("document.getElementById('headlessui-menu-item-:r5:').click()")
        # self.de_click(self.hubIcon)

        try:
            element1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-test-id='ime-hub-link']")
                                               ))
            script = "arguments[0].click();"
            self.driver.execute_script(script, element1)

        except TimeoutException:
            print("Element not found or not clickable within the timeout period.")
        time.sleep(7)
        self.de_click(self.steamIcon)
        time.sleep(3)

    def view_list_and_details_of_streams_history(self):

        log.logger.info(
            "****==Fetch The Details Of Stream History===***")

        dataAvail = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='relative min-h-[80vh]']/div/div/div/div/ul/li"))
        # value = dataAvail.text
        # log.logger.info("" + value)
        if dataAvail > 0:
            for i in range(dataAvail):
                titleOfLiveStream = []
                titleOfLiveStream = self.driver.find_elements(By.XPATH,
                                                               "//div[@class='relative min-h-[80vh]']/div/div/div/div/ul/li/div/div/div/span/a[1]")
                authorOfLiveStream = []
                authorOfLiveStream = self.driver.find_elements(By.XPATH,
                                                              "//div[@class='relative min-h-[80vh]']/div/div/div/div/ul/li/div/div/div/span/a[2]")
                detailsOfLiveStream = []
                detailsOfLiveStream = self.driver.find_elements(By.XPATH,
                                                                 "//div[@class='relative min-h-[80vh]']/div/div/div/div/ul/li/div/div/div/span/p")
                dateOfLiveStream = []
                dateOfLiveStream = self.driver.find_elements(By.XPATH,
                                                                        "//div[@class='relative min-h-[80vh]']/div/div/div/div/ul/li/div/div/a/div/div")

                # dateOfLiveStream = []
                # dateOfLiveStream = self.driver.find_elements(By.XPATH,
                #                                              "//div[@class='space-y-9']/div[1]/div/div/div/div/div/a/div[1]/div[3]")

                title = titleOfLiveStream[i].text
                author = authorOfLiveStream[i].text
                details = detailsOfLiveStream[i].text
                date = dateOfLiveStream[i].text
                # date = dateOfLiveStream[i].text

                log.logger.info("Title Of Live Stream  == > " + author)
                log.logger.info("Author Of Live Stream  == > " + title)
                log.logger.info("Details Of Live Stream  == > " + details)
                log.logger.info("Date Mode And View Of Live Stream  == > " + date)
                # log.logger.info("Date Of Live Stream  == > " + date)