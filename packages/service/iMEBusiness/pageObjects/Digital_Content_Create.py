import time
import os
import logging
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEBusiness.Utilities.excelReader import excel_Data
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Digital_Content_Create(BasePage):
    digitalContentIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[3]")
    uploadButton = (By.XPATH,
                    "//div[@class='flex flex-col md:flex-row w-full lg:w-fit md:justify-end items-end gap-4 mt-4 lg:mt-7']/div/button[1]")
    nameOfItem = (By.CSS_SELECTOR, "input[id='title']")
    descriptionOfItem = (By.CSS_SELECTOR, "textarea[id='description']")
    visibilityDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[5]/div[1]/button")
    publicOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[5]/div[1]/ul/li[1]")
    privateOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[5]/div[1]/ul/li[2]")
    hiddenOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[5]/div[1]/ul/li[3]")
    ageDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[5]/div[2]/button")
    noneOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[5]/div[2]/ul/li[1]")
    eightyPlusOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[5]/div[2]/ul/li[2]")
    publishInput = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[7]/div/input")
    nextButtonOne = (By.XPATH, "//div[@class='flex justify-between items-center gap-4']/div[2]/button")
    paymentTypeDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/button")
    nonePaymentOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/ul/li[1]")
    paynowOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/ul/li[2]")
    Amount = (By.CSS_SELECTOR,
              "input[name='paymentCost']")
    nextTwo = (By.XPATH, "//div[@class='flex justify-between items-center gap-4']/div[2]/button[2]")
    firstName = (By.CSS_SELECTOR, "input[name='firstName']")
    lastName = (By.CSS_SELECTOR, "input[name='lastName']")
    Contact = (By.CSS_SELECTOR, "input[name='contact']")
    contactDD = (By.XPATH, "//div[@class='mb-4 relative w-full !ml-0 md:w-1/2 md:pr-4 ']/div[1]/div/button")
    optionContact = (By.XPATH, "//div[@class='mb-4 relative w-full !ml-0 md:w-1/2 md:pr-4 ']/div[1]/div/div[1]")
    email = (By.CSS_SELECTOR, "input[name='email']")
    addApplicant = (By.XPATH, "//div[@class='flex md:flex-row w-full flex-wrap flex-col']/div[6]/button")
    saveButton = (By.XPATH, "//div[@class='flex items-center gap-4 ml-auto']/button[2]")

    # Create Folder
    createFolder = (By.XPATH, "//div[@class='flex gap-4 w-full md:w-fit']/button[2]")
    visibilityDDFolder = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[4]/div[1]/button")
    publicOptionOfDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[4]/div[1]/ul/li[1]")
    privateOptionOfDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[4]/div[1]/ul/li[2]")
    hiddenOptionOfDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[4]/div[1]/ul/li[3]")
    ageDDFolder = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[4]/div[2]/button")
    noneOptionDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[4]/div[2]/ul/li[1]")
    eightyPlusOptionDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[4]/div[2]/ul/li[2]")
    uploadFile = (By.XPATH,
                  "//div[@class='w-full mt-2 mb-4 cursor-pointer flex items-center justify-center border border-dashed border-ime-gray-300 dark:border-ime-gray-600 rounded-md']/section/div/input")
    publishInputFolder = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[2]/div/input")
    nextButtonOneFolder = (By.XPATH, "//div[@class='flex justify-between items-center gap-4']/div[1]/button")
    nextButtonTwoFolder = (By.XPATH, "//div[@class='flex justify-between items-center gap-4']/div[1]/button[2]")

    gbpPaymentOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[3]/div/div/div[1]")
    zarPaymentOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[3]/div/div/div[2]")
    usdPaymentOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[3]/div/div/div[3]")
    eurPaymentOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[3]/div/div/div[4]")

    # Create Item Under Document
    cogIconOne = (By.XPATH,
                  "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[9]/div/button")
    viewFolderOne = (By.XPATH,
                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[9]/div/div/a[1]")

    uploadButtonOne = (
        By.XPATH, "//div[@class='flex flex-col lg:flex-row justify-between pt-5 pb-8 items-center']/div/button[1]")

    saveButtonFolderItem = (By.XPATH, "//div[@class='flex items-center justify-between gap-4']/button")

    # Service DD
    recruitmentOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/ul/li[1]")
    awardOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/ul/li[2]")
    marketingOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/ul/li[3]")
    learningOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/ul/li[4]")
    auditionOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/ul/li[5]")
    admissionOption = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/ul/li[6]")

    # Service DD For Folder
    recruitmentOptionFD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/div/ul/li[1]")
    awardOptionFD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/div/ul/li[2]")
    marketingOptionFD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/div/ul/li[3]")
    learningOptionFD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/div/ul/li[4]")
    auditionOptionFD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/div/ul/li[5]")
    admissionOptionFD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/div/ul/li[6]")

    allFilesLink = (By.XPATH,"//div[@class='flex justify-between pb-3']/span[1]/a")


    def __init__(self, driver, environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_digital_content_icon(self):
        time.sleep(5)
        self.de_click(self.digitalContentIcon)
        time.sleep(4)

    def create_digital_content_item(self):
        log.logger.info("****==Create Item Under Digital Content Test Case Starts Here==***")
        self.de_click(self.uploadButton)
        base_dir = os.path.dirname(__file__)

        # Define the relative path to the Pricing.xlsx file
        relative_path = os.path.join(base_dir, '../excel/create_digital_content.xlsx')
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
                service = excel_Data.getCellData(path, sheetName, j, 6)
                excluded_area = excel_Data.getCellData(path, sheetName, j, 7)
                payment = excel_Data.getCellData(path, sheetName, j, 8)
                amount = excel_Data.getCellData(path, sheetName, j, 9)
                firstName = excel_Data.getCellData(path, sheetName, j, 10)
                lastName = excel_Data.getCellData(path, sheetName, j, 11)
                Contact = excel_Data.getCellData(path, sheetName, j, 12)
                Email = excel_Data.getCellData(path, sheetName, j, 13)
                log.logger.info("User Has Entered Digital Item Title ==> " + title)
                log.logger.info("User Has Entered Item Desc ==> " + description)
                log.logger.info("User Has Entered Item Visibility ==> " + visibility)
                log.logger.info("User Has Entered Item Age Restriction  ==> " + age)
                log.logger.info("User Has Entered Item Restriction ==> " + restriction)
                log.logger.info("User Has Entered Item Service Type ==> " + service)
                log.logger.info("User Has Entered Item Excluded for area ==> " + excluded_area)
                log.logger.info("User Has Entered Item  Payment Type==> " + payment)
                # log.logger.info("User Has Entered Item Amount To Pay ==> ", amount)
                log.logger.info("User Has Entered User FName ==> " + firstName)
                log.logger.info("User Has Entered User LName ==> " + lastName)
                # log.logger.info("User Has Entered User Contact ==> " + Contact)
                log.logger.info("User Has Entered User Email ==> " + Email)

                time.sleep(1)
                self.upload_document(title, base_dir)
                time.sleep(2)
                self.do_send_key(self.nameOfItem, title)
                time.sleep(0.5)
                self.do_send_key(self.descriptionOfItem, description)
                time.sleep(0.5)
                vDD = self.driver.find_element(By.XPATH,
                                               "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[5]/div[1]/button")
                self.de_scroll_into_view(vDD)
                time.sleep(1)
                self.de_scroll_into_view(vDD)
                time.sleep(0.5)
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
                self.de_click(self.ageDD)
                time.sleep(0.5)
                if age == "None":
                    self.de_click(self.noneOption)
                    log.logger.info("User Has Selected Restriction Mode Of Digital Content ==> " + age)
                elif age == "18+":
                    self.de_click(self.eightyPlusOption)
                    log.logger.info("User Has Selected Restriction Mode Of Digital Content ==> " + age)
                else:
                    self.de_click(self.noneOption)
                    log.logger.info("User Has Selected Restriction Mode Of Digital Content ==> " + age)
                time.sleep(0.5)
                serviceDD = self.driver.find_element(By.XPATH,
                                                     "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/button")
                self.de_scroll_into_view(serviceDD)
                time.sleep(1)
                serviceDD.click()
                time.sleep(0.5)
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
                time.sleep(0.5)
                pInput = self.driver.find_element(By.XPATH,
                                                  "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[7]/div/input")
                self.de_scroll_into_view(pInput)
                time.sleep(0.5)
                self.de_click(self.publishInput)
                time.sleep(0.5)
                # self.de_click(self.a)
                # time.sleep(0.5)
                # if excludedArea == "Afghanistan":
                #     self.de_click(self.firstOptionOfExcludedAreaDD)
                #     log.logger.info("User Has Selected Exclude Area For Stream ==> " + excludedArea)
                # else:
                #     log.logger.info("No Excluded Area Selected")

                time.sleep(0.5)

                self.de_click(self.nextButtonOne)
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
                    self.do_send_key(self.Amount, amount)
                    log.logger.info("User Has Selected Amount For Digital Content ==> " + payment)
                else:
                    self.de_click(self.nonePaymentOption)
                    log.logger.info("User Has Selected Payment Mode ==> " + payment)

                time.sleep(0.5)

                self.de_click(self.nextTwo)
                time.sleep(1)
                self.de_click(self.saveButton)
                time.sleep(25)
                if j < 5:
                    self.de_click(self.uploadButton)
                    continue
                else:
                    break

        time.sleep(5)

    def create_digital_content_folder(self):
        log.logger.info("****==Create Folder Under Digital Content Test Case Starts Here==***")
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
                service = excel_Data.getCellData(path, sheetName, j, 6)
                excluded_area = excel_Data.getCellData(path, sheetName, j, 7)
                payment = excel_Data.getCellData(path, sheetName, j, 8)
                code = excel_Data.getCellData(path, sheetName, j, 9)
                amount = excel_Data.getCellData(path, sheetName, j, 10)
                fName = excel_Data.getCellData(path, sheetName, j, 11)
                lName = excel_Data.getCellData(path, sheetName, j, 12)
                contact = excel_Data.getCellData(path, sheetName, j, 13)
                email = excel_Data.getCellData(path, sheetName, j, 14)
                log.logger.info("User Has Entered Digital Folder Title ==> " + title)
                log.logger.info("User Has Entered Digital Folder Desc ==> " + description)
                log.logger.info("User Has Entered Digital Folder Visibility ==> " + visibility)
                log.logger.info("User Has Entered Digital Folder Age ==> " + age)
                log.logger.info("User Has Entered Digital Folder Restriction ==> " + restriction)
                log.logger.info("User Has Entered Digital Folder Service Type ==> " + service)
                log.logger.info("User Has Entered Digital Folder Excluded For ==> " + excluded_area)
                log.logger.info("User Has Entered Digital Folder Payment Type ==> " + payment)
                log.logger.info("User Has Entered Digital Folder Country Code ==> " + code)
                log.logger.info("User Has Entered Digital Folder Amount ==> " + amount)
                log.logger.info("User Has Entered User Fname ==> " + fName)
                log.logger.info("User Has Entered User Lname ==> " + lName)
                # log.logger.info("User Has Entered Streaming Title ==> ", str(contact))
                log.logger.info("User Has Entered User Email ==> " + email)

                time.sleep(1)
                self.do_send_key(self.nameOfItem, title)
                time.sleep(0.5)
                self.do_send_key(self.descriptionOfItem, description)
                time.sleep(0.5)
                vDD = self.driver.find_element(By.XPATH,
                                               "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[4]/div[1]/button")
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

                time.sleep(2)

                serviceDD = self.driver.find_element(By.XPATH,
                                                     "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[1]/div/button")
                self.de_scroll_into_view(serviceDD)
                time.sleep(1)
                serviceDD.click()
                time.sleep(0.5)
                if service == "Recruitment":
                    self.de_click(self.recruitmentOptionFD)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                elif service == "Awards":
                    self.de_click(self.awardOptionFD)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                elif service == "Marketing":
                    self.de_click(self.marketingOptionFD)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                elif service == "Learning":
                    self.de_click(self.learningOptionFD)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                elif service == "Auditions":
                    self.de_click(self.auditionOptionFD)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                elif service == "Admissions":
                    self.de_click(self.admissionOptionFD)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                else:
                    self.de_click(self.recruitmentOptionFD)
                    log.logger.info("User Has Selected Visibility Mode Of Digital Content ==> " + visibility)
                time.sleep(0.5)

                pInput = self.driver.find_element(By.XPATH,
                                                  "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[6]/div[2]/div/input")
                self.de_scroll_into_view(pInput)
                time.sleep(0.5)
                self.de_click(self.publishInputFolder)
                time.sleep(5)
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
                                                             "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[3]/div/div/button")
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
                time.sleep(10)
                self.de_click(self.createFolder)
                time.sleep(1)

    def create_item_under_folder(self):
        data_avail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody"))
        )
        value = data_avail.text
        if len(value) > 0:
            for i in range(10):
                folders = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[3]/span")

                visibility = self.driver.find_elements(By.XPATH,
                                                       "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[6]/span")
                cog_icons = self.driver.find_elements(By.XPATH,
                                                      "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[9]/div/button")
                folder_name = folders[i].text
                visibility_name = visibility[i].text

                if folder_name == "Folder" or visibility_name == "Public" or visibility_name == "Private" or visibility_name == "Hidden":

                    cog_icons[i].click()
                    time.sleep(1)

                    locator = (By.XPATH,
                               f"//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[{i + 1}]/td[9]/div/div/a[1]")
                    WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator)).click()
                    time.sleep(3)
                    numberOfItem = self.driver.find_element(By.XPATH,
                                                            "//div[@class='flex justify-between pb-3']/span[2]").text
                    log.logger.info("numberOfItem" + numberOfItem)
                    parts = numberOfItem.split(" ")

                    # Extract the numeric values from the relevant parts
                    current_items = int(parts[0])  # First part before the '/'

                    log.logger.info("Item Value: " + str(current_items))

                    # Output the values to verify
                    print(f"Current items: {current_items}")
                    for current_items in range(20-current_items):
                        self.de_click(self.uploadButtonOne)
                        time.sleep(2)
                        base_dir = os.path.dirname(__file__)
                        # Find the file input element
                        file_input = self.driver.find_element(By.XPATH,
                                                              "//div[@class='flex flex-col w-full items-center justify-center  items-center']/input")

                        # Replace with the path to the video file you want to upload
                        relative_path = os.path.join(base_dir, '../video/one.mp4')
                        absolute_file_path = os.path.abspath(relative_path)

                        # Check if the file input element accepts the desired file types
                        accept_attribute = file_input.get_attribute('accept')

                        # Define accepted types
                        accepted_types = [
                            '.mp4', 'video/*', 'image/jpeg', '.jpeg', '.jpg', 'image/png', '.png',
                            'application/pdf', '.pdf', 'audio/mpeg', '.mp3', 'audio/wav', '.wav',
                            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                            '.docx', 'application/vnd.ms-powerpoint', '.ppt',
                            'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                            '.pptx',
                            'application/vnd.ms-excel', '.xls',
                            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', '.xlsx'
                        ]

                        # Extract the file extension and MIME type from the file path
                        file_extension = os.path.splitext(absolute_file_path)[1].lower()
                        mime_type = None

                        # Determine the MIME type for common file extensions (you may need to adjust this for your use case)
                        mime_type_mapping = {
                            '.mp4': 'video/mp4',
                            '.jpeg': 'image/jpeg',
                            '.jpg': 'image/jpeg',
                            '.png': 'image/png',
                            '.pdf': 'application/pdf',
                            '.mp3': 'audio/mpeg',
                            '.wav': 'audio/wav',
                            '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                            '.ppt': 'application/vnd.ms-powerpoint',
                            '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                            '.xls': 'application/vnd.ms-excel',
                            '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
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
                                if '*' in accepted_type and mime_type and mime_type.startswith(
                                        accepted_type.split('/')[0]):
                                    return True

                            return False

                        # Check if the file type is accepted
                        if is_accepted(file_extension, mime_type, accepted_types):
                            # Send the file path to the file input element
                            file_input.send_keys(absolute_file_path)
                            log.logger.info("User Has Uploaded Video For Stream")
                        else:
                            log.logger.info(
                                "File input does not accept the file type or format: " + accept_attribute)

                        time.sleep(2)

                        self.do_send_key(self.nameOfItem, "TestItem")
                        time.sleep(1)
                        self.do_send_key(self.descriptionOfItem, "Test")
                        time.sleep(1)
                        self.de_click(self.saveButtonFolderItem)
                        time.sleep(15)




                else:
                    break

                self.de_click(self.allFilesLink)
                time.sleep(3)



        else:
            log.logger.info("No Folder To Upload Item")



    def upload_document(self, title, base_dir):
        if title == "AutomatioTest1":

            # Find the file input element
            file_input = self.driver.find_element(By.XPATH,
                                                  "//div[@class='flex flex-col w-full items-center justify-center  items-center']/input")

            # Replace with the path to the video file you want to upload
            relative_path = os.path.join(base_dir, '../video/one.mp4')
            absolute_file_path = os.path.abspath(relative_path)

            # Check if the file input element accepts the desired file types
            accept_attribute = file_input.get_attribute('accept')

            # Define accepted types
            accepted_types = [
                '.mp4', 'video/*', 'image/jpeg', '.jpeg', '.jpg', 'image/png', '.png',
                'application/pdf', '.pdf', 'audio/mpeg', '.mp3', 'audio/wav', '.wav',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                '.docx', 'application/vnd.ms-powerpoint', '.ppt',
                'application/vnd.openxmlformats-officedocument.presentationml.presentation', '.pptx',
                'application/vnd.ms-excel', '.xls',
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', '.xlsx'
            ]

            # Extract the file extension and MIME type from the file path
            file_extension = os.path.splitext(absolute_file_path)[1].lower()
            mime_type = None

            # Determine the MIME type for common file extensions (you may need to adjust this for your use case)
            mime_type_mapping = {
                '.mp4': 'video/mp4',
                '.jpeg': 'image/jpeg',
                '.jpg': 'image/jpeg',
                '.png': 'image/png',
                '.pdf': 'application/pdf',
                '.mp3': 'audio/mpeg',
                '.wav': 'audio/wav',
                '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                '.ppt': 'application/vnd.ms-powerpoint',
                '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                '.xls': 'application/vnd.ms-excel',
                '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
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

            time.sleep(2)

        elif title == "AutomatioTest2":
            # Find the file input element
            file_input = self.driver.find_element(By.XPATH,
                                                  "//div[@class='flex flex-col w-full items-center justify-center  items-center']/input")

            # Replace with the path to the video file you want to upload
            relative_path = os.path.join(base_dir, '../video/test.pdf')
            absolute_file_path = os.path.abspath(relative_path)

            # Check if the file input element accepts the desired file types
            accept_attribute = file_input.get_attribute('accept')

            # Define accepted types
            accepted_types = [
                '.mp4', 'video/*', 'image/jpeg', '.jpeg', '.jpg', 'image/png', '.png',
                'application/pdf', '.pdf', 'audio/mpeg', '.mp3', 'audio/wav', '.wav',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                '.docx', 'application/vnd.ms-powerpoint', '.ppt',
                'application/vnd.openxmlformats-officedocument.presentationml.presentation', '.pptx',
                'application/vnd.ms-excel', '.xls',
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', '.xlsx'
            ]

            # Extract the file extension and MIME type from the file path
            file_extension = os.path.splitext(absolute_file_path)[1].lower()
            mime_type = None

            # Determine the MIME type for common file extensions (you may need to adjust this for your use case)
            mime_type_mapping = {
                '.mp4': 'video/mp4',
                '.jpeg': 'image/jpeg',
                '.jpg': 'image/jpeg',
                '.png': 'image/png',
                '.pdf': 'application/pdf',
                '.mp3': 'audio/mpeg',
                '.wav': 'audio/wav',
                '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                '.ppt': 'application/vnd.ms-powerpoint',
                '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                '.xls': 'application/vnd.ms-excel',
                '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
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

            time.sleep(2)

        elif title == "AutomatioTest3":
            # Find the file input element
            file_input = self.driver.find_element(By.XPATH,
                                                  "//div[@class='flex flex-col w-full items-center justify-center  items-center']/input")

            # Replace with the path to the video file you want to upload
            relative_path = os.path.join(base_dir, '../video/prfl.jpeg')
            absolute_file_path = os.path.abspath(relative_path)

            # Check if the file input element accepts the desired file types
            accept_attribute = file_input.get_attribute('accept')

            # Define accepted types
            accepted_types = [
                '.mp4', 'video/*', 'image/jpeg', '.jpeg', '.jpg', 'image/png', '.png',
                'application/pdf', '.pdf', 'audio/mpeg', '.mp3', 'audio/wav', '.wav',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                '.docx', 'application/vnd.ms-powerpoint', '.ppt',
                'application/vnd.openxmlformats-officedocument.presentationml.presentation', '.pptx',
                'application/vnd.ms-excel', '.xls',
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', '.xlsx'
            ]

            # Extract the file extension and MIME type from the file path
            file_extension = os.path.splitext(absolute_file_path)[1].lower()
            mime_type = None

            # Determine the MIME type for common file extensions (you may need to adjust this for your use case)
            mime_type_mapping = {
                '.mp4': 'video/mp4',
                '.jpeg': 'image/jpeg',
                '.jpg': 'image/jpeg',
                '.png': 'image/png',
                '.pdf': 'application/pdf',
                '.mp3': 'audio/mpeg',
                '.wav': 'audio/wav',
                '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                '.ppt': 'application/vnd.ms-powerpoint',
                '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                '.xls': 'application/vnd.ms-excel',
                '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
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

            time.sleep(2)

        elif title == "AutomatioTest4":
            # Find the file input element
            file_input = self.driver.find_element(By.XPATH,
                                                  "//div[@class='flex flex-col w-full items-center justify-center  items-center']/input")

            # Replace with the path to the video file you want to upload
            relative_path = os.path.join(base_dir, '../video/audio.wav')
            absolute_file_path = os.path.abspath(relative_path)

            # Check if the file input element accepts the desired file types
            accept_attribute = file_input.get_attribute('accept')

            # Define accepted types
            accepted_types = [
                '.mp4', 'video/*', 'image/jpeg', '.jpeg', '.jpg', 'image/png', '.png',
                'application/pdf', '.pdf', 'audio/mpeg', '.mp3', 'audio/wav', '.wav',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                '.docx', 'application/vnd.ms-powerpoint', '.ppt',
                'application/vnd.openxmlformats-officedocument.presentationml.presentation', '.pptx',
                'application/vnd.ms-excel', '.xls',
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', '.xlsx'
            ]

            # Extract the file extension and MIME type from the file path
            file_extension = os.path.splitext(absolute_file_path)[1].lower()
            mime_type = None

            # Determine the MIME type for common file extensions (you may need to adjust this for your use case)
            mime_type_mapping = {
                '.mp4': 'video/mp4',
                '.jpeg': 'image/jpeg',
                '.jpg': 'image/jpeg',
                '.png': 'image/png',
                '.pdf': 'application/pdf',
                '.mp3': 'audio/mpeg',
                '.wav': 'audio/wav',
                '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                '.ppt': 'application/vnd.ms-powerpoint',
                '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                '.xls': 'application/vnd.ms-excel',
                '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
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

            time.sleep(2)
