from selenium.webdriver.common.by import By
import logging
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEApplicant.pageObjects.BasePage import BasePage
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Awards(BasePage):
    oneWayInterviewIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[5]/a")
    awardsTab = (By.XPATH,
                 "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[3]")
    designationTitle = (By.XPATH,
                        "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[1]/div/div[1]")
    companyTitle = (By.XPATH,
                    "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[2]/div/div[1]")
    statusTitle = (By.XPATH,
                   "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[3]/div/div[1]")
    searchInput = (By.XPATH, "//div[@id='search']/div[2]/input")
    searchButton = (By.CSS_SELECTOR,
                    "button[class='ml-[16px] rounded-[4px] border-none bg-gradient-to-b from-purple-500 to-pink-500 p-[1px] w-[87px]']")

    closeIcon = (By.XPATH,
                 "//div[@id='search']/div[2]/*[local-name()='svg'][@class='fill-black dark:fill-white scale-[180%] h-[12px] cursor-pointer mt-3 relative right-2']")
    description = (By.XPATH, "//div[@class='max-w-[675px] overflow-hidden']/div")

    backButton = (By.XPATH, "//div[@class='hidden lg:flex items-center']/h2")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_oneWay_interview_icon(self):
        time.sleep(3)
        self.de_click(self.oneWayInterviewIcon)
        time.sleep(4)
        currentURL = self.driver.current_url
        log.logger.info(
            "==User Is On The Page=== " + currentURL)

    def fetch_interviews_details_via_company(self):

        log.logger.info(
            "****==Filter Interview Details using search box via company name for Company service===***")
        self.de_click(self.awardsTab)
        time.sleep(4)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            companyName = self.get_element_text(self.companyTitle)
            time.sleep(0.5)
            self.do_send_key(self.searchInput, companyName)
            time.sleep(1)
            self.de_click(self.searchButton)
            time.sleep(2)

            # Fetch The data from table using search box
            rows2 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols2 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows2))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols2))
            log.logger.info(" Filter data upon == ||Company Name|| ")

            for r2 in range(1, rows2):
                for p2 in range(1, 2):
                    # obtaining the text from each column of the table
                    if r2 <= 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                             r2) + "]/td[2]/div/div[1]").text

                        log.logger.info("" + str(value))
                        assert companyName in value
                        log.logger.info(
                            "<< !! Filter award interview list using Search box via company name ===  "
                            "!!>>" + str(companyName) + "=== executed Successfully")
                    else:
                        break

            else:
                log.logger.info("There's No Data Available")

    def fetch_interviews_details_via_designation(self):

        log.logger.info("****==Filter Interview Details using search box via Designation for Awards services "
                        "===***")
        time.sleep(1)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            self.de_click(self.closeIcon)
            time.sleep(1)
            designationName = self.get_element_text(self.designationTitle)
            time.sleep(0.5)
            self.do_send_key(self.searchInput, designationName)
            time.sleep(1)
            self.de_click(self.searchButton)

            time.sleep(2)

            # Fetch The data from table using search box
            rows2 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols2 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows2))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols2))
            log.logger.info(" Filter data upon == ||Designation|| ")

            for r2 in range(1, rows2):
                for p2 in range(1, 2):
                    # obtaining the text from each column of the table
                    if r2 <= 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                             r2) + "]/td[1]/div[1]/div").text

                        log.logger.info("" + str(value))
                        assert designationName in value
                        log.logger.info(
                            "<< !! Filter award interview list using Search box via designation name ===  "
                            "!!>>" + str(designationName) + "=== executed Successfully")
                    else:
                        break
            time.sleep(1)
            self.de_click(self.closeIcon)
        else:
            log.logger.info("There's No Data Available")

    def view_details_of_interview(self):

        log.logger.info("****==View Details Of Interview Of Awards Service===***")
        time.sleep(1)
        # self.de_click(self.iMEQueueIcon)
        # time.sleep(3)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            totalInterviews = len(self.driver.find_elements(By.XPATH,
                                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr"))

            for i in range(totalInterviews):
                elements = []
                elements = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr/td[4]/div/div[2]/*[local-name()='svg'][@class='hidden xl:block fill-ime-blue-gray-700 mr-[12px] dark:fill-ime-blue-gray-200']")
                if i < 10:
                    log.logger.info(
                        "Value of i" + str(i))
                    self.de_scroll_into_view(elements[i])
                    time.sleep(1)
                    elements[i].click()
                    log.logger.info(
                        "!!! == User Has clicked view interview icon against interview designation == !!!")
                    time.sleep(3)

                    rows = 1 + len(self.driver.find_elements(By.XPATH,
                                                             "//div[@class='max-w-[675px] border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden mr-[20px]']/table/tbody/tr"))

                    # Obtain the number of columns in table
                    cols = len(self.driver.find_elements(By.XPATH,
                                                         "//div[@class='max-w-[675px] border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden mr-[20px]']/table/tbody/tr[1]/td"))

                    # Print rows and columns
                    log.logger.info("Number Of Row" + str(rows))
                    log.logger.info("Number Of Column" + str(cols))
                    log.logger.info(
                        "**||Service||**              **||Learning Type||**               **||Position||**        "
                        "  **||Query Email||**        **||Estimated Time Required||**")

                    # Printing the data of the table
                    for r in range(1, rows):
                        for p in range(1, 2):
                            # obtaining the text from each column of the table
                            value = self.driver.find_element(By.XPATH,
                                                             "//div[@class='max-w-[675px] border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden mr-[20px]']/table/tbody/tr[" + str(
                                                                 r) + "]/td[2]").text

                            log.logger.info("" + str(value))
                            time.sleep(0.5)

                    Description = self.get_element_text(self.description)
                    log.logger.info("Description Of Interview Is === " + str(Description))
                    time.sleep(0.5)
                    self.de_click(self.backButton)
                    time.sleep(3)

                else:
                    log.logger.info("Details Of All Elements Ha s Been Fetched")

        else:
            log.logger.info("There's No Data Available")
