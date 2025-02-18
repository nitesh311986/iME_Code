from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from iMEApplicant.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class iMEHUbViewPage(BasePage):
    profileIcon = (By.XPATH,
                   "//div[@class='hidden md:flex items-center gap-x-4 lg:gap-x-6']/div/button")
    hubIcon = (By.CSS_SELECTOR,
               "a[class='flex items-center  rounded-md p-3 bg-[#E4E4E7] dark:bg-[#27272A]  hover:bg-[#E4E4E7] hover:dark:bg-[#27272A]']")

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

    def __init__(self, driver, environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_iME_HUb_icon(self):
        time.sleep(8)
        currentURL = self.driver.current_url
        log.logger.info(
            "==User Is On The Page=== " + currentURL)
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

    def view_list_and_details_of_streams(self):

        log.logger.info(
            "****==Fetch The List And Details Of Live Stream ===***")

        dataAvail = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='space-y-9']/div[1]/div/div/div/div/div"))
        # value = dataAvail.text
        # log.logger.info("" + value)
        if dataAvail > 0:
            for i in range(dataAvail):
                authorOfLiveStream = []
                authorOfLiveStream = self.driver.find_elements(By.XPATH,
                                                               "//div[@class='space-y-9']/div[1]/div/div/div/div/div/a/div/span/span[1]")
                titleOfLiveStream = []
                titleOfLiveStream = self.driver.find_elements(By.XPATH,
                                                              "//div[@class='space-y-9']/div[1]/div/div/div/div/div/a/div/span/p")
                durationOfLiveStream = []
                durationOfLiveStream = self.driver.find_elements(By.XPATH,
                                                                 "//div[@class='space-y-9']/div[1]/div/div/div/div/div/a/div[1]/div[1]")
                accessModeAndViewLiveStream = []
                accessModeAndViewLiveStream = self.driver.find_elements(By.XPATH,
                                                                        "//div[@class='space-y-9']/div[1]/div/div/div/div/div/a/div[1]/div[2]")

                # dateOfLiveStream = []
                # dateOfLiveStream = self.driver.find_elements(By.XPATH,
                #                                              "//div[@class='space-y-9']/div[1]/div/div/div/div/div/a/div[1]/div[3]")

                author = authorOfLiveStream[i].text
                title = titleOfLiveStream[i].text
                duration = durationOfLiveStream[i].text
                accessMode = accessModeAndViewLiveStream[i].text
                # date = dateOfLiveStream[i].text

                log.logger.info("Author Of Live Stream  == > " + author)
                log.logger.info("Title Of Live Stream  == > " + title)
                log.logger.info("Duration Of Live Stream  == > " + duration)
                log.logger.info("Access Mode And View Of Live Stream  == > " + accessMode)
                # log.logger.info("Date Of Live Stream  == > " + date)

    def view_list_and_details_of_folder(self):

        log.logger.info(
            "****==Fetch The List And Details Of Folder ===***")

        dataAvail = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='space-y-9']/div[2]/div/div/div/div/div"))
        # value = dataAvail.text
        # log.logger.info("" + value)
        if dataAvail > 0:
            time.sleep(3)
            for i in range(dataAvail):
                authorOfUploadStream = []
                authorOfUploadStream = self.driver.find_elements(By.XPATH,
                                                                 "//div[@class='space-y-9']/div[2]/div/div/div/div/div/a/div/span/span[1]")
                titleOfUploadStream = []
                titleOfUploadStream = self.driver.find_elements(By.XPATH,
                                                                "//div[@class='space-y-9']/div[2]/div/div/div/div/div/a/div/span/p")
                # dateOfUploadStream = []
                # dateOfUploadStream = self.driver.find_elements(By.XPATH,
                #                                                "//div[@class='space-y-9']/div[2]/div/div/div/div/div/a/div[1]/div[1]")
                # accessModeAndViewUploadStream = []
                # accessModeAndViewUploadStream = self.driver.find_elements(By.XPATH,
                #                                                           "//div[@class='space-y-9']/div[2]/div/div/div/div/div/a/div[1]/div[2]")
                #
                # dateOfUploadStream = []
                # dateOfUploadStream = self.driver.find_elements(By.XPATH,
                #                                                "//div[@class='space-y-9']/div[2]/div/div/div/div/div/a/div[1]/div[3]")

                author = authorOfUploadStream[i].text
                title = titleOfUploadStream[i].text
                # duration = durationOfUploadStream[i].text
                # accessMode = accessModeAndViewUploadStream[i].text
                # date = dateOfUploadStream[i].text

                log.logger.info("Author Of Upload Stream  == > " + author)
                log.logger.info("Title Of Upload Stream  == > " + title)
                # log.logger.info("Duration Of Upload Stream  == > " + duration)
                # log.logger.info("Access Mode And View Of Upload Stream  == > " + accessMode)
                # log.logger.info("Date Of Upload Stream  == > " + date)

    def filter_list_of_favourite_stream(self):
        log.logger.info(
            "****==Filter and fetch the details of the items From Favourite List ===***")
        dataAvail = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='ps-sidebar-container css-1h6ytad']/div[2]/div/nav[3]/ul/a"))
        # value = dataAvail.text
        # log.logger.info("" + value)
        if dataAvail > 0:
            totalFavourite = len(self.driver.find_elements(By.XPATH,
                                                           "//div[@class='ps-sidebar-container css-1h6ytad']/div[2]/div/nav[3]/ul/a"))

            for i in range(totalFavourite):
                favouriteList = []
                favouriteList = self.driver.find_elements(By.XPATH,
                                                          "//div[@class='ps-sidebar-container css-1h6ytad']/div[2]/div/nav[3]/ul/a")
                NameOfFavourite = favouriteList[i].text
                favouriteList[i].click()
                time.sleep(4)
                self.de_click(self.filterDD)
                time.sleep(0.5)
                self.de_click(self.streamOptionOfFilterDD)
                time.sleep(3)
                isStreamAvailable = self.driver.find_element(By.XPATH,
                                                             "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div")

                log.logger.info("Stream" + str(isStreamAvailable.text))

                if isStreamAvailable == "No Content Available":
                    log.logger.info("There's No Stream Available Under Live Stream")
                else:
                    totalStream = len(self.driver.find_elements(By.XPATH,
                                                                "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div/div/a/div[2]/span/p"))

                    # log.logger.info("Number Of Live Stream ", str(totalStream))
                    log.logger.info(
                        "Live Stream Details Of Favorite Stream === " + NameOfFavourite + " === is Under Below")
                    time.sleep(1)
                    for j in range(totalStream):
                        NameOfStream = []
                        NameOfStream = self.driver.find_elements(By.XPATH,
                                                                 "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div/div/a/div[2]/span/p")

                        viewOfStream = []
                        viewOfStream = self.driver.find_elements(By.XPATH,
                                                                 "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div/div/a/div/div[3]")

                        modeOfStream = []
                        modeOfStream = self.driver.find_elements(By.XPATH,
                                                                 "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div/div/a/div/div[2]")
                        durationOfStream = []
                        durationOfStream = self.driver.find_elements(By.XPATH,
                                                                     "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div/div/a/div/div[1]")
                        # dateOfStream = []
                        # dateOfStream = self.driver.find_elements(By.XPATH,
                        #                                          "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div/div/a/div/div[4]")

                        Name = NameOfStream[j].text
                        numberOfView = viewOfStream[j].text
                        title = modeOfStream[j].text
                        duration = durationOfStream[j].text
                        # accessMode = dateOfStream[j].text

                        log.logger.info("Name of Stream  == > " + Name)
                        log.logger.info("Number Of Views Of Stream  == > " + numberOfView)
                        log.logger.info("Title Of The Streams  == > " + title)
                        log.logger.info("Duration Of The Stream  == > " + duration)
                        # log.logger.info("Access Mode Of The Stream  == > " + accessMode)

                time.sleep(3)

                # Filter And Fetch Data For Folder

                self.de_click(self.filterDD)
                time.sleep(0.5)
                self.de_click(self.folderOptionOfFilterDD)
                time.sleep(3)

                isStreamAvailable = self.driver.find_element(By.XPATH,
                                                             "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div")

                log.logger.info("Folder" + str(isStreamAvailable.text))

                if isStreamAvailable == "No Content Available":
                    log.logger.info("There's No Folder Available")

                else:
                    totalStream = len(self.driver.find_elements(By.XPATH,
                                                                "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div/div/div/a/div[2]/span/p"))

                    # log.logger.info("Number Of Live Stream ", str(totalStream))

                    time.sleep(1)
                    log.logger.info(
                        "Folder Details Of Favorite Stream === " + NameOfFavourite + " === is Under Below")
                    for k in range(totalStream):
                        NameOfStream = []
                        NameOfStream = self.driver.find_elements(By.XPATH,
                                                                 "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div/div/div/a/div[2]/span/p")

                        # viewOfStream = []
                        # viewOfStream = self.driver.find_elements(By.XPATH,
                        #                                          "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div/div/a/div/div[3]")
                        #
                        # modeOfStream = []
                        # modeOfStream = self.driver.find_elements(By.XPATH,
                        #                                          "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div/div/a/div/div[2]")
                        # durationOfStream = []
                        # durationOfStream = self.driver.find_elements(By.XPATH,
                        #                                              "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div/div/a/div/div[1]")
                        # dateOfStream = []
                        # dateOfStream = self.driver.find_elements(By.XPATH,
                        #                                          "//div[@class='overflow-x-scroll [&::-webkit-scrollbar]:hidden']/div/div/div/div/a/div/div[4]")

                        Name = NameOfStream[k].text
                        # numberOfView = viewOfStream[i].text
                        # title = modeOfStream[i].text
                        # duration = durationOfStream[i].text
                        # accessMode = dateOfStream[i].text
                        log.logger.info("Name Of Folder  == > " + Name)
                        # log.logger.info("Number Of Views Of Folder  == > " + numberOfView)
                        # log.logger.info("Title Of The Folder  == > " + title)
                        # log.logger.info("Duration Of The Folder  == > " + duration)
                        # log.logger.info("Access Mode Of The Folder  == > " + accessMode)

                    # Filter And Fetch Data For Folder

                    self.de_click(self.filterDD)
                    time.sleep(0.5)
                    self.de_click(self.filesOptionOfFilterDD)
                    time.sleep(3)
                    isItemAvailable = self.driver.find_element(By.XPATH,
                                                               "//div[@class='space-y-9']/div[6]/h4")

                    log.logger.info("Item" + str(isItemAvailable.text))

                    if isItemAvailable == "No Item Available":
                        log.logger.info("There's No Item Available ")
                    else:
                        totalFiles = len(self.driver.find_elements(By.XPATH,
                                                                   "//div[@class='space-y-8']/table/tbody/tr/td[1]/div/a"))

                        # log.logger.info("Number Of Live Stream ", str(totalStream))
                        log.logger.info(
                            "Files  Details Of Favorite Stream === " + NameOfFavourite + " === is Under Below")
                        time.sleep(1)
                        for l in range(totalFiles):
                            nameOfFile = []
                            nameOfFile = self.driver.find_elements(By.XPATH,
                                                                   "//div[@class='space-y-8']/table/tbody/tr/td[1]/div/a")

                            typeOfFile = []
                            typeOfFile = self.driver.find_elements(By.XPATH,
                                                                   "//div[@class='space-y-8']/table/tbody/tr/td[2]")

                            Name = nameOfFile[l].text
                            Type = typeOfFile[l].text

                            log.logger.info("Name of File  == > " + Name)
                            log.logger.info("Type Of File Is  == > " + Type)
