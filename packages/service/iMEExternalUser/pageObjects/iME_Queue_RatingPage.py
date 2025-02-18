import time

from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
import logging
from iMEExternalUser.pageObjects.BasePage import BasePage
from iMEExternalUser.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class RatingPage(BasePage):
    imeQueueIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[1]/a")

    # Filter Button

    numberOfInterview = (By.XPATH,
                         "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[1]/div[1]/h6")

    filterIcon = (By.XPATH, "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[1]/div[2]/div[2]/button")

    statusDD = (By.XPATH,
                "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/button")

    notStartedStatus = (By.XPATH,
                        "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/ul/li[1]")
    inProgressStatus = (By.XPATH,
                        "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/ul/li[2]")

    clearAll = (By.XPATH,
                "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[1]/h2[2]")

    applyButton = (By.XPATH,
                   "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[5]/div/button")

    # Applicant Library

    firstApplicant = (By.XPATH, "//div[@class='hidden lg:flex w-full max-w-[328px]']/div/div[2]/div/div/div[1]")

    oneWayInterviewTab = (By.XPATH,
                          "//div[@class='text-base semibold h-[36px] bg-white dark:bg-ime-gray-900 flex justify-center items-center gap-[12px] sm:px-[5px] md:px-[12px] py-[8px] text-ime-gray-500 dark:text-ime-gray-400']")

    videoButton = (By.XPATH,
                   "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden mb-[8px]']/button[3]")

    numberOfInterviewQuestion = (By.XPATH, "//div[@id='headlessui-tabs-panel-:r49:']/div/div/div[2]/div")

    yourRatingStar = (
        By.XPATH, "//div[@id='headlessui-tabs-panel-:r49:']/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[5]")

    teamRatingStar = (
        By.XPATH, "//div[@id='headlessui-tabs-panel-:r49:']/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[5]")

    commentTextArea = (By.CSS_SELECTOR, "textarea[name='comment']")

    rateIconYour = (By.XPATH, "//div[@class='flex items-center justify-between']/div/div[2]/*[local-name()='svg']")

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
        "//div[@class='grid grid-cols-5 sm:flex flex-wrap gap-x-[20px] gap-y-[16px] pb-[16px]']/button[4]/div")

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
    emailCheckBox = (By.XPATH,
                     "//div[@class='flex flex-col w-full text-ime-gray-500 dark:text-ime-gray-400 text-[14px]']/div[2]/div/div/input")
    selectEmailDD = (By.XPATH, "//div[@class='flex flex-col space-y-2']/div/button")
    optionOfSelectEmailDD = (By.XPATH, "//div[@class='flex flex-col space-y-2']/div/ul/li[1]")
    submitButton = (By.XPATH, "//div[@class='flex justify-end gap-[16px]']/button")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def test_your_rating(self):
        time.sleep(5)

        log.logger.info("!!! == Rate Interview BY Internal User  == !!!")
        totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)

        log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))
        if int(totalNumberOfInterviews) > 0:
            # self.de_click(self.filterIcon)
            # time.sleep(1)
            # self.de_click(self.statusDD)
            # time.sleep(1)
            # self.de_click(self.inProgressStatus)
            # time.sleep(0.5)
            # self.de_click(self.statusDD)
            # time.sleep(0.5)
            # self.de_click(self.applyButton)
            # time.sleep(2)

            # totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)
            #
            # log.logger.info("Number Of Interviews After Applying Filtering Through In Progress Status == " + str(
            #     totalNumberOfInterviews))
            # if int(totalNumberOfInterviews) > 0:

            # Select Interview

            try:
                self.de_click(self.firstApplicant)
                time.sleep(5)

                try:
                    self.de_click(self.videoButton)
                except NoSuchElementException:
                    log.logger.error("Video button not found.")
                    # Handle the case where the video button is not found, e.g., exit or retry
                    raise
                except TimeoutException:
                    log.logger.error("Timed out while trying to click the video button.")
                    # Handle the timeout exception, e.g., retry or exit
                    raise
                except Exception as e:
                    log.logger.error(f"An unexpected error occurred: {e}")
                    # Handle any other unexpected exceptions
                    raise

                time.sleep(3)

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

                    time.sleep(3)
                    self.do_send_key(self.commentTextArea, "Good")
                    time.sleep(2)
                    self.de_click(self.rateIconYour)
                    time.sleep(2)
                    self.de_click(self.saveButton)
                    log.logger.info("!!! == External User has rated Interview (Your Rating) == !!!")
                    time.sleep(5)
            # else:
            #     log.logger.info("There's No Interview Available Under In Progress Status")

            except NoSuchElementException:
                log.logger.info("There's No Data Available")
            except Exception as e:
                log.logger.error(f"An unexpected error occurred: {e}")

    def test_team_rating(self):
        # time.sleep(3)
        log.logger.info("!!! == Rate Interview BY Team User  == !!!")
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

        try:
            totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)
            log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))

            if int(totalNumberOfInterviews) > 0:
                try:
                    # Fetch total number of questions
                    totalQuestions = len(self.driver.find_elements(By.XPATH,
                                                                   "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[2]/div[2]/div/div[2]"))
                    Questions = []
                    Questions = self.driver.find_elements(By.XPATH,
                                                          "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[2]/div[2]/div/div[2]")

                    for i in range(totalQuestions):
                        try:
                            elements = self.driver.find_elements(By.XPATH,
                                                                 "//div[@class='flex flex-col divide-y divide-ime-gray-200 dark:divide-ime-gray-700']/div/div[2]/div[2]/div[2]/div/div[2]")
                            elements[i].click()

                            time.sleep(3)
                            self.do_send_key(self.commentTextArea, "Good")
                            time.sleep(2)
                            self.de_click(self.rateIconTeam)
                            time.sleep(2)
                            self.de_click(self.saveButton)
                            log.logger.info("!!! == External User has rated Interview (Team Rating) == !!!")
                            time.sleep(5)
                        except NoSuchElementException:
                            log.logger.error(f"Element not found while processing question {i}.")
                        except StaleElementReferenceException:
                            log.logger.error(f"Stale element reference while processing question {i}.")
                        except TimeoutException:
                            log.logger.error(f"Timeout while interacting with question {i}.")
                        except Exception as e:
                            log.logger.error(f"An unexpected error occurred while processing question {i}: {e}")
                finally:
                    # Perform any necessary cleanup or final actions
                    # For example, close the browser or log final status
                    log.logger.info("Execution completed. Performing final cleanup.")
            else:
                log.logger.info("There's No Data Available")

        finally:
            # Perform any necessary cleanup or final actions
            # For example, close the browser or log final status
            log.logger.info("Execution completed. Performing final cleanup.")



    def test_complete_rating(self):
        time.sleep(4)
        log.logger.info("!!! == Complete Interview Rating Process  == !!!")
        try:
            totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)
            log.logger.info("Number Of Interviews == " + str(totalNumberOfInterviews))

            if int(totalNumberOfInterviews) > 0:
                try:
                    self.de_click(self.filterIcon)
                    time.sleep(2)
                    self.de_click(self.clearAll)
                    time.sleep(2)
                    self.de_click(self.filterIcon)
                    time.sleep(2)
                    self.de_click(self.statusDD)
                    time.sleep(2)
                    self.de_click(self.inProgressStatus)
                    time.sleep(1.5)
                    self.de_click(self.statusDD)
                    time.sleep(1.5)
                    self.de_click(self.applyButton)
                    time.sleep(1.5)

                    totalNumberOfInterviews = self.get_element_text(self.numberOfInterview)
                    log.logger.info(
                        "Number Of Interviews After Applying Filtering Through In Progress Status == " + str(
                            totalNumberOfInterviews))

                    if int(totalNumberOfInterviews) > 0:
                        try:
                            self.de_click(self.firstApplicant)
                            time.sleep(2)
                            self.de_click(self.completeButton)
                            time.sleep(3)
                            self.de_click(self.yesButton)
                            time.sleep(5)

                            try:
                                oneWayInterviewTab = self.driver.find_element(By.XPATH,
                                                                              "//div[@class='flex w-full justify-between h-[36px] mb-[12px]']/div/button[2]").is_displayed()
                                log.logger.info("One Way Interview Tab Is Visible After Completing Rating Process")
                            except NoSuchElementException:
                                log.logger.info("One Way Interview Tab Is Not Visible After Completing Rating Process")
                        except NoSuchElementException as e:
                            log.logger.error(f"Element not found during interview processing: {e}")
                        except TimeoutException as e:
                            log.logger.error(f"Timeout occurred during interview processing: {e}")
                        except Exception as e:
                            log.logger.error(f"An unexpected error occurred during interview processing: {e}")

                    else:
                        log.logger.info("There's No Interview Available Under In Progress Status")

                except NoSuchElementException as e:
                    log.logger.error(f"Element not found during filtering process: {e}")
                except TimeoutException as e:
                    log.logger.error(f"Timeout occurred during filtering process: {e}")
                except Exception as e:
                    log.logger.error(f"An unexpected error occurred during filtering process: {e}")

            else:
                log.logger.info("There's No Data Available")

        finally:
            # Perform any necessary final actions or cleanup
            log.logger.info("Execution completed. Performing final cleanup.")
            try:
                # Example cleanup action
                # self.driver.quit()  # Uncomment if you need to close the browser at the end of the script
                pass
            except Exception as e:
                log.logger.error(f"An error occurred during final cleanup: {e}")
    #
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
    #     time.sleep(3)
    #     self.de_click(self.assignedUserTab)
    #     time.sleep(1)
    #     assignUserEmail = self.get_element_text(self.userDetail)
    #     time.sleep(0.5)
    #     assert userEmail == assignUserEmail
    #     log.logger.info("!!! == Internal Or External User Has Been Assigned To Interview == !!!")
    #
    # def test_update_status_of_interview(self):
    #
    #     log.logger.info("!!! == Update Status Of Interview == !!!")
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
    #     value = self.driver.find_element(By.XPATH,
    #                                      "//div[@class='grid grid-cols-5 sm:flex flex-wrap gap-x-[20px] gap-y-[16px] pb-[16px]']/button[2]").is_enabled()
    #     time.sleep(0.5)
    #     validation = str(value)
    #     log.logger.info("Status == " + validation)
    #     if validation == 'True':
    #         self.de_click(self.shortListed)
    #         time.sleep(1)
    #         self.de_click(self.emailCheckBox)
    #         time.sleep(1)
    #         self.de_click(self.selectEmailDD)
    #         time.sleep(0.5)
    #         self.de_click(self.optionOfSelectEmailDD)
    #         time.sleep(0.5)
    #         self.de_click(self.submitButton)
    #         time.sleep(5)
    #         log.logger.info("Status Has Benn Updated")
    #
    #     else:
    #         log.logger.info("Status Update Button Is Disable")
