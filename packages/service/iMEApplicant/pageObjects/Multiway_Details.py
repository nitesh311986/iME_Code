from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import logging
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEApplicant.pageObjects.BasePage import BasePage
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Multiway_Details(BasePage):
    multiWayInterviewIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[6]/a")

    interviewDesignation = (By.XPATH,
                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[1]/div/div[1]")

    companyName = (By.XPATH,
                   "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[2]/div/div[1]")
    interviewStatus = (By.XPATH,
                       "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[5]/div/div[1]")
    searchInput = (By.XPATH, "//div[@id='search']/div[2]/input")
    searchButton = (By.CSS_SELECTOR,
                    "button[class='ml-[16px] rounded-[4px] border-none bg-gradient-to-b from-purple-500 to-pink-500 p-[1px] w-[87px]']")
    closeIcon = (By.XPATH,
                 "//div[@id='search']/div[2]/*[local-name()='svg'][@class='fill-black dark:fill-white scale-[180%] h-[12px] cursor-pointer mt-3 relative right-2']")

    descriptionOfInterview = (By.XPATH, "//div[@class='max-w-[675px] overflow-hidden']/div")

    backArrow = (By.XPATH, "//div[@class='hidden lg:flex items-center']/h2")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_multiWay_interview_icon(self):
        time.sleep(3)
        currentURL = self.driver.current_url
        log.logger.info(
            "==User Is On The Page=== " + currentURL)
        try:
            # Attempt to perform the click action
            self.de_click(self.multiWayInterviewIcon)
        except NoSuchElementException:
            # Handle case where the element is not found
            print("The element to click was not found.")
        except ElementNotInteractableException:
            # Handle case where the element is present but not clickable
            print("The element is not interactable.")
        except Exception as e:
            # Handle any other unexpected exceptions
            print(f"An unexpected error occurred while clicking the element: {e}")
        time.sleep(6)

    def fetch_multiway_interviews_details(self):

        log.logger.info(
            "****==Fetch The List Of Multiway Interview Request ===***")
        #dataAvail = self.driver.find_element(By.XPATH,"//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )

        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            # Fetch The data from table using search box
            rows = 1 + len(self.driver.find_elements(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols = len(self.driver.find_elements(By.XPATH,
                                                 "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols))
            log.logger.info("== ||Interview||==    == ||Company Name||==    == ||Duration||==    == ||Date And Time "
                            "||==     == ||Status||==")

            self.table_traverse(rows, cols)
        else:
            log.logger.info("There's No Data Available")

    def filter_the_multiway_interview_via_designation(self):
        log.logger.info(
            "****==Filter The List Of Multiway Interview Via Interview Designation ===***")
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            Designation = self.get_element_text(self.interviewDesignation)
            log.logger.info("Interview Designation On UI == " + str(Designation))
            time.sleep(0.5)
            self.do_send_key(self.searchInput, Designation)
            time.sleep(0.5)
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
            log.logger.info(" Filter data upon == ||Interview Designation|| ")
            self.filter_via_designation_multiway(rows2, cols2, Designation)
            time.sleep(1)
            self.de_click(self.closeIcon)
            time.sleep(1)
        else:
            log.logger.info("There's No Data Available")

    def filter_the_multiway_interview_via_company(self):
        log.logger.info(
            "****==Filter The List Of Multiway Interview Company Name ===***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            cName = self.get_element_text(self.companyName)
            log.logger.info("Company Name On UI == " + str(cName))
            time.sleep(0.5)
            self.do_send_key(self.searchInput, cName)
            time.sleep(0.5)
            self.de_click(self.searchButton)

            time.sleep(2)

            # Fetch The data from table using search box
            rows3 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols3 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows3))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols3))
            log.logger.info(" Filter data upon == ||Company Name|| ")
            self.filter_via_company_name(rows3, cols3, cName)
            time.sleep(1)
            self.de_click(self.closeIcon)
            time.sleep(1)
        else:
            log.logger.info("There's No Data Available")

    def filter_the_multiway_interview_via_status(self):
        log.logger.info(
            "****==Filter The List Of Multiway Interview via Status ===***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            Status = self.get_element_text(self.interviewStatus)
            log.logger.info("Interview Status On UI == " + str(Status))
            time.sleep(0.5)
            self.do_send_key(self.searchInput, Status)
            time.sleep(0.5)
            self.de_click(self.searchButton)

            time.sleep(2)

            # Fetch The data from table using search box
            rows4 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols4 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows4))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols4))
            log.logger.info(" Filter data upon == ||Company Name|| ")
            self.filter_via_interview_status(rows4, cols4, Status)
            time.sleep(1)
            self.de_click(self.closeIcon)
            time.sleep(1)
        else:
            log.logger.info("There's No Data Available")

    def fetch_details_of_individual_interview(self):
        log.logger.info(
            "****==Fetch the detail of individual interview of multiway  ===***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            totalElements = len(self.driver.find_elements(By.XPATH,
                                                          "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr/td[5]/div/div[2]/*[local-name()='svg'][@class='fill-ime-blue-gray-700 mr-[12px] dark:fill-ime-blue-gray-200']"))
            log.logger.info("Total Interviews == " + str(totalElements))
            for i in range(totalElements):
                if i < 10:
                    viewButton = []
                    viewButton = self.driver.find_elements(By.XPATH,
                                                           "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr/td[5]/div/div[2]/*[local-name()='svg'][@class='fill-ime-blue-gray-700 mr-[12px] dark:fill-ime-blue-gray-200']")

                    self.driver.execute_script("arguments[0].scrollIntoView();", viewButton[i])

                    viewButton[i].click()

                    time.sleep(4)

                    rows = 1 + len(self.driver.find_elements(By.XPATH,
                                                             "//div[@class='max-w-[675px] border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden mr-[20px]']/table/tbody/tr"))

                    # Obtain the number of columns in table
                    cols = len(self.driver.find_elements(By.XPATH,
                                                         "//div[@class='max-w-[675px] border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden mr-[20px]']/table/tbody/tr/td[2]"))

                    # Print rows and columns
                    log.logger.info("Number Of Row" + str(rows))
                    log.logger.info("Number Of Column" + str(cols))
                    log.logger.info(
                        "**||Service||**              **||Query Mail||**               **||Date And Time||**        "
                        "**||Duration||**        **||Linked One Way Interview||**  ")

                    # Printing the data of the table
                    for r in range(1, rows):
                        for p in range(1, 2):
                            # obtaining the text from each column of the table
                            value = self.driver.find_element(By.XPATH,
                                                             "//div[@class='max-w-[675px] border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden mr-[20px]']/table/tbody/tr[" + str(
                                                                 r) + "]/td[2]").text

                            log.logger.info("" + str(value))
                            time.sleep(0.5)

                    time.sleep(0.5)

                    Description = self.get_element_text(self.descriptionOfInterview)
                    log.logger.info("Description Of Interview Is === " + str(Description))
                    time.sleep(0.5)
                    self.de_click(self.backArrow)
                    time.sleep(1)

                else:
                    log.logger.info("All Interview Details Has Been Fetched")

        else:
            log.logger.info("There's No Data Available")