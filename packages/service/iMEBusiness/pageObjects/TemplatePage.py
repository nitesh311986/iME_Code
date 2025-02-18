import time
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Template_Details(BasePage):
    videoInterviewIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/button/div")
    templateProfileIcon = (
        By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/div/div/div[2]/button[1]")
    minimumRequirementIcon = (By.XPATH, "//div[@class='flex flex-col grow mx-[24px] md:mx-[32px]']/div/button[2]")
    questionSetIcon = (By.XPATH, "//div[@class='flex flex-col grow mx-[24px] md:mx-[32px]']/div/button[4]")
    multimediaSetIcon = (By.XPATH, "//div[@class='flex flex-col grow mx-[24px] md:mx-[32px]']/div/button[5]")

    # Filter Minimum requirement
    filterIcon = (By.XPATH,
                  "//div[@class='w-full flex flex-col lg:flex-row lg:items-center lg:justify-between rounded-[6px] mb-[16px]']/div[1]/div[2]/button")
    serviceDropDown = (By.XPATH,
                       "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[2]/button")
    recruitmentOption = (By.XPATH,
                         "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[2]/ul/li[1]")
    awardOption = (By.XPATH,
                   "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[2]/ul/li[2]")
    marketingOption = (By.XPATH,
                       "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[2]/ul/li[3]")
    learningOption = (By.XPATH,
                      "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[2]/ul/li[4]")
    auditionOption = (By.XPATH,
                      "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[2]/ul/li[5]")
    admissionOption = (By.XPATH,
                       "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[2]/ul/li[6]")
    answerTypeDropDown = (By.XPATH,
                          "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[3]/button")
    yesAnswerOption = (By.XPATH,
                       "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[3]/ul/li[1]")
    noAnswerOption = (By.XPATH,
                      "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[3]/ul/li[2]")
    applyButton = (By.XPATH,
                   "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[4]/div/button")
    searchInputBox = (By.CSS_SELECTOR, "input[name='templateSearch']")

    clearAllLink = (By.XPATH,
                    "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[1]/h2[2]")

    questionDisplayed = (By.XPATH,
                         "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[1]/div/div")

    serviceDisplayed = (By.XPATH,
                        "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[2]/div")

    answerTypeDisplayed = (By.XPATH,
                           "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[3]/div")

    # Filter Question Set
    applyButtonOfQuestionSet = (By.XPATH,
                                "//div[@class='border-[1px] dark:border-ime-gray-600 border-ime-gray-300 rounded-[6px] dark:bg-ime-gray-800 bg-white w-full px-[20px]']/div[3]/div/button")
    closeIconOfSearchBox = (By.XPATH,
                            "//div[@class='flex flex-row items-center border border-ime-gray-300 dark:border-ime-gray-600 rounded-[6px] h-[36px] p-2 w-full mr-4']/*[local-name()='svg'][@class='fill-black dark:fill-white scale-[180%] cursor-pointer relative right-2']")

    closeIconOfSearchBoxForQuestionSet = (By.XPATH,
                                          "//div[@class='flex flex-row items-center border border-ime-gray-300 dark:border-ime-gray-600 rounded-[6px] h-[36px] p-2 w-full mr-4']/*[local-name()='svg'][@class='fill-black dark:fill-white scale-[180%] cursor-pointer mt-4 h-[14px] relative right-2']")

    serviceTypeDisplayedQuestionSet = (By.XPATH,
                                       "//div[@class='border-[1px] border-ime-gray-300 dark:border-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[2]/div/div[1]")

    questionTypeDisplayedQuestionSet = (By.XPATH,
                                        "//div[@class='border-[1px] border-ime-gray-300 dark:border-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[1]/div/div[1]")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_template_icon(self):
        time.sleep(3)
        self.de_click(self.videoInterviewIcon)
        time.sleep(1)
        self.de_click(self.templateProfileIcon)
        time.sleep(4)

    def fetch_minimum_requirement(self):
        log.logger.info("****==View Minimum requirement details of template Test Case Starts Here==***")
        self.de_click(self.minimumRequirementIcon)
        time.sleep(4)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            rows = 1 + len(self.driver.find_elements(By.XPATH,
                                                     "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            # Obtain the number of columns in table
            cols = len(self.driver.find_elements(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Row" + str(rows))
            log.logger.info("Number Of Column" + str(cols))
            log.logger.info(" **||Questions||**              **||Service||**               **||AnswerTyp||**")

            # Printing the data of the table
            for r in range(1, rows, 3):
                for p in range(1, cols):
                    if r <= 10:
                        # obtaining the text from each column of the table
                        value = self.driver.find_element(By.XPATH,
                                                         "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                             r) + "]/td[" + str(p) + "]").text

                        log.logger.info("" + str(value))

                    else:
                        break
        else:
            log.logger.info("There's No Data Available ")

    def filter_minimum_requirement_via_filter_box(self):

        # 1.1 filter minimum requirement using filter
        log.logger.info("****==Filter Minimum requirement details based on service type of template test case starts "
                        "here==***")
        time.sleep(0.5)
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            serviceName = self.get_element_text(self.serviceDisplayed)
            time.sleep(0.5)
            self.de_click(self.filterIcon)
            time.sleep(1)
            self.de_click(self.serviceDropDown)
            time.sleep(1)
            if serviceName == "Recruitment":
                self.de_click(self.recruitmentOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceName == "Awards":
                self.de_click(self.awardOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceName == "Marketing":
                self.de_click(self.marketingOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceName == "Learning":
                self.de_click(self.learningOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceName == "Auditions":
                self.de_click(self.auditionOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceName == "Admissions":
                self.de_click(self.admissionOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            else:
                log.logger.info("Data Is Not Available")
            self.de_click(self.applyButton)
            time.sleep(0.5)

            # Fetch The data from table
            rows1 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            # Obtain the number of columns in table
            cols1 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation " + str(rows1))
            log.logger.info("Number Of Columns During Filter Operation" + str(cols1))
            log.logger.info(" **||Questions||**              **||Service||**               **||AnswerTyp||**")

            for r1 in range(1, rows1, 3):
                for p1 in range(1, 2):
                    # obtaining the text from each column of the table
                    if r1 <= 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                             r1) + "]/td[2]").text
                        assert serviceName in value
                        log.logger.info("**User Able to filter data based on Service type == **" + str(value))
                    else:
                        break

            time.sleep(1)
        else:
            log.logger.info("There's No Data Available")

        # Filter on answer type

        log.logger.info("****==Filter Minimum requirement details based on answer type of template test case starts "
                        "here==***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            self.de_click(self.filterIcon)
            time.sleep(0.5)
            self.de_click(self.clearAllLink)
            time.sleep(1)
            answerName = self.get_element_text(self.answerTypeDisplayed)
            time.sleep(0.5)
            self.de_click(self.filterIcon)
            time.sleep(1)
            self.de_click(self.answerTypeDropDown)
            time.sleep(1)
            if answerName == "Yes":
                self.de_click(self.yesAnswerOption)
                time.sleep(0.5)
                self.de_click(self.answerTypeDropDown)
                time.sleep(0.5)
            elif answerName == "No":
                self.de_click(self.noAnswerOption)
                time.sleep(0.5)
                self.de_click(self.answerTypeDropDown)
                time.sleep(0.5)

            else:
                log.logger.info("Data Is Not Available")
            self.de_click(self.applyButton)
            time.sleep(0.5)

            # Fetch The data from table
            rows2 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            # Obtain the number of columns in table
            cols2 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation " + str(rows2))
            log.logger.info("Number Of Columns During Filter Operation" + str(cols2))
            log.logger.info(" **||Questions||**              **||Service||**               **||AnswerTyp||**")

            for r2 in range(1, rows2, 3):
                for p2 in range(1, 2):
                    # obtaining the text from each column of the table
                    if r2 <= 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                             r2) + "]/td[3]").text
                        assert value == answerName
                        log.logger.info("**User Able to filter data based on Answer type == **" + str(value))
                    else:
                        break
        else:
            log.logger.info("There's No Data Available")

    def filter_minimum_requirement_via_search_box(self):
        # 1.2 filter minimum requirement data via search box using service type

        log.logger.info("****==Filter Minimum requirement using search box via service type details of template Test "
                        "Case Starts Here==***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            time.sleep(0.5)
            serviceName = self.get_element_text(self.serviceDisplayed)
            time.sleep(0.5)
            self.de_click(self.filterIcon)
            time.sleep(0.5)
            self.de_click(self.clearAllLink)
            time.sleep(1)
            self.do_send_key(self.searchInputBox, serviceName)
            time.sleep(1)

            # Fetch The data from table using search box
            rows3 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            # Obtain the number of columns in table
            cols3 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows3))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols3))
            log.logger.info(" Filter data upon == ||Service|| ")

            for r3 in range(1, rows3, 3):
                for p3 in range(1, 2):
                    # obtaining the text from each column of the table
                    if r3 <= 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                             r3) + "]/td[2]").text

                        assert serviceName in value
                        log.logger.info(
                            "<< !! Filter Via Search box using service type for minimum requirements working fine "
                            "!!>>" + str(value))
                    else:
                        break

            time.sleep(1)
        else:
            log.logger.info("There's No Data Available")

        # 1.3  filter minimum requirement data via search box using question value

        log.logger.info("****==Filter Minimum requirement using search box via question value of template Test "
                        "Case Starts Here==***")

        time.sleep(1)
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            self.de_click(self.closeIconOfSearchBoxForQuestionSet)
            time.sleep(0.5)
            questionValue = self.get_element_text(self.questionDisplayed)
            self.do_send_key(self.searchInputBox, questionValue)
            time.sleep(1)

            # Fetch The data from table using search box
            rows4 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            # Obtain the number of columns in table
            cols4 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows4))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols4))
            log.logger.info(" Filter data upon == ||Service|| ")

            for r4 in range(1, rows4, 3):
                for p4 in range(1, 2):
                    # obtaining the text from each column of the table
                    if r4 <= 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                             r4) + "]/td[1]").text

                        assert value == questionValue
                        log.logger.info(
                            "<< !! Filter Via Search box using question for minimum requirements working fine "
                            "!!>>" + str(questionValue))
                    else:
                        break
        else:
            log.logger.info("There's No Data Available")

    # Question Set

    def fetch_question_set(self):
        log.logger.info("**** === View all details of question set of template starts Here === ***")
        time.sleep(3)
        self.de_click(self.questionSetIcon)
        time.sleep(6)

        dataAvail = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-gray-300 dark:border-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            rows = 1 + len(self.driver.find_elements(By.XPATH,
                                                     "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            # Obtain the number of columns in table
            cols = len(self.driver.find_elements(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Row = " + str(rows))
            log.logger.info("Number Of Column = " + str(cols))
            log.logger.info("||Question Set||           ||Service|| ")
            # self.table_traverse(rows, cols)

            # Printing the data of the table
            for r in range(1, rows):
                for p in range(1, cols + 1):
                    # obtaining the text from each column of the table
                    if r <= 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                             r) + "]/td[" + str(p) + "]").text

                        log.logger.info("" + str(value))
            time.sleep(0.5)
        else:
            log.logger.info("There's no data Available")

    def filter_question_set_via_filter_box(self):

        # 2.1 Filter Via filter feature using service type

        log.logger.info(
            "**** === Filter question set details of based on service type template test case starts here === ***")
        time.sleep(1)
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-gray-300 dark:border-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            time.sleep(0.5)
            serviceTypeName = self.get_element_text(self.serviceTypeDisplayedQuestionSet)
            time.sleep(0.5)
            self.de_click(self.filterIcon)
            time.sleep(1)
            self.de_click(self.serviceDropDown)
            time.sleep(0.5)
            time.sleep(1)
            if serviceTypeName == "Recruitment":
                self.de_click(self.recruitmentOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceTypeName == "Awards":
                self.de_click(self.awardOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceTypeName == "Marketing":
                self.de_click(self.marketingOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceTypeName == "Learning":
                self.de_click(self.learningOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceTypeName == "Auditions":
                self.de_click(self.auditionOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceTypeName == "Admissions":
                self.de_click(self.admissionOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            else:
                log.logger.info("Data Is Not Available")
            self.de_click(self.applyButtonOfQuestionSet)
            time.sleep(0.5)

            # Fetch The data from table
            rows1 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            # Obtain the number of columns in table
            cols1 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows1))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols1))
            log.logger.info(" Filter data upon == ||Service|| ")

            for r1 in range(1, rows1):
                for p1 in range(1, 2):
                    # obtaining the text from each column of the table
                    if r1 < 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                             r1) + "]/td[2]").text

                        try:
                            if len(value) > 0:
                                assert serviceTypeName in value
                                log.logger.info(
                                    "<< !!Filter Via Service Type for question set  Working Fine !!>>" + str(value))
                        except:
                            print("Something went wrong")
                        finally:
                            print("Loop Is Fetching One More Row")
        log.logger.info("There's no data available")

    def filter_question_set_via_search_box(self):

        # 2.2 Filter Via Search box using service type

        log.logger.info("*** === Test case to filter question Set via search box using service type for template starts"
                        "here === ***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-gray-300 dark:border-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            self.de_click(self.filterIcon)
            time.sleep(0.5)
            self.de_click(self.clearAllLink)
            time.sleep(1)
            serviceTypeName = self.get_element_text(self.serviceTypeDisplayedQuestionSet)
            time.sleep(0.5)
            self.do_send_key(self.searchInputBox, serviceTypeName)
            time.sleep(1)

            # Fetch The data from table using search box
            rows2 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            # Obtain the number of columns in table
            cols2 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows2))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols2))
            log.logger.info(" Filter data upon == ||Service|| ")

            for r2 in range(1, rows2):
                for p2 in range(1, 2):
                    if r2 < 10:
                        # obtaining the text from each column of the table
                        value = self.driver.find_element(By.XPATH,
                                                         "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                             r2) + "]/td[2]").text

                        assert value == serviceTypeName
                        log.logger.info(
                            "<< !! Filter Via Search box using service type for question set working fine !!>>" + str(
                                value))
            time.sleep(1)
        log.logger.info("There's no data available")

        # 2.3 Filter Via Search box using question type
        log.logger.info("****== Filter Question Set via search box using question type of template test case "
                        "starts here==***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-gray-300 dark:border-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            self.de_click(self.closeIconOfSearchBoxForQuestionSet)
            time.sleep(0.5)
            questionName = self.get_element_text(self.questionTypeDisplayedQuestionSet)
            time.sleep(0.5)
            self.do_send_key(self.searchInputBox, questionName)
            time.sleep(1)

            # Fetch The data from table using search box
            rows3 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            # Obtain the number of columns in table
            cols3 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows3))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols3))
            log.logger.info(" Filter data upon == ||Question Set||  ")

            for r3 in range(1, rows3):
                for p3 in range(1, 2):
                    # obtaining the text from each column of the table
                    if r3 < 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                             r3) + "]/td[1]").text

                        assert questionName in value
                        log.logger.info(
                            "<<!! Filter Via Search box using question for question set working fine !!>>" + str(value))
        else:
            log.logger.info("There's No Data Available")

    # Multimedia Details

    def fetch_multimedia_details(self):
        log.logger.info("****==View Multimedia details of template Test Case Starts Here==***")
        time.sleep(3)
        self.de_click(self.multimediaSetIcon)
        time.sleep(6)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            rows = 1 + len(self.driver.find_elements(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols = len(self.driver.find_elements(By.XPATH,
                                                 "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Row = " + str(rows))
            log.logger.info("Number Of Column = " + str(cols))
            log.logger.info(" ||Questions||             ||Service||              ||AnswerTyp||")
            # Printing the data of the table
            for r in range(1, rows):
                for p in range(1, cols + 1):
                    if r < 10:
                        # obtaining the text from each column of the table
                        value = self.driver.find_element(By.XPATH,
                                                         "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                             r) + "]/td[" + str(p) + "]").text
                        log.logger.info("" + str(value))

        else:
            log.logger.info("There's no data available")

    def filter_multimedia_via_filter_box(self):
        # 3.1 Filter Via filter feature using service type
        log.logger.info(
            "**** === Filter multimedia details of template  via service type test case starts here === ***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )

        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            time.sleep(0.5)
            serviceName = self.get_element_text(self.serviceDisplayed)
            time.sleep(0.5)
            self.de_click(self.filterIcon)
            time.sleep(1)
            self.de_click(self.serviceDropDown)
            time.sleep(1)
            if serviceName == "Recruitment":
                self.de_click(self.recruitmentOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceName == "Awards":
                self.de_click(self.awardOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceName == "Marketing":
                self.de_click(self.marketingOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceName == "Learning":
                self.de_click(self.learningOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceName == "Auditions":
                self.de_click(self.auditionOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            elif serviceName == "Admissions":
                self.de_click(self.admissionOption)
                time.sleep(0.5)
                self.de_click(self.serviceDropDown)
                time.sleep(0.5)
            else:
                log.logger.info("Data Is Not Available")
            self.de_click(self.applyButton)
            time.sleep(0.5)

            # Fetch The data from table
            rows1 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols1 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows1))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols1))
            log.logger.info(" ||Service|| ")

            for r1 in range(1, rows1):
                for p1 in range(2, cols1 + 1):

                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                         r1) + "]/td[2]").text

                    if r1 <= 8:
                        assert value == serviceName
                        log.logger.info(
                            "<<!!  Filter Via Service Type for multimedia Working Fine !!>>" + str(value))

        else:
            log.logger.info("There's No Data Available")

    def filter_multimedia_via_search_box(self):
        # 3.2 Filter Via Search box using service type
        log.logger.info("*** === Test case to filter multimedia via search box using service type for template "
                        "starts"
                        "here === ***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            self.de_click(self.filterIcon)
            time.sleep(0.5)
            self.de_click(self.clearAllLink)
            time.sleep(1)
            time.sleep(0.5)
            serviceName = self.get_element_text(self.serviceDisplayed)
            time.sleep(0.5)
            self.do_send_key(self.searchInputBox, serviceName)
            time.sleep(1)

            # Fetch The data from table using search box
            rows2 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols2 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows2))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols2))
            log.logger.info(" Filter data upon == ||Service|| ")

            for r2 in range(1, rows2):
                for p2 in range(1, 2):

                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                         r2) + "]/td[2]").text
                    if r2 <= 8:
                        log.logger.info("  " + str(value))
                        assert value == serviceName
                        log.logger.info(
                            "<< !! Filter Via Search box using service type for multimedia working fine !!>>" + str(
                                value))
                    else:
                        break

            else:
                log.logger.info("There's No Data Available")

        # 3.3 Filter Via Search box using answer type

        log.logger.info("****== Filter Multimedia via search box using answer type of template test case "
                        "starts here==***")

        # dataAvail = self.driver.find_element(By.XPATH,
        #                                      "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            self.de_click(self.closeIconOfSearchBox)
            time.sleep(1)
            answerName = self.get_element_text(self.answerTypeDisplayed)
            time.sleep(0.5)
            self.do_send_key(self.searchInputBox, answerName)
            time.sleep(1)

            # Fetch The data from table using search box
            rows3 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols3 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows3))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols3))
            log.logger.info(" Filter data upon == ||Answer Type||  ")

            for r3 in range(1, rows3 + 1):
                for p3 in range(1, 2):
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                         r3) + "]/td[3]").text
                    if r3 <= 8:
                        try:
                            if len(value) > 0:
                                assert value == answerName
                                log.logger.info(
                                    "<<!! Filter Via Search box using answer type for multimedia working fine !!>>" + str(
                                        value))
                        except:
                            print("Something went wrong")
                        finally:
                            print("Loop Is Fetching One More Row")
                    else:
                        break

        else:
            log.logger.info("There's no data available")

        # 3.4 Filter Via Search box using question

        log.logger.info("****== Filter Multimedia via search box using question test case "
                        "starts here==***")

        # dataAvail = self.driver.find_element(By.XPATH,
        #                                      "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            self.de_click(self.closeIconOfSearchBox)
            time.sleep(1)
            questionName = self.get_element_text(self.questionDisplayed)
            time.sleep(0.5)
            self.do_send_key(self.searchInputBox, questionName)
            time.sleep(1)

            # Fetch The data from table using search box
            rows4 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols4 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows4))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols4))
            log.logger.info(" Filter data upon == ||Question||  ")

            for r4 in range(1, rows4 + 1):
                for p4 in range(1, cols4 - 1):
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                         r4) + "]/td[1]").text

                    if r4 <= 8:
                        try:
                            if len(value) > 0:
                                if questionName in value:
                                    log.logger.info(
                                        "<<!! Filter Via Search box using question for multimedia working fine !!>>" + str(
                                            value))
                        except:
                            print("Something went wrong")
                            assert False
                        finally:
                            print("Loop Is Fetching One More Row")

                    else:
                        break

            else:
                log.logger.info("There's no dara available")
