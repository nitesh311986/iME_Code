from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import logging
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEApplicant.pageObjects.BasePage import BasePage
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class contentLibrary(BasePage):
    contentLibrary = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[3]/a")
    documentName = (By.XPATH,
                    "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr[1]/td[2]/div/div[1]/div[1]/span")
    documentType = (By.XPATH,
                    "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr[1]/td[3]/div/div")
    inputCheckBox = (By.XPATH,
                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr[1]/td[1]/div/div/div/input")
    deleteButton = (By.XPATH, "//div[@class='flex space-x-4 ml-auto mt-4']/button[2]")
    popUpDeleteButton = (By.XPATH,
                         "//div[@class='flex flex-col w-full text-ime-gray-500 dark:text-ime-gray-400 text-[14px]']/div/div[2]/button[1]")
    settingButton = (By.XPATH,
                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr[1]/td[8]/div/button")
    editButton = (By.XPATH, "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-["
                            "10px] rounded-md mb-20']/table/tbody/tr[1]/td[8]/div/div/button[1]")
    updateFileNameInput = (By.XPATH,
                           "//div[@class='flex flex-col w-full text-ime-gray-500 dark:text-ime-gray-400 text-[14px]']/form/div[1]/div/input")
    saveButton = (
        By.XPATH,
        "//div[@class='flex flex-col w-full text-ime-gray-500 dark:text-ime-gray-400 text-[14px]']/form/button")
    documentTitle = (By.XPATH,
                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr[1]/td[2]/div/div/div[1]/span")

    # Search

    searchBox = (By.XPATH,
                 "//div[@class='flex flex-col md:flex-col lg:flex-row justify-between items-center']/div[1]/div/div/div[2]/input")
    closeIcon = (By.XPATH,
                 "//div[@class='flex flex-col md:flex-col lg:flex-row justify-between items-center']/div[1]/div/div/div[2]/*[local-name()='svg'][@class='fill-black dark:fill-white scale-[180%] h-[12px] cursor-pointer mt-3 relative right-2']")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_content_Library(self):
        time.sleep(3)
        currentURL = self.driver.current_url
        log.logger.info(
            "==User Is On The Page=== " + currentURL)
        try:
            # Attempt to perform the click action
            self.de_click(self.contentLibrary)
        except NoSuchElementException:
            # Handle case where the element is not found
            print("The element to click was not found.")
        except ElementNotInteractableException:
            # Handle case where the element is present but not clickable
            print("The element is not interactable.")
        except Exception as e:
            # Handle any other unexpected exceptions
            print(f"An unexpected error occurred while clicking the element: {e}")
        time.sleep(3)

    def delete_files(self):
        log.logger.info("****==Delete Document From Content Library Content Test Case===***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            time.sleep(1.5)
            self.de_click(self.inputCheckBox)
            time.sleep(1.5)
            self.de_click(self.deleteButton)
            time.sleep(2)
            self.de_click(self.popUpDeleteButton)
            time.sleep(3)
            log.logger.info("Item Has been deleted successfully form content library")
        else:
            log.logger.info("There's No Data Available")

    def update_file_title(self):
        log.logger.info("****==Update File Title Of Content Library Test Case===***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            self.de_click(self.settingButton)
            time.sleep(1.5)
            self.de_click(self.editButton)
            time.sleep(1)
            self.do_clear_using_java_script(self.updateFileNameInput)
            time.sleep(1)
            self.do_send_key(self.updateFileNameInput, "")
            time.sleep(1)
            self.do_send_key(self.updateFileNameInput, "Update Title")
            self.de_click(self.saveButton)
            time.sleep(4)
            title = self.get_element_text(self.documentTitle)
            # assert "update title" in title
            log.logger.info("Updated Title == "+str(title))
            log.logger.info("****==Title has been updated successfully===***")

        else:
            log.logger.info("There's No Data Available")

    def fetch_all_details_of_content_library(self):
        log.logger.info("****==Fetch All Documents Details OF Content Library===***")
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            rows2 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols2 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows2))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols2))
            log.logger.info(
                " Documents Details == ||Document Title||     ||File Type||     ||Date Added||    ||Visibility||     ||File Size|| ")

            for r in range(1, rows2):
                for c in range(2, cols2 - 1, ):
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr[" + str(
                                                         r) + "]/td[" + str(c) + "]/div/div").text

                    log.logger.info("" + str(value))

            time.sleep(2)
        else:
            log.logger.info("There's No Data Available")

    def search_content_library_items_via_document_type(self):
        log.logger.info("****==Filter Content Library items using search box via document type Test Case===***")
        time.sleep(1)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            document_Type = self.get_element_text(self.documentType)
            time.sleep(0.5)
            self.do_send_key(self.searchBox, document_Type)
            time.sleep(1)

            # Fetch The data from table using search box
            rows = 1 + len(self.driver.find_elements(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols = len(self.driver.find_elements(By.XPATH,
                                                 "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols))
            log.logger.info(" Filter data upon == ||Document Type|| ")

            for r2 in range(1, rows):
                for p2 in range(1, 2):
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr[" + str(
                                                         r2) + "]/td[3]/div/div").text

                    log.logger.info("" + str(value))
                    assert value == document_Type
                    log.logger.info("<< !! Filter content library list using Search box via document type ===  "
                                    "!!>>" + str(document_Type) + "=== executed Successfully")

            time.sleep(1)
            self.de_click(self.closeIcon)
        else:
            log.logger.info("There's No Data Available")

    def search_content_library_items_via_document_title(self):
        time.sleep(1)
        log.logger.info("****==Filter Content Library items using search box via document title Test Case===***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            document_Title = self.get_element_text(self.documentName)
            time.sleep(0.5)
            self.do_send_key(self.searchBox, document_Title)
            time.sleep(1)

            rows1 = 1 + len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr"))

            # Obtain the number of columns in table
            cols1 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr[1]/td"))

            # Print rows and columns
            log.logger.info("Number Of Rows During Filter Operation = " + str(rows1))
            log.logger.info("Number Of Columns During Filter Operation = " + str(cols1))
            log.logger.info(" Filter data upon == ||Document Title|| ")

            for r2 in range(1, rows1):
                for p2 in range(1, 2):
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr[" + str(
                                                         r2) + "]/td[2]/div/div").text

                    log.logger.info("" + str(value))
                    assert value == document_Title
                    log.logger.info(
                        "<< !! Filter content library list using Search box via document title ===  "
                        "!!>>" + str(document_Title) + "=== executed Successfully")

            self.de_click(self.closeIcon)
            time.sleep(0.5)
        else:
            log.logger.info("There's No Data Available")
