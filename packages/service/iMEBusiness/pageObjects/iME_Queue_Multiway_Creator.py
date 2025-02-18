import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
import logging
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class iME_Queue_Multiway_Creator(BasePage):
    imeQueueIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[10]/a")
    numberOfInterview = (By.XPATH,
                         "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[1]/div[1]/h6")

    filterIcon = (By.XPATH, "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[1]/div[2]/div[2]/button")
    statusDD = (By.XPATH,
                "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/button")
    notStartedYet = (By.XPATH,
                     "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/ul/li[1]")
    applyButton = (By.XPATH,
                   "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[5]/div/button")
    firstApplicant = (By.XPATH, "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div[1]")
    oneWayInterviewTab = (By.XPATH,
                          "//div[@class='text-base semibold h-[36px] bg-white dark:bg-ime-gray-900 flex justify-center items-center gap-[12px] sm:px-[5px] md:px-[12px] py-[8px] text-ime-gray-500 dark:text-ime-gray-400']")
    multiwayIcon = (
        By.XPATH, "//div[@class='grid grid-cols-5 sm:flex flex-wrap gap-x-[20px] gap-y-[16px] pb-[16px]']/button[5]/p")
    dateInput = (By.XPATH, "//div[@class='!mb-0 mt-auto ime-form-input']/input")
    fromTime1 = (By.XPATH, "//input[@name='multiwayTimeslots.0.startDateTime']")
    toTime1 = (By.XPATH, "//input[@name='multiwayTimeslots.0.endDateTime']")
    fromTime2 = (By.XPATH, "//input[@name='multiwayTimeslots.1.startDateTime']")
    toTime2 = (By.XPATH, "//input[@name='multiwayTimeslots.1.endDateTime']")
    fromTime3 = (By.XPATH, "//input[@name='multiwayTimeslots.2.startDateTime']")
    toTime3 = (By.XPATH, "//input[@name='multiwayTimeslots.2.endDateTime']")
    plusButtonOne = (By.XPATH, "//div[@class='flex flex-col md:flex-row gap-2 mt-4']/div[3]/button")
    plusButtonTwo = (By.XPATH, "//form[@class='p-6 max-w-2xl']/div/div/div[2]/div[3]")
    description = (By.CSS_SELECTOR, "textArea[name='interviewDescription']")
    searchDD = (By.XPATH, "//div[@id='search']")
    addUser = (By.XPATH, "//div[@class='relative w-full border-gray-300 rounded-md my-4 ']/div/div[2]")
    submitButton = (
        By.XPATH,
        "//button[@class='mt-6 flex-1 disabled:bg-black bg-[#0070F3] rounded-[4px] transition-colors h-[32px] px-[22px] text-xs bg-ime-accent hover:bg-blue-700 text-white']")
    multiWayTab = (By.XPATH,
                   "//div[@class='ime-tab-group font-semibold flex flex-row max-sm:basis-full border rounded-md overflow-hidden divide-x border-gray-300 dark:border-gray-600 divide-ime-gray-300 dark:divide-ime-gray-600']/button[2]")
    clearAll = (By.XPATH, "//div[@class='flex justify-between items-center my-[20px]']/h2[2]")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def test_create_multiway(self):
        time.sleep(8)
        log.logger.info("!!! == Create Multiway Vide Session From iME Queue  == !!!")
        self.de_click(self.filterIcon)
        time.sleep(0.5)
        self.de_click(self.statusDD)
        time.sleep(0.5)
        self.de_click(self.notStartedYet)
        time.sleep(0.5)
        self.de_click(self.statusDD)
        time.sleep(0.5)
        self.de_click(self.applyButton)
        time.sleep(0.5)
        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)

        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))
        if int(totalNumberOfInterviews) > 0:
            log.logger.info("!!! == Action Of Filtering Interview list Completed   !!!")
            self.de_click(self.firstApplicant)
            time.sleep(0.5)
            log.logger.info("!!! == Clicks On First Applicant Appears In The Queue   !!!")
            self.de_click(self.oneWayInterviewTab)
            time.sleep(5)
            log.logger.info("!!! == Clicks On One Way Interview Tab  !!!")

            totalList = len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='flex flex-col sm:flex-row gap-[16px]']/div[1]/div/div[1]/button"))

            log.logger.info("Number Of Interviewer Blocks == " + str(totalList))

            ActionsIcon = []
            ActionsIcon = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='flex flex-col sm:flex-row gap-[16px]']/div[1]/div/div[1]/button/p")

            ActionsButton = []
            ActionsButton = self.driver.find_elements(By.XPATH,
                                                      "//div[@class='flex flex-col sm:flex-row gap-[16px]']/div[1]/div/div[1]/button")
            for i in range(totalList):
                NameOfAction = ActionsIcon[i].text
                log.logger.info("Icon Tag Is == " + str(NameOfAction))
                if NameOfAction == "Multiway":
                    Status = ActionsButton[i].is_enabled()
                    log.logger.info("!!! == Checked That Multiway Icon Is Enabled For Action  !!!" + str(Status))
                    if str(Status) == "True":
                        ActionsButton[i].click()
                        time.sleep(4)
                        log.logger.info("!!! == Cliks On Multiway Icon   !!!")
                        current_time = datetime.now().replace(second=0, microsecond=0)
                        log.logger.info("Current Date And Time" + str(current_time))

                        # Create a datetime object for manipulation
                        current_datetime = datetime.combine(datetime.today(), current_time.time())

                        # Add 2 hours to the current time
                        new_startTime = current_datetime + timedelta(hours=2)
                        new_endTime1 = current_datetime + timedelta(hours=3)
                        new_startTime1 = current_datetime + timedelta(hours=4)
                        new_endTime2 = current_datetime + timedelta(hours=5)
                        new_startTime2 = current_datetime + timedelta(hours=6)
                        new_endTime3 = current_datetime + timedelta(hours=7)

                        # Extract the time part from the resulting datetime
                        new_startTimeOne = new_startTime.strftime("%H:%M")
                        new_endTime_One = new_endTime1.strftime("%H:%M")
                        new_startTimeTwo = new_startTime1.strftime("%H:%M")
                        new_endTime_Two = new_endTime2.strftime("%H:%M")
                        new_startTimeThree = new_startTime2.strftime("%H:%M")
                        new_endTime_Three = new_endTime3.strftime("%H:%M")

                        time.sleep(1)
                        self.do_clear_using_java_script(self.fromTime1)
                        time.sleep(1)
                        self.do_send_key(self.fromTime1, new_startTimeOne)
                        log.logger.info("Start Time Of First Video Session Slot Is" + str(new_startTimeOne))
                        self.do_clear_using_java_script(self.toTime1)
                        time.sleep(1)
                        self.do_send_key(self.toTime1, new_endTime_One)
                        log.logger.info("End Time Of First Video Session Slot Is" + str(new_endTime_One))
                        time.sleep(1)
                        # self.de_click(self.plusButtonOne)
                        # time.sleep(2)
                        # self.do_clear_using_java_script(self.fromTime2)
                        # time.sleep(1)
                        # self.do_send_key(self.fromTime2, new_startTimeTwo)
                        # log.logger.info("Start Time Of Second Video Session Slot Is" + str(new_startTimeTwo))
                        # self.do_clear_using_java_script(self.toTime2)
                        # time.sleep(1)
                        # self.do_send_key(self.toTime2, new_endTime_Two)
                        # log.logger.info("End Time Of Second Video Session Slot Is" + str(new_endTime_Two))
                        # time.sleep(1)
                        # self.de_click(self.plusButtonTwo)
                        # time.sleep(2)
                        # self.do_clear_using_java_script(self.fromTime3)
                        # time.sleep(1)
                        # self.do_send_key(self.fromTime3, new_startTimeThree)
                        # log.logger.info("Start Time Of Third Video Session Slot Is" + str(new_startTimeThree))
                        # self.do_clear_using_java_script(self.toTime3)
                        # time.sleep(1)
                        # self.do_send_key(self.toTime3, new_endTime_Three)
                        # log.logger.info("End Time Of Third Video Session Slot Is" + str(new_endTime_Three))
                        # time.sleep(1)
                        self.do_send_key(self.description, "Test Automation")
                        log.logger.info("Enter Description Of Video Session")
                        time.sleep(1)
                        # self.de_click(self.searchDD)
                        # time.sleep(1)
                        # totalUser = len(self.driver.find_elements(By.XPATH,
                        #                                           "//div[@class='relative w-full border-gray-300 rounded-md my-4 ']/div/div[2]"))
                        # log.logger.info(
                        #     "Number Of User Available In to The system for Video session ==" + str(totalUser))

                        # for j in range(totalUser + 1):
                        #     self.de_click(self.searchDD)
                        #     time.sleep(1)
                        #     # log.logger.info("Selected User For Video Session Is ==" + str(self.get_element_text(self.addUser)))
                        #     self.de_click(self.addUser)
                        #     time.sleep(1)

                        self.de_click(self.submitButton)
                        time.sleep(7)
                        break
                    else:
                        log.logger.info("MultiWay Video Session Already Created For This Interview")
                else:
                    log.logger.info("No To Perform Any Action")
        else:
            log.logger.info("There's No Interview Available to Create Multiway Video Session")

    def fetch_over_all_history_of_interview(self):
        time.sleep(4)
        log.logger.info("Fetch The Over all History Of Multiway Interview ")
        self.de_click(self.filterIcon)
        time.sleep(1)
        self.de_click(self.clearAll)
        time.sleep(1)
        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)

        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))
        if int(totalNumberOfInterviews) > 0:
            totalList = len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div"))
            applicantName = []
            applicantName = self.driver.find_elements(By.XPATH,
                                                      "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[1]/div[2]/h4")
            designation = []
            designation = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[1]/div[2]/h3")
            for i in range(totalList):
                totalInterview = []
                totalInterview = self.driver.find_elements(By.XPATH,
                                                           "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div")
                aName = applicantName[i].text
                time.sleep(0.5)
                desig = designation[i].text
                time.sleep(0.5)
                log.logger.info("Applicant Name ==" + str(aName) + "appeared for interview designation" + str(desig))
                totalInterview[i].click()
                time.sleep(1)
                self.de_click(self.multiWayTab)
                time.sleep(4)
                try:
                    checkDetails = self.driver.find_element(By.XPATH,
                                                            "//div[@class='bg-ime-gray-100 overflow-y-scroll [&::-webkit-scrollbar]:hidden dark:bg-black w-full flex p-[16px] flex-col pb-20 md:pb-[0px]']/div[2]/div/div[1]/div[2]/div/span").is_displayed()
                    value = str(checkDetails)
                    log.logger.info("" + str(value))
                    if value == "True":

                        numberOfChats = len(self.driver.find_elements(By.XPATH,
                                                                      "//div[@class='bg-ime-gray-100 overflow-y-scroll [&::-webkit-scrollbar]:hidden dark:bg-black w-full flex p-[16px] flex-col pb-20 md:pb-[0px]']/div[2]/div/div/div[2]/div/span"))
                        for j in range(numberOfChats):
                            history = []
                            history = self.driver.find_elements(By.XPATH,
                                                                "//div[@class='bg-ime-gray-100 overflow-y-scroll [&::-webkit-scrollbar]:hidden dark:bg-black w-full flex p-[16px] flex-col pb-20 md:pb-[0px]']/div[2]/div/div/div[2]/div/span")
                            historyInformation = history[j].text
                            log.logger.info("History Information For Above Applicant Is" + str(historyInformation))


                except Exception as e:
                    log.logger.info("There's No History Available")

        else:
            log.logger.info("There's No Interview Available")
