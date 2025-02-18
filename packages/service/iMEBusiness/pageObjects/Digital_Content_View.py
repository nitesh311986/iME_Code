import time
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEBusiness.Utilities.customLogger import Logger
from iMEBusiness.pageObjects.BasePage import BasePage

log = Logger(__name__, logging.INFO)


class Digital_Content_View(BasePage):
    digitalContentIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[3]")
    documentTitle = (By.XPATH,
                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[2]/div/div[2]")
    closeIconOfSearchBox = (By.XPATH,
                            "//div[@class='flex flex-col lg:flex-row justify-between pt-5 pb-8 items-center']/div[1]/div[1]/div/*[local-name()='svg'][@class='fill-black dark:fill-white scale-[180%] cursor-pointer mt-4 h-[14px] relative right-2']")

    viewDetailsOfDocument = (By.XPATH,
                             "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600 py-1']/table/tbody/tr/td[9]/div/div/a[2]")

    # Details Of Documents

    documentLink = (By.XPATH, "//div[@class='hidden justify-between lg:flex']/div[1]/span")

    titleOfDocumnet = (By.XPATH,
                       "//div[@class='grid grid-cols-3 gap-4 pb-8']/div[1]/div[2]/div/input")

    Description = (By.XPATH,
                   "//div[@class='grid grid-cols-3 gap-4 pb-8']/div[1]/div[3]/div/textarea")
    totalPurchase = (By.XPATH, "//div[@class='col-span-3 lg:col-span-1']/div[2]/div[1]/p")
    totalAmount = (By.XPATH, "//div[@class='col-span-3 lg:col-span-1']/div[2]/div[2]/p")

    amount = (By.XPATH,
              "//div[@class='col-span-3 lg:col-span-1']/div[5]/div/input")
    paymentType = (By.XPATH,
                   "//div[@class='col-span-3 lg:col-span-1']/div[4]/button")

    backToStreamIcon = (By.XPATH, "//div[@class='flex justify-between items-center pb-5']/a")

    # Delete Stream

    cogIcon = (By.XPATH,
               "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[9]/div/button/*[local-name()='svg']")
    deleteIcon = (By.XPATH,
                  "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[9]/div/div/button[1]")
    deleteButton = (By.XPATH, "//div[@class='flex gap-4 mt-5 mb-9']/button[1]")
    deleteButtonForBulk = (By.XPATH,
                           "//div[@class='flex flex-col md:flex-row w-full lg:w-fit md:justify-end items-end gap-4 mt-4 lg:mt-7']/button")

    # Bulk Delete

    checkBoxOne = (By.XPATH,
                   "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[1]/div/div/input")
    checkBoxTwo = (By.XPATH,
                   "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[2]/td[1]/div/div/input")

    # fetch data via search box

    searchBox = (By.CSS_SELECTOR, "input[name='searchName']")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_digital_content_icon(self):
        time.sleep(5)
        self.de_click(self.digitalContentIcon)
        time.sleep(4)

    def fetch_digital_content_details(self):
        log.logger.info("****==View list of Digital Content Items Test Case Starts Here==***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            rows = len(self.driver.find_elements(By.XPATH,
                                                 "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr"))

            cols = len(self.driver.find_elements(By.XPATH,
                                                 "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td"))
            log.logger.info("Number Of Row == " + str(rows))
            log.logger.info("Number Of Column == " + str(cols))
            log.logger.info("**||Name||**        **||File Type||**        **||Modified||**      "
                            "**||Visibility||**     **||Paid||**       ")

            self.table_traverse_of_digital_content(rows, cols)
        else:
            log.logger.info("There's No Data Available")

        # 1.1 filter list of recruitment interviews via search box
        # log.logger.info("****==Filter list of digital content items via search box using document name "
        #                 " test case starts here==***")
        #
        # time.sleep(1)
        #
        # dataAvail = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH,
        #                                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody"))
        # )
        # value = dataAvail.text
        # # log.logger.info("" + value)
        # if len(value) > 0:
        #
        #     is_document_titile_visible = self.driver.find_element(By.XPATH,
        #                                                           "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[2]/div/div[2]").is_displayed()
        #
        #     value = str(is_document_titile_visible)
        #     if value == "True":
        #         Title = self.get_element_text(self.documentTitle)
        #         time.sleep(0.5)
        #     else:
        #         log.logger.info("No Information Available")
        #     time.sleep(0.5)
        #     self.do_send_key(self.searchBox, Title)
        #     time.sleep(1.5)
        #
        #     rows1 = len(self.driver.find_elements(By.XPATH,
        #                                           "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr"))
        #
        #     cols1 = len(self.driver.find_elements(By.XPATH,
        #                                           "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td"))
        #
        #     log.logger.info("Number Of Row == " + str(rows1))
        #     log.logger.info("Number Of Column == " + str(cols1))
        #     log.logger.info("**||Document Title||** ")
        #
        #     self.table_traverse_search_digital_content(rows1, cols1, Title)
        #     self.de_click(self.closeIconOfSearchBox)
        #     time.sleep(1)
        # else:
        #     log.logger.info("There's No Data Available")

    def test_fetch_details_of_each_document(self):
        log.logger.info("****==View Details Of individual Document===***")
        time.sleep(1)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody"))
        )

        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            totalDocument = len(self.driver.find_elements(By.XPATH,
                                                          "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr"))

            for i in range(totalDocument):

                if i < 8:
                    paymentOption = []

                    paymentOption = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_all_elements_located((By.XPATH,
                                                             "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[7]/span"))
                    )

                    payment = paymentOption[i].text

                    elements = []
                    elements = self.driver.find_elements(By.XPATH,
                                                         "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[9]/div/button/*[local-name()='svg']")
                    elements[i].click()
                    time.sleep(1)
                    self.de_click(self.viewDetailsOfDocument)
                    log.logger.info(
                        "!!! == User Has clicked view details link against documnet  title == !!!")
                    time.sleep(4)

                    log.logger.info("Please Find Details Of |Document Link|   |Title|   |Discription|      "
                                    " |Total Purchase|  |Total Amount|  |Payment Type|  |Amount| Of Documnet")

                    videoLinkOfStream = self.get_element_text(self.documentLink)
                    log.logger.info("Video Link Of Stream Is === " + str(videoLinkOfStream))
                    time.sleep(0.5)
                    Title = self.get_attribute(self.titleOfDocumnet, "value")
                    log.logger.info("Title Of Stream Is === " + str(Title))
                    time.sleep(0.5)
                    descriptionOfDocument = self.get_element_text(self.Description)
                    log.logger.info("Description Of Stream Is === " + str(descriptionOfDocument))
                    time.sleep(0.5)
                    if payment == "No":
                        paymentType = self.get_element_text(self.paymentType)
                        log.logger.info("Payment Type Of Stream Is === " + str(paymentType))
                        time.sleep(0.5)

                    else:
                        purchase = self.get_element_text(self.totalPurchase)
                        log.logger.info("Total Purchase For Streaming Is === " + str(purchase))
                        amount = self.get_element_text(self.totalAmount)
                        log.logger.info("Total Amount Paid For Streaming Is === " + str(amount))
                        amountOfStream = self.get_attribute(self.amount, "value")
                        log.logger.info("Amount Of Stream Is === " + str(amountOfStream))
                        time.sleep(0.5)

                    self.de_click(self.backToStreamIcon)
                    time.sleep(1)

        else:
            log.logger.info("There's No Data Available")

    def test_delete_individual_item(self):

        log.logger.info("****== Test Case To Delete Individual Item )f Digital Content ===***")
        time.sleep(1)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody"))
        )

        value = dataAvail.text

        if len(value) > 0:
            for j in range(10):
                try:
                    # Locate the table (replace 'table' with the appropriate selector)
                    table = self.driver.find_element(By.TAG_NAME, 'table')

                    # Count the rows (assuming rows are represented by <tr> elements)
                    rows = table.find_elements(By.TAG_NAME, 'tr')

                    # Check if the table has data
                    if len(rows) == 0:
                        print("No data found in the table.")
                    else:
                        visibility = []
                        visibility = self.driver.find_elements(By.XPATH,
                                                               "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[5]/span")

                        cogIcon = []
                        cogIcon = self.driver.find_elements(By.XPATH,
                                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[9]/div/button")

                        for i in range(len(visibility)):
                            vName = str(visibility[i].text)
                            print(f"Visibility Status: {vName}")  # Use print or proper logging
                            # log.logger.info("Visibility Status", vName)

                            if vName != "Video Pending":
                                cogIcon[i].click()
                                time.sleep(1)

                                locator = (By.XPATH,
                                           f"//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[{i + 1}]/td[9]/div/div/button[1]")
                                wait = WebDriverWait(self.driver, 20)  # Increase timeout to 20 seconds

                                # Wait until the element is visible and enabled
                                element = wait.until(EC.element_to_be_clickable(locator))

                                # Interact with the element
                                element.click()
                                self.de_click(self.deleteButton)
                                time.sleep(2)
                                break
                            else:
                                log.logger.info("Not Allowed To Delete")

                        break

                except Exception as e:
                    print(f"An error occurred: {e}")




        else:
            log.logger.info("Not Item To delete")

    def test_delete_bulk_item(self):

        log.logger.info("****== Test Case To Delete  Bulk  Item of Digital Content ===***")
        time.sleep(1)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody"))
        )

        value = dataAvail.text

        if len(value) > 0:
            for j in range(10):
                try:
                    # Locate the table (replace 'table' with the appropriate selector)
                    table = self.driver.find_element(By.TAG_NAME, 'table')

                    # Count the rows (assuming rows are represented by <tr> elements)
                    rows = table.find_elements(By.TAG_NAME, 'tr')

                    # Check if the table has data
                    if len(rows) != 0:
                        visibility = []
                        visibility = self.driver.find_elements(By.XPATH,
                                                               "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[5]/span")

                        totalItem = len(visibility)

                        if totalItem > 3:

                            for i in range(len(visibility)):
                                vName = str(visibility[i].text)
                                print(f"Visibility Status: {vName}")  # Use print or proper logging
                                # log.logger.info("Visibility Status", vName)

                                if vName != "Video Pending":
                                    self.de_click(self.checkBoxOne)
                                    time.sleep(0.5)
                                    self.de_click(self.checkBoxTwo)
                                    time.sleep(0.5)
                                    self.de_click(self.deleteButtonForBulk)
                                    time.sleep(1)
                                    self.de_click(self.deleteButton)
                                    time.sleep(2)
                                    break

                            break
                        else:
                            log.logger.info("There's No Enough Item For Bulk delete")
                    else:
                        log.logger.info("There's No Enough Item For Bulk delete")

                except Exception as e:
                    print(f"An error occurred: {e}")
        else:
            log.logger.info("There's No Item To delete")
