import time
import logging
from selenium.webdriver.common.by import By
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Ime_Queue_Video_Transcription(BasePage):
    imeQueueIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[10]/a")

    numberOfInterview = (By.XPATH,
                         "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[1]/div[1]/h6")
    blockOfInterview = (By.XPATH,
                        "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div")

    # Filter iME queue

    filterIcon = (By.XPATH, "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[1]/div[2]/div[2]/button")

    clearAll = (By.XPATH,
                "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[1]/h2[2]")

    applyButton = (By.XPATH,
                   "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[5]/div/button")
    # Status DD

    statusDD = (By.XPATH,
                "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/button")

    notStartedStatus = (By.XPATH,
                        "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/ul/li[1]")

    searchInput = (By.CSS_SELECTOR, "input[name='searchName']")

    oneWayInterviewTab = (By.XPATH,
                          "//div[@class='text-base semibold h-[36px] bg-white dark:bg-ime-gray-900 flex justify-center items-center gap-[12px] sm:px-[5px] md:px-[12px] py-[8px] text-ime-gray-500 dark:text-ime-gray-400']")

    videoButton = (By.XPATH,
                   "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden mb-[8px]']/button[3]")

    designationName = (
        By.XPATH,
        "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div[1]/button/div[1]/div[2]/h3")

    transcriptionButton = (By.XPATH,
                           "//div[@class='ime-tab-group pl-6 pt-6 w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[2]")

    transcriptionPara = (By.XPATH, "//div[@class='h-[25vh] md:h-[30vh] lg:h-[53vh] overflow-y-auto']/div/p")

    closeVideoScreen = (By.XPATH,"//div[@class='min-w-[60%] flex flex-col bg-ime-gray-100 dark:bg-ime-gray-900 rounded-t-2xl p-6 lg:rounded-tl-none lg:rounded-r-2xl']/div[1]/*[local-name()='svg']")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def fetch_video_transcription(self):
        time.sleep(4)
        global designationTitle
        log.logger.info(
            "!!! == Fetch the transcription Of Each Video  == !!!")
        time.sleep(1)
        self.de_click(self.filterIcon)
        time.sleep(1)
        self.de_click(self.statusDD)
        time.sleep(1)
        self.de_click(self.notStartedStatus)
        time.sleep(1)
        self.de_click(self.statusDD)
        time.sleep(1)
        self.de_click(self.applyButton)
        time.sleep(1)
        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)

        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))
        if int(totalNumberOfInterviews) > 0:
            totalList = len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div"))
            List = []
            List = self.driver.find_elements(By.XPATH,
                                             "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div")

            for i in range(totalList):
                List[i].click()
                time.sleep(2)
                self.de_click(self.oneWayInterviewTab)
                time.sleep(2)
                self.de_click(self.videoButton)
                time.sleep(1)
                totalQuestions = len(self.driver.find_elements(By.XPATH,
                                                               "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[1]/div[2]/div/div[2]"))
                Questions = []
                Questions = self.driver.find_elements(By.XPATH,
                                                      "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[1]/div[2]/div/div[2]")

                for j in range(totalQuestions):
                    Questions[j].click()
                    time.sleep(2.5)
                    self.de_click(self.transcriptionButton)
                    time.sleep(1)
                    Transcription = self.get_element_text(self.transcriptionPara)
                    time.sleep(1)
                    if len(Transcription) > 0:
                        log.logger.info("Transcription == " + Transcription)
                    else:
                        log.logger.info("There's No Transcription")
                    time.sleep(1)
                    self.de_click(self.closeVideoScreen)
                    time.sleep(2)
