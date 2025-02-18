import os
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEBusiness.Utilities.excelReader import excel_Data
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Create_Live_Stream(BasePage):
    streamingIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[2]/a")
    liveTab = (By.XPATH, "//div[@class='ime-tab-group w-full font-semibold flex flex-row ["
                         "&::-webkit-scrollbar]:hidden']/button[2]")
    setUpStreamButton = (By.XPATH, "//div[@class='flex flex-col md:flex-row w-full lg:w-fit md:justify-end items-end gap-4 mt-4 lg:mt-7']/div/button[1]")
    Title = (By.CSS_SELECTOR, "input[name ='title']")
    Description = (By.CSS_SELECTOR, "textArea[name = 'description']")
    visibilityDD = (
        By.XPATH, "//div[@class='flex mt-4 space-x-4 w-full flex-col md:flex-row md:gap-4']/div[1]/button")
    publicOptionOfVisibilityDD = (
        By.XPATH, "//div[@class='flex mt-4 space-x-4 w-full flex-col md:flex-row md:gap-4']/div[1]/ul/li[1]")
    privateOptionOfVisibilityDD = (
        By.XPATH, "//div[@class='flex mt-4 space-x-4 w-full flex-col md:flex-row md:gap-4']/div[1]/ul/li[2]")
    hiddenOptionOfVisibilityDD = (
        By.XPATH, "//div[@class='flex mt-4 space-x-4 w-full flex-col md:flex-row md:gap-4']/div[1]/ul/li[3]")
    restrictionDD = (
        By.XPATH, "//div[@class='flex mt-4 space-x-4 w-full flex-col md:flex-row md:gap-4']/div[2]/button")
    noneOptionOfRestrictionDD = (
        By.XPATH, "//div[@class='flex mt-4 space-x-4 w-full flex-col md:flex-row md:gap-4']/div[2]/ul/li[1]")
    ageOptionOfRestrictionDD = (
        By.XPATH, "//div[@class='flex mt-4 space-x-4 w-full flex-col md:flex-row md:gap-4']/div[2]/ul/li[2]")
    serviceTypeDD = (By.XPATH,"//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[5]/div/button")
    recruitmentOption = (By.XPATH,"//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[5]/div/ul/li[1]")
    awardOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[5]/div/ul/li[2]")
    marketingOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[5]/div/ul/li[3]")
    learningOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[5]/div/ul/li[4]")
    auditionOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[5]/div/ul/li[5]")
    admissionOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[5]/div/ul/li[6]")
    excludedAreaDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[6]/button")
    firstOptionOfExcludedAreaDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[6]/ul/li[1]")
    firstNextButton = (By.XPATH, "//div[@class ='flex justify-between items-center gap-4']/div/button")



    liveChat = (By.CSS_SELECTOR,"input[id='form-field-streamChatActive']")
    liveChatReply = (By.CSS_SELECTOR,"input[id='form-field-streamChatLiveReplay']")
    goLiveCheckBox = (By.CSS_SELECTOR, "input[id='form-field-goLiveNow']")
    secondNextButton = (By.XPATH,
                        "//div[@class ='flex justify-between items-center gap-4']/div/button[2]")



    PaymentTypeDD = (By.XPATH, "//div[@class ='px-7 pb-[150px] overflow-y-auto']/div[2]/div[1]/button")
    noneOptionOfPaymentDD = (
        By.XPATH, "//div[@class ='px-7 pb-[150px] overflow-y-auto']/div[2]/div[1]/ul/li[1]")
    payNowOptionOfPaymentDD = (
        By.XPATH, "//div[@class ='px-7 pb-[150px] overflow-y-auto']/div[2]/div[1]/ul/li[2]")
    Amount = (By.XPATH, "//div[@class ='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[2]/input")
    thirdNextButton = (By.XPATH,
                       "//div[@class ='flex justify-between items-center gap-4']/div/button[2]")

    firstName = (By.CSS_SELECTOR, "input[name='firstName']")
    lastName = (By.CSS_SELECTOR, "input[name='lastName']")
    countryCode = (By.XPATH,"//div[@class='flex md:flex-row mt-8 w-full flex-wrap flex-col']/div[3]/div/div/div[1]")
    contactNumber = (By.CSS_SELECTOR, "input[name='contact']")
    Email = (By.CSS_SELECTOR, "input[name='email']")
    addApplicantButton = (By.XPATH, "//div[@class='w-full flex flex-row-reverse']/button")
    submitButton = (By.XPATH, "//div[@class ='flex justify-between items-center gap-4']/div/button[2]")

    # Streaming Window

    chooseLocalDevice = (By.XPATH, "//div[@class='flex gap-4 flex-col md:flex-col lg:flex-row ']/button[2]")
    continueButton = (By.XPATH, "//div[@class='flex gap-6 mr-0']/button[2]")
    endStreamButton = (By.XPATH, "//div[@class='hidden md:block']/button")
    endStreamButtonOfPopUp = (By.XPATH, "//div[@class='flex flex-col items-center space-y-3']/div/button[1]")

    # Create Folder
    nameOfItem = (By.CSS_SELECTOR, "input[name='title']")
    descriptionOfItem = (By.CSS_SELECTOR, "textarea[name='description']")

    publishInput = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div/input")
    nextButtonOne = (By.XPATH, "//div[@class='flex items-center justify-between gap-4']/div[2]/button")
    paymentTypeDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[1]/button")
    nonePaymentOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[1]/ul/li[1]")
    paynowOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[1]/ul/li[2]")

    nextTwo = (By.XPATH, "//div[@class='flex justify-between items-center gap-4']/div/button[2]")

    Contact = (By.CSS_SELECTOR, "input[name='contact']")
    contactDD = (By.XPATH, "//div[@class='mb-4 relative w-full !ml-0 md:w-1/2 md:pr-4 ']/div[1]/div/button")
    optionContact = (By.XPATH, "//div[@class='mb-4 relative w-full !ml-0 md:w-1/2 md:pr-4 ']/div[1]/div/div[1]")
    email = (By.CSS_SELECTOR, "input[name='email']")
    addApplicant = (By.XPATH, "//div[@class='flex md:flex-row w-full flex-wrap flex-col']/div[6]/button")
    saveButton = (By.XPATH, "//div[@class='flex items-center gap-4 ml-auto']/button[2]")

    # Create Folder
    createFolder = (By.XPATH, "//div[@class='flex gap-4 w-full md:w-fit']/button[2]")
    visibilityDDFolder = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[4]/div[1]/button")
    publicOptionOfDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[4]/div[1]/ul/li[1]")
    privateOptionOfDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[4]/div[1]/ul/li[2]")
    hiddenOptionOfDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[4]/div[1]/ul/li[3]")
    ageDDFolder = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[4]/div[2]/button")
    noneOptionDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[4]/div[2]/ul/li[1]")
    eightyPlusOptionDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[4]/div[2]/ul/li[2]")
    uploadFile = (By.XPATH,
                  "//div[@class='w-full mt-2 mb-4 cursor-pointer flex items-center justify-center border border-dashed border-ime-gray-300 dark:border-ime-gray-600 rounded-md']/section/div/input")
    publishInputFolder = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/div/input")
    nextButtonOneFolder = (By.XPATH, "//div[@class='flex justify-between items-center gap-4']/div[1]/button")
    nextButtonTwoFolder = (By.XPATH, "//div[@class='flex justify-between items-center gap-4']/div[1]/button[2]")
    gbpPaymentOption = (By.XPATH, "//div[@class ='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div/div[1]")
    zarPaymentOption = (By.XPATH, "//div[@class ='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div/div[2]")
    usdPaymentOption = (By.XPATH, "//div[@class ='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div/div[3]")
    eurPaymentOption = (By.XPATH, "//div[@class ='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div/div[4]")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_streaming_icon(self):
        time.sleep(4)
        self.de_click(self.streamingIcon)
        time.sleep(4)
        # self.de_click(self.liveTab)
        # time.sleep(4)

    def create_live_streaming(self):

        log.logger.info("****==Create Live Streaming ==***")
        self.de_click(self.setUpStreamButton)
        log.logger.info("User Has Clicked On Set Up Live Stream Button")

        log.logger.info("Current working directory:" + str(os.getcwd()))
        base_dir = os.path.dirname(__file__)

        # Define the relative path to the Pricing.xlsx file
        relative_path = os.path.join(base_dir, '../excel/create_live_streaming.xlsx')
        sheetName = 'stream'

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

        for j in range(2, row + 1):
            for k in range(1, 2):
                titleOfStream = excel_Data.getCellData(path, sheetName, j, 1)
                descriptionOfStream = excel_Data.getCellData(path, sheetName, j, 2)
                visibilityOption = excel_Data.getCellData(path, sheetName, j, 3)
                restrictionOption = excel_Data.getCellData(path, sheetName, j, 4)
                serviceType = excel_Data.getCellData(path, sheetName, j, 5)
                excludedArea = excel_Data.getCellData(path, sheetName, j, 6)
                livechat = excel_Data.getCellData(path, sheetName, j, 7)
                livechatreply = excel_Data.getCellData(path, sheetName, j, 8)
                paymentType = excel_Data.getCellData(path, sheetName, j, 9)
                amount = excel_Data.getCellData(path, sheetName, j, 10)
                fName = excel_Data.getCellData(path, sheetName, j, 11)
                lName = excel_Data.getCellData(path, sheetName, j, 12)
                Number = excel_Data.getCellData(path, sheetName, j, 13)
                aEmail = excel_Data.getCellData(path, sheetName, j, 14)
                log.logger.info("User Has Entered Streaming Title ==> " + titleOfStream)
                log.logger.info("User Has Entered Streaming Description ==> " + descriptionOfStream)
                log.logger.info("User Has Entered Streaming Visibility ==> " + visibilityOption)
                log.logger.info("User Has Entered Streaming Restriction Mode ==> " + restrictionOption)
                log.logger.info("User Has Entered Streaming Service Type ==> " + serviceType)
                log.logger.info("User Has Entered Streaming Excluded Area ==> " + excludedArea)
                log.logger.info("User Has Entered Streaming Live Chat Value ==> " + livechat)
                log.logger.info("User Has Entered Streaming Live Chat Reply Value ==> " + livechatreply)
                log.logger.info("User Has Entered Streaming Payment Type ==> " + paymentType)
                # log.logger.info("User Has Entered Streaming Title ==> " + amount)
                log.logger.info("User Has Entered Streaming First Name Of Applicant ==> " + fName)
                log.logger.info("User Has Entered Streaming Last Name Of Applicant ==> " + lName)
                # log.logger.info("User Has Entered Streaming Number Of Applicant ==> " + Number)
                log.logger.info("User Has Entered Streaming Email Of Applicant ==> " + aEmail)

                time.sleep(1)
                self.do_send_key(self.Title, titleOfStream)
                log.logger.info("User Has Entered Streaming Title ==> " + titleOfStream)
                time.sleep(0.5)
                self.do_send_key(self.Description, descriptionOfStream)
                log.logger.info("User Has Entered Streaming Description ==> " + descriptionOfStream)
                time.sleep(1)
                vDD = self.driver.find_element(By.XPATH,
                                                  "//div[@class='flex mt-4 space-x-4 w-full flex-col md:flex-row md:gap-4']/div[1]/button")
                self.de_scroll_into_view(vDD)
                time.sleep(0.5)
                self.de_click(self.visibilityDD)
                time.sleep(0.5)
                if visibilityOption == "Public":
                    self.de_click(self.publicOptionOfVisibilityDD)
                    log.logger.info("User Has Selected Visibility Mode Of Stream ==> " + visibilityOption)
                elif visibilityOption == "Private":
                    self.de_click(self.privateOptionOfVisibilityDD)
                    log.logger.info("User Has Selected Visibility Mode Of Stream ==> " + visibilityOption)
                elif visibilityOption == "Hidden":
                    self.de_click(self.hiddenOptionOfVisibilityDD)
                    log.logger.info("User Has Selected Visibility Mode Of Stream ==> " + visibilityOption)
                else:
                    self.de_click(self.publicOptionOfVisibilityDD)
                    log.logger.info("User Has Selected Visibility Mode Of Stream ==> " + visibilityOption)
                time.sleep(0.5)
                self.de_click(self.restrictionDD)
                time.sleep(0.5)
                if restrictionOption == "None":
                    self.de_click(self.noneOptionOfRestrictionDD)
                    log.logger.info("User Has Selected Restriction Mode Of Stream ==> " + restrictionOption)
                elif restrictionOption == "18+":
                    self.de_click(self.ageOptionOfRestrictionDD)
                    log.logger.info("User Has Selected Restriction Mode Of Stream ==> " + restrictionOption)
                else:
                    self.de_click(self.noneOptionOfRestrictionDD)
                    log.logger.info("User Has Selected Restriction Mode Of Stream ==> " + restrictionOption)
                time.sleep(0.5)

                sDD = self.driver.find_element(By.XPATH,
                                               "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[5]/div/button")
                self.de_scroll_into_view(sDD)
                time.sleep(0.5)

                self.de_click(self.serviceTypeDD)
                time.sleep(0.5)
                if serviceType == "Recruitment":
                    self.de_click(self.recruitmentOption)
                    log.logger.info("User Has Selected Service Type  Stream ==> " + serviceType)
                elif serviceType == "Award":
                    self.de_click(self.awardOption)
                    log.logger.info("User Has Selected Service Type  Stream ==> " + serviceType)
                elif serviceType == "Marketing":
                    self.de_click(self.marketingOption)
                    log.logger.info("User Has Selected Service Type  Stream ==> " + serviceType)
                elif serviceType == "Learning":
                    self.de_click(self.learningOption)
                    log.logger.info("User Has Selected Service Type  Stream ==> " + serviceType)
                elif serviceType == "Audition":
                    self.de_click(self.auditionOption)
                    log.logger.info("User Has Selected Service Type  Stream ==> " + serviceType)
                elif serviceType == "Admission":
                    self.de_click(self.admissionOption)
                    log.logger.info("User Has Selected Service Type  Stream ==> " + serviceType)
                else:
                    self.de_click(self.recruitmentOption)

                self.de_click(self.excludedAreaDD)
                time.sleep(0.5)
                if excludedArea == "Afghanistan":
                    self.de_click(self.firstOptionOfExcludedAreaDD)
                    log.logger.info("User Has Selected Exclude Area For Stream ==> " + excludedArea)
                    self.de_click(self.excludedAreaDD)
                    time.sleep(0.5)
                else:
                    log.logger.info("No Excluded Area Selected")
                time.sleep(0.5)
                self.de_click(self.firstNextButton)
                log.logger.info("User Has Clicked On Next Button")


                time.sleep(2)
                if livechat == "Yes":
                    self.de_click(self.liveChat)

                time.sleep(1)
                if livechatreply == "Yes":
                    self.de_click(self.liveChatReply)

                self.de_click(self.goLiveCheckBox)
                log.logger.info("User Has Clicked On Go Live Check Box For Stream ")
                time.sleep(1)
                self.de_click(self.secondNextButton)
                log.logger.info("User Has Clicked On Next Button")

                time.sleep(2)
                self.de_click(self.PaymentTypeDD)
                time.sleep(0.5)
                if paymentType == "None":
                    self.de_click(self.noneOptionOfPaymentDD)
                    log.logger.info("User Has Selected Payment Mode ==> " + paymentType)
                elif paymentType == "Pay Now":
                    self.de_click(self.noneOptionOfPaymentDD)
                    log.logger.info("User Has Selected Payment Mode ==> " + paymentType)
                    time.sleep(0.5)
                    self.do_send_key(self.Amount, amount)
                    log.logger.info("User Has Selected Amount For Streaming ==> " + paymentType)
                else:
                    self.de_click(self.noneOptionOfPaymentDD)
                    log.logger.info("User Has Selected Payment Mode ==> " + paymentType)
                self.de_click(self.thirdNextButton)
                log.logger.info("User Has Clicked On Next Button")


                time.sleep(2)
                self.do_send_key(self.firstName, fName)
                time.sleep(1)
                self.do_send_key(self.lastName, lName)
                time.sleep(1)
                country_code = self.driver.find_element(By.XPATH,
                                                        "//div[@class='flex md:flex-row mt-8 w-full flex-wrap flex-col']/div[3]/div/div/button")
                # select = Select(currency_code)
                country_code.click()
                time.sleep(1)
                self.de_click(self.countryCode)
                time.sleep(1)
                self.do_send_key(self.contactNumber, Number)
                time.sleep(1)
                self.do_send_key(self.Email, aEmail)
                time.sleep(1)
                self.de_click(self.addApplicantButton)
                time.sleep(2)

                #
                original_window = self.driver.current_window_handle
                #
                # # Check we don't have other windows open already
                assert len(self.driver.window_handles) == 1

                # Click the link which opens in a new window
                self.de_click(self.submitButton)
                # Wait for the new window or tab
                WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

                # Loop through until we find a new window handle
                for window_handle in self.driver.window_handles:
                    if window_handle != original_window:
                        self.driver.switch_to.window(window_handle)
                        break

                        # Wait for the new tab to finish loading content
                time.sleep(5)
                self.browser_zoom_out()
                time.sleep(2)
                self.de_click(self.chooseLocalDevice)
                time.sleep(10)
                self.de_click(self.continueButton)
                time.sleep(7)
                self.de_click(self.endStreamButton)
                time.sleep(5)
                self.de_click(self.endStreamButtonOfPopUp)
                time.sleep(5)
                self.driver.close()
                time.sleep(0.5)
                self.driver.switch_to.window(original_window)
                time.sleep(3)
                self.de_click(self.setUpStreamButton)

    def create_folder(self):
        log.logger.info("****==Create Folder Under Live Streaming Test Case Starts Here==***")
        self.de_click(self.createFolder)

        base_dir = os.path.dirname(__file__)

        # Define the relative path to the Pricing.xlsx file
        relative_path = os.path.join(base_dir, '../excel/create_digital_content_folder.xlsx')
        sheetName = 'digital_content'

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

        for j in range(2, row + 1):
            for k in range(1, 2):
                title = excel_Data.getCellData(path, sheetName, j, 1)
                description = excel_Data.getCellData(path, sheetName, j, 2)
                visibility = excel_Data.getCellData(path, sheetName, j, 3)
                age = excel_Data.getCellData(path, sheetName, j, 4)
                restriction = excel_Data.getCellData(path, sheetName, j, 5)
                excluded_area = excel_Data.getCellData(path, sheetName, j, 6)
                payment = excel_Data.getCellData(path, sheetName, j, 7)
                code = excel_Data.getCellData(path, sheetName, j, 8)
                amount = excel_Data.getCellData(path, sheetName, j, 9)
                fName = excel_Data.getCellData(path, sheetName, j, 10)
                lName = excel_Data.getCellData(path, sheetName, j, 11)
                contact = excel_Data.getCellData(path, sheetName, j, 12)
                email = excel_Data.getCellData(path, sheetName, j, 13)
                log.logger.info("User Has Entered Folder Title ==> " + title)
                log.logger.info("User Has Entered Folder Description ==> " + description)
                log.logger.info("User Has Entered Folder Visibility ==> " + visibility)
                log.logger.info("User Has Entered Folder Age  ==> " + age)
                log.logger.info("User Has Entered Folder Restriction Option ==> " + restriction)
                log.logger.info("User Has Entered Folder Excluded Area ==> " + excluded_area)
                log.logger.info("User Has Entered Folder Payment Option ==> " + payment)
                log.logger.info("User Has Entered Folder Title ==> " + code)
                log.logger.info("User Has Entered Folder Amount ==> " + amount)
                log.logger.info("User Has Entered Folder Title ==> " + fName)
                log.logger.info("User Has Entered Folder Title ==> " + lName)
                # log.logger.info("User Has Entered Streaming Title ==> ", str(contact))
                log.logger.info("User Has Entered Folder Title ==> " + email)

                time.sleep(1)
                self.do_send_key(self.nameOfItem, title)
                time.sleep(0.5)
                self.do_send_key(self.descriptionOfItem, description)
                time.sleep(0.5)
                vDD = self.driver.find_element(By.XPATH,
                                               "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[4]/div[1]/button")
                self.de_scroll_into_view(vDD)
                time.sleep(0.5)
                self.de_click(self.visibilityDDFolder)
                time.sleep(0.5)
                if visibility == "Public":
                    self.de_click(self.publicOptionOfDD)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                elif visibility == "Private":
                    self.de_click(self.privateOptionOfDD)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                elif visibility == "Hidden":
                    self.de_click(self.hiddenOptionOfDD)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                else:
                    self.de_click(self.publicOptionOfDD)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                time.sleep(0.5)
                self.de_click(self.ageDDFolder)
                time.sleep(0.5)
                if age == "None":
                    self.de_click(self.noneOptionDD)
                    log.logger.info("User Has Selected Restriction Mode Of Digital Content ==> " + age)
                elif age == "18+":
                    self.de_click(self.eightyPlusOptionDD)
                    log.logger.info("User Has Selected Restriction Mode Of Digital Content ==> " + age)
                else:
                    self.de_click(self.noneOptionDD)
                    log.logger.info("User Has Selected Restriction Mode Of Digital Content ==> " + age)
                time.sleep(0.5)
                # Find the file input element
                file_input = self.driver.find_element(By.XPATH,
                                                      "//div[@class='w-full mt-2 mb-4 cursor-pointer flex items-center justify-center border border-dashed border-ime-gray-300 dark:border-ime-gray-600 rounded-md']/section/div/input")

                # Replace with the path to the video file you want to upload
                relative_path = os.path.join(base_dir, '../Document/07.png')
                absolute_file_path = os.path.abspath(relative_path)

                # Check if the file input element accepts the desired file types
                accept_attribute = file_input.get_attribute('accept')

                # Define accepted types
                accepted_types = [
                    'image/jpeg', '.jpeg', '.jpg', 'image/png', '.png'
                ]

                # Extract the file extension and MIME type from the file path
                file_extension = os.path.splitext(absolute_file_path)[1].lower()
                mime_type = None

                # Determine the MIME type for common file extensions (you may need to adjust this for your use case)
                mime_type_mapping = {
                    '.jpeg': 'image/jpeg',
                    '.jpg': 'image/jpeg',
                    '.png': 'image/png',

                }

                if file_extension in mime_type_mapping:
                    mime_type = mime_type_mapping[file_extension]

                # Function to check if file type is accepted
                def is_accepted(file_extension, mime_type, accepted_types):
                    for accepted_type in accepted_types:
                        if file_extension == accepted_type or mime_type == accepted_type:
                            return True
                        if '*' in accepted_type and file_extension in accepted_type:
                            return True
                        if '*' in accepted_type and mime_type and mime_type.startswith(accepted_type.split('/')[0]):
                            return True

                    return False

                # Check if the file type is accepted
                if is_accepted(file_extension, mime_type, accepted_types):
                    # Send the file path to the file input element
                    file_input.send_keys(absolute_file_path)
                    log.logger.info("User Has Uploaded Video For Stream")
                else:
                    log.logger.info("File input does not accept the file type or format: " + accept_attribute)

                time.sleep(5)

                # pInput = self.driver.find_element(By.XPATH,
                #                                   "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/div/input")
                # self.de_scroll_into_view(pInput)
                # time.sleep(0.5)
                # self.de_click(self.publishInputFolder)
                # time.sleep(4)
                # self.de_click(self.a)
                # time.sleep(0.5)
                # if excludedArea == "Afghanistan":
                #     self.de_click(self.firstOptionOfExcludedAreaDD)
                #     log.logger.info("User Has Selected Exclude Area For Stream ==> " + excludedArea)
                # else:
                #     log.logger.info("No Excluded Area Selected")

                self.de_click(self.nextButtonOneFolder)
                time.sleep(1)
                self.de_click(self.paymentTypeDD)
                time.sleep(0.5)
                if payment == "None":
                    self.de_click(self.nonePaymentOption)
                    log.logger.info("User Has Selected Payment Mode ==> " + payment)
                elif payment == "Pay Now":
                    self.de_click(self.paynowOption)
                    log.logger.info("User Has Selected Payment Mode ==> " + payment)
                    time.sleep(0.5)
                    currency_code = self.driver.find_element(By.XPATH,
                                                             "//div[@class ='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div/button")
                    # select = Select(currency_code)
                    currency_code.click()
                    time.sleep(1)
                    if code == "GBP":
                        # select.select_by_visible_text("GBP")
                        self.de_click(self.gbpPaymentOption)
                        time.sleep(0.5)
                        self.do_send_key(self.Amount, amount)
                    elif code == "ZAR":
                        # select.select_by_visible_text("ZAR")
                        self.de_click(self.zarPaymentOption)
                        time.sleep(0.5)
                        self.do_send_key(self.Amount, amount)
                    elif code == "USD":
                        # select.select_by_visible_text("USD")
                        self.de_click(self.usdPaymentOption)
                        time.sleep(0.5)
                        self.do_send_key(self.Amount, amount)
                    elif code == "EUR":
                        # select.select_by_visible_text("EUR")
                        self.de_click(self.eurPaymentOption)
                        time.sleep(0.5)
                        self.do_send_key(self.Amount, amount)
                    else:
                        # select.select_by_visible_text("GBP")
                        self.de_click(self.gbpPaymentOption)
                        time.sleep(0.5)
                        self.do_send_key(self.Amount, amount)
                    log.logger.info("User Has Selected Amount For Digital Content ==> " + payment)
                else:
                    self.de_click(self.nonePaymentOption)
                    log.logger.info("User Has Selected Payment Mode ==> " + payment)

                time.sleep(1)

                self.de_click(self.nextButtonTwoFolder)
                time.sleep(1)
                self.de_click(self.saveButton)
                time.sleep(5)


