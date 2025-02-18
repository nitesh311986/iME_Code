import time
from datetime import datetime, timedelta
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Recruitment_Details(BasePage):
    recruitmentIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[6]/a")
    numberOfInterview = (By.XPATH,
                         "//div[@class='w-full h-full min-h-screen overflow-hidden duration-300 flex flex-col ml-[250px]']/div/div[3]/div/div/div[1]/h1")
    blockOfInterview = (By.XPATH,
                        "//div[@class='w-full h-full min-h-screen overflow-hidden duration-300 flex flex-col ml-[250px]']/div/div[3]/div/div/div[2]/div/div/div")
    postTitle = (By.XPATH,
                 "//div[@class='grid grid-cols-1 md:grid-cols-1 xl:grid-cols-1 gap-[16px] ']/div/div/div/div[1]/div/div[2]")
    numberOfApplication = (By.XPATH,
                           "//div[@class='grid grid-cols-1 md:grid-cols-1 xl:grid-cols-1 gap-[16px] ']/div/div/div/div[2]/div/div/div[1]")

    # Application Details Page
    backButton = (By.XPATH,
                  "//div[@class='dark:bg-black w-full px-[24px] pb-[24px] mt-8 h-full ']/button/*[local-name()='svg'][@class='h-[8px] w-[5px]']")
    numberOfApplicants = (By.XPATH, "//div[@class='flex justify-between items-center mt-[16px] mb-[32px]']/h1")
    detailsOfApplicants = (By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div")
    viewButton = (By.XPATH,
                  "//div[@class='grid grid-cols-1 md:grid-cols-1 xl:grid-cols-1 gap-[16px] ']/div[1]/div/div/div[2]/button[1]")

    filterButton = (By.XPATH, "//div[@class='flex justify-between items-center mt-[16px] mb-[32px]']/div/div[2]/button")

    statusDD = (By.XPATH, "//div[@class='mb-4 relative w-full lg:max-w-[328px]']/button")

    completedOption = (By.XPATH, "//div[@class='mb-4 relative w-full lg:max-w-[328px]']/ul/li[1]")

    inReviewOption = (By.XPATH, "//div[@class='mb-4 relative w-full lg:max-w-[328px]']/ul/li[2]")
    shortlistedOption = (By.XPATH, "//div[@class='mb-4 relative w-full lg:max-w-[328px]']/ul/li[3]")
    rejectedOption = (By.XPATH, "//div[@class='mb-4 relative w-full lg:max-w-[328px]']/ul/li[4]")
    interviewStatus = (By.XPATH,
                       "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div[1]/div[3]/div/div[4]/div[1]/p")

    hiredOption = (By.XPATH, "//div[@class='mb-4 relative w-full lg:max-w-[328px]']/ul/li[6]")

    applyButton = (
        By.XPATH, "//div[@class='mt-[16px] self-start mb-[20px] flex flex-row w-[67px] justify-end']/div/button")

    closeButton = (By.XPATH, "//div[@class='mb-4 relative w-full lg:max-w-[328px]']/button/div/div/div/div")

    clearAllLink = (By.XPATH, "//div[@class='flex justify-between items-center my-[20px]']/h2[2]")

    searchInput = (By.CSS_SELECTOR, "input[name='searchName']")
    interviewerName = (
        By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div[1]/div[1]/div[2]/h3")

    # Rating Function
    viewApplicationButton = (
        By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div[1]/button")
    interviewTab = (By.XPATH,
                    "//div[@class='ime-tab-group font-semibold flex flex-row max-sm:basis-full overflow-hidden border rounded-md divide-x border-gray-300 dark:border-gray-600 divide-ime-gray-300 dark:divide-ime-gray-600']/button[2]")
    videoButton = (By.XPATH,
                   "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden mb-[8px]']/button[3]")
    numberOfQuestions = (
        By.XPATH, "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div")

    commentTextArea = (By.CSS_SELECTOR, "textarea[name='comment']")

    rateIcon = (By.XPATH, "//div[@class='flex items-center justify-between']/div/div[2]/*[local-name()='svg']")

    rateIconTeam = (By.XPATH, "//div[@class='flex items-center justify-between']/div/div[3]/*[local-name()='svg']")

    saveButton = (By.CSS_SELECTOR,
                  "button[class=' bg-ime-orange-accent hover:bg-ime-orange-accent !text-white rounded-[6px] rounded-[4px] transition-colors h-[32px] px-[22px] text-xs bg-ime-accent hover:bg-blue-700 text-white']")

    # Multimedia Resubmission
    viewApplicationButtonForMultimedia = (
        By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div[2]/button")
    oneWayInterViewTab = (By.XPATH, "//div[@class='flex w-full justify-between h-[36px] mb-[12px]']/div/button[2]/div")
    multiMediaTab = (By.XPATH,
                     "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden mb-[8px]']/button[4]")
    inputCheckBox = (By.XPATH,
                     "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div/div[1]/div/div/input")
    requestResubmission = (By.XPATH, "//div[@class='w-full flex flex-col ']/div[1]/button")
    Comment = (By.CSS_SELECTOR, "textarea[name='comment']")
    resubmissionButton = (By.XPATH, "//div[@class='flex flex-row items-center justify-center gap-[16px]']/button[1]")
    verificationText = (By.XPATH, "//div[@class='flex flex-row justify-between items-center']/div/div")

    # Back Button
    backApplicantProfile = (By.XPATH, "//div[@class='flex w-full justify-between h-[36px] mb-[12px]']/button")
    backApplicationPage = (By.XPATH, "//div[@class='dark:bg-black w-full px-[24px] pb-[24px] mt-8 h-full ']/button")

    # Interview Status Update
    Shortlisted = (By.XPATH,
                   "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div[1]/div[3]/div/div[1]/button[2]")
    Rejected = (By.XPATH,
                "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div[1]/div[3]/div/div[1]/button[3]")
    emailCheckBox = (By.XPATH,
                     "//div[@class='flex flex-col w-full text-ime-gray-500 dark:text-ime-gray-400 text-[14px]']/div[2]/div[1]/div/input")
    selectEmailDD = (By.XPATH, "//div[@class='flex flex-col space-y-2']/div/button")
    optionOfSelectEmailDD = (By.XPATH, "//div[@class='flex flex-col space-y-2']/div/ul/li[1]")
    submitButton = (By.XPATH, "//div[@class='flex justify-end gap-[16px]']/button")

    transcriptionButton = (By.XPATH,
                           "//div[@class='ime-tab-group pl-6 pt-6 w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[2]")

    transcriptionPara = (By.XPATH, "//div[@class='h-[25vh] md:h-[30vh] lg:h-[53vh] overflow-y-auto']/div/p")

    closeVideoScreen = (By.XPATH,
                        "//div[@class='min-w-[60%] flex flex-col bg-ime-gray-100 dark:bg-ime-gray-900 rounded-t-2xl p-6 lg:rounded-tl-none lg:rounded-r-2xl']/div[1]/*[local-name()='svg']")

    # MultiWay

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
    submitButtonMul = (
        By.XPATH,
        "//button[@class='mt-6 flex-1 disabled:bg-black bg-[#0070F3] rounded-[4px] transition-colors h-[32px] px-[22px] text-xs bg-ime-accent hover:bg-blue-700 text-white']")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_recruitment_icon(self):
        time.sleep(5)
        self.de_click(self.recruitmentIcon)
        time.sleep(4)

    def fetch_overall_interviews_details(self):
        log.logger.info(
            "!!! == Assert that digit of interviews displayed should match the total number of interview details list "
            "for recruitment  == !!!")
        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)
        number = totalNumberOfInterviews.split()
        numberOfInterviews = number[0]
        log.logger.info("Number Of Interviews == " + str(numberOfInterviews))
        if int(numberOfInterviews) > 0:
            totalNumberOfBlocks = len(self.driver.find_elements(By.XPATH,
                                                                "//div[@class='w-full h-full min-h-screen overflow-hidden duration-300 flex flex-col ml-[250px]']/div/div[3]/div/div/div[2]/div/div/div"))

            log.logger.info("Number Of Interview Inside List Of Blocks == " + str(totalNumberOfBlocks))
            # assert str(totalNumberOfBlocks) in totalNumberOfInterviews
            assert int(totalNumberOfBlocks) == int(numberOfInterviews)
        else:
            log.logger.info("There's No Data Available")

    def fetch_interview_position_applicant_numbers_for_recruitment(self):
        log.logger.info(
            "!!! == Fetch the list of positions and applicants appeared for particular position of Recruitment Vertical"
            "== !!!")

        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)
        number = totalNumberOfInterviews.split()
        numberOfInterviews = number[0]
        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))
        if int(numberOfInterviews) > 0:

            totalList = len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='grid grid-cols-1 md:grid-cols-1 xl:grid-cols-1 gap-[16px] ']/div"))

            totalPosition = []
            totalPosition = self.driver.find_elements(By.XPATH,
                                                      "//div[@class='grid grid-cols-1 md:grid-cols-1 xl:grid-cols-1 gap-[16px] ']/div/div/div/div[1]/div/div[2]")
            totalApplication = []
            totalApplication = self.driver.find_elements(By.XPATH,
                                                         "//div[@class='grid grid-cols-1 md:grid-cols-1 xl:grid-cols-1 gap-[16px] ']/div/div/div/div[2]/div/div/div[1]")
            for i in range(totalList):
                log.logger.info("Name Of Designation For Interview == " + str(totalPosition[i].text))
                log.logger.info("Number Of Applicant Applied For Designation == " + str(totalApplication[i].text))

        else:
            log.logger.info("There's no data available")

    def traverse_recruitment_interview_list(self):
        log.logger.info(
            "!!! == Fetch the details of all interviewer appeared in the Recruitment interviews for same position  == "
            "!!!")
        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)
        number = totalNumberOfInterviews.split()
        numberOfInterviews = number[0]
        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))
        if int(numberOfInterviews) > 0:

            self.de_click(self.viewButton)
            time.sleep(3)
            Number = self.get_element_text(self.numberOfApplicants)
            totalNumber = Number.split()
            applicantDigit = totalNumber[0]
            log.logger.info("Number Of Application == " + str(applicantDigit))
            List = len(self.driver.find_elements(By.XPATH,
                                                 "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div"))
            log.logger.info("Number Of Interviewer Blocks == " + str(List))
            assert int(applicantDigit) == int(List)
            time.sleep(1)

            totalList = len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div"))

            Name = []
            Name = self.driver.find_elements(By.XPATH,
                                             "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div/div/div[2]/h3")
            Email = []
            Email = self.driver.find_elements(By.XPATH,
                                              "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div/div/div[2]/h5")
            Position = []
            Position = self.driver.find_elements(By.XPATH,
                                                 "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div/div[3]/div/div[3]/div[1]/p")
            Date = []
            Date = self.driver.find_elements(By.XPATH,
                                             "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div/div[3]/div/div[3]/div[2]/p")
            Status = []
            Status = self.driver.find_elements(By.XPATH,
                                               "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div/div[3]/div/div[3]/div[1]/p")
            UpdatedOn = []
            UpdatedOn = self.driver.find_elements(By.XPATH,
                                                  "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div/div[3]/div/div[3]/div[2]/p")
            UpdatedBy = []
            UpdatedBy = self.driver.find_elements(By.XPATH,
                                                  "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div/div[3]/div/div[3]/div[3]/p")

            for i in range(totalList):
                log.logger.info("Name Of Interviewer == " + str(Name[i].text))
                log.logger.info("Email Of Interviewer == " + str(Email[i].text))
                log.logger.info("Position Applied For == " + str(Position[i].text))
                # log.logger.info("Date Appeared For Interview == " + str(Date[i].text))
                # log.logger.info("Interview Status == " + str(Status[i].text))
                # log.logger.info("Interview Status Updated On == " + str(UpdatedOn[i].text))
                # log.logger.info("Interview Status Updated By == " + str(UpdatedBy[i].text))
            self.de_click(self.backButton)
            time.sleep(1)
        else:
            log.logger.info("There's No Data Available")

    def filter_interview_details(self):
        log.logger.info(
            "!!! == Filter the details of all interviewer appeared in the Recruitment interview based on interview status  == !!!")
        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)
        number = totalNumberOfInterviews.split()
        numberOfInterviews = number[0]
        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))
        if int(numberOfInterviews) > 0:
            self.de_click(self.viewButton)
            time.sleep(3)
            status = self.get_element_text(self.interviewStatus)
            log.logger.info(" Status" + status)
            time.sleep(0.5)
            self.de_click(self.filterButton)
            time.sleep(0.5)
            self.de_click(self.statusDD)
            time.sleep(0.5)
            if status == "Completed":
                self.de_click(self.completedOption)
                time.sleep(0.5)
                self.de_click(self.statusDD)
                time.sleep(0.5)
                self.de_click(self.applyButton)
                time.sleep(0.5)
            elif status == "In Review":
                self.de_click(self.rejectedOption)
                time.sleep(0.5)
                self.de_click(self.statusDD)
                time.sleep(0.5)
                self.de_click(self.applyButton)
                time.sleep(0.5)
            elif status == "Shortlisted":
                self.de_click(self.shortlistedOption)
                time.sleep(0.5)
                self.de_click(self.statusDD)
                time.sleep(0.5)
                self.de_click(self.applyButton)
                time.sleep(0.5)
            elif status == "Rejected":
                self.de_click(self.rejectedOption)
                time.sleep(0.5)
                self.de_click(self.statusDD)
                time.sleep(0.5)
                self.de_click(self.applyButton)
                time.sleep(0.5)
            else:
                log.logger.info("Interview Is Not Available")
            Status = []
            Status = self.driver.find_elements(By.XPATH,
                                               "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div/div[3]/div/div[4]/div[1]/p")
            for i in Status:
                interview_status = i.text
                assert interview_status == status
            log.logger.info(
                "!!! == Filtered the details of all interviewer appeared in the Admission interview based on interview "
                "status  === !!!" + str(status))
            time.sleep(0.5)
            self.de_click(self.filterButton)
            time.sleep(0.5)
            self.de_click(self.closeButton)
            time.sleep(1)
            self.de_click(self.applyButton)
            time.sleep(1)
            self.de_click(self.backButton)
            time.sleep(1)
        else:
            log.logger.info("There's no data available")

        # time.sleep(0.5)
        # self.de_click(self.filterButton)
        # time.sleep(0.5)
        # self.de_click(self.closeButton)
        # time.sleep(0.5)
        # self.de_click(self.statusDD)
        # time.sleep(0.5)
        # self.de_click(self.shortlistedOption)
        # time.sleep(0.5)
        # self.de_click(self.statusDD)
        # time.sleep(0.5)
        # self.de_click(self.applyButton)
        # time.sleep(0.5)
        #
        # for i in Status:
        #     status = i.text
        #     log.logger.info("Interview Status == " + str(status))
        #     assert status == "Shortlisted"
        # time.sleep(0.5)

    def filter_interview_details_through_search(self):
        log.logger.info(
            "!!! == Filter the details of all interviewer appeared in the Recruitment interview based on interviewer "
            "Name  == !!!")
        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)
        number = totalNumberOfInterviews.split()
        numberOfInterviews = number[0]
        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))
        if int(numberOfInterviews) > 0:
            time.sleep(0.5)
            self.de_click(self.viewButton)
            time.sleep(2)
            applicantName = self.get_element_text(self.interviewerName)
            time.sleep(0.5)
            self.de_click(self.filterButton)
            time.sleep(0.5)
            self.do_send_key(self.searchInput, applicantName)
            time.sleep(0.5)
            self.de_click(self.applyButton)

            Name = []
            Name = self.driver.find_elements(By.XPATH,
                                             "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div/div/div[2]/h3")

            for i in Name:
                name = i.text
                log.logger.info("Interviewer Name == " + str(name))
                assert name == applicantName
            time.sleep(0.5)
            log.logger.info(
                "!!! == Filtered the details of all interviewer appeared in the Recruitment interview based on interview "
                "Name  === !!!" + str(applicantName))
            time.sleep(0.5)
            self.de_click(self.filterButton)
            time.sleep(0.5)
            self.de_click(self.clearAllLink)
            time.sleep(1)
            self.de_click(self.applyButton)
            time.sleep(1)
            self.de_click(self.backButton)
            time.sleep(1)
        else:
            log.logger.info("There's No data available")

        # Rate The Interview

    def test_your_rating_function(self):
        log.logger.info(
            "!!! == Update Or Add Rating Star Function For Recruitment Interview   == !!!")

        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)
        number = totalNumberOfInterviews.split()
        numberOfInterviews = number[0]
        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))
        if int(numberOfInterviews) > 0:

            self.de_click(self.viewButton)
            time.sleep(3)
            log.logger.info(
                "!!! == User Has clicked on view application button  == !!!")
            self.de_click(self.viewApplicationButton)
            time.sleep(2)
            self.de_click(self.oneWayInterViewTab)
            log.logger.info(
                "!!! == User Has clicked on interview details tab  == !!!")
            time.sleep(3)
            self.de_click(self.videoButton)
            log.logger.info(
                "!!! == User Has clicked on video answer details tab  == !!!")
            time.sleep(1)

            # Find Number Of Interviews And Rate The Same

            totalQuestions = len(self.driver.find_elements(By.XPATH,
                                                           "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div"))

            for i in range(totalQuestions):
                elements = []
                elements = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[1]/div[2]/div/div[2]")
                elements[i].click()
                log.logger.info(
                    "!!! == User Has clicked on your rating star == !!!")
                time.sleep(2)
                self.do_send_key(self.commentTextArea, "Good")
                time.sleep(1)
                self.de_click(self.rateIcon)
                time.sleep(1)
                self.de_click(self.saveButton)
                time.sleep(6)
                log.logger.info(
                    "!!! == User Has completed your rating process == !!!")

                # Team Rating
                log.logger.info(
                    "!!! == Update Or Add Rating Star Function For Interview  == !!!")

                time.sleep(1)
                totalQuestions = len(self.driver.find_elements(By.XPATH,
                                                               "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div"))

                for i in range(totalQuestions):
                    elements = []
                    elements = self.driver.find_elements(By.XPATH,
                                                         "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[2]/div[2]/div/div[4]")
                    elements[i].click()
                    log.logger.info(
                        "!!! == User Has clicked on team rating star == !!!")
                    time.sleep(2)
                    self.do_send_key(self.commentTextArea, "Good")
                    time.sleep(1)
                    self.de_click(self.rateIconTeam)
                    time.sleep(1)
                    self.de_click(self.saveButton)
                    time.sleep(6)
                    log.logger.info(
                        "!!! == User Has completed team rating process == !!!")

        else:
            log.logger.info("There's no data available")

            # Multimedia Resubmission

    def test_multimedia_resubmission(self):
        log.logger.info(
            "!!! == Resubmit  Multimedia Request Test Case For Recruitment == !!!")
        time.sleep(1)
        self.de_click(self.backApplicantProfile)
        time.sleep(1)
        self.de_click(self.backApplicationPage)
        time.sleep(1)
        self.de_click(self.viewButton)
        time.sleep(3)
        log.logger.info(
            "!!! == User Has clicked on view application button  == !!!")
        self.de_click(self.viewApplicationButton)
        time.sleep(2)
        self.de_click(self.oneWayInterViewTab)
        log.logger.info(
            "!!! == User Has clicked on one way interview tab  == !!!")
        time.sleep(2)
        self.de_click(self.multiMediaTab)
        time.sleep(2)
        noMultiMedia = self.driver.find_element(By.XPATH,
                                                "//div[@class='flex flex-col gap-[16px]']/div[2]/div[2]/div/div/div")
        Message = noMultiMedia.text
        if "No Multimedia" in Message:
            log.logger.info("There's No Multimedia Document Available")
        else:
            resubmission = self.driver.find_element(By.XPATH,
                                                    "//div[@class='flex flex-col gap-[16px]']/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div")
            message = noMultiMedia.text
            if "Resubmission Requested" in message:
                log.logger.info("Multimedia Resubmission Request Generated Already")

            # try:
            #     submissionMessage = self.driver.find_element(By.XPATH,
            #                                                  "//div[@class='flex flex-row justify-center items-center rounded-[12px] bg-ime-red-500 bg-opacity-20 text-ime-red-700 w-[186px] h-6 text-[12px]']").is_displayed()
            #     log.logger.info(
            #         "!!! == Multimedia Resubmission Request Has Already Been Submitted == !!!")
            # except Exception as e:
            else:
                self.de_click(self.inputCheckBox)
                time.sleep(1)
                self.de_click(self.requestResubmission)
                time.sleep(1)
                log.logger.info(
                    "!!! == User Has clicked on resubmission button  == !!!")
                self.do_send_key(self.commentTextArea, "Please Submit Documents Again")
                time.sleep(1)
                self.de_click(self.resubmissionButton)
                time.sleep(7)
                # Message = self.get_element_text(self.verificationText)
                # assert Message == "Resubmission Requested"
                log.logger.info(
                    "!!! == Multimedia Resubmission Request Submitted Successfully == !!!")

    def test_update_interview_status(self):
        log.logger.info(
            "!!! == Update The Status Of Recruitment Interview == !!!")
        time.sleep(1)
        self.de_click(self.backApplicantProfile)
        time.sleep(1.5)
        self.de_click(self.backApplicationPage)
        time.sleep(1.5)
        self.de_click(self.viewButton)
        time.sleep(3)
        # time.sleep(2)
        # self.de_click(self.backApplicantProfile)
        # time.sleep(2)
        value = self.driver.find_element(By.XPATH,
                                         "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div[1]/div[3]/div/div[1]/button[2]").is_enabled()
        time.sleep(0.5)
        validation = str(value)
        log.logger.info("Status == " + validation)
        if validation == 'True':
            self.de_click(self.Shortlisted)
            time.sleep(1)
            self.de_click(self.emailCheckBox)
            time.sleep(1)
            self.de_click(self.selectEmailDD)
            time.sleep(0.5)
            self.de_click(self.optionOfSelectEmailDD)
            time.sleep(0.5)
            self.de_click(self.submitButton)
            time.sleep(10)
            log.logger.info("Status of interview Has Benn Updated to shortlisted")

        else:
            self.de_click(self.Rejected)
            time.sleep(1)
            self.de_click(self.emailCheckBox)
            time.sleep(1)
            self.de_click(self.selectEmailDD)
            time.sleep(0.5)
            self.de_click(self.optionOfSelectEmailDD)
            time.sleep(0.5)
            self.de_click(self.submitButton)
            time.sleep(10)
            log.logger.info("Status of interview Has Been Updated to rejected")
            stat = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div[1]/div[3]/div/div[4]/div[1]/p"))
            )
            # Replace with your element locator and expected text
            log.logger.info("Status Of Interview Is === " + stat.text)

    def fetch_interview_transcript(self):
        log.logger.info("==== Verify and fetched transcription of Recruitment interviews ==== ")
        self.de_click(self.backApplicationPage)
        time.sleep(1.5)
        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)
        number = totalNumberOfInterviews.split()
        numberOfInterviews = number[0]
        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))
        if int(numberOfInterviews) > 0:
            totalList = len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='grid grid-cols-1 md:grid-cols-1 xl:grid-cols-1 gap-[16px] ']/div"))

            for i in range(totalList):
                time.sleep(1.5)
                numberOfDesignation = []
                numberOfDesignation = self.driver.find_elements(By.XPATH,
                                                                "//div[@class='grid grid-cols-1 md:grid-cols-1 xl:grid-cols-1 gap-[16px] ']/div/div/div/div[2]/button[1]")
                nameOfDesignation = []
                nameOfDesignation = self.driver.find_elements(By.XPATH,
                                                              "//div[@class='grid grid-cols-1 md:grid-cols-1 xl:grid-cols-1 gap-[16px] ']/div/div/div/div[1]/div/div[2]/h5")
                time.sleep(0.5)
                Designation = nameOfDesignation[i].text
                log.logger.info("Name Of Designation ===" + Designation)
                numberOfDesignation[i].click()
                time.sleep(3)

                totalInterview = len(self.driver.find_elements(By.XPATH,
                                                               "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div/button"))

                for j in range(totalInterview):
                    nameOfInterviewer = []
                    nameOfInterviewer = self.driver.find_elements(By.XPATH,
                                                                  "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div/div/div[2]/h3")
                    time.sleep(1.5)
                    log.logger.info("Number Of Applicants" + str(j))
                    Name = nameOfInterviewer[j].text
                    log.logger.info("Name Of Interviewer Name ===" + Name)
                    viewButton = []
                    viewButton = self.driver.find_elements(By.XPATH,
                                                           "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div/button")

                    viewButton[j].click()
                    time.sleep(3)
                    self.de_click(self.oneWayInterViewTab)
                    time.sleep(2)
                    self.de_click(self.videoButton)
                    time.sleep(2)
                    totalQuestions = len(self.driver.find_elements(By.XPATH,
                                                                   "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div"))

                    for k in range(totalQuestions):
                        elements = []
                        elements = self.driver.find_elements(By.XPATH,
                                                             "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[1]/div[2]/div/div[2]")
                        elements[k].click()
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

                    self.de_click(self.backApplicantProfile)
                    time.sleep(2)
                self.de_click(self.backApplicationPage)
                time.sleep(2)

    def test_create_multiway_for_recruitment(self):
        time.sleep(2)
        log.logger.info("!!! == Create Multiway Vide Session From Recruitment Vertical  == !!!")
        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)
        number = totalNumberOfInterviews.split()
        numberOfInterviews = number[0]
        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))
        if int(numberOfInterviews) > 0:
            self.de_click(self.viewButton)
            time.sleep(5)
            totalList = len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div[1]/div[3]/div/div[1]/button"))

            log.logger.info("Number Of Interviewer Blocks == " + str(totalList))

            ActionsIcon = []
            ActionsIcon = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div[1]/div[3]/div/div[1]/button/p")

            ActionsButton = []
            ActionsButton = self.driver.find_elements(By.XPATH,
                                                      "//div[@class='grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-[16px] ']/div[1]/div[3]/div/div[1]/button")
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
                        time.sleep(2)
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
                        time.sleep(2)
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

                        self.de_click(self.submitButtonMul)
                        time.sleep(7)
                        break
                    else:
                        log.logger.info("MultiWay Video Session Already Created For This Interview")
                else:
                    log.logger.info("No To Perform Any Action")

        else:
            log.logger.info("There's No Interview Available to Create Multiway Video Session")
