import time
import logging
from selenium.webdriver.common.by import By
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class ImeQueue_Details(BasePage):
    imeQueueIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[10]/a")

    numberOfInterview = (By.XPATH,
                         "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[1]/div[1]/h6")
    blockOfInterview = (By.XPATH,
                        "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div")

    # Filter iME queue

    filterIcon = (By.XPATH, "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[1]/div[2]/div[2]/button")

    serviceNameDD = (By.XPATH,
                     "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[3]/button")

    clearAll = (By.XPATH,
                "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[1]/h2[2]")

    applyButton = (By.XPATH,
                   "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[5]/div/button")
    # Service DD

    recruitmentService = (By.XPATH,
                          "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[3]/ul/li[1]")

    awardService = (By.XPATH,
                    "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[3]/ul/li[2]")

    marketingService = (By.XPATH,
                        "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[3]/ul/li[3]")

    learningService = (By.XPATH,
                       "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[3]/ul/li[4]")

    auditionService = (By.XPATH,
                       "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[3]/ul/li[5]")

    admissionService = (By.XPATH,
                        "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[3]/ul/li[6]")

    closeButton = (By.XPATH,
                   "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[3]/button/div/div/div/div")
    # Status DD

    statusDD = (By.XPATH,
                "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/button")

    notStartedStatus = (By.XPATH,
                        "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/ul/li[1]")

    inProgressStatus = (By.XPATH,
                        "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/ul/li[2]")

    completeStatus = (By.XPATH,
                      "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/ul/li[3]")

    rejectStatus = (By.XPATH,
                    "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/ul/li[4]")

    searchInput = (By.CSS_SELECTOR, "input[name='searchName']")

    designationName = (
        By.XPATH,
        "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div[1]/button/div[1]/div[2]/h3")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_imeQueue_icon(self):
        time.sleep(4)

    def fetch_overall_iMEQueue_details(self):
        log.logger.info("!!! == Assert that digit of iME Queue interviews displayed should match the total number of "
                        "interview"
                        "details list  == !!!")
        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)

        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))
        if int(totalNumberOfInterviews) > 0:
            totalNumberOfBlocks = len(self.driver.find_elements(By.XPATH,
                                                                "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div"))

            log.logger.info("Number Of Interview Inside List Of Blocks == " + str(totalNumberOfBlocks))
            # assert str(totalNumberOfBlocks) in totalNumberOfInterviews
            assert int(totalNumberOfBlocks) == int(totalNumberOfInterviews)
        else:
            log.logger.info("There's no interview available in iME Queue Library")

    def fetch_interview_iME_Queue(self):
        log.logger.info(
            "!!! == Fetch the list of interviews with all details inside IME queue == "
            "!!!")
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
            service = []
            service = self.driver.find_elements(By.XPATH,
                                                "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[1]/p")
            status = []
            status = self.driver.find_elements(By.XPATH,
                                               "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[2]/p")
            for i in range(totalList):
                log.logger.info("Name of applicant == " + str(applicantName[i].text))
                log.logger.info("Number Designation == " + str(designation[i].text))
                log.logger.info("Name Of Service  == " + str(service[i].text))
                log.logger.info("Interview Status == " + str(status[i].text))
        else:
            log.logger.info("There's no Interview available inside iME queue")

    def filter_interview_details(self):
        log.logger.info(
            "!!! == Filter the details of all interviewer based on service  == !!!")

        for i in range(6):
            self.de_click(self.filterIcon)
            time.sleep(0.5)
            self.de_click(self.serviceNameDD)
            time.sleep(0.5)
            serviceName = []
            serviceName = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[3]/ul/li")
            re = str(serviceName[i].text)
            log.logger.info(" " + str(re))

            if re == "Recruitment":
                self.de_click(self.recruitmentService)
                time.sleep(0.5)
                self.de_click(self.serviceNameDD)
                time.sleep(0.5)
                self.de_click(self.applyButton)

                totalService = len(self.driver.find_elements(By.XPATH,
                                                             "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[1]/p"))
                Service = []
                Service = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[1]/p")
                if totalService > 0:
                    for j in range(totalService):
                        name = str(Service[j].text)
                        if name == "Recruitment":
                            log.logger.info("Interviews Belong to service === " + name)
                else:
                    log.logger.info("Theres No Interview Available ")



            elif re == "Awards":
                self.de_click(self.clearAll)
                time.sleep(0.5)
                self.de_click(self.filterIcon)
                time.sleep(0.5)
                self.de_click(self.serviceNameDD)
                time.sleep(0.5)
                self.de_click(self.awardService)
                time.sleep(0.5)
                self.de_click(self.serviceNameDD)
                time.sleep(0.5)
                self.de_click(self.applyButton)

                totalService = len(self.driver.find_elements(By.XPATH,
                                                             "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[1]/p"))
                Service = []
                Service = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[1]/p")
                if totalService > 0:
                    for j in range(totalService):
                        name = str(Service[j].text)
                        if name == "Awards":
                            log.logger.info("Interviews Belong to service === " + name)
                else:
                    log.logger.info("There's no Interview Available")


            elif re == "Marketing":
                self.de_click(self.clearAll)
                time.sleep(0.5)
                self.de_click(self.filterIcon)
                time.sleep(0.5)
                self.de_click(self.serviceNameDD)
                time.sleep(0.5)
                self.de_click(self.marketingService)
                time.sleep(0.5)
                self.de_click(self.serviceNameDD)
                time.sleep(0.5)
                self.de_click(self.applyButton)

                totalService = len(self.driver.find_elements(By.XPATH,
                                                             "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[1]/p"))
                Service = []
                Service = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[1]/p")
                if totalService > 0:
                    for j in range(totalService):
                        name = str(Service[j].text)
                        if name == "Marketing":
                            log.logger.info("Interviews Belong to service === " + name)
                else:
                    log.logger.info("There's no Interview available")


            elif re == "Learning":
                self.de_click(self.clearAll)
                time.sleep(0.5)
                self.de_click(self.filterIcon)
                time.sleep(0.5)
                self.de_click(self.serviceNameDD)
                time.sleep(0.5)
                self.de_click(self.learningService)
                time.sleep(0.5)
                self.de_click(self.serviceNameDD)
                time.sleep(0.5)
                self.de_click(self.applyButton)

                totalService = len(self.driver.find_elements(By.XPATH,
                                                             "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[1]/p"))
                Service = []
                Service = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[1]/p")
                if totalService > 0:
                    for j in range(totalService):
                        name = str(Service[j].text)
                        if name == "Learning":
                            log.logger.info("Interviews Belong to service === " + name)
                else:
                    log.logger.info("There's no Interview available")




            elif re == "Auditions":
                self.de_click(self.clearAll)
                time.sleep(0.5)
                self.de_click(self.filterIcon)
                time.sleep(0.5)
                self.de_click(self.serviceNameDD)
                time.sleep(0.5)
                self.de_click(self.auditionService)
                time.sleep(0.5)
                self.de_click(self.serviceNameDD)
                time.sleep(0.5)
                self.de_click(self.applyButton)

                totalService = len(self.driver.find_elements(By.XPATH,
                                                             "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[1]/p"))
                Service = []
                Service = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[1]/p")
                if totalService > 0:
                    for j in range(totalService):
                        name = str(Service[j].text)
                        if name == "Auditions":
                            log.logger.info("Interviews Belong to service === " + name)
                else:
                    log.logger.info("There's no interview available")

            elif re == "Admissions":
                self.de_click(self.clearAll)
                time.sleep(0.5)
                self.de_click(self.filterIcon)
                time.sleep(0.5)
                self.de_click(self.serviceNameDD)
                time.sleep(0.5)
                self.de_click(self.admissionService)
                time.sleep(0.5)
                self.de_click(self.serviceNameDD)
                time.sleep(0.5)
                self.de_click(self.applyButton)

                totalService = len(self.driver.find_elements(By.XPATH,
                                                             "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[1]/p"))
                Service = []
                Service = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[1]/p")
                if totalService > 0:
                    for j in range(totalService):
                        name = str(Service[j].text)
                        if name == "Admissions":
                            log.logger.info("Interviews Belong to service === " + name)
                    else:
                        log.logger.info("There's no interview available")

            else:
                break

    def filter_interview_details_on_status(self):

        log.logger.info(
            "!!! == Filter the details of all interviewer based on interview Status  == !!!")
        self.de_click(self.filterIcon)
        time.sleep(0.5)
        self.de_click(self.clearAll)
        time.sleep(0.5)

        for i in range(2):
            self.de_click(self.filterIcon)
            time.sleep(0.5)
            self.de_click(self.statusDD)
            time.sleep(0.5)
            statusName = []
            statusName = self.driver.find_elements(By.XPATH,
                                                   "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/ul/li")
            status = str(statusName[i].text)
            log.logger.info(" " + str(status))

            if status == "Not Started":
                self.de_click(self.notStartedStatus)
                time.sleep(0.5)
                self.de_click(self.statusDD)
                time.sleep(0.5)
                self.de_click(self.applyButton)

                totalStatus = len(self.driver.find_elements(By.XPATH,
                                                            "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[2]/p"))
                Status = []
                Status = self.driver.find_elements(By.XPATH,
                                                   "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[2]/p")
                if totalStatus > 0:
                    for j in range(totalStatus):
                        name = str(Status[j].text)
                        if name == "Not Started":
                            log.logger.info("Interview status is === " + name)
                else:
                    log.logger.info("There's no interview available")


            elif status == "In Progress":
                self.de_click(self.clearAll)
                time.sleep(0.5)
                self.de_click(self.filterIcon)
                time.sleep(0.5)
                self.de_click(self.statusDD)
                time.sleep(0.5)
                self.de_click(self.inProgressStatus)
                time.sleep(0.5)
                self.de_click(self.statusDD)
                time.sleep(0.5)
                self.de_click(self.applyButton)

                totalStatus = len(self.driver.find_elements(By.XPATH,
                                                            "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[2]/p"))
                Status = []
                Status = self.driver.find_elements(By.XPATH,
                                                   "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[2]/p")
                if totalStatus > 0:
                    for j in range(totalStatus):
                        name = str(Status[j].text)
                        if name == "In Progress":
                            log.logger.info("Interview status is === " + name)
                else:
                    log.logger.info("There's no interview available")


            elif status == "Complete":
                self.de_click(self.clearAll)
                time.sleep(0.5)
                self.de_click(self.filterIcon)
                time.sleep(0.5)
                self.de_click(self.statusDD)
                time.sleep(0.5)
                self.de_click(self.completeStatus)
                time.sleep(0.5)
                self.de_click(self.statusDD)
                time.sleep(0.5)
                self.de_click(self.applyButton)

                totalStatus = len(self.driver.find_elements(By.XPATH,
                                                            "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[2]/p"))
                Status = []
                Status = self.driver.find_elements(By.XPATH,
                                                   "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[2]/p")
                if totalStatus > 0:
                    for j in range(totalStatus):
                        name = str(Status[j].text)
                        if name == "Complete":
                            log.logger.info("Interview status is === " + name)
                else:
                    log.logger.info("There's no interview available")

            elif status == "Reject":
                self.de_click(self.clearAll)
                time.sleep(0.5)
                self.de_click(self.filterIcon)
                time.sleep(0.5)
                self.de_click(self.statusDD)
                time.sleep(0.5)
                self.de_click(self.rejectStatus)
                time.sleep(0.5)
                self.de_click(self.statusDD)
                time.sleep(0.5)
                self.de_click(self.applyButton)

                totalStatus = len(self.driver.find_elements(By.XPATH,
                                                            "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[2]/p"))
                Status = []
                Status = self.driver.find_elements(By.XPATH,
                                                   "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[2]/div[2]/p")
                if totalStatus > 0:
                    for j in range(totalStatus):
                        name = str(Status[j].text)
                        if name == "Reject":
                            log.logger.info("Interview status is === " + name)
                else:
                    log.logger.info("There's no interview available")


            else:
                break

    def filter_interview_details_by_designation(self):
        global designationTitle
        log.logger.info(
            "!!! == Filter the details of all interviewer based on interview designation  == !!!")
        time.sleep(1)
        self.de_click(self.filterIcon)
        time.sleep(0.5)
        self.de_click(self.clearAll)
        time.sleep(2)
        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)

        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))
        if int(totalNumberOfInterviews) > 0:
            titleValue = self.driver.find_element(By.XPATH,
                                                  "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div[1]/button/div[1]/div[2]/h3")
            time.sleep(0.5)
            # value = str(titleValue)
            designationTitle = self.get_element_text(self.designationName)
            time.sleep(0.5)
            self.de_click(self.filterIcon)
            time.sleep(0.5)
            self.do_send_key(self.searchInput, designationTitle)
            time.sleep(0.5)
            self.de_click(self.applyButton)
            time.sleep(0.5)
            totalDesignation = len(self.driver.find_elements(By.XPATH,
                                                             "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[1]/div[2]/h3"))
            Designation = []
            Designation = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div/button/div[1]/div[2]/h3")
            log.logger.info("Total Available Interview For  === " + str(totalDesignation))
            for j in range(totalDesignation):
                name = str(Designation[j].text)
                assert name == designationTitle
                log.logger.info("Interviewer applied for the designation is === " + designationTitle)
                log.logger.info("Interviewer applied for the designation is === " + name)

        else:
            log.logger.info("There's No Data Available")
