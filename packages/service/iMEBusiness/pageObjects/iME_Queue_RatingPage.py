import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class RatingPage(BasePage):
    imeQueueIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[10]/a")

    # Filter Button
    numberOfInterview = (By.XPATH,
                         "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[1]/div[1]/h6")

    filterIcon = (By.XPATH, "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[1]/div[2]/div[2]/button")

    statusDD = (By.XPATH,
                "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/button")

    inProgressStatus = (By.XPATH,
                        "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/ul/li[2]")
    notStartedYet = (By.XPATH,
                     "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/ul/li[1]")

    clearAll = (By.XPATH,
                "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[1]/h2[2]")

    applyButton = (By.XPATH,
                   "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[5]/div/button")

    # Applicant Library

    firstApplicant = (By.XPATH, "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div[1]")

    oneWayInterviewTab = (By.XPATH,
                          "//div[@class='flex w-full justify-between h-[36px] mb-[12px]']/div/button[2]")

    videoButton = (By.XPATH,
                   "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden mb-[8px]']/button[3]")
    multiMediaButton = (By.XPATH,
                        "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden mb-[8px]']/button[4]")

    numberOfInterviewQuestion = (By.XPATH, "//div[@id='headlessui-tabs-panel-:r49:']/div/div/div[2]/div")

    yourRatingStar = (
        By.XPATH, "//div[@id='headlessui-tabs-panel-:r49:']/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[5]")

    teamRatingStar = (
        By.XPATH, "//div[@id='headlessui-tabs-panel-:r49:']/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[5]")

    commentTextArea = (By.CSS_SELECTOR, "textarea[name='comment']")

    rateIconYour = (By.XPATH, "//div[@class='flex items-center justify-between']/div/div[3]/*[local-name()='svg']")

    rateIconTeam = (By.XPATH, "//div[@class='flex items-center justify-between']/div/div[4]/*[local-name()='svg']")

    saveButton = (By.CSS_SELECTOR,
                  "button[class=' bg-ime-orange-accent hover:bg-ime-orange-accent !text-white rounded-[6px] rounded-[4px] transition-colors h-[32px] px-[22px] text-xs bg-ime-accent hover:bg-blue-700 text-white']")

    # Complete Rating

    completeButton = (By.XPATH,
                      "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div[1]/button/div[2]/div[3]/button")

    yesButton = (By.XPATH,
                 "//div[@class='flex flex-col w-full text-ime-gray-500 dark:text-ime-gray-400 text-[14px]']/div/div[2]/button[1]")

    # Update Status
    assignUser = (
        By.XPATH,
        "//div[@class='flex flex-wrap gap-x-[20px] gap-y-[16px] pb-[16px]']/button[6]/div")

    selectUserDD = (By.XPATH,
                    "//div[@class='flex flex-col w-full text-ime-gray-500 dark:text-ime-gray-400 text-[14px]']/form/div[1]/div/button")

    optionOfSelectUserDD = (By.XPATH,
                            "//div[@class='flex flex-col w-full text-ime-gray-500 dark:text-ime-gray-400 text-[14px]']/form/div[1]/div/ul/li[1]")

    assignButton = (By.XPATH,
                    "//div[@class='flex flex-col w-full text-ime-gray-500 dark:text-ime-gray-400 text-[14px]']/form/div[2]/button")

    assignedUserTab = (By.XPATH,
                       "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden mb-[8px]']/button[5]")

    userDetail = (By.XPATH,
                  "//div[@class='w-full flex flex-col border rounded-md border-ime-gray-300 dark:border-ime-gray-700 bg-white dark:bg-ime-gray-900 overflow-hidden']/table/tbody/tr[1]/td[1]/div[2]/h5")

    # Update Status

    shortListed = (
        By.XPATH,
        "//div[@class='grid grid-cols-5 sm:flex flex-wrap gap-x-[20px] gap-y-[16px] pb-[16px]']/button[2]/div")
    rejected = (By.XPATH, "//div[@class='grid grid-cols-5 sm:flex flex-wrap gap-x-[20px] gap-y-[16px] pb-[16px]']/button[3]/div")
    emailCheckBox = (By.XPATH,
                     "//div[@class='flex flex-col w-full text-ime-gray-500 dark:text-ime-gray-400 text-[14px]']/div[2]/div/div/input")
    selectEmailDD = (By.XPATH, "//div[@class='flex flex-col space-y-2']/div/button")
    optionOfSelectEmailDD = (By.XPATH, "//div[@class='flex flex-col space-y-2']/div/ul/li[1]")
    submitButton = (By.XPATH, "//div[@class='flex justify-end gap-[16px]']/button")

    # Multimedia

    multiMediaTab = (By.XPATH,
                     "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden mb-[8px]']/button[4]")
    inputCheckBox = (By.XPATH,
                     "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div/div[1]/div/div/input")
    requestResubmission = (By.XPATH, "//div[@class='w-full flex flex-col ']/div[1]/button")
    Comment = (By.CSS_SELECTOR, "textarea[name='comment']")
    resubmissionButton = (By.XPATH, "//div[@class='flex flex-row items-center justify-center gap-[16px]']/button[1]")
    verificationText = (By.XPATH, "//div[@class='flex flex-row justify-between items-center']/div/div")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def test_your_rating(self):
        time.sleep(3)
        log.logger.info("!!! == Rate Interview BY Internal User (Your Rating)  == !!!")

        self.de_click(self.filterIcon)
        time.sleep(1)
        self.de_click(self.statusDD)
        time.sleep(1)
        self.de_click(self.notStartedYet)
        time.sleep(0.5)
        self.de_click(self.statusDD)
        time.sleep(0.5)
        self.de_click(self.applyButton)
        time.sleep(1)

        # Select Interview

        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)

        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))

        if int(totalNumberOfInterviews) > 0:
            self.de_click(self.firstApplicant)
            time.sleep(2)
            self.de_click(self.oneWayInterviewTab)
            time.sleep(2)
            self.de_click(self.videoButton)
            time.sleep(1)

            # Find Number Of Interviews And Rate The Same

            totalQuestions = len(self.driver.find_elements(By.XPATH,
                                                           "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[1]/div[2]/div/div[2]"))
            Questions = []
            Questions = self.driver.find_elements(By.XPATH,
                                                  "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[1]/div[2]/div/div[2]")

            for i in range(totalQuestions):
                elements = []
                elements = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[1]/div[2]/div/div[2]")
                elements[i].click()

                time.sleep(2)
                self.do_send_key(self.commentTextArea, "Good")
                time.sleep(1)
                self.de_click(self.rateIconYour)
                time.sleep(1)
                self.de_click(self.saveButton)
                log.logger.info("!!! == Interview Has been rated BY Internal User (Your Rating)  == !!!")
                time.sleep(4)

                log.logger.info("!!! == Rate Interview BY Team User (Team Rating)  == !!!")

                totalQuestions = len(self.driver.find_elements(By.XPATH,
                                                               "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[2]/div[2]/div/div[2]"))
                Questions = []
                Questions = self.driver.find_elements(By.XPATH,
                                                      "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[2]/div[2]/div/div[2]")

                for j in range(totalQuestions):
                    elements = []
                    elements = self.driver.find_elements(By.XPATH,
                                                         "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[2]/div[2]/div/div[2]")
                    elements[j].click()

                    time.sleep(2)
                    self.do_send_key(self.commentTextArea, "Good")
                    time.sleep(1)
                    self.de_click(self.rateIconTeam)
                    time.sleep(1)
                    self.de_click(self.saveButton)
                    log.logger.info("!!! == Interview Has been rated BY Internal User (Team Rating)  == !!!")
                    time.sleep(4)

        else:
            log.logger.info("Theres No Interview Available To Rate")

    def test_team_rating(self):
        # time.sleep(3)
        log.logger.info("!!! == Rate Interview BY Team User (Team Rating)  For iME Queue Interviews  == !!!")
        # self.de_click(self.filterIcon)
        # time.sleep(1)
        # self.de_click(self.statusDD)
        # time.sleep(1)
        # self.de_click(self.inProgressStatus)
        # time.sleep(0.5)
        # self.de_click(self.statusDD)
        # time.sleep(0.5)
        # self.de_click(self.applyButton)
        # time.sleep(1)
        #
        # # Select Interview
        #
        # self.de_click(self.firstApplicant)
        # time.sleep(2)
        # self.de_click(self.oneWayInterviewTab)
        # time.sleep(2)
        # self.de_click(self.videoButton)
        # time.sleep(1)

        # Find Number Of Interviews And Rate The Same

        # totalQuestions = len(self.driver.find_elements(By.XPATH,
        #                                                "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[2]/div[2]/div/div[2]"))
        # Questions = []
        # Questions = self.driver.find_elements(By.XPATH,
        #                                       "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[2]/div[2]/div/div[2]")
        #
        # for i in range(totalQuestions):
        #     elements = []
        #     elements = self.driver.find_elements(By.XPATH,
        #                                          "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[2]/div[2]/div/div[2]")
        #     elements[i].click()
        #
        #     time.sleep(2)
        #     self.do_send_key(self.commentTextArea, "Good")
        #     time.sleep(1)
        #     self.de_click(self.rateIconTeam)
        #     time.sleep(1)
        #     self.de_click(self.saveButton)
        #     log.logger.info("!!! == Interview Has been rated BY Internal User (Team Rating)  == !!!")
        #     time.sleep(4)

    def test_complete_rating(self):
        time.sleep(3)
        log.logger.info("!!! == Complete Interview Rating Process  For iME Queue Interviews  == !!!")
        self.de_click(self.filterIcon)
        time.sleep(1)
        self.de_click(self.clearAll)
        time.sleep(1)
        self.de_click(self.filterIcon)
        time.sleep(1)
        self.de_click(self.statusDD)
        time.sleep(1)
        self.de_click(self.inProgressStatus)
        time.sleep(0.5)
        self.de_click(self.statusDD)
        time.sleep(0.5)
        self.de_click(self.applyButton)
        time.sleep(1)

        # Select Interview
        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)

        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))

        if int(totalNumberOfInterviews) > 0:

            self.de_click(self.firstApplicant)
            time.sleep(1)
            self.de_click(self.completeButton)
            time.sleep(2)
            self.de_click(self.yesButton)
            time.sleep(5)
            try:
                oneWayInterviewTab = self.driver.find_element(By.XPATH,
                                                              "//div[@class='flex w-full justify-between h-[36px] mb-[12px]']/div/button[2]").is_displayed()
            except NoSuchElementException:
                log.logger.info("One Way Interview Tab Is Visible After Completing Rating Process")
            else:
                log.logger.info("One Way Interview Tab Is Visible After Completing Rating Process")
            finally:
                log.logger.info("One Way Interview Tab Is Not Visible After Completing Rating Process")

        else:
            log.logger.info("Theres No Interview Remains For Completion")

    # def test_assign_user_to_interview(self):
    #
    #     log.logger.info("!!! == Assign Internal Or External user To Interview == !!!")
    #     time.sleep(2)
    #     self.de_click(self.filterIcon)
    #     time.sleep(1)
    #     self.de_click(self.clearAll)
    #     time.sleep(1)
    #     self.de_click(self.filterIcon)
    #     time.sleep(1)
    #     self.de_click(self.statusDD)
    #     time.sleep(1)
    #     self.de_click(self.inProgressStatus)
    #     time.sleep(0.5)
    #     self.de_click(self.statusDD)
    #     time.sleep(0.5)
    #     self.de_click(self.applyButton)
    #     time.sleep(1)
    #
    #     # Select Interview
    #
    #     self.de_click(self.firstApplicant)
    #     time.sleep(1)
    #     self.de_click(self.oneWayInterviewTab)
    #     time.sleep(2)
    #     self.de_click(self.assignUser)
    #     time.sleep(2)
    #     self.de_click(self.selectUserDD)
    #     time.sleep(1)
    #     userEmail = self.get_element_text(self.optionOfSelectUserDD)
    #     time.sleep(0.5)
    #     self.de_click(self.optionOfSelectUserDD)
    #     time.sleep(1)
    #     self.de_click(self.assignButton)
    #     time.sleep(3.5)
    #     self.de_click(self.assignedUserTab)
    #     time.sleep(1)
    #     assignUserEmail = self.get_element_text(self.userDetail)
    #     time.sleep(0.5)
    #     assert userEmail == assignUserEmail
    #     log.logger.info("!!! == Internal Or External User Has Been Assigned To Interview == !!!")

    def test_update_status_of_interview(self):

        log.logger.info("!!! == Update Status Of Interview  Of  iME Queue  == !!!")
        time.sleep(2)
        self.de_click(self.filterIcon)
        time.sleep(1)
        self.de_click(self.clearAll)
        time.sleep(1)
        self.de_click(self.filterIcon)
        time.sleep(1)
        self.de_click(self.statusDD)
        time.sleep(1)
        self.de_click(self.inProgressStatus)
        time.sleep(0.5)
        self.de_click(self.statusDD)
        time.sleep(0.5)
        self.de_click(self.applyButton)
        time.sleep(1)

        # Select Interview

        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)

        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))

        if int(totalNumberOfInterviews) > 0:

            self.de_click(self.firstApplicant)
            time.sleep(3)
            self.de_click(self.oneWayInterviewTab)
            time.sleep(5)
            value = self.driver.find_element(By.XPATH,
                                             "//div[@class='grid grid-cols-5 sm:flex flex-wrap gap-x-[20px] gap-y-[16px] pb-[16px]']/button[2]/div").is_enabled()
            time.sleep(1)
            validation = str(value)
            log.logger.info("Status == " + validation)
            if validation == 'True':
                self.de_click(self.shortListed)
                time.sleep(1)
                self.de_click(self.emailCheckBox)
                time.sleep(1)
                self.de_click(self.selectEmailDD)
                time.sleep(0.5)
                self.de_click(self.optionOfSelectEmailDD)
                time.sleep(0.5)
                self.de_click(self.submitButton)
                time.sleep(7)
                log.logger.info("Status of interview Has Benn Updated to shortlisted")

            else:
                self.de_click(self.rejected)
                time.sleep(1)
                self.de_click(self.emailCheckBox)
                time.sleep(1)
                self.de_click(self.selectEmailDD)
                time.sleep(0.5)
                self.de_click(self.optionOfSelectEmailDD)
                time.sleep(0.5)
                self.de_click(self.submitButton)
                time.sleep(7)
                log.logger.info("Status of interview Has Benn Updated to rejected")

        else:
            log.logger.info("Theres No Interview Available For Status Updation")

    def test_multimedia_resubmission_feature(self):
        log.logger.info("!!! == Test Multimedia Resubmission For iME Queue Interviews  == !!!")
        time.sleep(2)
        self.de_click(self.filterIcon)
        time.sleep(1)
        self.de_click(self.clearAll)
        time.sleep(1)
        self.de_click(self.filterIcon)
        time.sleep(1)
        self.de_click(self.statusDD)
        time.sleep(1)
        self.de_click(self.inProgressStatus)
        time.sleep(0.5)
        self.de_click(self.statusDD)
        time.sleep(0.5)
        self.de_click(self.applyButton)
        time.sleep(1)

        # Select Interview

        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)

        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))

        if int(totalNumberOfInterviews) > 0:
            self.de_click(self.firstApplicant)
            time.sleep(2)
            self.de_click(self.oneWayInterviewTab)
            time.sleep(2)
            self.de_click(self.multiMediaTab)
            time.sleep(2)
            noMultiMediaSubmission = self.driver.find_element(By.XPATH,
                                                              "//div[@class='flex flex-col gap-[16px]']/div[2]/div[2]/div/div/div")
            Message = noMultiMediaSubmission.text
            if len(Message) > 0:
                log.logger.info("There's No Multimedia Document Available")
            else:
                try:
                    submissionMessage = self.driver.find_element(By.XPATH,
                                                                 "//div[@class='flex flex-row justify-center items-center rounded-[12px] bg-ime-red-500 bg-opacity-20 text-ime-red-700 w-[186px] h-6 text-[12px]']").is_displayed()
                    log.logger.info(
                        "!!! == Multimedia Resubmission Request Has Already Been Submitted == !!!")
                except Exception as e:
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
                    Message = self.get_element_text(self.verificationText)
                    assert Message == "Resubmission Requested"
                    log.logger.info(
                        "!!! == Multimedia Resubmission Request Submitted Successfully == !!!")
        else:
            log.logger.info("There's No Interview Available For Multimedia Resubmission ")
