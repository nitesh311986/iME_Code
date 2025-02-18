import time
import pytest
from selenium.webdriver.common.by import By
import logging
import os
from iMEBusiness.Utilities.excelReader import excel_Data
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Multimedia_Create(BasePage):
    videoInterviewIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/button/div")

    templateProfileIcon = (
    By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/div/div/div[2]/button[1]")
    multimediaIcon = (By.XPATH, "//div[@class='flex flex-col grow mx-[24px] md:mx-[32px]']/div/button[5]")
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
    documentRadioOption = (By.XPATH, "//div[@class='mb-4 relative flex w-full flex-col mt-4']/div/div[1]/div[1]")
    videoRadioOption = (By.XPATH, "//div[@class='mb-4 relative flex w-full flex-col mt-4']/div/div[2]/div[1]")
    imageRadioOption = (By.XPATH, "//div[@class='mb-4 relative flex w-full flex-col mt-4']/div/div[3]/div[1]")
    saveQuestion = (By.XPATH, "//div[@class='flex flex-row-reverse w-full']/button")

    def __init__(self, driver, environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_template_icon(self):
        time.sleep(5)
        self.de_click(self.videoInterviewIcon)
        time.sleep(1)
        self.de_click(self.templateProfileIcon)
        time.sleep(4)

    def add_multimedia(self):

        log.logger.info("****==Add a New Multimedia Requirement  for all services Test Case Starts Here==***")
        self.de_click(self.multimediaIcon)
        time.sleep(5)
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
                relative_path = os.path.join(base_dir, '../excel/multimedia_creation.xlsx')
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
                        self.upload_document(cellData1, j, row)
                        # if cellData1 == "Document":
                        #     self.de_click(self.documentRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j == " + str(j))
                        #     log.logger.info("value of row == " + str(row))
                        # elif cellData1 == "Video":
                        #     self.de_click(self.videoRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))
                        # else:
                        #     self.de_click(self.imageRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))

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
                relative_path = os.path.join(base_dir, '../excel/multimedia_creation.xlsx')
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
                        self.upload_document(cellData1, j, row)
                        # if cellData1 == "Document":
                        #     self.de_click(self.documentRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))
                        # elif cellData1 == "Video":
                        #     self.de_click(self.videoRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))
                        # else:
                        #     self.de_click(self.imageRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))

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
                relative_path = os.path.join(base_dir, '../excel/multimedia_creation.xlsx')
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
                        self.upload_document(cellData1, j, row)
                        # if cellData1 == "Document":
                        #     self.de_click(self.documentRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))
                        # elif cellData1 == "Video":
                        #     self.de_click(self.videoRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))
                        # else:
                        #     self.de_click(self.imageRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))

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
                relative_path = os.path.join(base_dir, '../excel/multimedia_creation.xlsx')
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
                        self.upload_document(cellData1, j, row)
                        # if cellData1 == "Document":
                        #     self.de_click(self.documentRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))
                        # elif cellData1 == "Video":
                        #     self.de_click(self.videoRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))
                        # else:
                        #     self.de_click(self.imageRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))

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
                relative_path = os.path.join(base_dir, '../excel/multimedia_creation.xlsx')
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
                        self.upload_document(cellData1, j, row)
                        # if cellData1 == "Document":
                        #     self.de_click(self.documentRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))
                        # elif cellData1 == "Video":
                        #     self.de_click(self.videoRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))
                        # else:
                        #     self.de_click(self.imageRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))

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
                relative_path = os.path.join(base_dir, '../excel/multimedia_creation.xlsx')
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
                        self.upload_document(cellData1, j, row)
                        # if cellData1 == "Document":
                        #     self.de_click(self.documentRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))
                        # elif cellData1 == "Video":
                        #     self.de_click(self.videoRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))
                        # else:
                        #     self.de_click(self.imageRadioOption)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveQuestion)
                        #     time.sleep(3.5)
                        #     log.logger.info("value of j" + str(j))
                        #     log.logger.info("value of row" + str(row))
                        if j < row:
                            self.de_click(self.addButton)
                            time.sleep(1)
                            self.de_click(self.serviceDD)
                            time.sleep(0.5)
                            self.de_click(self.admissionService)
                            time.sleep(0.5)
                        else:
                            break

    def upload_document(self, cellData1, j, row):
        if cellData1 == "Document":
            self.de_click(self.documentRadioOption)
            time.sleep(1)
            self.upload(cellData1)
            time.sleep(2)
            self.de_click(self.saveQuestion)
            time.sleep(20)
            log.logger.info("value of j == " + str(j))
            log.logger.info("value of row == " + str(row))
            return
        elif cellData1 == "Video":
            self.de_click(self.videoRadioOption)
            time.sleep(1)
            self.upload(cellData1)
            time.sleep(2)
            self.de_click(self.saveQuestion)
            time.sleep(20)
            log.logger.info("value of j" + str(j))
            log.logger.info("value of row" + str(row))
            return
        elif cellData1 == "Image":
            self.de_click(self.imageRadioOption)
            time.sleep(1)
            self.upload(cellData1)
            time.sleep(2)
            self.de_click(self.saveQuestion)
            time.sleep(20)
            log.logger.info("value of j" + str(j))
            log.logger.info("value of row" + str(row))
            return
        else:
            log.logger.info("Nothing")



    def upload(self,cellData1):
        relative_path= ""
        time.sleep(1)
        base_dir = os.path.dirname(__file__)
        # Find the file input element
        file_input = self.driver.find_element(By.XPATH,
                                              "//div[@class='flex flex-col w-full items-center justify-center  items-center']/input")

        if cellData1 == "Document":
            relative_path = os.path.join(base_dir, '../video/prfl.jpeg')
        elif cellData1 == "Video":
            relative_path = os.path.join(base_dir, '../video/one.mp4')
        elif cellData1 =="Image":
            relative_path = os.path.join(base_dir, '../video/prfl.jpeg')
        else:
            relative_path = os.path.join(base_dir, '../video/prfl.jpeg')


        # Replace with the path to the video file you want to upload
        #relative_path = os.path.join(base_dir, '../video/one.mp4')
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
