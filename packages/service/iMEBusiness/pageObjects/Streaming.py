import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Streaming(BasePage):
    streamingIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[2]/a")
    liveTab = (By.XPATH, "//div[@class='ime-tab-group w-full font-semibold flex flex-row ["
                         "&::-webkit-scrollbar]:hidden']/button[2]")

    searchBar = (By.CSS_SELECTOR,
                 "input[name='searchName']")
    ftitleDisplayed = (By.XPATH,
                       "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[2]/div/div[2]/div")
    titleDisplayed = (By.XPATH,
                      "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[2]/div/div[2]/div")

    closeIconOfSearchBox = (By.XPATH,
                            "//div[@id='search']/*[local-name()='svg'][@class='fill-black dark:fill-white scale-[180%] cursor-pointer mt-4 h-[14px] relative right-2']")

    viewDetailsOfLiveStreaming = (By.XPATH,
                                  "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[9]/div/div/a[1]")

    deleteStream = (By.XPATH,
                    "//div[@class='border border-ime-gray-300 dark:border-zinc-600 my-[10px] rounded-md']/table/tbody/tr/td[7]/div/div/button[2]")

    # Streaming Details

    videoLink = (By.XPATH, "//div[@class='border-b dark:border-ime-gray-600 flex justify-between']/div[1]")

    titleOfStream = (By.CSS_SELECTOR,
                     "input[name='title']")

    Description = (By.CSS_SELECTOR,
                   "textarea[name='description']")

    visibilityMode = (By.XPATH,
                      "//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[5]/button/div")
    visibilityModeWithNoPayment = (By.XPATH,
                                   "//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[4]/button/div")
    visibilityModeWithNoPaymentForPrivate = (By.XPATH, "//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[3]/button/div")

    visibilityModeDD = (By.XPATH,
                        "//div[@class='grid grid-cols-1 md:grid-cols-3 w-full lg:grid-cols-3 sm:gap-x-[16px]']/div[1]/div[4]/div[2]/div[1]/button/*[local-name()='svg']")
    publicOptionOfVisibility = (By.XPATH,
                                "//div[@class='grid grid-cols-1 md:grid-cols-3 w-full lg:grid-cols-3 sm:gap-x-[16px]']/div[1]/div[4]/div[2]/div[1]/ul/li[1]")
    privateOptionOfVisibility = (By.XPATH,
                                 "//div[@class='grid grid-cols-1 md:grid-cols-3 w-full lg:grid-cols-3 sm:gap-x-[16px]']/div[1]/div[4]/div[2]/div[1]/ul/li[2]")
    hiddenOptionOfVisibility = (By.XPATH,
                                "//div[@class='grid grid-cols-1 md:grid-cols-3 w-full lg:grid-cols-3 sm:gap-x-[16px]']/div[1]/div[4]/div[2]/div[1]/ul/li[3]")

    restrictionMode = (By.XPATH,
                       "//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[6]/button/div")
    restrictionModeWithPrivate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[5]/button/div")
    restrictionModeWithNoPayment = (By.XPATH,
                                    "//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[5]/button/div")
    restrictionModeWithNoPaymentForPrivate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[4]/button/div")
    restrictionModeDD = (By.XPATH,
                         "//div[@class='grid grid-cols-1 md:grid-cols-3 w-full lg:grid-cols-3 sm:gap-x-[16px]']/div[1]/div[4]/div[2]/div[2]/button/*[local-name()='svg']")
    noneOptionOfRestriction = (By.XPATH,
                               "//div[@class='grid grid-cols-1 md:grid-cols-3 w-full lg:grid-cols-3 sm:gap-x-[16px]']/div[1]/div[4]/div[2]/div[2]/ul/li[1]")
    eightyPlusOptionOfRestriction = (By.XPATH,
                                     "//div[@class='grid grid-cols-1 md:grid-cols-3 w-full lg:grid-cols-3 sm:gap-x-[16px]']/div[1]/div[4]/div[2]/div[2]/ul/li[2]")

    dateOfStream = (By.XPATH,
                    "//div[@class='grid grid-cols-1 md:grid-cols-3 w-full lg:grid-cols-3 sm:gap-x-[16px]']/div[1]/div[5]/div/div[1]/div/input")

    timeOfStream = (By.XPATH,
                    "//div[@class='grid grid-cols-1 md:grid-cols-3 w-full lg:grid-cols-3 sm:gap-x-[16px]']/div[1]/div[5]/div/div[2]/div/input")

    paymentStatics = (By.XPATH,
                      "//div[@class='grid grid-cols-1 md:grid-cols-3 w-full lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/div/div[1]/h4")

    paymentTypeOfStream = (By.XPATH,
                           "//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[3]/button/div")

    amountForStream = (By.XPATH,
                       "//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[4]/div[2]/input")
    amountForStreamForPrivate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[3]/div[2]/input")

    totalPurchase = (By.XPATH,
                     "//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[2]/div/div/div[1]/p")

    totalPurchaseWithPrivate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div/div/div/div[1]/p")

    totalAmount = (By.XPATH,
                   "//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[2]/div/div/div[2]/p")
    totalAmountWithPrivate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div/div/div/div[2]/p")


    backToStreamIcon = (By.XPATH, "//div[@class='flex justify-between items-center pb-5 p-8']/a")

    itemName = (By.XPATH,
                "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[3]/span")

    # Delete Stream Item
    firstItem = (By.XPATH,
                 "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[1]/div/div/input")

    deleteLink = (By.XPATH,
                  "//div[@class='border border-ime-gray-300 dark:border-zinc-600 my-[10px] rounded-md']/table/tbody/tr[1]/td[7]/div/div/button[2]")

    deleteButton = (By.XPATH,
                    "//div[@class='flex flex-col items-center justify-center text-center']/div/button[1]")

    # Update Stream

    updateTitle = (By.CSS_SELECTOR, "input[name='title']")
    updateDescription = (By.CSS_SELECTOR, "textarea[name='description']")

    applicantDDArrow = (By.XPATH,
                        "//div[@class='pl-4 py-3 border border-ime-gray-300 dark:border-ime-gray-600 rounded']/div/button")
    deleteIconOfApplicantDetails = (By.XPATH,
                                    "//div[@class='w-full flex flex-col border rounded-md border-zinc-300 dark:border-zinc-600 last:rounded-lg max-h-[22vh] overflow-y-scroll custom-scrollbar']/table/tbody/tr[1]/td[3]/*[local-name()='svg'")
    addApplicantButtonUpdate = (By.XPATH,"//div[@class='pl-4 py-3 border border-ime-gray-300 dark:border-ime-gray-600 rounded']/div[2]/div[1]/button")
    inviteApplicantUpdate= (By.XPATH, "//div[@class='w-full flex flex-row-reverse']/button")
    firstName = (By.CSS_SELECTOR, "input[name='firstName']")
    lastName = (By.CSS_SELECTOR, "input[name='lastName']")
    countryCode = (By.XPATH,"//div[@class='flex flex-row sm:gap-x-[16px] mt-8 w-full flex-wrap']/div[3]/div[1]/div/button")
    firstCountryCode = (By.XPATH,"//div[@class='flex flex-row sm:gap-x-[16px] mt-8 w-full flex-wrap']/div[3]/div[1]/div/div[1]")
    contactNumber = (By.CSS_SELECTOR, "input[name='contact']")
    Email = (By.CSS_SELECTOR, "input[name='email']")

    submitButton = (By.XPATH, "//div[@class='flex gap-2 md:ml-auto m-4']/button[2]")
    paymentDDValueUpdate = (By.XPATH,
                     "//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[3]/button/div")
    paymentDDUpdate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[3]/button")
    noneOptionOfPaymentDDUpdate = (By.XPATH,
                             "//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[3]/ul/li[1]")
    payNowOptionOfPaymentDDUpdate = (By.XPATH,
                                   "//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[3]/ul/li[2]")
    amountInputUpdate = (By.XPATH, "//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[3]/div[2]/input")

    visibilityModeValueUpdate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[5]/button/div")
    visibilityDDUpdate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[5]/button")
    publicOptionUpdate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[5]/ul/li[1]")
    privateOptionUpdate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[5]/ul/li[2]")
    hiddenOptionUpdate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[5]/ul/li[3]")

    ageDDValueUpdate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[6]/button/div")
    ageDDUpdate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[6]/button")
    noneOptionAgeUpdate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[6]/ul/li[1]")
    eightyPlusOptionUpdate = (By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[6]/ul/li[2]")
    updateButton = (By.XPATH,
                    "//div[@class='flex items-center justify-between w-full pb-16 mb-16']/div/button")



    deleteButtonBulk = (By.XPATH,
                        "//div[@class='flex flex-col md:flex-row w-full lg:w-fit md:justify-end items-end gap-4 mt-4 lg:mt-7']/button")

    # Upload Stream Section

    uploadTab = (By.XPATH,
                 "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[1]")

    titleOfUploadStream = (By.XPATH,
                           "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[2]/h5/div")

    viewDetailsOfUploadStreaming = (By.XPATH,
                                    "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr/td[7]/div/div/a")

    cogIcon = (By.XPATH,
               "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr/td[7]/div/button/*[local-name()='svg']")

    deleteLinkOfUpload = (By.XPATH,
                          "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr/td[7]/div/div/button[2]")

    deleteButtonOfUpload = (By.XPATH,
                            "//div[@class='flex flex-col w-full text-ime-gray-500 dark:text-ime-gray-400 text-[14px]']/div/div/button[1]")

    addApplicant = (By.CSS_SELECTOR,"button[class='rounded-[4px] transition-colors h-[32px] px-[22px] text-xs bg-ime-accent hover:bg-blue-700 text-white']")

    def __init__(self, driver, environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_streaming_icon(self):
        time.sleep(4)
        self.de_click(self.streamingIcon)
        time.sleep(4)

    def fetch_live_streaming_details(self):

        log.logger.info("****==View list of live streaming items starts here==***")
        # self.de_click(self.liveTab)
        # time.sleep(4)

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
            log.logger.info("**||Title||**        **||Date And Time ||**        **||Visibility||**      "
                            "**||Paid||**         ")

            self.table_traverse_of_stream(rows, cols)
        else:
            log.logger.info("There's No Data Available")

    def filter_live_stream_list_via_title(self):

        log.logger.info("****==Filter list of live streaming details via search box using item title "
                        "test case starts here==***")
        time.sleep(1)
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody"))
        )

        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            Name = self.get_element_text(self.itemName)

            if Name == "Folder":

                is_f_title_visible = self.driver.find_element(By.XPATH,
                                                              "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[2]/div/div[2]/div").is_displayed()

                value = str(is_f_title_visible)
                if value == "True":
                    f_titleName = self.get_element_text(self.ftitleDisplayed)
                    time.sleep(0.5)
                else:
                    log.logger.info("No Information Available")
                time.sleep(0.5)
                self.do_send_key(self.searchBar, f_titleName)
                time.sleep(1.5)

                rows1 = len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr"))

                # Obtain the number of columns in table
                cols1 = len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td"))

                # Print rows and columns
                log.logger.info("Number Of Row" + str(rows1))
                log.logger.info("Number Of Column" + str(cols1))
                log.logger.info("**||Title||** ")

                self.table_traverse_live_streaming_folder_item_title(rows1, cols1, f_titleName)

                self.de_click(self.closeIconOfSearchBox)

            else:

                is_title_visible = self.driver.find_element(By.XPATH,
                                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[2]/div/div[2]/div").is_displayed()

                value = str(is_title_visible)
                if value == "True":
                    titleName = self.get_element_text(self.titleDisplayed)
                    time.sleep(0.5)
                else:
                    log.logger.info("No Information Available")
                time.sleep(0.5)
                self.do_send_key(self.searchBar, titleName)
                time.sleep(1.5)

                rows1 = len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr"))

                # Obtain the number of columns in table
                cols1 = len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td"))

                # Print rows and columns
                log.logger.info("Number Of Row" + str(rows1))
                log.logger.info("Number Of Column" + str(cols1))
                log.logger.info("**||Title||** ")

                self.table_traverse_live_streaming_item_title(rows1, cols1, titleName)

                self.de_click(self.closeIconOfSearchBox)

        else:
            log.logger.info("There's No Data Available")

    def view_details_of_individual_live_streaming(self):

        log.logger.info("****==View Details Of individual Live Streaming===***")
        time.sleep(1)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody"))
        )

        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            totalInterviews = len(self.driver.find_elements(By.XPATH,
                                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr"))

            for i in range(totalInterviews):

                if i < 10:
                    itemType = []
                    itemType = self.driver.find_elements(By.XPATH,
                                                         "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[3]/span")
                    Type = itemType[i].text
                    if Type == "Stream":
                        paymentOption = []
                        paymentOption = self.driver.find_elements(By.XPATH,
                                                                  "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[7]")

                        visibilityMode = []
                        visibilityMode = self.driver.find_elements(By.XPATH,
                                                                   "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[6]")

                        payment = paymentOption[i].text

                        visibilityType = visibilityMode[i].text

                        elements = []
                        elements = self.driver.find_elements(By.XPATH,
                                                             "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[9]/div/button")
                        self.de_scroll_into_view(elements[i])
                        time.sleep(1)
                        elements[i].click()
                        time.sleep(1)
                        self.de_click(self.viewDetailsOfLiveStreaming)
                        log.logger.info(
                            "!!! == User Has clicked view details link against streaming  title == !!!")
                        time.sleep(9)

                        log.logger.info(
                            "Please Find Details Of |Video Link|   |Title|   |Visibility|   |Restriction|   "
                            "|Date|   |Time|  |Payment Type|  |Amount| for Stream")

                        # videoLinkOfStream = self.get_element_text(self.videoLink)
                        # log.logger.info("Video Link Of Stream Is === " + str(videoLinkOfStream))
                        time.sleep(0.5)
                        Title = self.get_attribute(self.titleOfStream, "value")
                        log.logger.info("Title Of Stream Is === " + str(Title))
                        time.sleep(0.5)
                        descriptionOfStream = self.get_element_text(self.Description)
                        log.logger.info("Description Of Stream Is === " + str(descriptionOfStream))
                        time.sleep(0.5)
                        # dateStream = self.get_attribute(self.dateOfStream, "value")
                        # log.logger.info("Date Of Stream Is === " + str(dateStream))
                        # time.sleep(0.5)
                        # timeStream = self.get_attribute(self.timeOfStream, "value")
                        # log.logger.info("Time Of Stream Is === " + str(timeStream))
                        # time.sleep(0.5)
                        if payment == "No" and visibilityType == "Public":
                            Visibility = self.get_element_text(self.visibilityModeWithNoPayment)
                            log.logger.info("Visibility Of Stream With No Payment Option Is === " + str(Visibility))
                            time.sleep(0.5)
                            Restriction = self.get_element_text(self.restrictionModeWithNoPayment)
                            log.logger.info("Restriction Of Stream With No Payment Option Is === " + str(Restriction))
                            time.sleep(0.5)

                        elif payment == "Yes" and visibilityType == "Public":
                            purchase = self.get_element_text(self.totalPurchase)
                            log.logger.info("Total Purchase For Streaming Is === " + str(purchase))
                            amount = self.get_element_text(self.totalAmount)
                            log.logger.info("Total Amount Paid For Streaming Is === " + str(amount))
                            amountOfStream = self.get_attribute(self.amountForStream, "value")
                            log.logger.info("Amount Of Stream Is === " + str(amountOfStream))
                            time.sleep(0.5)
                            Visibility = self.get_element_text(self.visibilityMode)
                            log.logger.info("Visibility Of Stream Is === " + str(Visibility))
                            time.sleep(0.5)
                            Restriction = self.get_element_text(self.restrictionMode)
                            log.logger.info("Restriction Of Stream If Any Is === " + str(Restriction))
                            time.sleep(0.5)

                        elif payment == "No" and visibilityType == "Private":
                            Visibility = self.get_element_text(self.visibilityModeWithNoPaymentForPrivate)
                            log.logger.info("Visibility Of Stream With No Payment Option Is === " + str(Visibility))
                            time.sleep(0.5)
                            Restriction = self.get_element_text(self.restrictionModeWithNoPaymentForPrivate)
                            log.logger.info("Restriction Of Stream With No Payment Option Is === " + str(Restriction))
                            time.sleep(0.5)

                        elif payment == "Yes" and visibilityType == "Private":
                            purchase = self.get_element_text(self.totalPurchaseWithPrivate)
                            log.logger.info("Total Purchase For Streaming Is === " + str(purchase))
                            amount = self.get_element_text(self.totalPurchaseWithPrivate)
                            log.logger.info("Total Amount Paid For Streaming Is === " + str(amount))
                            amountOfStream = self.get_attribute(self.amountForStreamForPrivate, "value")
                            log.logger.info("Amount Of Stream Is === " + str(amountOfStream))
                            time.sleep(0.5)
                            Restriction = self.get_element_text(self.restrictionModeWithNoPaymentForPrivate)
                            log.logger.info("Restriction Of Stream If Any Is === " + str(Restriction))
                            time.sleep(0.5)

                        elif payment == "No" and visibilityType == "Hidden":
                            Visibility = self.get_element_text(self.visibilityModeWithNoPaymentForPrivate)
                            log.logger.info("Visibility Of Stream With No Payment Option Is === " + str(Visibility))
                            time.sleep(0.5)
                            Restriction = self.get_element_text(self.restrictionModeWithNoPaymentForPrivate)
                            log.logger.info("Restriction Of Stream With No Payment Option Is === " + str(Restriction))
                            time.sleep(0.5)

                        elif payment == "Yes" and visibilityType == "Hidden":
                            purchase = self.get_element_text(self.totalPurchaseWithPrivate)
                            log.logger.info("Total Purchase For Streaming Is === " + str(purchase))
                            amount = self.get_element_text(self.totalPurchaseWithPrivate)
                            log.logger.info("Total Amount Paid For Streaming Is === " + str(amount))
                            amountOfStream = self.get_attribute(self.amountForStreamForPrivate, "value")
                            log.logger.info("Amount Of Stream Is === " + str(amountOfStream))
                            time.sleep(0.5)
                            Restriction = self.get_element_text(self.restrictionModeWithNoPaymentForPrivate)
                            log.logger.info("Restriction Of Stream If Any Is === " + str(Restriction))
                            time.sleep(0.5)

                        self.de_click(self.backToStreamIcon)
                        time.sleep(1)
                        # self.de_click(self.liveTab)
                        time.sleep(4)
                else:
                    log.logger.info("There's only folder")
        else:
            log.logger.info("There's No Data Available")

    def update_live_streaming(self):

        log.logger.info("****==Update The Details Of Live Streaming===***")
        time.sleep(1)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody"))
        )

        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            totalInterviews = len(self.driver.find_elements(By.XPATH,
                                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr"))

            for i in range(totalInterviews):

                if i < 1:
                    paymentOption = []
                    paymentOption = self.driver.find_elements(By.XPATH,
                                                              "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[7]")

                    payment = paymentOption[i].text

                    elements = []
                    elements = self.driver.find_elements(By.XPATH,
                                                         "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[9]/div/button/*[local-name()='svg']")

                    self.de_scroll_into_view(elements[i])
                    time.sleep(1)
                    elements[i].click()
                    time.sleep(1)
                    self.de_click(self.viewDetailsOfLiveStreaming)
                    log.logger.info(
                        "!!! == User Has clicked view details link against streaming  title == !!!")
                    time.sleep(4)
                    self.do_clear_using_java_script(self.updateTitle)
                    time.sleep(0.5)
                    title = self.generate_webinar_title()
                    time.sleep(0.5)
                    self.do_send_key(self.updateTitle, title)
                    log.logger.info("New Title Of Stream Is ===  New Title")
                    time.sleep(0.5)
                    self.do_clear_using_java_script(self.updateDescription)
                    time.sleep(0.5)
                    self.do_send_key(self.updateDescription, "New Description")
                    log.logger.info("New Description Of Stream Is ===  New Description")
                    time.sleep(0.5)
                    addApplicantArrow = self.driver.find_element(By.XPATH,"//div[@class='pl-4 py-3 border border-ime-gray-300 dark:border-ime-gray-600 rounded']/div/button")
                    time.sleep(0.5)
                    self.de_scroll_into_view(addApplicantArrow)
                    time.sleep(1)
                    self.de_click(self.applicantDDArrow)
                    time.sleep(0.5)
                    self.de_click(self.addApplicantButtonUpdate)
                    time.sleep(0.5)
                    self.do_send_key(self.firstName,"Update Name")
                    time.sleep(0.5)
                    self.do_send_key(self.lastName,"Update LastName")
                    time.sleep(0.5)
                    self.de_click(self.countryCode)
                    time.sleep(0.5)
                    self.de_click(self.firstCountryCode)
                    self.do_send_key(self.contactNumber,"9090909090")
                    time.sleep(0.5)
                    email=self.generate_random_email()
                    self.do_send_key(self.Email,email)
                    time.sleep(0.5)
                    self.de_click(self.inviteApplicantUpdate)
                    time.sleep(1)


                    pDD = self.driver.find_element(By.XPATH,"//div[@class='grid grid-cols-3 gap-4 pb-8 p-8']/div[2]/div[3]/button")
                    time.sleep(0.5)
                    self.de_scroll_into_view(pDD)
                    time.sleep(1)
                    payment = self.get_element_text(self.paymentDDValueUpdate)
                    time.sleep(0.5)
                    if payment == "No":
                        self.de_click(self.paymentDDUpdate)
                        time.sleep(0.5)
                        self.de_click(self.payNowOptionOfPaymentDDUpdate)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInputUpdate, "50")
                        time.sleep(0.5)

                    else:
                        self.de_click(self.paymentDDUpdate)
                        time.sleep(0.5)
                        self.de_click(self.noneOptionOfPaymentDDUpdate)
                        time.sleep(0.5)


                    Visibility = self.get_element_text(self.visibilityModeValueUpdate)
                    log.logger.info("Visibility Of Stream Is === " + str(Visibility))
                    time.sleep(0.5)
                    if Visibility == "Public":
                        self.de_click(self.visibilityDDUpdate)
                        time.sleep(0.5)
                        self.de_click(self.privateOptionUpdate)
                        log.logger.info("New Visibility Mode Of Stream Is === Private ")
                        time.sleep(0.5)
                    elif Visibility == "Private":
                        self.de_click(self.visibilityDDUpdate)
                        time.sleep(0.5)
                        self.de_click(self.publicOptionUpdate)

                        log.logger.info("New Visibility Mode Of Stream Is === Public")
                        time.sleep(0.5)
                    elif Visibility == "Hidden":
                        self.de_click(self.visibilityDDUpdate)
                        time.sleep(0.5)
                        self.de_click(self.publicOptionUpdate)

                        log.logger.info("New Visibility Mode Of Stream Is === Public")
                        time.sleep(0.5)
                    else:
                        self.de_click(self.visibilityDDUpdate)
                        time.sleep(0.5)
                        self.de_click(self.publicOptionUpdate)


                    ageR = self.get_element_text(self.ageDDValueUpdate)
                    time.sleep(0.5)
                    log.logger.info("Restriction Of Stream If Any Is === " + str(ageR))
                    time.sleep(0.5)
                    if ageR == "None":
                        self.de_click(self.ageDDUpdate)
                        time.sleep(0.5)
                        self.de_click(self.eightyPlusOptionUpdate)
                        log.logger.info("New Restriction Of Stream If Any Is === 18+")
                        time.sleep(0.5)


                    elif ageR == "18+":
                        self.de_click(self.ageDDUpdate)
                        time.sleep(0.5)
                        self.de_click(self.noneOptionAgeUpdate)
                        log.logger.info("New Restriction Of Stream If Any Is === None")
                        time.sleep(0.5)
                    else:
                        self.de_click(self.ageDDUpdate)
                        time.sleep(0.5)
                        self.de_click(self.noneOptionAgeUpdate)
                        time.sleep(0.5)



                    self.de_scroll_by_pixels()
                    self.de_click(self.updateButton)
                    time.sleep(3)
                    self.de_click(self.backToStreamIcon)
                    time.sleep(4)
                    break

    def delete_live_streaming_item(self):

        log.logger.info("****==Delete Any  Live Stream Item===***")
        time.sleep(1)
        # self.de_click(self.liveTab)
        time.sleep(4)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody"))
        )

        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            self.de_click(self.firstItem)
            time.sleep(0.5)
            self.de_click(self.deleteButtonBulk)
            time.sleep(1)
            self.de_click(self.deleteButton)
            time.sleep(3)
        else:
            log.logger.info("There's No Streaming Item Displays")

    def bulk_delete_live_streaming_item(self):
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody"))
        )

        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            totalInterviews = len(self.driver.find_elements(By.XPATH,
                                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 my-[10px] rounded-md']/table/tbody/tr"))
            if totalInterviews > 2:
                for i in range(2):
                    elements = []
                    elements = self.driver.find_elements(By.XPATH,
                                                         "//div[@class='border border-ime-gray-300 dark:border-zinc-600 my-[10px] rounded-md']/table/tbody/tr/td[1]/h5/div/div/input")
                    elements[i].click()

                self.de_click(self.deleteButtonBulk)
                time.sleep(2)
                self.de_click(self.deleteButton)
                time.sleep(3)


            else:
                log.logger.info("There is Two or Less then 2 streams")
        else:
            log.logger.info("There is No Streams Available")

    # # UPLOAD STREAM PART
    #
    # def fetch_upload_streaming_details(self):
    #     log.logger.info("****==View list of Upload streaming items starts here==***")
    #     self.de_click(self.uploadTab)
    #     time.sleep(4)
    #
    #     dataAvail = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH,
    #                                         "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
    #     )
    #     value = dataAvail.text
    #     # log.logger.info("" + value)
    #     if len(value) > 0:
    #         rows = len(self.driver.find_elements(By.XPATH,
    #                                              "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr"))
    #
    #         cols = len(self.driver.find_elements(By.XPATH,
    #                                              "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td"))
    #         log.logger.info("Number Of Row == " + str(rows))
    #         log.logger.info("Number Of Column == " + str(cols))
    #         log.logger.info("**||Title||**        **||Added ||**        **||Visibility||**      "
    #                         "**||Paid||**         ")
    #
    #         self.table_traverse(rows, cols)
    #     else:
    #         log.logger.info("There's No Data Available")
    #
    # def filter_upload_stream_list_via_title(self):
    #
    #     log.logger.info("****==Filter list of upload streaming details via search box using item title "
    #                     "test case starts here==***")
    #     time.sleep(1)
    #     dataAvail = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH,
    #                                         "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
    #     )
    #
    #     value = dataAvail.text
    #     # log.logger.info("" + value)
    #     if len(value) > 0:
    #
    #         is_title_visible = self.driver.find_element(By.XPATH,
    #                                                     "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[2]/h5/div").is_displayed()
    #
    #         value = str(is_title_visible)
    #         if value == "True":
    #             titleName = self.get_element_text(self.titleOfUploadStream)
    #             time.sleep(0.5)
    #         else:
    #             log.logger.info("No Information Available")
    #         time.sleep(0.5)
    #         self.do_send_key(self.searchBar, titleName)
    #         time.sleep(1.5)
    #
    #         rows1 = len(self.driver.find_elements(By.XPATH,
    #                                               "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr"))
    #
    #         # Obtain the number of columns in table
    #         cols1 = len(self.driver.find_elements(By.XPATH,
    #                                               "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td"))
    #
    #         # Print rows and columns
    #         log.logger.info("Number Of Row" + str(rows1))
    #         log.logger.info("Number Of Column" + str(cols1))
    #         log.logger.info("**||Title||** ")
    #
    #         self.table_traverse_upload_streaming_item_title(rows1, cols1, titleName)
    #
    #         self.de_click(self.closeIconOfSearchBox)
    #
    #     else:
    #         log.logger.info("There's No Data Available")
    #
    # def view_details_of_individual_upload_streaming(self):
    #
    #     log.logger.info("****==View Details Of individual Upload Streaming===***")
    #     time.sleep(1)
    #
    #     dataAvail = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH,
    #                                         "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
    #     )
    #
    #     value = dataAvail.text
    #     # log.logger.info("" + value)
    #     if len(value) > 0:
    #
    #         totalInterviews = len(self.driver.find_elements(By.XPATH,
    #                                                         "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr"))
    #
    #         for i in range(totalInterviews):
    #             if i < 8:
    #                 paymentOption = []
    #                 paymentOption = self.driver.find_elements(By.XPATH,
    #                                                           "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr/td[5]/h5")
    #
    #                 payment = paymentOption[i].text
    #
    #                 elements = []
    #                 elements = self.driver.find_elements(By.XPATH,
    #                                                      "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr/td[7]/div/button/*[local-name()='svg']")
    #                 elements[i].click()
    #                 time.sleep(1)
    #                 self.de_click(self.viewDetailsOfUploadStreaming)
    #                 log.logger.info(
    #                     "!!! == User Has clicked view details link against streaming  title == !!!")
    #                 time.sleep(4)
    #
    #                 log.logger.info("Please Find Details Of |Video Link|   |Title|   |Visibility|   |Restriction|   "
    #                                 "|Date|   |Time|  |Payment Type|  |Amount| for Stream")
    #
    #                 videoLinkOfStream = self.get_element_text(self.videoLink)
    #                 log.logger.info("Video Link Of Stream Is === " + str(videoLinkOfStream))
    #                 time.sleep(0.5)
    #                 Title = self.get_attribute(self.titleOfStream, "value")
    #                 log.logger.info("Title Of Stream Is === " + str(Title))
    #                 time.sleep(0.5)
    #                 descriptionOfStream = self.get_element_text(self.Description)
    #                 log.logger.info("Description Of Stream Is === " + str(descriptionOfStream))
    #                 time.sleep(0.5)
    #                 Visibility = self.get_element_text(self.visibilityMode)
    #                 log.logger.info("Visibility Of Stream Is === " + str(Visibility))
    #                 time.sleep(0.5)
    #                 Restriction = self.get_element_text(self.restrictionMode)
    #                 log.logger.info("Restriction Of Stream If Any Is === " + str(Restriction))
    #                 time.sleep(0.5)
    #                 dateStream = self.get_attribute(self.dateOfStream, "value")
    #                 log.logger.info("Date Of Stream Is === " + str(dateStream))
    #                 time.sleep(0.5)
    #                 timeStream = self.get_attribute(self.timeOfStream, "value")
    #                 log.logger.info("Time Of Stream Is === " + str(timeStream))
    #                 time.sleep(0.5)
    #                 if payment == "No":
    #                     paymentType = self.get_element_text(self.paymentTypeOfStream)
    #                     log.logger.info("Payment Type Of Stream Is === " + str(paymentType))
    #                     time.sleep(0.5)
    #
    #                 else:
    #                     purchase = self.get_element_text(self.totalPurchase)
    #                     log.logger.info("Total Purchase For Streaming Is === " + str(purchase))
    #                     amount = self.get_element_text(self.totalAmount)
    #                     log.logger.info("Total Amount Paid For Streaming Is === " + str(amount))
    #                     amountOfStream = self.get_attribute(self.amountForStream, "value")
    #                     log.logger.info("Amount Of Stream Is === " + str(amountOfStream))
    #                     time.sleep(0.5)
    #
    #                 self.de_click(self.backToStreamIcon)
    #                 time.sleep(1)
    #
    #     else:
    #         log.logger.info("There's No Data Available")
    #
    # def update_uploads_streaming(self):
    #
    #     log.logger.info("****==Update The Details Of Upload Streaming===***")
    #     time.sleep(1)
    #
    #     dataAvail = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH,
    #                                         "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
    #     )
    #
    #     value = dataAvail.text
    #     # log.logger.info("" + value)
    #     if len(value) > 0:
    #
    #         totalInterviews = len(self.driver.find_elements(By.XPATH,
    #                                                         "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr"))
    #
    #         for i in range(totalInterviews):
    #             paymentOption = []
    #             paymentOption = self.driver.find_elements(By.XPATH,
    #                                                       "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr/td[5]/h5")
    #
    #             payment = paymentOption[i].text
    #
    #             elements = []
    #             elements = self.driver.find_elements(By.XPATH,
    #                                                  "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr/td[7]/div/button/*[local-name()='svg']")
    #             elements[i].click()
    #             time.sleep(1)
    #             self.de_click(self.viewDetailsOfUploadStreaming)
    #             log.logger.info(
    #                 "!!! == User Has clicked view details link against streaming  title == !!!")
    #             time.sleep(4)
    #             self.do_clear(self.updateTitle)
    #             time.sleep(0.5)
    #             self.do_send_key(self.titleOfStream, "New Title")
    #             log.logger.info("New Title Of Upload Stream Is ===  New Title")
    #             time.sleep(0.5)
    #             self.do_clear(self.updateDescription)
    #             time.sleep(0.5)
    #             self.do_send_key(self.Description, "New Description")
    #             log.logger.info("New Description Of Upload Stream Is ===  New Description")
    #             time.sleep(0.5)
    #             self.de_scroll_by_pixels()
    #             time.sleep(0.5)
    #             Visibility = self.get_element_text(self.visibilityMode)
    #             log.logger.info("Visibility Of Upload Stream Is === " + str(Visibility))
    #             time.sleep(0.5)
    #             if Visibility == "Public":
    #                 self.de_click(self.visibilityModeDD)
    #                 time.sleep(0.5)
    #                 self.de_click(self.privateOptionOfVisibility)
    #                 log.logger.info("New Visibility Mode Of Upload Stream Is === Private ")
    #                 time.sleep(0.5)
    #             elif Visibility == "Private":
    #                 self.de_click(self.visibilityModeDD)
    #                 time.sleep(0.5)
    #                 self.de_click(self.publicOptionOfVisibility)
    #
    #                 log.logger.info("New Visibility Mode Of Upload Stream Is === Public")
    #                 time.sleep(0.5)
    #             elif Visibility == "Hidden":
    #                 self.de_click(self.visibilityModeDD)
    #                 time.sleep(0.5)
    #                 self.de_click(self.privateOptionOfVisibility)
    #
    #                 log.logger.info("New Visibility Mode Of Upload Stream Is === Private")
    #                 time.sleep(0.5)
    #             else:
    #                 self.de_click(self.visibilityModeDD)
    #                 time.sleep(0.5)
    #                 self.de_click(self.publicOptionOfVisibility)
    #             Restriction = self.get_element_text(self.restrictionMode)
    #             time.sleep(0.5)
    #             log.logger.info("Restriction Of Upload Stream If Any Is === " + str(Restriction))
    #             time.sleep(0.5)
    #             if Restriction == "None":
    #                 self.de_click(self.restrictionModeDD)
    #                 time.sleep(0.5)
    #                 self.de_click(self.eightyPlusOptionOfRestriction)
    #                 log.logger.info("New Restriction Of Upload Stream If Any Is === 18+")
    #                 time.sleep(0.5)
    #
    #
    #             elif Restriction == "18+":
    #                 self.de_click(self.restrictionModeDD)
    #                 time.sleep(0.5)
    #                 self.de_click(self.noneOptionOfRestriction)
    #                 log.logger.info("New Restriction Of Upload Stream If Any Is === None")
    #                 time.sleep(0.5)
    #             else:
    #                 self.de_click(self.restrictionModeDD)
    #                 time.sleep(0.5)
    #                 self.de_click(self.noneOptionOfRestriction)
    #                 time.sleep(0.5)
    #
    #             self.de_scroll_by_pixels()
    #             time.sleep(0.5)
    #             self.de_click(self.applicantDDArrow)
    #             time.sleep(0.5)
    #             self.de_click(self.inviteApplicant)
    #             time.sleep(0.5)
    #             self.do_send_key(self.firstName, "Nitesh")
    #             log.logger.info("New Applicant First Name Of Is === Nitesh ")
    #             time.sleep(0.5)
    #             self.do_send_key(self.lastName, "Barot")
    #             log.logger.info("New Applicant Last Name Of Is === Barot ")
    #             time.sleep(0.5)
    #             self.do_send_key(self.contactNumber, "9090909090")
    #             log.logger.info("New Applicant Contact Number  Is === 9090909090 ")
    #             time.sleep(0.5)
    #             self.do_send_key(self.Email, "nitesh@gmail.com")
    #             log.logger.info("New Applicant Email Is === nitesh@gmail.com ")
    #             time.sleep(0.5)
    #             self.de_click(self.addApplicantButton)
    #             time.sleep(0.5)
    #             self.de_scroll_by_up_pixels()
    #             time.sleep(0.5)
    #             if payment == "No":
    #                 self.de_click(self.paymentDDOfNo)
    #                 time.sleep(0.5)
    #                 self.de_click(self.payNowOptionOfPaymentDDOfNo)
    #                 time.sleep(0.5)
    #                 self.do_send_key(self.amountInput, "5")
    #                 time.sleep(0.5)
    #
    #             else:
    #                 self.de_click(self.paymentDDOfYes)
    #                 time.sleep(0.5)
    #                 self.de_click(self.noneOptionOfPaymentDDofYes)
    #                 time.sleep(0.5)
    #
    #             self.de_scroll_by_pixels()
    #             self.de_click(self.updateButton)
    #             time.sleep(3)
    #             self.de_click(self.backToStreamIcon)
    #             time.sleep(2)
    #             break
    #
    # def delete_upload_streaming_item(self):
    #
    #     log.logger.info("****==Delete Any  Live Stream Item===***")
    #     time.sleep(1)
    #
    #     dataAvail = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH,
    #                                         "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
    #     )
    #
    #     value = dataAvail.text
    #     # log.logger.info("" + value)
    #     if len(value) > 0:
    #         self.de_click(self.cogIcon)
    #         time.sleep(0.5)
    #         self.de_click(self.deleteLinkOfUpload)
    #         time.sleep(1)
    #         self.de_click(self.deleteButtonOfUpload)
    #         time.sleep(3)
    #     else:
    #         log.logger.info("There's No Streaming Item Displays")
