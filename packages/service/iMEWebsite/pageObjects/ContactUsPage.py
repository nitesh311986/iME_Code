import os
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import logging
from iMEWebsite.pageObjects.BasePage import BasePage
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.Utilities.excelReader import excel_Data


log = Logger(__name__, logging.INFO)


class ContactUs(BasePage):
    contactUsIcon = (By.XPATH, "//div[@class='framer-1id1vs8']/div[1]/div[4]/p")
    firstName = (By.CSS_SELECTOR, "input[name='firstName']")
    lastName = (By.CSS_SELECTOR, "input[name='lastName']")
    Email = (By.CSS_SELECTOR, "input[name='emailAddress']")
    contactNumber = (By.CSS_SELECTOR, "input[name='contactNumber']")
    companyName = (By.CSS_SELECTOR, "input[name='company']")
    interestedInDD = (By.XPATH, "//div[@class='framer-pcceit-container']/form/div[4]/div/div")
    imeProduct = (By.XPATH, "//div[@class='framer-pcceit-container']/form/div[4]/div/div[2]/div[1]")
    imePartner = (By.XPATH, "//div[@class='framer-pcceit-container']/form/div[4]/div/div[2]/div[2]")
    generalEnquiry = (By.XPATH, "//div[@class='framer-pcceit-container']/form/div[4]/div/div[2]/div[3]")
    imeCustomer = (By.XPATH, "//div[@class='framer-pcceit-container']/form/div[4]/div/div[2]/div[4]")
    other = (By.XPATH, "//div[@class='framer-pcceit-container']/form/div[4]/div/div[2]/div[5]")
    Message = (By.CSS_SELECTOR, "textArea[name='additionalNotes']")
    sendMessage = (By.XPATH, "//div[@class='framer-pcceit-container']/form/div[6]/button")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def send_enquiry(self):
        log.logger.info("****==Verify iME Contact Us Feature==***")
        time.sleep(2)
        self.de_click(self.contactUsIcon)
        time.sleep(3)


        base_dir = os.path.dirname(__file__)

        # Define the relative path to the Pricing.xlsx file
        relative_path = os.path.join(base_dir, '../excel/ContactOne.xlsx')

        # Get the absolute path
        path = os.path.abspath(relative_path)
        print("Absolute path:", path)

        # Check if the file exists
        if os.path.exists(path):
            print("File found!")
            # Proceed with file operations
        else:
            raise FileNotFoundError(f"File not found: {path}")
        sheetName = 'contact'
        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))

        for j in range(2, row + 1):
            for k in range(1, 2):
                fName = excel_Data.getCellData(path, sheetName, j, 1)
                lName = excel_Data.getCellData(path, sheetName, j, 2)
                email = excel_Data.getCellData(path, sheetName, j, 3)
                contact = excel_Data.getCellData(path, sheetName, j, 4)
                company = excel_Data.getCellData(path, sheetName, j, 5)
                find_us = excel_Data.getCellData(path, sheetName, j, 6)
                interested = excel_Data.getCellData(path, sheetName, j, 7)
                message = excel_Data.getCellData(path, sheetName, j, 8)
                log.logger.info("" + str(fName))
                log.logger.info("" + str(lName))
                log.logger.info("" + str(email))
                log.logger.info("" + str(contact))
                log.logger.info("" + str(company))
                log.logger.info("" + str(find_us))
                log.logger.info("" + str(interested))
                log.logger.info("" + str(message))

                self.do_send_key(self.firstName, fName)
                time.sleep(0.5)
                self.do_send_key(self.lastName, lName)
                time.sleep(0.5)
                self.do_send_key(self.Email, email)
                time.sleep(0.5)
                self.do_send_key(self.contactNumber, contact)
                time.sleep(0.5)
                self.do_send_key(self.companyName, company)
                time.sleep(0.5)

                # Select Region

                select_region = self.driver.find_element(By.XPATH, "//div[@class='framer-pcceit-container']/form/div["
                                                                   "3]/div[2]/select")
                selectRe = Select(select_region)
                select_region.click()
                time.sleep(0.5)
                selectRe.select_by_index(4)
                time.sleep(0.5)


                # Select Code
                select_element = self.driver.find_element(By.XPATH,
                                                          "//div[@class='framer-pcceit-container']/form/div[4]/div[1]/select")
                select = Select(select_element)
                select_element.click()
                time.sleep(0.5)
                option_list = select.options

                for k in range(len(option_list)):
                    if find_us == "Online Search":
                        select.select_by_visible_text('Online Search')
                        break
                    elif find_us == "Social Media":
                        select.select_by_visible_text('Social Media')
                        break
                    elif find_us == "SRecommendation from a Friend or Colleague":
                        select.select_by_visible_text('Recommendation from a Friend or Colleague')
                        break
                    elif find_us == "Email Marketing":
                        select.select_by_visible_text('Email Marketing')
                        break
                    elif find_us == "Online Advertisement":
                        select.select_by_visible_text('Online Advertisement')
                        break
                    elif find_us == "Industry Event or Conference":
                        select.select_by_visible_text('Industry Event or Conference')
                        break
                    elif find_us == "Partner Referral":
                        select.select_by_visible_text('Partner Referral')
                        break
                    elif find_us == "Print Media":
                        select.select_by_visible_text('Print Media')
                        break
                    elif find_us == "Television or Radio":
                        select.select_by_visible_text('Television or Radio')
                        break

                time.sleep(0.5)

                # Enquiry Code

                self.de_click(self.interestedInDD)
                time.sleep(0.5)
                totalInterested = len(self.driver.find_elements(By.XPATH,
                                                                "//div[@class='framer-pcceit-container']/form/div[4]/div[2]"))
                Interested = []
                Interested = self.driver.find_elements(By.XPATH,
                                                       "//div[@class='framer-pcceit-container']/form/div[4]/div[2]")

                for l in range(totalInterested):

                    title = str(Interested[l].text)
                    # log.logger.info("" + str(title))
                    log.logger.info("" + str(title))
                    if interested == "iME Product Offering - Sales":
                        self.de_click(self.imeProduct)
                        self.de_click(self.interestedInDD)
                        break
                    elif interested == "Partnerships & Distribution":
                        self.de_click(self.imePartner)
                        self.de_click(self.interestedInDD)
                        break
                    elif interested == "General Enquiry":
                        self.de_click(self.generalEnquiry)
                        self.de_click(self.interestedInDD)
                        break
                    elif interested == "Existing iME customer or Applicant":
                        self.de_click(self.imeCustomer)
                        self.de_click(self.interestedInDD)
                        break
                    elif interested == "Other":
                        self.de_click(self.other)
                        self.de_click(self.interestedInDD)
                        break

                time.sleep(0.5)
                self.do_send_key(self.Message, message)
                time.sleep(0.5)
                # self.de_click(self.sendMessage)
                time.sleep(2)
                log.logger.info("****==Enquiry Has Been Sent Successfully==***")
