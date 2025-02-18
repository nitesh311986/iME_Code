from selenium.common import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import logging
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEApplicant.pageObjects.BasePage import BasePage
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class iME_Queue(BasePage):
    iMEQueueIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[4]/a")

    DesignationTitle = (By.XPATH,
                        "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr[1]/td[1]/div/div[1]")

    companyTitle = (By.XPATH,
                    "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr[1]/td[3]/div/div[1]")
    serviceTitle = (By.XPATH,
                    "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr[1]/td[4]/div/div[1]")
    searchButton = (By.CSS_SELECTOR,
                    "button[class='ml-[16px] rounded-[4px] border-none bg-gradient-to-b from-purple-500 to-pink-500 p-[1px] w-[87px]']")
    searchInput = (By.XPATH, "//div[@id='search']/div[2]/input")

    closeIcon = (By.XPATH,
                 "//div[@id='search']/div[2]/*[local-name()='svg'][@class='fill-black dark:fill-white scale-[180%] h-[12px] cursor-pointer mt-3 relative right-2']")
    numberOfInterview = (By.XPATH,
                         "//div[@class='w-full h-full min-h-screen overflow-hidden duration-300 flex flex-col ml-[250px]']/div/div[3]/div/div/div[1]/h1")
    acceptButton = (By.XPATH,
                    "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr[1]/td[4]/div/div[2]/div[2]/button")

    oneWayInterviewIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[5]/a")

    statusOfInterview = (By.XPATH,
                         "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr[1]/td[4]/div/div[2]/button")

    description = (By.XPATH, "//div[@class='max-w-[675px] overflow-hidden']/div")

    backButton = (By.XPATH, "//div[@class='hidden lg:flex items-center']/h2")

    awardTab = (By.XPATH,
                "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[2]")
    marketingTab = (By.XPATH,
                    "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[3]")
    learningTab = (By.XPATH,
                   "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[4]")
    auditionTab = (By.XPATH,
                   "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[5]")
    admissionTab = (By.XPATH,
                    "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[6]")

    interviewType = (By.XPATH,
                     "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr[1]/td[2]/div/div[1]")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_iME_Queue_icon(self):
        time.sleep(3)
        currentURL = self.driver.current_url
        log.logger.info(
            "==User Is On The Page=== " + currentURL)
        try:
            # Attempt to perform the click action
            self.de_click(self.iMEQueueIcon)
        except NoSuchElementException:
            # Handle case where the element is not found
            print("The element to click was not found.")
        except ElementNotInteractableException:
            # Handle case where the element is present but not clickable
            print("The element is not interactable.")
        except Exception as e:
            # Handle any other unexpected exceptions
            print(f"An unexpected error occurred while clicking the element: {e}")
        time.sleep(4)

    def fetch_interviews_details_via_service(self):

        log.logger.info("****==Filter Interview Details using search box via service type details of ===***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            serviceName = self.get_element_text(self.serviceTitle)
            time.sleep(0.5)
            self.do_send_key(self.searchInput, serviceName)
            time.sleep(1)

            self.de_click(self.searchButton)

            time.sleep(2)

            # Fetch The data from table using search box
            rows2 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols2 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows2))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols2))
            log.logger.info(" Filter data upon == ||Service Type|| ")

            for r2 in range(1, rows2):
                for p2 in range(1, 2):
                    # obtaining the text from each column of the table
                    if r2 <= 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr[" + str(
                                                             r2) + "]/td[4]/div[1]/div").text

                        log.logger.info("" + str(value))
                        assert serviceName in value
                        log.logger.info(
                            "<< !! Filter interview list using Search box via service type ===  "
                            "!!>>" + str(serviceName) + " === executed Successfully")
                    else:
                        break
        else:
            log.logger.info("There's No Data Available")

    def fetch_interviews_details_via_company(self):
        global companyName
        log.logger.info("****==Filter Interview Details using search box via company name===***")
        time.sleep(1)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            self.de_click(self.closeIcon)
            time.sleep(1)
            try:
                companyName = self.get_element_text(self.companyTitle)
                time.sleep(0.5)
                self.do_send_key(self.searchInput, companyName)
            except NoSuchElementException as e:
                print(f"Element not found: {str(e)}")
            except TimeoutException as e:
                print(f"Timeout waiting for element: {str(e)}")

            time.sleep(1)
            self.de_click(self.searchButton)
            time.sleep(2)

            # Fetch The data from table using search box
            rows2 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols2 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows2))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols2))
            log.logger.info(" Filter data upon == ||Company Name|| ")

            for r2 in range(1, rows2):
                for p2 in range(1, 2, 4):
                    # obtaining the text from each column of the table
                    if r2 <= 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr[" + str(
                                                             r2) + "]/td[3]/div[1]/div").text

                        log.logger.info("" + str(value))
                        assert value == companyName
                        log.logger.info(
                            "<< !! Filter interview list using Search box via company name ===  "
                            "!!>>" + str(companyName) + " === executed Successfully")
                    else:
                        break
        else:
            log.logger.info("There's No Data Available")

    def fetch_interviews_details_via_designation(self):

        log.logger.info("****==Filter Interview Details using search box via Designation ===***")
        time.sleep(1)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            self.de_click(self.closeIcon)
            time.sleep(1)
            designationName = self.get_element_text(self.DesignationTitle)
            time.sleep(0.5)
            self.do_send_key(self.searchInput, designationName)
            time.sleep(1)

            self.de_click(self.searchButton)

            time.sleep(2)

            # Fetch The data from table using search box
            rows2 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols2 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows2))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols2))
            log.logger.info(" Filter data upon == ||Designation|| ")

            for r2 in range(1, rows2):
                for p2 in range(1, 2):
                    # obtaining the text from each column of the table
                    if r2 <= 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr[" + str(
                                                             r2) + "]/td[1]/div[1]/div").text

                        log.logger.info("" + str(value))
                        assert value == designationName
                        log.logger.info(
                            "<< !! Filter interview list using Search box via designation name ===  "
                            "!!>>" + str(designationName) + "=== executed Successfully")
                    else:
                        break
        else:
            log.logger.info("There's No Data Available")

    def verify_status_of_accepted_interview(self):

        log.logger.info("****== Verify the feature of accept button on iME Queue ===***")
        time.sleep(1)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            time.sleep(1)
            self.do_send_key(self.searchInput, "invite")
            time.sleep(1)
            self.de_click(self.searchButton)
            time.sleep(2)
            dataInvite = self.driver.find_element(By.XPATH,
                                                  "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody")
            valueInvite = dataInvite.text
            # log.logger.info("" + value)
            if len(valueInvite) > 0:
                serviceName = self.get_element_text(self.serviceTitle)
                time.sleep(1)

                # Fetch The data from table using search box
                rows2 = 1 + len(self.driver.find_elements(By.XPATH,
                                                          "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr"))

                # Obtain the number of columns in table
                cols2 = len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr[1]/td"))

                # Print rows and columns
                log.logger.info("Number Of Rows During Filter Operation = " + str(rows2))
                log.logger.info("Number Of Columns During Filter Operation = " + str(cols2))

                for r2 in range(1, 2):
                    for p2 in range(1, 2):
                        Designation = self.driver.find_element(By.XPATH,
                                                               "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr[1]/td[1]").text

                        self.de_click(self.acceptButton)
                        time.sleep(15)
                        url = self.driver.current_url

                log.logger.info("Applicant Accepts Interview For Designation === " + str(Designation))
                log.logger.info(" Url Of Landing Page Of Interview === " + str(url))
                self.driver.back()
                time.sleep(4)

                self.de_click(self.oneWayInterviewIcon)
                time.sleep(5)
                if serviceName == "Recruitment":
                    interviewValue = self.driver.find_element(By.XPATH,
                                                              "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[1]").text
                    time.sleep(0.5)
                    statusOfInterview1 = self.get_element_text(self.statusOfInterview)
                    time.sleep(1)
                    log.logger.info("Status Of Interview === " + str(statusOfInterview1))
                    assert Designation == interviewValue
                    assert statusOfInterview1 == "Start Interview"
                elif serviceName == "Awards":
                    time.sleep(0.5)
                    self.de_click(self.awardTab)
                    time.sleep(3)
                    interviewValue = self.driver.find_element(By.XPATH,
                                                              "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[1]").text
                    time.sleep(0.5)
                    statusOfInterview1 = self.get_element_text(self.statusOfInterview)
                    time.sleep(1)
                    log.logger.info("Status Of Interview === " + str(statusOfInterview1))
                    assert Designation == interviewValue
                    assert statusOfInterview1 == "Start Interview"
                elif serviceName == "Marketing":
                    time.sleep(0.5)
                    self.de_click(self.marketingTab)
                    time.sleep(3)
                    interviewValue = self.driver.find_element(By.XPATH,
                                                              "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[1]").text
                    time.sleep(0.5)
                    statusOfInterview1 = self.get_element_text(self.statusOfInterview)
                    time.sleep(1)
                    log.logger.info("Status Of Interview === " + str(statusOfInterview1))
                    assert Designation == interviewValue
                    assert statusOfInterview1 == "Start Interview"

                elif serviceName == "Learning":
                    time.sleep(0.5)
                    self.de_click(self.learningTab)
                    time.sleep(3)
                    interviewValue = self.driver.find_element(By.XPATH,
                                                              "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[1]").text
                    time.sleep(0.5)
                    statusOfInterview1 = self.get_element_text(self.statusOfInterview)
                    time.sleep(1)
                    log.logger.info("Status Of Interview === " + str(statusOfInterview1))
                    assert Designation == interviewValue
                    assert statusOfInterview1 == "Start Interview"
                elif serviceName == "Auditions":
                    time.sleep(0.5)
                    self.de_click(self.auditionTab)
                    time.sleep(3)
                    interviewValue = self.driver.find_element(By.XPATH,
                                                              "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[1]").text
                    time.sleep(0.5)
                    statusOfInterview1 = self.get_element_text(self.statusOfInterview)
                    time.sleep(1)
                    log.logger.info("Status Of Interview === " + str(statusOfInterview1))
                    assert Designation == interviewValue
                    assert statusOfInterview1 == "Start Interview"

                elif serviceName == "Admissions":
                    time.sleep(0.5)
                    self.de_click(self.admissionTab)
                    time.sleep(3)
                    interviewValue = self.driver.find_element(By.XPATH,
                                                              "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[1]").text
                    time.sleep(0.5)
                    statusOfInterview1 = self.get_element_text(self.statusOfInterview)
                    time.sleep(1)
                    log.logger.info("Status Of Interview === " + str(statusOfInterview1))
                    assert Designation == interviewValue
                    assert statusOfInterview1 == "Start Interview"

                else:
                    log.logger.info("Interview Request Has Not generated")
            else:
                log.logger.info("There's No Interview Request Is Available")
        else:
            log.logger.info("There's No Data Available")

    def view_details_of_individual_interview(self):

        log.logger.info("****==Fetch Details Of  Individual Interview ===***")
        time.sleep(1)

        try:

            dataAvail = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody"))
            )

            value = dataAvail.text
        except NoSuchElementException as e:
            print(f"Element not found: {str(e)}")
        except TimeoutException as e:
            print(f"Timeout waiting for element: {str(e)}")

        # log.logger.info("" + value)
        if len(value) > 0:
            self.de_click(self.closeIcon)
            time.sleep(1)
            totalInterviews = len(self.driver.find_elements(By.XPATH,
                                                            "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr/td[4]/div/div[2]/*[local-name()='svg'][@class='fill-ime-blue-gray-700 mr-[12px] dark:fill-ime-blue-gray-200']"))

            for i in range(10):
                elements = []
                elements = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='mt-[10px] rounded-md overflow-hidden border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600']/table/tbody/tr/td[4]/div/div[2]/*[local-name()='svg'][@class='fill-ime-blue-gray-700 mr-[12px] dark:fill-ime-blue-gray-200']")
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
            log.logger.info("There's No Data Available")
