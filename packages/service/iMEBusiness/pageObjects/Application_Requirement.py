import os
import time
import logging
from selenium.webdriver.common.by import By
from iMEBusiness.Utilities.excelReader import excel_Data
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Application_Requirement_Create(BasePage):
    videoInterviewIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/button/div")

    templateProfileIcon = (
        By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/div/div/div[2]/button[1]")
    application_requirement_Icon = (By.XPATH, "//div[@class='flex flex-col grow mx-[24px] md:mx-[32px]']/div/button[3]")
    createQuestionSetButton = (By.XPATH,
                               "//div[@class='w-full flex flex-col lg:flex-row lg:items-center lg:justify-between rounded-[6px] mb-[16px]']/div[2]/button")

    serviceDD = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[1]/button")
    recruitmentService = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[1]/ul/li[1]")
    awardService = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[1]/ul/li[2]")
    marketingService = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[1]/ul/li[3]")
    learningService = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[1]/ul/li[4]")
    auditionService = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[1]/ul/li[5]")
    admissionService = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[1]/ul/li[6]")

    requireTypeDD = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[2]/button")
    booleanType = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[2]/ul/li[1]")
    emailType = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[2]/ul/li[2]")
    websiteType = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[2]/ul/li[3]")
    textType = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[2]/ul/li[4]")
    regionType = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[2]/ul/li[5]")
    mobileType = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[2]/ul/li[6]")
    listType = (
        By.XPATH, "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[2]/ul/li[7]")

    Requirement = (By.CSS_SELECTOR, "input[name='requirement']")

    saveButton = (By.XPATH, "//div[@class='flex flex-row-reverse w-full']/button")

    listInput = (By.XPATH,"//div[@class='mb-4 relative w-full w-full mt-[20px]']/button/div/input")

    closeButton = (By.XPATH,"//div[@class='flex min-h-full items-center justify-center p-4 text-center']/div/*[local-name()='svg']")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_template_icon(self):
        time.sleep(5)
        self.de_click(self.videoInterviewIcon)
        time.sleep(1)
        self.de_click(self.templateProfileIcon)
        time.sleep(4)

    def add_application_requirement(self):
        log.logger.info("****==Add a New Application Requirement for all services Test Case Starts Here==***")
        self.de_click(self.application_requirement_Icon)
        time.sleep(5)

        for i in range(6):
            self.de_click(self.createQuestionSetButton)
            time.sleep(1)
            self.de_click(self.serviceDD)
            time.sleep(1)

            serviceName = []
            serviceName = self.driver.find_elements(By.XPATH,
                                                    "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[1]/ul/li")
            re = str(serviceName[i].text)
            log.logger.info(" " + str(re))

            if re == "Recruitment":
                self.de_click(self.recruitmentService)
                time.sleep(0.5)
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/application_requirement_creation.xlsx')
                sheetName = 'Recruitment'

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
                        # log.logger.info("" + str(j))
                        cellData = excel_Data.getCellData(path, sheetName, j, k)
                        cellData1 = excel_Data.getCellData(path, sheetName, j, 2)
                        log.logger.info("Value Of Require Type == " + str(cellData))
                        log.logger.info("Value Of Requirement == " + str(cellData1))
                        time.sleep(0.5)
                        self.de_click(self.requireTypeDD)
                        time.sleep(0.5)
                        if cellData == "Boolean":
                            time.sleep(0.5)
                            self.de_click(self.booleanType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Email":
                            time.sleep(0.5)
                            self.de_click(self.emailType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Website":
                            time.sleep(0.5)
                            self.de_click(self.websiteType)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Text":
                            time.sleep(0.5)
                            self.de_click(self.textType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Region":
                            time.sleep(0.5)
                            self.de_click(self.regionType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Mobile":
                            time.sleep(0.5)
                            self.de_click(self.mobileType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "List":
                            time.sleep(0.5)
                            self.de_click(self.listType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.do_send_key(self.listInput, "one")
                            time.sleep(0.5)
                            self.de_click(self.Requirement)
                            time.sleep(0.5)
                            self.do_send_key(self.listInput, "two")
                            time.sleep(0.5)
                            self.de_click(self.Requirement)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        else:
                            time.sleep(0.5)
                            self.de_click(self.closeButton)

                        time.sleep(5)

                        if j < row:
                            self.de_click(self.createQuestionSetButton)
                            time.sleep(1)
                            self.de_click(self.serviceDD)
                            time.sleep(0.5)
                            self.de_click(self.recruitmentService)
                            time.sleep(0.5)
                        else:
                            break

            if re == "Awards":
                self.de_click(self.awardService)
                time.sleep(0.5)
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/application_requirement_creation.xlsx')
                sheetName = 'Awards'

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
                        # log.logger.info("" + str(j))
                        cellData = excel_Data.getCellData(path, sheetName, j, k)
                        cellData1 = excel_Data.getCellData(path, sheetName, j, 2)
                        log.logger.info("Value Of Require Type" + str(cellData))
                        log.logger.info("Value Of Requirement" + str(cellData1))
                        time.sleep(0.5)
                        self.de_click(self.requireTypeDD)
                        time.sleep(0.5)
                        if cellData == "Boolean":
                            time.sleep(0.5)
                            self.de_click(self.booleanType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Email":
                            time.sleep(0.5)
                            self.de_click(self.emailType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Website":
                            time.sleep(0.5)
                            self.de_click(self.websiteType)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Text":
                            time.sleep(0.5)
                            self.de_click(self.textType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Region":
                            time.sleep(0.5)
                            self.de_click(self.regionType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Mobile":
                            time.sleep(0.5)
                            self.de_click(self.mobileType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "List":
                            time.sleep(0.5)
                            self.de_click(self.listType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.do_send_key(self.listInput, "one")
                            time.sleep(0.5)
                            self.de_click(self.Requirement)
                            time.sleep(0.5)
                            self.do_send_key(self.listInput, "two")
                            time.sleep(0.5)
                            self.de_click(self.Requirement)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        else:
                            time.sleep(0.5)
                            self.de_click(self.closeButton)

                        time.sleep(5)

                        if j < row:
                            self.de_click(self.createQuestionSetButton)
                            time.sleep(1)
                            self.de_click(self.serviceDD)
                            time.sleep(0.5)
                            self.de_click(self.awardService)
                            time.sleep(0.5)
                        else:
                            break

            if re == "Marketing":
                self.de_click(self.marketingService)
                time.sleep(0.5)
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/application_requirement_creation.xlsx')
                sheetName = 'Marketing'

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
                        # log.logger.info("" + str(j))
                        cellData = excel_Data.getCellData(path, sheetName, j, k)
                        cellData1 = excel_Data.getCellData(path, sheetName, j, 2)
                        log.logger.info("Value Of Require Type" + str(cellData))
                        log.logger.info("Value Of Requirement" + str(cellData1))
                        time.sleep(0.5)
                        self.de_click(self.requireTypeDD)
                        time.sleep(0.5)
                        if cellData == "Boolean":
                            time.sleep(0.5)
                            self.de_click(self.booleanType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Email":
                            time.sleep(0.5)
                            self.de_click(self.emailType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Website":
                            time.sleep(0.5)
                            self.de_click(self.websiteType)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Text":
                            time.sleep(0.5)
                            self.de_click(self.textType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Region":
                            time.sleep(0.5)
                            self.de_click(self.regionType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Mobile":
                            time.sleep(0.5)
                            self.de_click(self.mobileType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "List":
                            time.sleep(0.5)
                            self.de_click(self.listType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.do_send_key(self.listInput, "one")
                            time.sleep(0.5)
                            self.de_click(self.Requirement)
                            time.sleep(0.5)
                            self.do_send_key(self.listInput, "two")
                            time.sleep(0.5)
                            self.de_click(self.Requirement)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        else:
                            time.sleep(0.5)
                            self.de_click(self.closeButton)

                        time.sleep(5)

                        if j < row:
                            self.de_click(self.createQuestionSetButton)
                            time.sleep(1)
                            self.de_click(self.serviceDD)
                            time.sleep(0.5)
                            self.de_click(self.marketingService)
                            time.sleep(0.5)
                        else:
                            break

            if re == "Learning":
                self.de_click(self.learningService)
                time.sleep(0.5)
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/application_requirement_creation.xlsx')
                sheetName = 'Learning'

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
                        # log.logger.info("" + str(j))
                        cellData = excel_Data.getCellData(path, sheetName, j, k)
                        cellData1 = excel_Data.getCellData(path, sheetName, j, 2)
                        log.logger.info("Value Of Require Type" + str(cellData))
                        log.logger.info("Value Of Requirement" + str(cellData1))
                        time.sleep(0.5)
                        self.de_click(self.requireTypeDD)
                        time.sleep(0.5)
                        if cellData == "Boolean":
                            time.sleep(0.5)
                            self.de_click(self.booleanType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Email":
                            time.sleep(0.5)
                            self.de_click(self.emailType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Website":
                            time.sleep(0.5)
                            self.de_click(self.websiteType)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Text":
                            time.sleep(0.5)
                            self.de_click(self.textType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Region":
                            time.sleep(0.5)
                            self.de_click(self.regionType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Mobile":
                            time.sleep(0.5)
                            self.de_click(self.mobileType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "List":
                            time.sleep(0.5)
                            self.de_click(self.listType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.do_send_key(self.listInput, "one")
                            time.sleep(0.5)
                            self.de_click(self.Requirement)
                            time.sleep(0.5)
                            self.do_send_key(self.listInput, "two")
                            time.sleep(0.5)
                            self.de_click(self.Requirement)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        else:
                            time.sleep(0.5)
                            self.de_click(self.closeButton)

                        time.sleep(5)

                        if j < row:
                            self.de_click(self.createQuestionSetButton)
                            time.sleep(1)
                            self.de_click(self.serviceDD)
                            time.sleep(0.5)
                            self.de_click(self.learningService)
                            time.sleep(0.5)
                        else:
                            break

            if re == "Auditions":
                self.de_click(self.auditionService)
                time.sleep(0.5)
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/application_requirement_creation.xlsx')
                sheetName = 'Auditions'

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
                        # log.logger.info("" + str(j))
                        cellData = excel_Data.getCellData(path, sheetName, j, k)
                        cellData1 = excel_Data.getCellData(path, sheetName, j, 2)
                        log.logger.info("Value Of Require Type" + str(cellData))
                        log.logger.info("Value Of Requirement" + str(cellData1))
                        time.sleep(0.5)
                        self.de_click(self.requireTypeDD)
                        time.sleep(0.5)
                        if cellData == "Boolean":
                            time.sleep(0.5)
                            self.de_click(self.booleanType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Email":
                            time.sleep(0.5)
                            self.de_click(self.emailType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Website":
                            time.sleep(0.5)
                            self.de_click(self.websiteType)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Text":
                            time.sleep(0.5)
                            self.de_click(self.textType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Region":
                            time.sleep(0.5)
                            self.de_click(self.regionType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Mobile":
                            time.sleep(0.5)
                            self.de_click(self.mobileType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "List":
                            time.sleep(0.5)
                            self.de_click(self.listType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.do_send_key(self.listInput, "one")
                            time.sleep(0.5)
                            self.de_click(self.Requirement)
                            time.sleep(0.5)
                            self.do_send_key(self.listInput, "two")
                            time.sleep(0.5)
                            self.de_click(self.Requirement)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        else:
                            time.sleep(0.5)
                            self.de_click(self.closeButton)

                        time.sleep(5)

                        if j < row:
                            self.de_click(self.createQuestionSetButton)
                            time.sleep(1)
                            self.de_click(self.serviceDD)
                            time.sleep(0.5)
                            self.de_click(self.auditionService)
                            time.sleep(0.5)
                        else:
                            break

            if re == "Admissions":
                self.de_click(self.admissionService)
                time.sleep(0.5)
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/application_requirement_creation.xlsx')
                sheetName = 'Admissions'

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
                        # log.logger.info("" + str(j))
                        cellData = excel_Data.getCellData(path, sheetName, j, k)
                        cellData1 = excel_Data.getCellData(path, sheetName, j, 2)
                        log.logger.info("Value Of Require Type" + str(cellData))
                        log.logger.info("Value Of Requirement" + str(cellData1))
                        time.sleep(0.5)
                        self.de_click(self.requireTypeDD)
                        time.sleep(0.5)
                        if cellData == "Boolean":
                            time.sleep(0.5)
                            self.de_click(self.booleanType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Email":
                            time.sleep(0.5)
                            self.de_click(self.emailType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Website":
                            time.sleep(0.5)
                            self.de_click(self.websiteType)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Text":
                            time.sleep(0.5)
                            self.de_click(self.textType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Region":
                            time.sleep(0.5)
                            self.de_click(self.regionType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "Mobile":
                            time.sleep(0.5)
                            self.de_click(self.mobileType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        elif cellData == "List":
                            time.sleep(0.5)
                            self.de_click(self.listType)
                            time.sleep(0.5)
                            self.do_send_key(self.Requirement, cellData1)
                            time.sleep(0.5)
                            self.do_send_key(self.listInput, "one")
                            time.sleep(0.5)
                            self.de_click(self.Requirement)
                            time.sleep(0.5)
                            self.do_send_key(self.listInput, "two")
                            time.sleep(0.5)
                            self.de_click(self.Requirement)
                            time.sleep(0.5)
                            self.de_click(self.saveButton)
                        else:
                            time.sleep(0.5)
                            self.de_click(self.closeButton)

                        time.sleep(5)

                        if j < row:
                            self.de_click(self.createQuestionSetButton)
                            time.sleep(1)
                            self.de_click(self.serviceDD)
                            time.sleep(0.5)
                            self.de_click(self.admissionService)
                            time.sleep(0.5)
                        else:
                            break






