import time
from selenium.webdriver.common.by import By
import logging
import os
from iMEBusiness.Utilities.excelReader import excel_Data
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Template_Create(BasePage):
    videoInterviewIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/button/div")

    templateProfileIcon = (
        By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/div/div/div[2]/button[1]")
    minimumRequirementIcon = (By.XPATH, "//div[@class='flex flex-col grow mx-[24px] md:mx-[32px]']/div/button[2]")
    questionSetIcon = (By.XPATH, "//div[@class='flex flex-col grow mx-[24px] md:mx-[32px]']/div/button[3]")
    multimediaSetIcon = (By.XPATH, "//div[@class='flex flex-col grow mx-[24px] md:mx-[32px]']/div/button[4]")
    addButton = (By.XPATH,
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

    questionInput = (By.CSS_SELECTOR, "input[name='question']")
    yesRadioOption = (By.XPATH, "//div[@class='mb-4 relative flex w-full flex-col mt-[16px]']/div/div[1]/div")
    noRadioOption = (By.XPATH,"//div[@class='mb-4 relative flex w-full flex-col mt-[16px]']/div/div[3]/div")
    saveQuestion = (By.XPATH, "//div[@class='flex flex-row-reverse w-full']/button")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_template_icon(self):
        time.sleep(5)
        self.de_click(self.videoInterviewIcon)
        time.sleep(1)
        self.de_click(self.templateProfileIcon)
        time.sleep(4)

    def add_minimum_requirement(self):

        log.logger.info("****==Add a New Minimum Requirement Question for all services Test Case Starts Here==***")
        self.de_click(self.minimumRequirementIcon)
        time.sleep(4)
        for i in range(6):
            self.de_click(self.addButton)
            time.sleep(1)
            self.de_click(self.serviceDD)
            time.sleep(0.5)

            serviceName = []
            serviceName = self.driver.find_elements(By.XPATH,
                                                    "//form[@class='w-full flex flex-col flex-wrap lg:justify-center lg:items-center']/div[1]/ul/li")
            re = str(serviceName[i].text)
            log.logger.info(" " + str(re))

            if re == "Recruitment":
                self.de_click(self.recruitmentService)
                time.sleep(0.5)

                log.logger.info("Current working directory:" + str(os.getcwd()))
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/template_creation.xlsx')
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
                    for k in range(1, col + 1, 3):
                        cellData = excel_Data.getCellData(path, sheetName, j, k)
                        cellData1 = excel_Data.getCellData(path, sheetName, j, 2)
                        time.sleep(0.5)
                        log.logger.info("" + str(cellData))
                        log.logger.info("" + str(cellData1))
                        self.do_send_key(self.questionInput, cellData)
                        time.sleep(0.5)
                        if cellData1 == "Yes":
                            self.de_click(self.yesRadioOption)
                            time.sleep(0.5)
                            self.de_click(self.saveQuestion)
                            time.sleep(3.5)
                            log.logger.info("value of j" + str(j))
                            log.logger.info("value of row" + str(row))
                        else:
                            self.de_click(self.noRadioOption)
                            time.sleep(0.5)
                            self.de_click(self.saveQuestion)
                            time.sleep(3.5)
                            log.logger.info("value of j" + str(j))
                            log.logger.info("value of row" + str(row))

                        if j < row:
                            self.de_click(self.addButton)
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

                log.logger.info("Current working directory:" + str(os.getcwd()))
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/template_creation.xlsx')
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
                    for k in range(1, col + 1, 3):
                        cellData = excel_Data.getCellData(path, sheetName, j, k)
                        cellData1 = excel_Data.getCellData(path, sheetName, j, 2)
                        time.sleep(0.5)
                        log.logger.info("" + str(cellData))
                        log.logger.info("" + str(cellData1))
                        self.do_send_key(self.questionInput, cellData)
                        time.sleep(0.5)
                        if cellData1 == "Yes":
                            self.de_click(self.yesRadioOption)
                            time.sleep(0.5)
                            self.de_click(self.saveQuestion)
                            time.sleep(3.5)
                            log.logger.info("value of j" + str(j))
                            log.logger.info("value of row" + str(row))
                        else:
                            self.de_click(self.noRadioOption)
                            time.sleep(0.5)
                            self.de_click(self.saveQuestion)
                            time.sleep(3.5)
                            log.logger.info("value of j" + str(j))
                            log.logger.info("value of row" + str(row))

                        if j < row:
                            self.de_click(self.addButton)
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

                log.logger.info("Current working directory:" + str(os.getcwd()))
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/template_creation.xlsx')
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
                    for k in range(1, col + 1, 3):
                        cellData = excel_Data.getCellData(path, sheetName, j, k)
                        cellData1 = excel_Data.getCellData(path, sheetName, j, 2)
                        time.sleep(0.5)
                        log.logger.info("" + str(cellData))
                        log.logger.info("" + str(cellData1))
                        self.do_send_key(self.questionInput, cellData)
                        time.sleep(0.5)
                        if cellData1 == "Yes":
                            self.de_click(self.yesRadioOption)
                            time.sleep(0.5)
                            self.de_click(self.saveQuestion)
                            time.sleep(3.5)
                            log.logger.info("value of j" + str(j))
                            log.logger.info("value of row" + str(row))
                        else:
                            self.de_click(self.noRadioOption)
                            time.sleep(0.5)
                            self.de_click(self.saveQuestion)
                            time.sleep(3.5)
                            log.logger.info("value of j" + str(j))
                            log.logger.info("value of row" + str(row))

                        if j < row:
                            self.de_click(self.addButton)
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

                log.logger.info("Current working directory:" + str(os.getcwd()))
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/template_creation.xlsx')
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
                    for k in range(1, col + 1, 3):
                        cellData = excel_Data.getCellData(path, sheetName, j, k)
                        cellData1 = excel_Data.getCellData(path, sheetName, j, 2)
                        time.sleep(0.5)
                        log.logger.info("" + str(cellData))
                        log.logger.info("" + str(cellData1))
                        self.do_send_key(self.questionInput, cellData)
                        time.sleep(0.5)
                        if cellData1 == "Yes":
                            self.de_click(self.yesRadioOption)
                            time.sleep(0.5)
                            self.de_click(self.saveQuestion)
                            time.sleep(3.5)
                            log.logger.info("value of j" + str(j))
                            log.logger.info("value of row" + str(row))
                        else:
                            self.de_click(self.noRadioOption)
                            time.sleep(0.5)
                            self.de_click(self.saveQuestion)
                            time.sleep(3.5)
                            log.logger.info("value of j" + str(j))
                            log.logger.info("value of row" + str(row))

                        if j < row:
                            self.de_click(self.addButton)
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
                log.logger.info("Current working directory:" + str(os.getcwd()))
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/template_creation.xlsx')
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
                    for k in range(1, col + 1, 3):
                        cellData = excel_Data.getCellData(path, sheetName, j, k)
                        cellData1 = excel_Data.getCellData(path, sheetName, j, 2)
                        time.sleep(0.5)
                        log.logger.info("" + str(cellData))
                        log.logger.info("" + str(cellData1))
                        self.do_send_key(self.questionInput, cellData)
                        time.sleep(0.5)
                        if cellData1 == "Yes":
                            self.de_click(self.yesRadioOption)
                            time.sleep(0.5)
                            self.de_click(self.saveQuestion)
                            time.sleep(3.5)
                            log.logger.info("value of j" + str(j))
                            log.logger.info("value of row" + str(row))
                        else:
                            self.de_click(self.noRadioOption)
                            time.sleep(0.5)
                            self.de_click(self.saveQuestion)
                            time.sleep(3.5)
                            log.logger.info("value of j" + str(j))
                            log.logger.info("value of row" + str(row))

                        if j < row:
                            self.de_click(self.addButton)
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
                log.logger.info("Current working directory:" + str(os.getcwd()))
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/template_creation.xlsx')
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
                    for k in range(1, col + 1, 3):
                        cellData = excel_Data.getCellData(path, sheetName, j, k)
                        cellData1 = excel_Data.getCellData(path, sheetName, j, 2)
                        time.sleep(0.5)
                        log.logger.info("" + str(cellData))
                        log.logger.info("" + str(cellData1))
                        self.do_send_key(self.questionInput, cellData)
                        time.sleep(0.5)
                        if cellData1 == "Yes":
                            self.de_click(self.yesRadioOption)
                            time.sleep(0.5)
                            self.de_click(self.saveQuestion)
                            time.sleep(3.5)
                            log.logger.info("value of j" + str(j))
                            log.logger.info("value of row" + str(row))
                        else:
                            self.de_click(self.noRadioOption)
                            time.sleep(0.5)
                            self.de_click(self.saveQuestion)
                            time.sleep(3.5)
                            log.logger.info("value of j" + str(j))
                            log.logger.info("value of row" + str(row))

                        if j < row:
                            self.de_click(self.addButton)
                            time.sleep(1)
                            self.de_click(self.serviceDD)
                            time.sleep(0.5)
                            self.de_click(self.admissionService)
                            time.sleep(0.5)
                        else:
                            break
