from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import logging
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEApplicant.pageObjects.BasePage import BasePage
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class iME_Queue_MultiWay(BasePage):
    iMEMultiwayIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[6]/a")
    videoInterviewTitle = (By.XPATH,"//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[1]/div/div[1]")

    searchInput = (By.XPATH, "//div[@id='search']/div[2]/input")
    searchButton = (By.CSS_SELECTOR,
                    "button[class='ml-[16px] rounded-[4px] border-none bg-gradient-to-b from-purple-500 to-pink-500 p-[1px] w-[87px]']")

    closeIcon = (By.XPATH,
                 "//div[@id='search']/div[2]/*[local-name()='svg'][@class='fill-black dark:fill-white scale-[180%] h-[12px] cursor-pointer mt-3 relative right-2']")

    videoInterviewStatus = (By.XPATH,"//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[5]/div/div[1]")
    interviewSlotButton = (By.CSS_SELECTOR,
                           "button[class='border group border-ime-blue-gray-300 text-ime-blue-gray-200 dark:text-ime-blue-gray-700 rounded flex col-span-2 md:col-span-1 p-2 w-full ']")

    submitButton = (By.CSS_SELECTOR,
                    "button[class='ml-auto mt-4 rounded-[4px] transition-colors h-[32px] px-[22px] text-xs bg-ime-accent hover:bg-blue-700 text-white']")

    # Webinar Section
    webinarIcon = (By.XPATH,"//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[2]")
    webinarTitle = (By.XPATH,"//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[1]/td[1]/div/div[1]")

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
            self.de_click(self.iMEMultiwayIcon)
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

    def view_multiway_video(self):

        log.logger.info("****==Filter List Of Multiway Video Call Interview Via Interview Title===***")

        dataAvail = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )

        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            interviewName = self.get_element_text(self.videoInterviewTitle)
            time.sleep(0.5)
            self.do_send_key(self.searchInput, interviewName)
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
            log.logger.info(" Filter data upon == ||Interview Title|| ")

            for r2 in range(1, rows2):
                for p2 in range(1, 2):
                    # obtaining the text from each column of the table
                    if r2 <= 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                             r2) + "]/td[1]/div/div[1]").text

                        log.logger.info("" + str(value))
                        assert interviewName in value
                        log.logger.info(
                            "<< !! Filter multiway video call list using Search box via interview title ===  "
                            "!!>>" + str(interviewName) + "=== executed Successfully")
                    else:
                        break

        else:
            log.logger.info("There's No Data Available")

        self.de_click(self.closeIcon)
        time.sleep(1)

        # 1.2 Filter List Of Video Call Via Interview Status

        log.logger.info("****==Filter List Of Multiway Video Call Interview Via Interview Status===***")

        dataAvail = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )

        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            interviewStatus = self.get_element_text(self.videoInterviewStatus)
            time.sleep(0.5)
            self.do_send_key(self.searchInput, interviewStatus)
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
            log.logger.info(" Filter data upon == ||Interview Status|| ")

            for r2 in range(1, rows2):
                for p2 in range(1, 2):
                    # obtaining the text from each column of the table
                    if r2 <= 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                             r2) + "]/td[5]/div/div[1]").text

                        log.logger.info("" + str(value))
                        assert interviewStatus in value
                        log.logger.info(
                            "<< !! Filter multiway video call list using Search box via interview Status ===  "
                            "!!>>" + str(interviewStatus) + "=== executed Successfully")
                    else:
                        break

        else:
            log.logger.info("There's No Data Available")

        self.de_click(self.closeIcon)
        time.sleep(1)

    def view_multiway_webinar(self):

        log.logger.info("****==Filter List Of Multiway Webinar Call Interview Via Interview Title===***")

        self.de_click(self.webinarIcon)
        time.sleep(3)
        dataAvail = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody"))
        )

        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            webinarName = self.get_element_text(self.webinarTitle)
            time.sleep(0.5)
            self.do_send_key(self.searchInput, webinarName)
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
            log.logger.info(" Filter data upon == ||Interview Title|| ")

            for r2 in range(1, rows2):
                for p2 in range(1, 2):
                    # obtaining the text from each column of the table
                    if r2 <= 10:
                        value = self.driver.find_element(By.XPATH,
                                                         "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                             r2) + "]/td[1]/div/div[1]").text

                        log.logger.info("" + str(value))
                        assert webinarName in value
                        log.logger.info(
                            "<< !! Filter multiway webinar call list using Search box via webinar title ===  "
                            "!!>>" + str(webinarName) + "=== executed Successfully")
                    else:
                        break

        else:
            log.logger.info("There's No Data Available")

        self.de_click(self.closeIcon)
        time.sleep(1)



