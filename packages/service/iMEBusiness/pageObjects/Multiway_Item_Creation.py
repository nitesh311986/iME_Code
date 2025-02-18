import os
import time
from datetime import datetime, timedelta
import logging

import pytz
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from iMEBusiness.Utilities.excelReader import excel_Data
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Multiway_Item_Creation(BasePage):
    multiWayInterviewIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[4]")
    videoCallsIcon = (By.XPATH,
                      "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[2]")

    setUpInterviewIcon = (
        By.XPATH, "//div[@class='flex flex-col lg:flex-row justify-between pt-5 pb-8 items-center']/div[2]/button")
    videoTitle = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[1]/div[1]/input")
    visibilityDD = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[1]/button")
    publicOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[1]/ul/li[1]")
    privateOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[1]/ul/li[2]")
    hiddenOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[1]/ul/li[3]")
    serviceDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[2]/button")
    recruitmentOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[1]")
    awardOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[2]")
    marketingOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[3]")
    learningOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[4]")
    auditionOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[5]")
    admissionOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[6]")
    queryMail = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[3]/div/input")
    descriptionOfVideo = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[4]/div/textarea")
    startVideo = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[5]/div/div/input")
    nextButton = (By.XPATH, "//div[@class='flex justify-between items-center gap-4']/div/button")
    userInput = (By.XPATH, "//div[@id='search']/input")

    applicantName = (By.CSS_SELECTOR, "input[name='participantUserFirstName']")
    applicantLastName = (By.CSS_SELECTOR, "input[name='participantUserLastName']")
    applicantCountryCode = (By.XPATH,
                            "//div[@class='absolute z-10 mt-2 w-56 top-14 origin-top-right rounded-md shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none overflow-y-auto -webkit-overflow-scrolling: touch h-96 bg-white dark:bg-gray-800 border mt-4 dark:!border-ime-gray-600 !border-ime-gray-300 dark:bg-ime-gray-800 transform opacity-100 scale-100']/div[1]")
    applicantContactNumber = (By.CSS_SELECTOR, "input[name='participantContactNumber']")
    applicantEmail = (By.CSS_SELECTOR, "input[name='participantUserEmail']")
    addApplicantButton = (
        By.XPATH, "//div[@class='col-span-5 lg:col-span-2 lg:px-4 order-1 lg:order-2 mb-4']/form/button")
    nextButtonThree = (By.XPATH, "//div[@class='flex justify-between items-center gap-4']/div/button[2]")
    joinMeeting = (By.XPATH, "//button[@class='sc-gEvEer kxHJeQ']")
    startTime = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[6]/div[2]/div/input")

    # Webinar
    webinarIcon = (By.XPATH,
                   "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[3]")
    deadlineOfWebinar = (By.XPATH, "//div[@class='col-span-3 hidden lg:block']/div/div[7]/div[2]/div/div[1]/input")
    paymentDD = (By.XPATH, "//div[@class='col-span-3 hidden lg:block']/div/div[8]/div/button")
    noneOption = (By.XPATH, "//div[@class='col-span-3 hidden lg:block']/div/div[8]/div/ul/li[1]")
    paynowOption = (By.XPATH, "//div[@class='col-span-3 hidden lg:block']/div/div[8]/div/ul/li[2]")
    amountDD = (By.XPATH, "//div[@class='col-span-3 hidden lg:block']/div/div[8]/div[2]/div[1]/div/button")
    gbpOption = (By.XPATH, "://div[@class='col-span-3 hidden lg:block']/div/div[8]/div[2]/div[1]/div/div[1]")
    zarOption = (By.XPATH, "://div[@class='col-span-3 hidden lg:block']/div/div[8]/div[2]/div[1]/div/div[2]")
    usdOption = (By.XPATH, "://div[@class='col-span-3 hidden lg:block']/div/div[8]/div[2]/div[1]/div/div[3]")
    eurOption = (By.XPATH, "://div[@class='col-span-3 hidden lg:block']/div/div[8]/div[2]/div[1]/div/div[4]")
    amountInput = (By.XPATH, "//div[@class='col-span-3 hidden lg:block']/div/div[8]/div[2]/div[2]/input")
    startTimeWebinar = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[6]/div[2]/div/input")

    def __init__(self, driver, environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_interview_icon(self):
        time.sleep(3)
        self.de_click(self.multiWayInterviewIcon)
        time.sleep(5)

    def create_multiway_video_call(self):
        # log.logger.info("Create Multiway Video Call Test Case Starts Here")
        self.de_click(self.videoCallsIcon)
        time.sleep(4)
        self.de_click(self.setUpInterviewIcon)
        time.sleep(3)
        # self.de_click(self.setUpInterviewIcon)
        # time.sleep(2)
        # base_dir = os.path.dirname(__file__)
        #
        # # Define the relative path to the Pricing.xlsx file
        # relative_path = os.path.join(base_dir, '../excel/create_video_call.xlsx')
        # sheetName = 'video_call'
        #
        # # Get the absolute path
        # path = os.path.abspath(relative_path)
        # print("Absolute path:", path)
        #
        # # Check if the file exists
        # if os.path.exists(path):
        #     print("File found!")
        #     # Proceed with file operations
        # else:
        #     raise FileNotFoundError(f"File not found: {path}")
        #
        # row = excel_Data.getRowCount(path, sheetName)
        # log.logger.info("" + str(row))
        # col = excel_Data.getColCount(path, sheetName)
        # log.logger.info("" + str(col))
        #
        # for j in range(2, 3):
        #     for k in range(1, 2):
        #         title = excel_Data.getCellData(path, sheetName, j, 1)
        #         visibility = excel_Data.getCellData(path, sheetName, j, 2)
        #         service = excel_Data.getCellData(path, sheetName, j, 3)
        #         qmail = excel_Data.getCellData(path, sheetName, j, 4)
        #         description = excel_Data.getCellData(path, sheetName, j, 5)
        #         firstName = excel_Data.getCellData(path, sheetName, j, 6)
        #         lastName = excel_Data.getCellData(path, sheetName, j, 7)
        #         Contact = excel_Data.getCellData(path, sheetName, j, 8)
        #         Email = excel_Data.getCellData(path, sheetName, j, 9)
        #         log.logger.info("User Has Entered Digital Item Title ==> " + title)
        #         log.logger.info("User Has Entered Item Visibility ==> " + visibility)
        #         log.logger.info("User Has Entered Item Service Type ==> " + service)
        #         log.logger.info("User Has Entered Item Desc ==> " + description)
        #         log.logger.info("User Has Entered Query Mail  ==> " + qmail)
        #         log.logger.info("User Has Entered User FName ==> " + firstName)
        #         log.logger.info("User Has Entered User LName ==> " + lastName)
        #         # log.logger.info("User Has Entered User Contact ==> " + Contact)
        #         log.logger.info("User Has Entered User Email ==> " + Email)
        #         time.sleep(1)
        #         dateTime = self.get_date_time_using_time_zone()
        #         time.sleep(1)
        #         self.do_send_key(self.videoTitle,title+dateTime)
        #         time.sleep(1)
        #         self.de_click(self.visibilityDD)
        #         time.sleep(0.5)
        #         if visibility == "Public":
        #             self.de_click(self.publicOption)
        #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
        #         elif visibility == "Private":
        #             self.de_click(self.privateOption)
        #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
        #         elif visibility == "Hidden":
        #             self.de_click(self.hiddenOption)
        #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
        #         else:
        #             self.de_click(self.publicOption)
        #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
        #         time.sleep(0.5)
        #         self.de_click(self.serviceDD)
        #         time.sleep(1)
        #         if service == "Recruitment":
        #             self.de_click(self.recruitmentOption)
        #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
        #         elif service == "Awards":
        #             self.de_click(self.awardOption)
        #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
        #         elif service == "Marketing":
        #             self.de_click(self.marketingOption)
        #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
        #         elif service == "Learning":
        #             self.de_click(self.learningOption)
        #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
        #         elif service == "Auditions":
        #             self.de_click(self.auditionOption)
        #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
        #         elif service == "Admissions":
        #             self.de_click(self.admissionOption)
        #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
        #         else:
        #             self.de_click(self.recruitmentOption)
        #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
        #         time.sleep(1)
        #         self.do_send_key(self.queryMail,qmail)
        #         time.sleep(1)
        #         self.do_send_key(self.descriptionOfVideo, description)
        #         time.sleep(1)
        #         startV = self.driver.find_element(By.XPATH,
        #                                           "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[5]/div/div/input")
        #         self.de_scroll_into_view(startV)
        #         time.sleep(0.5)
        #         self.do_clear_using_java_script(self.startTime)
        #         time.sleep(0.5)
        #         self.do_send_key(self.startTime,"12:58")
        #         # self.de_click(self.startVideo)
        #         # time.sleep(1)
        #         self.de_click(self.nextButton)
        #         time.sleep(3)
        #         self.de_click(self.nextButtonThree)
        #         time.sleep(3)
        #         self.do_send_key(self.applicantName,firstName)
        #         time.sleep(1)
        #         self.do_send_key(self.applicantLastName,lastName)
        #         time.sleep(1)
        #         country_code = self.driver.find_element(By.XPATH,
        #                                                  "//div[@class='col-span-5 lg:col-span-2 lg:px-4 order-1 lg:order-2 mb-4']/form/div[3]/div[1]/div/button")
        #         # select = Select(currency_code)
        #         country_code.click()
        #         time.sleep(1)
        #         self.de_click(self.applicantCountryCode)
        #         time.sleep(1)
        #         self.do_send_key(self.applicantContactNumber,"2324252789")
        #         time.sleep(1)
        #         self.do_send_key(self.applicantEmail,Email)
        #         time.sleep(1)
        #         self.de_click(self.nextButtonThree)
        #         time.sleep(2)
        #         original_window = self.driver.current_window_handle#
        #         # # Check we don't have other windows open already
        #         assert len(self.driver.window_handles) == 1
        #         # Click the link which opens in a new window
        #         self.de_click(self.nextButtonThree)
        #         # Wait for the new window or tab
        #         WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        #
        #         # Loop through until we find a new window handle
        #         for window_handle in self.driver.window_handles:
        #             if window_handle != original_window:
        #                 self.driver.switch_to.window(window_handle)
        #                 break
        #
        #                 # Wait for the new tab to finish loading content
        #         time.sleep(7)
        #         self.de_scroll_by_pixels()
        #         time.sleep(3)
        #         self.de_click(self.joinMeeting)
        #         time.sleep(3)
        #         url = self.driver.current_url
        #         log.logger.info("Url Of Meet Page === " +str(url))
        #         self.driver.close()
        #         time.sleep(1)
        #         self.driver.switch_to.window(original_window)
        #         time.sleep(5)
        #         break

        # List of target time zones
        time_zones = [
            "Europe/London",  # UK
            "America/New_York",  # US (Eastern Time)
            "Australia/Sydney",  # Australia
            "Asia/Dubai",  # Dubai
            "Africa/Johannesburg",  # South Africa
            "Africa/Lagos"  # Nigeria (West Africa Time)
        ]

        # Logger info
        log.logger.info("Create Multiway Video Call Test Case Starts Here")

        # Time zone processing and looping
        for time_zone in time_zones:
            log.logger.info(f"Processing for time zone: {time_zone}")

            # Get the current time in UTC and convert to the target time zone
            utc_now = datetime.now(pytz.utc)
            target_time = utc_now.astimezone(pytz.timezone(time_zone)) + timedelta(hours=2)
            formatted_time = target_time.strftime("%H:%M")  # Format to HH:MM for input

            log.logger.info(f"Calculated start time for {time_zone}: {formatted_time}")

            # Begin the video call creation process

            time.sleep(2)

            # Excel file handling
            base_dir = os.path.dirname(__file__)
            relative_path = os.path.join(base_dir, '../excel/create_video_call.xlsx')
            path = os.path.abspath(relative_path)
            if not os.path.exists(path):
                raise FileNotFoundError(f"File not found: {path}")

            sheetName = 'video_call'
            row = excel_Data.getRowCount(path, sheetName)
            log.logger.info("" + str(row))
            col = excel_Data.getColCount(path, sheetName)
            log.logger.info("" + str(col))

            for j in range(2, 3):
                title = excel_Data.getCellData(path, sheetName, j, 1)
                visibility = excel_Data.getCellData(path, sheetName, j, 2)
                service = excel_Data.getCellData(path, sheetName, j, 3)
                qmail = excel_Data.getCellData(path, sheetName, j, 4)
                description = excel_Data.getCellData(path, sheetName, j, 5)
                firstName = excel_Data.getCellData(path, sheetName, j, 6)
                lastName = excel_Data.getCellData(path, sheetName, j, 7)
                Email = excel_Data.getCellData(path, sheetName, j, 9)

                # Enter data into form
                dateTime = self.get_date_time_using_time_zone()
                time.sleep(1)
                self.do_send_key(self.videoTitle, title + dateTime)
                time.sleep(1)
                self.de_click(self.visibilityDD)
                time.sleep(0.5)
                if visibility == "Public":
                    self.de_click(self.publicOption)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                elif visibility == "Private":
                    self.de_click(self.privateOption)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                elif visibility == "Hidden":
                    self.de_click(self.hiddenOption)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                else:
                    self.de_click(self.publicOption)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                time.sleep(0.5)
                self.de_click(self.serviceDD)
                time.sleep(1)
                if service == "Recruitment":
                    self.de_click(self.recruitmentOption)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                elif service == "Awards":
                    self.de_click(self.awardOption)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                elif service == "Marketing":
                    self.de_click(self.marketingOption)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                elif service == "Learning":
                    self.de_click(self.learningOption)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                elif service == "Auditions":
                    self.de_click(self.auditionOption)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                elif service == "Admissions":
                    self.de_click(self.admissionOption)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                else:
                    self.de_click(self.recruitmentOption)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                time.sleep(1)
                self.do_send_key(self.queryMail, qmail)
                time.sleep(1)
                self.do_send_key(self.descriptionOfVideo, description)
                time.sleep(1)
                startV = self.driver.find_element(By.XPATH,
                                                  "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[5]/div/div/input")
                self.de_scroll_into_view(startV)
                time.sleep(0.5)
                self.do_clear_using_java_script(self.startTime)
                time.sleep(1)
                self.do_send_key(self.startTime, formatted_time)
                time.sleep(1)

                self.de_click(self.nextButton)
                time.sleep(3)
                self.de_click(self.nextButtonThree)
                time.sleep(3)
                self.do_send_key(self.applicantName, firstName)
                time.sleep(1)
                self.do_send_key(self.applicantLastName, lastName)
                time.sleep(1)
                country_code = self.driver.find_element(By.XPATH,
                                                        "//div[@class='col-span-5 lg:col-span-2 lg:px-4 order-1 lg:order-2 mb-4']/form/div[3]/div[1]/div/button")
                # select = Select(currency_code)
                country_code.click()
                time.sleep(1)
                self.de_click(self.applicantCountryCode)
                time.sleep(1)
                self.do_send_key(self.applicantContactNumber, "2324252789")
                time.sleep(1)
                self.do_send_key(self.applicantEmail, Email)
                time.sleep(1)
                self.de_click(self.nextButtonThree)
                time.sleep(2)
                self.de_click(self.nextButtonThree)
                time.sleep(6)

            self.de_click(self.setUpInterviewIcon)
            time.sleep(4)

    def create_multiway_webinar(self):

        log.logger.info("Create Multiway Webinar Test Case Starts Here")
        self.de_click(self.webinarIcon)
        time.sleep(4)
        self.de_click(self.setUpInterviewIcon)
        time.sleep(3)
        time_zones = [
            "Europe/London",  # UK
            "America/New_York",  # US (Eastern Time)
            "Australia/Sydney",  # Australia
            "Asia/Dubai",  # Dubai
            "Africa/Johannesburg",  # South Africa
            "Africa/Lagos"  # Nigeria (West Africa Time)
        ]

        # Logger info
        log.logger.info("Create Multiway Video Call Test Case Starts Here")

        # Time zone processing and looping
        for time_zone in time_zones:
            log.logger.info(f"Processing for time zone: {time_zone}")

            # Get the current time in UTC and convert to the target time zone
            utc_now = datetime.now(pytz.utc)
            target_time = utc_now.astimezone(pytz.timezone(time_zone)) + timedelta(hours=2)
            formatted_time = target_time.strftime("%H:%M")  # Format to HH:MM for input

            log.logger.info(f"Calculated start time for {time_zone}: {formatted_time}")

            # Begin the video call creation process

            time.sleep(2)
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/create_webinar.xlsx')
            sheetName = 'webinar_call'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
            # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

            row = excel_Data.getRowCount(path, sheetName)
            log.logger.info("" + str(row))
            col = excel_Data.getColCount(path, sheetName)
            log.logger.info("" + str(col))

            for j in range(2, 3):
                for k in range(1, 2):
                    title = excel_Data.getCellData(path, sheetName, j, 1)
                    visibility = excel_Data.getCellData(path, sheetName, j, 2)
                    service = excel_Data.getCellData(path, sheetName, j, 3)
                    qmail = excel_Data.getCellData(path, sheetName, j, 4)
                    description = excel_Data.getCellData(path, sheetName, j, 5)
                    pType = excel_Data.getCellData(path, sheetName, j, 6)
                    cType = excel_Data.getCellData(path, sheetName, j, 7)
                    amount = excel_Data.getCellData(path, sheetName, j, 8)
                    firstName = excel_Data.getCellData(path, sheetName, j, 9)
                    lastName = excel_Data.getCellData(path, sheetName, j, 10)
                    Contact = excel_Data.getCellData(path, sheetName, j, 11)
                    Email = excel_Data.getCellData(path, sheetName, j, 12)
                    log.logger.info("User Has Entered Digital Item Title ==> " + title)
                    log.logger.info("User Has Entered Item Visibility ==> " + visibility)
                    log.logger.info("User Has Entered Item Service Type ==> " + service)
                    log.logger.info("User Has Entered Item Desc ==> " + description)
                    log.logger.info("User Has Entered Query Mail  ==> " + qmail)
                    log.logger.info("User Has Entered Pyment Type Is ==> " + pType)
                    log.logger.info("User Has Entered Currency Type Is ==> " + pType)
                    # log.logger.info("User Has Entered Amount To Pay  ==> " + amount)
                    log.logger.info("User Has Entered User FName ==> " + firstName)
                    log.logger.info("User Has Entered User LName ==> " + lastName)
                    # log.logger.info("User Has Entered User Contact ==> " + Contact)
                    log.logger.info("User Has Entered User Email ==> " + Email)
                    time.sleep(1)
                    dateTime = self.get_date_time_using_time_zone()
                    time.sleep(1)
                    self.do_send_key(self.videoTitle, title + dateTime)
                    time.sleep(1)
                    self.de_click(self.visibilityDD)
                    time.sleep(0.5)
                    if visibility == "Public":
                        self.de_click(self.publicOption)
                        log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                    elif visibility == "Private":
                        self.de_click(self.privateOption)
                        log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                    elif visibility == "Hidden":
                        self.de_click(self.hiddenOption)
                        log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                    else:
                        self.de_click(self.publicOption)
                        log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                    time.sleep(0.5)
                    self.de_click(self.serviceDD)
                    time.sleep(1)
                    if service == "Recruitment":
                        self.de_click(self.recruitmentOption)
                        log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                    elif service == "Awards":
                        self.de_click(self.awardOption)
                        log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                    elif service == "Marketing":
                        self.de_click(self.marketingOption)
                        log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                    elif service == "Learning":
                        self.de_click(self.learningOption)
                        log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                    elif service == "Auditions":
                        self.de_click(self.auditionOption)
                        log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                    elif service == "Admissions":
                        self.de_click(self.admissionOption)
                        log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                    else:
                        self.de_click(self.recruitmentOption)
                        log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                    time.sleep(1)
                    self.do_send_key(self.queryMail, qmail)
                    time.sleep(1)
                    self.do_send_key(self.descriptionOfVideo, description)
                    time.sleep(1)
                    startV = self.driver.find_element(By.XPATH,
                                                      "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[5]/div/div/input")
                    self.de_scroll_into_view(startV)
                    time.sleep(0.5)
                    self.do_clear_using_java_script(self.startTimeWebinar)
                    time.sleep(1)
                    self.do_send_key(self.startTimeWebinar, formatted_time)
                    time.sleep(1)
                    # self.de_click(self.startVideo)
                    # time.sleep(1)
                    deadlineV = self.driver.find_element(By.XPATH,
                                                         "//div[@class='col-span-3 hidden lg:block']/div/div[7]/div[2]/div/div[1]/input")
                    self.de_scroll_into_view(deadlineV)
                    time.sleep(0.5)
                    self.de_click(self.deadlineOfWebinar)
                    time.sleep(0.5)
                    self.de_click(self.paymentDD)
                    time.sleep(1)
                    if pType == "None":
                        self.de_click(self.noneOption)
                        log.logger.info("User Has Selected Payment Type of webinar ==> " + pType)
                    elif pType == "Pay Now":
                        self.de_click(self.paynowOption)
                        log.logger.info("User Has Selected Payment Type of webinar ==> " + pType)
                        time.sleep(1)
                        self.de_click(self.amountDD)
                        time.sleep(1)
                        if cType == "GBP":
                            self.de_click(self.gbpOption)
                            log.logger.info("User Has Selected Currency Type ==> " + cType)
                        elif service == "Awards":
                            self.de_click(self.zarOption)
                            log.logger.info("User Has Selected Currency Type ==> " + cType)
                        elif service == "Marketing":
                            self.de_click(self.usdOption)
                            log.logger.info("User Has Selected Currency Type ==> " + cType)
                        elif service == "Learning":
                            self.de_click(self.eurOption)
                            log.logger.info("User Has Selected Currency Type ==> " + cType)
                        elif service == "Auditions":
                            self.de_click(self.gbpOption)
                            log.logger.info("User Has Selected Currency Type ==> " + cType)
                        time.sleep(1)
                    else:
                        self.de_click(self.noneOption)
                        log.logger.info("User Has Selected Payment Type of webinar ==> " + pType)

                    self.de_click(self.nextButton)
                    time.sleep(3)
                    self.de_click(self.nextButtonThree)
                    time.sleep(3)
                    self.do_send_key(self.applicantName, firstName)
                    time.sleep(1)
                    self.do_send_key(self.applicantLastName, lastName)
                    time.sleep(1)
                    country_code = self.driver.find_element(By.XPATH,
                                                            "//div[@class='col-span-5 lg:col-span-2 px-4']/form/div[3]/div[1]/div/button")
                    # select = Select(currency_code)
                    country_code.click()
                    time.sleep(1)
                    self.de_click(self.applicantCountryCode)
                    time.sleep(1)
                    self.do_send_key(self.applicantContactNumber, "2324252789")
                    time.sleep(1)
                    self.do_send_key(self.applicantEmail, Email)
                    time.sleep(1)
                    self.de_click(self.nextButtonThree)
                    time.sleep(3)
                    self.de_click(self.nextButtonThree)
                    time.sleep(7)

            self.de_click(self.setUpInterviewIcon)
            time.sleep(3)

            # log.logger.info("Create Multiway Webinar Test Case Starts Here")
            # self.de_click(self.webinarIcon)
            # time.sleep(4)
            # self.de_click(self.setUpInterviewIcon)
            # time.sleep(2)
            # base_dir = os.path.dirname(__file__)
            #
            # # Define the relative path to the Pricing.xlsx file
            # relative_path = os.path.join(base_dir, '../excel/create_webinar.xlsx')
            # sheetName = 'webinar_call'
            #
            # # Get the absolute path
            # path = os.path.abspath(relative_path)
            # print("Absolute path:", path)
            #
            # # Check if the file exists
            # if os.path.exists(path):
            #     print("File found!")
            #     # Proceed with file operations
            # else:
            #     raise FileNotFoundError(f"File not found: {path}")
            #
            # row = excel_Data.getRowCount(path, sheetName)
            # log.logger.info("" + str(row))
            # col = excel_Data.getColCount(path, sheetName)
            # log.logger.info("" + str(col))
            #
            # for j in range(2, 3):
            #     for k in range(1, 2):
            #         title = excel_Data.getCellData(path, sheetName, j, 1)
            #         visibility = excel_Data.getCellData(path, sheetName, j, 2)
            #         service = excel_Data.getCellData(path, sheetName, j, 3)
            #         qmail = excel_Data.getCellData(path, sheetName, j, 4)
            #         description = excel_Data.getCellData(path, sheetName, j, 5)
            #         pType = excel_Data.getCellData(path, sheetName, j, 6)
            #         cType = excel_Data.getCellData(path, sheetName, j, 7)
            #         amount = excel_Data.getCellData(path, sheetName, j, 8)
            #         firstName = excel_Data.getCellData(path, sheetName, j, 9)
            #         lastName = excel_Data.getCellData(path, sheetName, j, 10)
            #         Contact = excel_Data.getCellData(path, sheetName, j, 11)
            #         Email = excel_Data.getCellData(path, sheetName, j, 12)
            #         log.logger.info("User Has Entered Digital Item Title ==> " + title)
            #         log.logger.info("User Has Entered Item Visibility ==> " + visibility)
            #         log.logger.info("User Has Entered Item Service Type ==> " + service)
            #         log.logger.info("User Has Entered Item Desc ==> " + description)
            #         log.logger.info("User Has Entered Query Mail  ==> " + qmail)
            #         log.logger.info("User Has Entered Pyment Type Is ==> " + pType)
            #         log.logger.info("User Has Entered Currency Type Is ==> " + pType)
            #         # log.logger.info("User Has Entered Amount To Pay  ==> " + amount)
            #         log.logger.info("User Has Entered User FName ==> " + firstName)
            #         log.logger.info("User Has Entered User LName ==> " + lastName)
            #         # log.logger.info("User Has Entered User Contact ==> " + Contact)
            #         log.logger.info("User Has Entered User Email ==> " + Email)
            #         time.sleep(1)
            #         dateTime = self.get_date_time_using_time_zone()
            #         time.sleep(1)
            #         self.do_send_key(self.videoTitle,title+dateTime)
            #         time.sleep(1)
            #         self.de_click(self.visibilityDD)
            #         time.sleep(0.5)
            #         if visibility == "Public":
            #             self.de_click(self.publicOption)
            #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
            #         elif visibility == "Private":
            #             self.de_click(self.privateOption)
            #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
            #         elif visibility == "Hidden":
            #             self.de_click(self.hiddenOption)
            #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
            #         else:
            #             self.de_click(self.publicOption)
            #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
            #         time.sleep(0.5)
            #         self.de_click(self.serviceDD)
            #         time.sleep(1)
            #         if service == "Recruitment":
            #             self.de_click(self.recruitmentOption)
            #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
            #         elif service == "Awards":
            #             self.de_click(self.awardOption)
            #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
            #         elif service == "Marketing":
            #             self.de_click(self.marketingOption)
            #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
            #         elif service == "Learning":
            #             self.de_click(self.learningOption)
            #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
            #         elif service == "Auditions":
            #             self.de_click(self.auditionOption)
            #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
            #         elif service == "Admissions":
            #             self.de_click(self.admissionOption)
            #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
            #         else:
            #             self.de_click(self.recruitmentOption)
            #             log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
            #         time.sleep(1)
            #         self.do_send_key(self.queryMail,qmail)
            #         time.sleep(1)
            #         self.do_send_key(self.descriptionOfVideo, description)
            #         time.sleep(1)
            #         startV = self.driver.find_element(By.XPATH,
            #                                           "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[5]/div/div/input")
            #         self.de_scroll_into_view(startV)
            #         time.sleep(0.5)
            #         self.do_clear_using_java_script(self.startTimeWebinar)
            #         time.sleep(1)
            #         self.do_send_key(self.startTimeWebinar,"11:30")
            #         time.sleep(1)
            #         # self.de_click(self.startVideo)
            #         # time.sleep(1)
            #         deadlineV = self.driver.find_element(By.XPATH,
            #                                           "//div[@class='col-span-3 hidden lg:block']/div/div[7]/div[2]/div/div[1]/input")
            #         self.de_scroll_into_view(deadlineV)
            #         time.sleep(0.5)
            #         self.de_click(self.deadlineOfWebinar)
            #         time.sleep(0.5)
            #         self.de_click(self.paymentDD)
            #         time.sleep(1)
            #         if pType == "None":
            #             self.de_click(self.noneOption)
            #             log.logger.info("User Has Selected Payment Type of webinar ==> " + pType)
            #         elif pType == "Pay Now":
            #             self.de_click(self.paynowOption)
            #             log.logger.info("User Has Selected Payment Type of webinar ==> " + pType)
            #             time.sleep(1)
            #             self.de_click(self.amountDD)
            #             time.sleep(1)
            #             if cType == "GBP":
            #                 self.de_click(self.gbpOption)
            #                 log.logger.info("User Has Selected Currency Type ==> " + cType)
            #             elif service == "Awards":
            #                 self.de_click(self.zarOption)
            #                 log.logger.info("User Has Selected Currency Type ==> " + cType)
            #             elif service == "Marketing":
            #                 self.de_click(self.usdOption)
            #                 log.logger.info("User Has Selected Currency Type ==> " + cType)
            #             elif service == "Learning":
            #                 self.de_click(self.eurOption)
            #                 log.logger.info("User Has Selected Currency Type ==> " + cType)
            #             elif service == "Auditions":
            #                 self.de_click(self.gbpOption)
            #                 log.logger.info("User Has Selected Currency Type ==> " + cType)
            #             time.sleep(1)
            #         else:
            #             self.de_click(self.noneOption)
            #             log.logger.info("User Has Selected Payment Type of webinar ==> " + pType)
            #
            #         self.de_click(self.nextButton)
            #         time.sleep(3)
            #         self.de_click(self.nextButtonThree)
            #         time.sleep(3)
            #         self.do_send_key(self.applicantName,firstName)
            #         time.sleep(1)
            #         self.do_send_key(self.applicantLastName,lastName)
            #         time.sleep(1)
            #         country_code = self.driver.find_element(By.XPATH,
            #                                                  "//div[@class='col-span-5 lg:col-span-2 px-4']/form/div[3]/div[1]/div/button")
            #         # select = Select(currency_code)
            #         country_code.click()
            #         time.sleep(1)
            #         self.de_click(self.applicantCountryCode)
            #         time.sleep(1)
            #         self.do_send_key(self.applicantContactNumber,"2324252789")
            #         time.sleep(1)
            #         self.do_send_key(self.applicantEmail,Email)
            #         time.sleep(1)
            #         self.de_click(self.nextButtonThree)
            #         time.sleep(2)
            #         self.de_click(self.nextButtonThree)

            # original_window = self.driver.current_window_handle  #
            # # # Check we don't have other windows open already
            # assert len(self.driver.window_handles) == 1
            # # Click the link which opens in a new window
            # self.de_click(self.nextButtonThree)
            # # Wait for the new window or tab
            # WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
            #
            # # Loop through until we find a new window handle
            # for window_handle in self.driver.window_handles:
            #     if window_handle != original_window:
            #         self.driver.switch_to.window(window_handle)
            #         break
            #
            #         # Wait for the new tab to finish loading content
            # time.sleep(7)
            # self.de_scroll_by_pixels()
            # time.sleep(3)
            # self.de_click(self.joinMeeting)
            # time.sleep(3)
            # url = self.driver.current_url
            # log.logger.info("Url Of Meet Page === " + str(url))
            # self.driver.close()
            # time.sleep(1)
            # self.driver.switch_to.window(original_window)
            # time.sleep(5)
            # break
