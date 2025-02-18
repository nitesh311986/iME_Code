import time
from selenium.webdriver.common.by import By
import logging
import os
from iMEBusiness.Utilities.excelReader import excel_Data
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Question_Set_Create(BasePage):
    videoInterviewIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/button/div")

    templateProfileIcon = (
    By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/div/div/div[2]/button[1]")
    questionSetIcon = (By.XPATH, "//div[@class='flex flex-col grow mx-[24px] md:mx-[32px]']/div/button[4]")
    createQuestionSetButton = (By.XPATH,
                               "//div[@class='w-full flex flex-col lg:flex-row lg:items-center lg:justify-between rounded-[6px] mb-[16px]']/button")
    questionSetTitle = (By.CSS_SELECTOR, "input[name='templateTitle']")
    serviceDD = (By.XPATH, "//div[@class='flex flex-col md:flex-row justify-between']/div[2]/button")
    recruitmentService = (By.XPATH, "//div[@class='flex flex-col md:flex-row justify-between']/div[2]/ul/li[1]")
    awardService = (By.XPATH, "//div[@class='flex flex-col md:flex-row justify-between']/div[2]/ul/li[2]")
    marketingService = (By.XPATH, "//div[@class='flex flex-col md:flex-row justify-between']/div[2]/ul/li[3]")
    learningService = (By.XPATH, "//div[@class='flex flex-col md:flex-row justify-between']/div[2]/ul/li[4]")
    auditionService = (By.XPATH, "//div[@class='flex flex-col md:flex-row justify-between']/div[2]/ul/li[5]")
    admissionService = (By.XPATH, "//div[@class='flex flex-col md:flex-row justify-between']/div[2]/ul/li[6]")
    addTextButton = (By.XPATH, "//div[@class='flex flex-row justify-center w-full']/button")
    firstQuestion = (By.CSS_SELECTOR, "input[name='questions.0.questionTitle']")
    firstThinkTime = (By.CSS_SELECTOR, "input[name='questions.0.thinkTimeInSeconds']")
    firstAnswerTime = (By.CSS_SELECTOR, "input[name='questions.0.answerTimeInSeconds']")
    secondQuestion = (By.CSS_SELECTOR, "input[name='questions.1.questionTitle']")
    secondThinkTime = (By.CSS_SELECTOR, "input[name='questions.1.thinkTimeInSeconds']")
    secondAnswerTime = (By.CSS_SELECTOR, "input[name='questions.1.answerTimeInSeconds']")
    thirdQuestion = (By.CSS_SELECTOR, "input[name='questions.2.questionTitle']")
    thirdThinkTime = (By.CSS_SELECTOR, "input[name='questions.2.thinkTimeInSeconds']")
    thirdAnswerTime = (By.CSS_SELECTOR, "input[name='questions.2.answerTimeInSeconds']")
    retakeOption = (By.CSS_SELECTOR, "input[name='questions.2.numberOfRetakes']")
    saveButton = (By.XPATH, "//div[@class='w-full md:max-w-[700px] flex flex-row justify-end mb-[12px]']/button[2]")
    questionInList = (By.XPATH, "//div[@class='hidden lg:flex h-screen']/div/div[2]/div[1]/h5")
    searchInput = (By.XPATH,"//div[@class='hidden lg:flex h-screen']/div/div[1]/div[2]/div/input")
    closeButton = (By.XPATH, "//div[@class='hidden lg:flex h-screen']/div/div[1]/div[2]/div/div[2]")


    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_template_icon(self):
        time.sleep(5)
        self.de_click(self.videoInterviewIcon)
        time.sleep(1)
        self.de_click(self.templateProfileIcon)
        time.sleep(4)

    def add_question_set(self):
        log.logger.info("****==Add a New Question Set using text questions for all services Test Case Starts Here==***")
        self.de_click(self.questionSetIcon)
        time.sleep(5)

        for i in range(6):
            self.de_click(self.
                          createQuestionSetButton)
            time.sleep(1)
            self.de_click(self.serviceDD)
            time.sleep(0.5)

            serviceName = []
            serviceName = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='flex flex-col md:flex-row justify-between']/div[2]/ul/li")
            re = str(serviceName[i].text)
            log.logger.info(" " + str(re))

            if re == "Recruitment":
                self.de_click(self.recruitmentService)
                time.sleep(0.5)
                log.logger.info("Current working directory:" + str(os.getcwd()))
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/question_set_creation.xlsx')
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
                    for k in range(1, col + 1, 5):
                        question = excel_Data.getCellData(path, sheetName, j, k)
                        designation = excel_Data.getCellData(path, sheetName, j, 2)
                        thinkTime = excel_Data.getCellData(path, sheetName, j, 3)
                        answerTime = excel_Data.getCellData(path, sheetName, j, 4)
                        time.sleep(0.5)
                        log.logger.info("" + str(designation))
                        log.logger.info("" + str(question))
                        if j == 2 and designation == "Technician":
                            self.do_send_key(self.questionSetTitle, designation)
                            time.sleep(0.5)
                            self.de_click(self.addTextButton)
                            time.sleep(0.5)
                            self.do_send_key(self.firstQuestion, question)
                            time.sleep(0.5)
                            self.do_send_key(self.firstThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.firstAnswerTime, answerTime)
                        elif j == 3 and designation == "Technician":
                            time.sleep(0.5)
                            self.de_click(self.addTextButton)
                            time.sleep(0.5)
                            self.do_send_key(self.secondQuestion, question)
                            time.sleep(0.5)
                            self.do_send_key(self.secondThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.secondAnswerTime, answerTime)
                        # elif j == 4 and designation == "Technician":
                        #     time.sleep(0.5)
                        #     self.de_click(self.addTextButton)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdQuestion, question)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdThinkTime, thinkTime)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdAnswerTime, answerTime)
                        #     time.sleep(1)
                            saveButton = self.driver.find_element(By.XPATH,
                                                                  "//div[@class='w-full md:max-w-[700px] flex flex-row justify-end mb-[12px]']/button[2]")
                            self.de_action_method(saveButton)
                            time.sleep(8)

                        # elif j == 5 and designation == "SDET":
                        #     self.driver.implicitly_wait(10)
                        #     self.de_click(self.createQuestionSetButton)
                        #     time.sleep(1.5)
                        #     self.de_click(self.serviceDD)
                        #     time.sleep(0.5)
                        #     self.de_click(self.recruitmentService)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.questionSetTitle, designation)
                        #     time.sleep(0.5)
                        #     self.de_click(self.addTextButton)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.firstQuestion, question)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.firstThinkTime, thinkTime)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.firstAnswerTime, answerTime)
                        #
                        # elif j == 6 and designation == "SDET":
                        #     time.sleep(0.5)
                        #     self.de_click(self.addTextButton)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.secondQuestion, question)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.secondThinkTime, thinkTime)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.secondAnswerTime, answerTime)
                        #     time.sleep(0.5)
                        #     self.de_click(self.saveButton)
                        #     time.sleep(3)

            if re == "Awards":
                question = self.get_element_text_question_set(self.questionInList)
                time.sleep(0.5)
                log.logger.info("question Need to appear to solve synchronisation problem " + str(question))
                self.de_click(self.awardService)
                time.sleep(0.5)
                log.logger.info("Current working directory:" + str(os.getcwd()))
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/question_set_creation.xlsx')
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
                    for k in range(1, col + 1, 5):
                        question = excel_Data.getCellData(path, sheetName, j, k)
                        designation = excel_Data.getCellData(path, sheetName, j, 2)
                        thinkTime = excel_Data.getCellData(path, sheetName, j, 3)
                        answerTime = excel_Data.getCellData(path, sheetName, j, 4)
                        time.sleep(0.5)
                        log.logger.info("" + str(designation))
                        log.logger.info("" + str(question))
                        if j == 2 and designation == "Award distributor":
                            self.do_send_key(self.questionSetTitle, designation)
                            time.sleep(0.5)
                            self.de_click(self.addTextButton)
                            time.sleep(0.5)
                            self.do_send_key(self.firstQuestion, question)
                            time.sleep(0.5)
                            self.do_send_key(self.firstThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.firstAnswerTime, answerTime)
                        elif j == 3 and designation == "Award distributor":
                            time.sleep(0.5)
                            self.de_click(self.addTextButton)
                            time.sleep(0.5)
                            self.do_send_key(self.secondQuestion, question)
                            time.sleep(0.5)
                            self.do_send_key(self.secondThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.secondAnswerTime, answerTime)
                        # elif j == 4 and designation == "Award distributor":
                        #     time.sleep(0.5)
                        #     self.de_click(self.addTextButton)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdQuestion, question)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdThinkTime, thinkTime)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdAnswerTime, answerTime)
                        #     time.sleep(1)
                            saveButton = self.driver.find_element(By.XPATH,
                                                                  "//div[@class='w-full md:max-w-[700px] flex flex-row justify-end mb-[12px]']/button[2]")
                            self.de_action_method(saveButton)
                            time.sleep(8)

            if re == "Marketing":
                question = self.get_element_text_question_set(self.questionInList)
                time.sleep(0.5)
                log.logger.info("question Need to appear to solve synchronisation problem " + str(question))
                self.de_click(self.marketingService)
                time.sleep(0.5)

                log.logger.info("Current working directory:" + str(os.getcwd()))
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/question_set_creation.xlsx')
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
                    for k in range(1, col + 1, 5):
                        question = excel_Data.getCellData(path, sheetName, j, k)
                        designation = excel_Data.getCellData(path, sheetName, j, 2)
                        thinkTime = excel_Data.getCellData(path, sheetName, j, 3)
                        answerTime = excel_Data.getCellData(path, sheetName, j, 4)
                        time.sleep(0.5)
                        log.logger.info("" + str(designation))
                        log.logger.info("" + str(question))
                        if j == 2 and designation == "Retail Manager":
                            self.do_send_key(self.questionSetTitle, designation)
                            time.sleep(0.5)
                            self.de_click(self.addTextButton)
                            time.sleep(0.5)
                            self.do_send_key(self.firstQuestion, question)
                            time.sleep(0.5)
                            self.do_send_key(self.firstThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.firstAnswerTime, answerTime)
                        elif j == 3 and designation == "Retail Manager":
                            time.sleep(0.5)
                            self.de_click(self.addTextButton)
                            time.sleep(0.5)
                            self.do_send_key(self.secondQuestion, question)
                            time.sleep(0.5)
                            self.do_send_key(self.secondThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.secondAnswerTime, answerTime)
                        # elif j == 4 and designation == "Retail Manager":
                        #     time.sleep(0.5)
                        #     self.de_click(self.addTextButton)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdQuestion, question)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdThinkTime, thinkTime)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdAnswerTime, answerTime)
                        #     time.sleep(1)
                            saveButton = self.driver.find_element(By.XPATH,
                                                                  "//div[@class='w-full md:max-w-[700px] flex flex-row justify-end mb-[12px]']/button[2]")
                            self.de_action_method(saveButton)

                            time.sleep(8)

            if re == "Learning":
                question = self.get_element_text_question_set(self.questionInList)
                time.sleep(0.5)
                log.logger.info("question Need to appear to solve synchronisation problem " + str(question))
                self.de_click(self.learningService)
                time.sleep(0.5)

                log.logger.info("Current working directory:" + str(os.getcwd()))
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/question_set_creation.xlsx')
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
                    for k in range(1, col + 1, 5):
                        question = excel_Data.getCellData(path, sheetName, j, k)
                        designation = excel_Data.getCellData(path, sheetName, j, 2)
                        thinkTime = excel_Data.getCellData(path, sheetName, j, 3)
                        answerTime = excel_Data.getCellData(path, sheetName, j, 4)
                        time.sleep(0.5)
                        log.logger.info("" + str(designation))
                        log.logger.info("" + str(question))
                        if j == 2 and designation == "Asst Professor":
                            self.do_send_key(self.questionSetTitle, designation)
                            time.sleep(0.5)
                            self.de_click(self.addTextButton)
                            time.sleep(0.5)
                            self.do_send_key(self.firstQuestion, question)
                            time.sleep(0.5)
                            self.do_send_key(self.firstThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.firstAnswerTime, answerTime)
                        elif j == 3 and designation == "Asst Professor":
                            time.sleep(0.5)
                            self.de_click(self.addTextButton)
                            time.sleep(0.5)
                            self.do_send_key(self.secondQuestion, question)
                            time.sleep(0.5)
                            self.do_send_key(self.secondThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.secondAnswerTime, answerTime)
                        # elif j == 4 and designation == "Asst Professor":
                        #     time.sleep(0.5)
                        #     self.de_click(self.addTextButton)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdQuestion, question)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdThinkTime, thinkTime)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdAnswerTime, answerTime)
                        #     time.sleep(1)
                            saveButton = self.driver.find_element(By.XPATH,
                                                                  "//div[@class='w-full md:max-w-[700px] flex flex-row justify-end mb-[12px]']/button[2]")
                            self.de_action_method(saveButton)

                            time.sleep(8)

            if re == "Auditions":
                question = self.get_element_text_question_set(self.questionInList)
                time.sleep(0.5)
                log.logger.info("question Need to appear to solve synchronisation problem " + str(question))
                self.de_click(self.auditionService)
                time.sleep(0.5)

                log.logger.info("Current working directory:" + str(os.getcwd()))
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/question_set_creation.xlsx')
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
                    for k in range(1, col + 1, 5):
                        question = excel_Data.getCellData(path, sheetName, j, k)
                        designation = excel_Data.getCellData(path, sheetName, j, 2)
                        thinkTime = excel_Data.getCellData(path, sheetName, j, 3)
                        answerTime = excel_Data.getCellData(path, sheetName, j, 4)
                        time.sleep(0.5)
                        log.logger.info("" + str(designation))
                        log.logger.info("" + str(question))
                        if j == 2 and designation == "Action Director":
                            self.do_send_key(self.questionSetTitle, designation)
                            time.sleep(0.5)
                            self.de_click(self.addTextButton)
                            time.sleep(0.5)
                            self.do_send_key(self.firstQuestion, question)
                            time.sleep(0.5)
                            self.do_send_key(self.firstThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.firstAnswerTime, answerTime)
                        elif j == 3 and designation == "Action Director":
                            time.sleep(0.5)
                            self.de_click(self.addTextButton)
                            time.sleep(0.5)
                            self.do_send_key(self.secondQuestion, question)
                            time.sleep(0.5)
                            self.do_send_key(self.secondThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.secondAnswerTime, answerTime)
                        # elif j == 4 and designation == "Action Director":
                        #     time.sleep(0.5)
                        #     self.de_click(self.addTextButton)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdQuestion, question)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdThinkTime, thinkTime)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdAnswerTime, answerTime)
                        #     time.sleep(1)
                            saveButton = self.driver.find_element(By.XPATH,
                                                                  "//div[@class='w-full md:max-w-[700px] flex flex-row justify-end mb-[12px]']/button[2]")
                            self.de_action_method(saveButton)

                            time.sleep(8)

            if re == "Admissions":
                question = self.get_element_text_question_set(self.questionInList)
                time.sleep(0.5)
                log.logger.info("question Need to appear to solve synchronisation problem " + str(question))
                self.de_click(self.admissionService)
                time.sleep(0.5)


                log.logger.info("question Need to appear to solve synchronisation problem " + str(question))
                self.de_click(self.auditionService)
                time.sleep(0.5)

                log.logger.info("Current working directory:" + str(os.getcwd()))
                base_dir = os.path.dirname(__file__)

                # Define the relative path to the Pricing.xlsx file
                relative_path = os.path.join(base_dir, '../excel/question_set_creation.xlsx')
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
                    for k in range(1, col + 1, 5):
                        question = excel_Data.getCellData(path, sheetName, j, k)
                        designation = excel_Data.getCellData(path, sheetName, j, 2)
                        thinkTime = excel_Data.getCellData(path, sheetName, j, 3)
                        answerTime = excel_Data.getCellData(path, sheetName, j, 4)
                        time.sleep(0.5)
                        log.logger.info("" + str(designation))
                        log.logger.info("" + str(question))
                        if j == 2 and designation == "Admission Coordinator":
                            self.do_send_key(self.questionSetTitle, designation)
                            time.sleep(0.5)
                            self.de_click(self.addTextButton)
                            time.sleep(0.5)
                            self.do_send_key(self.firstQuestion, question)
                            time.sleep(0.5)
                            self.do_send_key(self.firstThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.firstAnswerTime, answerTime)
                        elif j == 3 and designation == "Admission Coordinator":
                            time.sleep(0.5)
                            self.de_click(self.addTextButton)
                            time.sleep(0.5)
                            self.do_send_key(self.secondQuestion, question)
                            time.sleep(0.5)
                            self.do_send_key(self.secondThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.secondAnswerTime, answerTime)
                        # elif j == 4 and designation == "Admission Coordinator":
                        #     time.sleep(0.5)
                        #     self.de_click(self.addTextButton)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdQuestion, question)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdThinkTime, thinkTime)
                        #     time.sleep(0.5)
                        #     self.do_send_key(self.thirdAnswerTime, answerTime)
                        #     time.sleep(1)
                            saveButton = self.driver.find_element(By.XPATH,
                                                                  "//div[@class='w-full md:max-w-[700px] flex flex-row justify-end mb-[12px]']/button[2]")
                            self.de_action_method(saveButton)

                            time.sleep(8)

    def add_question_from_list(self):
        log.logger.info("****==Add a New Question Set using text questions for all services from available questions on system Test Case Starts Here==***")
        self.de_click(self.questionSetIcon)
        time.sleep(4)

        for i in range(6):
            self.de_click(self.createQuestionSetButton)
            time.sleep(1)
            self.de_click(self.serviceDD)
            time.sleep(0.5)

            serviceName = []
            serviceName = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='flex flex-col md:flex-row justify-between']/div[2]/ul/li")
            re = str(serviceName[i].text)
            log.logger.info(" " + str(re))

            # if re == "Recruitment":
            #     self.de_click(self.recruitmentService)
            #     time.sleep(0.5)
            #     path = ".\\excel\\question_set_creation.xlsx"
            #     sheetName = 'Recruitment_List'
            #     row = excel_Data.getRowCount(path, sheetName)
            #     log.logger.info("" + str(row))
            #     col = excel_Data.getColCount(path, sheetName)
            #     log.logger.info("" + str(col))
            #
            #     for j in range(2, row + 1):
            #         for k in range(1, col + 1, 5):
            #             question = excel_Data.getCellData(path, sheetName, j, k)
            #             designation = excel_Data.getCellData(path, sheetName, j, 2)
            #             thinkTime = excel_Data.getCellData(path, sheetName, j, 3)
            #             answerTime = excel_Data.getCellData(path, sheetName, j, 4)
            #             time.sleep(0.5)
            #             log.logger.info("" + str(designation))
            #             log.logger.info("" + str(question))
            #             if j == 2 and designation == "Web Developer":
            #                 self.do_send_key(self.questionSetTitle, designation)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.searchInput, question)
            #                 time.sleep(0.5)
            #                 self.de_click(self.questionInList)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.firstThinkTime, thinkTime)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.firstAnswerTime, answerTime)
            #             elif j == 3 and designation == "Web Developer":
            #                 self.de_click(self.closeButton)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.searchInput, question)
            #                 time.sleep(0.5)
            #                 self.de_click(self.questionInList)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.secondThinkTime, thinkTime)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.secondAnswerTime, answerTime)
            #                 saveButton = self.driver.find_element(By.XPATH,
            #                                                       "//div[@class='w-full md:max-w-[700px] flex flex-row justify-end mb-[12px]']/button[2]")
            #                 self.de_action_method(saveButton)
            #                 time.sleep(5)
            #
            #
            #
            #
            # if re == "Awards":
            #     question = self.get_element_text_question_set(self.questionInList)
            #     time.sleep(0.5)
            #     log.logger.info("question Need to appear to solve synchronisation problem " + str(question))
            #     self.de_click(self.awardService)
            #     time.sleep(0.5)
            #     path = ".\\excel\\question_set_creation.xlsx"
            #     sheetName = 'Awards_List'
            #     row = excel_Data.getRowCount(path, sheetName)
            #     log.logger.info("" + str(row))
            #     col = excel_Data.getColCount(path, sheetName)
            #     log.logger.info("" + str(col))
            #
            #     for j in range(2, row + 1):
            #         for k in range(1, col + 1, 5):
            #             question = excel_Data.getCellData(path, sheetName, j, k)
            #             designation = excel_Data.getCellData(path, sheetName, j, 2)
            #             thinkTime = excel_Data.getCellData(path, sheetName, j, 3)
            #             answerTime = excel_Data.getCellData(path, sheetName, j, 4)
            #             time.sleep(0.5)
            #             log.logger.info("" + str(designation))
            #             log.logger.info("" + str(question))
            #             if j == 2 and designation == "Salesperson":
            #                 self.do_send_key(self.questionSetTitle, designation)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.searchInput, question)
            #                 time.sleep(0.5)
            #                 self.de_click(self.questionInList)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.firstThinkTime, thinkTime)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.firstAnswerTime, answerTime)
            #             elif j == 3 and designation == "Salesperson":
            #                 self.de_click(self.closeButton)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.searchInput, question)
            #                 time.sleep(0.5)
            #                 self.de_click(self.questionInList)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.secondThinkTime, thinkTime)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.secondAnswerTime, answerTime)
            #                 saveButton = self.driver.find_element(By.XPATH,
            #                                                       "//div[@class='w-full md:max-w-[700px] flex flex-row justify-end mb-[12px]']/button[2]")
            #                 self.de_action_method(saveButton)
            #                 time.sleep(5)
            #
            # if re == "Marketing":
            #     question = self.get_element_text_question_set(self.questionInList)
            #     time.sleep(0.5)
            #     log.logger.info("question Need to appear to solve synchronisation problem " + str(question))
            #     self.de_click(self.marketingService)
            #     time.sleep(0.5)
            #     path = ".\\excel\\question_set_creation.xlsx"
            #     sheetName = 'Marketing_List'
            #     row = excel_Data.getRowCount(path, sheetName)
            #     log.logger.info("" + str(row))
            #     col = excel_Data.getColCount(path, sheetName)
            #     log.logger.info("" + str(col))
            #
            #     for j in range(2, row + 1):
            #         for k in range(1, col + 1, 5):
            #             question = excel_Data.getCellData(path, sheetName, j, k)
            #             designation = excel_Data.getCellData(path, sheetName, j, 2)
            #             thinkTime = excel_Data.getCellData(path, sheetName, j, 3)
            #             answerTime = excel_Data.getCellData(path, sheetName, j, 4)
            #             time.sleep(0.5)
            #             log.logger.info("" + str(designation))
            #             log.logger.info("" + str(question))
            #             if j == 2 and designation == "Purchase Manager":
            #                 self.do_send_key(self.questionSetTitle, designation)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.searchInput, question)
            #                 time.sleep(0.5)
            #                 self.de_click(self.questionInList)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.firstThinkTime, thinkTime)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.firstAnswerTime, answerTime)
            #             elif j == 3 and designation == "Purchase Manager":
            #                 self.de_click(self.closeButton)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.searchInput, question)
            #                 time.sleep(0.5)
            #                 self.de_click(self.questionInList)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.secondThinkTime, thinkTime)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.secondAnswerTime, answerTime)
            #                 time.sleep(0.5)
            #                 saveButton = self.driver.find_element(By.XPATH,
            #                                                       "//div[@class='w-full md:max-w-[700px] flex flex-row justify-end mb-[12px]']/button[2]")
            #                 self.de_action_method(saveButton)
            #
            #                 time.sleep(5)
            #
            # if re == "Learning":
            #     question = self.get_element_text_question_set(self.questionInList)
            #     time.sleep(0.5)
            #     log.logger.info("question Need to appear to solve synchronisation problem " + str(question))
            #     self.de_click(self.learningService)
            #     time.sleep(0.5)
            #     path = ".\\excel\\question_set_creation.xlsx"
            #     sheetName = 'Learning_List'
            #     row = excel_Data.getRowCount(path, sheetName)
            #     log.logger.info("" + str(row))
            #     col = excel_Data.getColCount(path, sheetName)
            #     log.logger.info("" + str(col))
            #
            #     for j in range(2, row + 1):
            #         for k in range(1, col + 1, 5):
            #             question = excel_Data.getCellData(path, sheetName, j, k)
            #             designation = excel_Data.getCellData(path, sheetName, j, 2)
            #             thinkTime = excel_Data.getCellData(path, sheetName, j, 3)
            #             answerTime = excel_Data.getCellData(path, sheetName, j, 4)
            #             time.sleep(0.5)
            #             log.logger.info("" + str(designation))
            #             log.logger.info("" + str(question))
            #             if j == 2 and designation == "Field  Executive":
            #                 self.do_send_key(self.questionSetTitle, designation)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.searchInput, question)
            #                 time.sleep(0.5)
            #                 self.de_click(self.questionInList)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.firstThinkTime, thinkTime)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.firstAnswerTime, answerTime)
            #             elif j == 3 and designation == "Field  Executive":
            #                 self.de_click(self.closeButton)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.searchInput, question)
            #                 time.sleep(0.5)
            #                 self.de_click(self.questionInList)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.secondThinkTime, thinkTime)
            #                 time.sleep(0.5)
            #                 self.do_send_key(self.secondAnswerTime, answerTime)
            #                 saveButton = self.driver.find_element(By.XPATH,
            #                                                       "//div[@class='w-full md:max-w-[700px] flex flex-row justify-end mb-[12px]']/button[2]")
            #                 self.de_action_method(saveButton)
            #
            #                 time.sleep(5)

            if re == "Auditions":
                question = self.get_element_text_question_set(self.questionInList)
                time.sleep(0.5)
                log.logger.info("question Need to appear to solve synchronisation problem " + str(question))
                self.de_click(self.auditionService)
                time.sleep(0.5)
                path = ".\\excel\\question_set_creation.xlsx"
                sheetName = 'Auditions_List'
                row = excel_Data.getRowCount(path, sheetName)
                log.logger.info("" + str(row))
                col = excel_Data.getColCount(path, sheetName)
                log.logger.info("" + str(col))

                for j in range(2, row + 1):
                    for k in range(1, col + 1, 5):
                        question = excel_Data.getCellData(path, sheetName, j, k)
                        designation = excel_Data.getCellData(path, sheetName, j, 2)
                        thinkTime = excel_Data.getCellData(path, sheetName, j, 3)
                        answerTime = excel_Data.getCellData(path, sheetName, j, 4)
                        time.sleep(0.5)
                        log.logger.info("" + str(designation))
                        log.logger.info("" + str(question))
                        if j == 2 and designation == "Casting Director":
                            self.do_send_key(self.questionSetTitle, designation)
                            time.sleep(0.5)
                            self.do_send_key(self.searchInput, question)
                            time.sleep(0.5)
                            self.de_click(self.questionInList)
                            time.sleep(0.5)
                            self.do_send_key(self.firstThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.firstAnswerTime, answerTime)
                        elif j == 3 and designation == "Casting Director":
                            self.de_click(self.closeButton)
                            time.sleep(0.5)
                            self.do_send_key(self.searchInput, question)
                            time.sleep(0.5)
                            self.de_click(self.questionInList)
                            time.sleep(0.5)
                            self.do_send_key(self.secondThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.secondAnswerTime, answerTime)
                            saveButton = self.driver.find_element(By.XPATH,
                                                                  "//div[@class='w-full md:max-w-[700px] flex flex-row justify-end mb-[12px]']/button[2]")
                            self.de_action_method(saveButton)

                            time.sleep(5)

            if re == "Admissions":
                question = self.get_element_text_question_set(self.questionInList)
                time.sleep(0.5)
                log.logger.info("question Need to appear to solve synchronisation problem " + str(question))
                self.de_click(self.admissionService)
                time.sleep(0.5)
                path = ".\\excel\\question_set_creation.xlsx"
                sheetName = 'Admissions_List'
                row = excel_Data.getRowCount(path, sheetName)
                log.logger.info("" + str(row))
                col = excel_Data.getColCount(path, sheetName)
                log.logger.info("" + str(col))

                for j in range(2, row + 1):
                    for k in range(1, col + 1, 5):
                        question = excel_Data.getCellData(path, sheetName, j, k)
                        designation = excel_Data.getCellData(path, sheetName, j, 2)
                        thinkTime = excel_Data.getCellData(path, sheetName, j, 3)
                        answerTime = excel_Data.getCellData(path, sheetName, j, 4)
                        time.sleep(0.5)
                        log.logger.info("" + str(designation))
                        log.logger.info("" + str(question))
                        if j == 2 and designation == "Admission Incharge":
                            self.do_send_key(self.questionSetTitle, designation)
                            time.sleep(0.5)
                            self.do_send_key(self.searchInput, question)
                            time.sleep(0.5)
                            self.de_click(self.questionInList)
                            time.sleep(0.5)
                            self.do_send_key(self.firstThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.firstAnswerTime, answerTime)
                        elif j == 3 and designation == "Admission Incharge":
                            self.de_click(self.closeButton)
                            time.sleep(0.5)
                            self.do_send_key(self.searchInput, question)
                            time.sleep(0.5)
                            self.de_click(self.questionInList)
                            time.sleep(0.5)
                            self.do_send_key(self.secondThinkTime, thinkTime)
                            time.sleep(0.5)
                            self.do_send_key(self.secondAnswerTime, answerTime)
                            saveButton = self.driver.find_element(By.XPATH,
                                                                  "//div[@class='w-full md:max-w-[700px] flex flex-row justify-end mb-[12px]']/button[2]")
                            self.de_action_method(saveButton)

                            time.sleep(5)
