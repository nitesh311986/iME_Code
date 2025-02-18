import time
from datetime import datetime, timedelta
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Multiway_Interview_Details(BasePage):
    videoInterviewIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/button/div")
    multiWayInterviewIcon = (
        By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[4]")

    videoCallsIcon = (By.XPATH,
                      "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[2]")
    searchBox = (By.CSS_SELECTOR, "input[name='searchName']")
    closeIconOfSearchBox = (By.XPATH,
                            "//div[@id='search']/*[local-name()='svg'][@class='fill-black dark:fill-white scale-[180%] cursor-pointer mt-4 h-[14px] relative right-2']")
    designationDisplayed = (By.XPATH,
                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[1]")
    serviceDisplayed = (By.XPATH,
                        "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[2]/h5/div")
    viewInviteDetailsIcon = (By.XPATH,
                             "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[6]/div/div/a")

    viewVideoDetailsIcon = (By.XPATH,
                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[4]/div/div/a")

    viewWebinarDetailsIcon = (By.XPATH,
                              "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[6]/div/div/a")

    descriptionArrow = (By.XPATH, "//div[@class='grid grid-cols-6 gap-4']/div/div[2]/button")

    Description = (By.XPATH, "//div[@class='grid grid-cols-6 gap-4']/div[1]/div[2]/div[1]")

    usersArrow = (By.XPATH, "//div[@class='grid grid-cols-6 gap-4']/div/div[3]/button")

    userDetails = (By.XPATH, "//div[@class='grid grid-cols-6 gap-4']/div/div[3]/div/div/table/tbody/tr[1]")

    invitedApplicant = (By.XPATH, "//div[@class='grid grid-cols-6 gap-4']/div/div[4]/button")

    applicantDetails = (By.XPATH, "//div[@class='grid grid-cols-6 gap-4']/div/div[4]/div/div/table/tbody/tr[1]")
    webinarLink = (By.XPATH, "//div[@class='grid grid-cols-6 gap-4']/div[2]/div[2]/div/span")
    registeredPeople = (By.XPATH, "//div[@class='grid grid-cols-6 gap-4']/div[2]/div[3]/div/div/div[1]/p")
    Attendance = (By.XPATH, "//div[@class='grid grid-cols-6 gap-4']/div[2]/div[3]/div/div/div[2]/p")
    backToInterviewIcon = (By.XPATH, "//div[@class='flex justify-between flex-col-reverse md:flex-row gap-2']/div/a")

    firstSlotTimings = (By.XPATH,
                        "//div[@class='border-[1px] w-full p-4 border-ime-gray-300 dark:border-zinc-600 rounded-[6px]']/div[3]/ul/li/div[2]/ul/li")

    rescheduleButton = (By.XPATH, "//div[@class='flex gap-4 flex-col md:flex-row']/div[2]/div[1]/button[1]")
    dateInput = (By.XPATH, "//div[@class='!mb-0 mt-auto ime-form-input']/input")
    fromTime1 = (By.XPATH, "//input[@name='multiwayTimeslots.0.startDateTime']")
    toTime1 = (By.XPATH, "//input[@name='multiwayTimeslots.0.endDateTime']")
    fromTime2 = (By.XPATH, "//input[@name='multiwayTimeslots.1.startDateTime']")
    toTime2 = (By.XPATH, "//input[@name='multiwayTimeslots.1.endDateTime']")
    fromTime3 = (By.XPATH, "//input[@name='multiwayTimeslots.2.startDateTime']")
    toTime3 = (By.XPATH, "//input[@name='multiwayTimeslots.2.endDateTime']")
    plusButtonOne = (By.XPATH, "//div[@class='flex flex-col md:flex-row gap-2 mt-4']/div[3]/button")
    plusButtonTwo = (By.XPATH, "//form[@class='p-6 max-w-2xl']/div/div/div[2]/div[3]")
    description = (By.CSS_SELECTOR, "textArea[name='interviewDescription']")
    searchDD = (By.XPATH, "//div[@id='search']")
    addUser = (By.XPATH, "//div[@class='relative w-full border-gray-300 rounded-md my-4 ']/div/div[2]")
    submitButton = (
        By.XPATH,
        "//button[@class='mt-6 flex-1 disabled:bg-black bg-[#0070F3] rounded-[4px] transition-colors h-[32px] px-[22px] text-xs bg-ime-accent hover:bg-blue-700 text-white']")

    invitesButton = (By.XPATH,
                     "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[2]")

    designationDisplayedForInvites = (By.XPATH,
                                      "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[1]/h5/div/div[1]")

    nextButtonPagging = (By.XPATH,
                         "//div[@class='w-full flex flex-row justify-center mt-[32px] gap-[32px] font-semibold pb-[37px]']/button[2]")

    viewDetailsIconOfInvites = (By.XPATH,
                                "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr/td[4]/div/div/a")

    # Webinar Call
    webinarIcon = (By.XPATH,
                   "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[3]")

    editButton = (
        By.XPATH, "//div[@class='col-span-6 lg:col-span-2 order-1 lg:order-none mt-5 lg:mt-5']/div[1]/div[2]/button[1]")

    title = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[1]/div[1]/input")

    visibilityDD = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[1]/button")

    privateDDOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[1]/ul/li[2]")

    publicDDOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[1]/ul/li[1]")

    hiddenDDOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[1]/ul/li[3]")

    serviceDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[2]/button")

    serviceDDOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[2]")

    emailInput = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[3]/div/input")

    descriptionEdit = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[4]/div/textarea")

    paymentDD = (By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[8]/div[1]/button")
    noneOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[8]/div[1]/ul/li[1]")
    payNowOption = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[8]/div[1]/ul/li[2]")
    amountInput = (
        By.XPATH, "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[8]/div[2]/div[2]/input")

    submit = (By.XPATH, "//div[@class='flex justify-between items-center gap-4']/div/button")

    serviceTypeAfterEdit = (By.XPATH,
                            "//div[@class='border-[1px] w-full border-ime-gray-300 dark:border-ime-gray-600 rounded-[6px] overflow-hidden']/table/tbody/tr[1]/td[2]")
    titleTypeAfterEdit = (By.XPATH,
                          "//div[@class='border-[1px] w-full border-ime-gray-300 dark:border-ime-gray-600 rounded-[6px] overflow-hidden']/table/tbody/tr[1]/td[2]")

    visibilityAfterEdit = (By.XPATH,
                           "//div[@class='border-[1px] w-full border-ime-gray-300 dark:border-ime-gray-600 rounded-[6px] overflow-hidden']/table/tbody/tr[2]/td[2]")
    serviceAfterEdit = (By.XPATH,
                        "//div[@class='border-[1px] w-full border-ime-gray-300 dark:border-ime-gray-600 rounded-[6px] overflow-hidden']/table/tbody/tr[3]/td[2]")

    qmailAfterEditInVideo = (By.XPATH,
                             "//div[@class='border-[1px] w-full border-ime-gray-300 dark:border-ime-gray-600 rounded-[6px] overflow-hidden']/table/tbody/tr[4]/td[2]")

    queryMailAfterEdit = (By.XPATH,
                          "//div[@class='border-[1px] w-full border-ime-gray-300 dark:border-ime-gray-600 rounded-[6px] overflow-hidden']/table/tbody/tr[7]/td[2]")

    visibilityOfWebinar = (
        By.XPATH, "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[2]")

    global designationName, statusName

    def __init__(self, driver, environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_interview_icon(self):
        time.sleep(3)
        self.de_click(self.multiWayInterviewIcon)
        time.sleep(5)

    def view_multiway_invites_details(self):
        log.logger.info("****==View list of Multiway Invites test case starts here==***")

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
            log.logger.info("**||Interviews||**        **||Type||**     **||Schedule||**       **||Status||**")

            self.table_traverse_multiway_video_calls(rows, cols)
        else:
            log.logger.info("There's No Data Available")

        # # 1.2 filter list of multiway Invites  via search box
        log.logger.info("****==Filter list of multiway invites details via search box using interview "
                        "position test case starts here==***")

        time.sleep(1)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            is_designation_visible = self.driver.find_element(By.XPATH,
                                                              "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[1]").is_displayed()

            value = str(is_designation_visible)
            if value == "True":
                designationName = self.get_element_text(self.designationDisplayed)
                time.sleep(0.5)
            else:
                log.logger.info("No Information Available")
            time.sleep(0.5)
            self.do_send_key(self.searchBox, designationName)
            time.sleep(1.5)

            rows1 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr"))

            cols1 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row == " + str(rows1))
            log.logger.info("Number Of Column == " + str(cols1))
            log.logger.info("**||Employment Position||** ")

            self.multiway_invites_table_traverse_search_via_title(rows1, cols1, designationName)
            self.de_click(self.closeIconOfSearchBox)
            time.sleep(1)
        else:
            log.logger.info("There's No Data Available")
        #
        # 1.3 View Details of Individual Invites

        log.logger.info("****==View Details Of individual Invites Of Multiway Interviews===***")

        time.sleep(2)

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
                    elements = []
                    elements = self.driver.find_elements(By.XPATH,
                                                         "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[6]/div/button/*[local-name()='svg']")
                    time.sleep(0.5)
                    Type = []
                    Type = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[2]")
                    time.sleep(0.5)
                    invite_type = Type[i].text
                    time.sleep(0.5)
                    self.de_scroll_into_view(elements[i])
                    elements[i].click()
                    time.sleep(1)
                    self.de_click(self.viewInviteDetailsIcon)
                    log.logger.info(
                        "!!! == User Has clicked view interview icon against interview designation == !!!")
                    time.sleep(4)

                    rows = 1 + len(self.driver.find_elements(By.XPATH,
                                                             "//div[@class='border-[1px] w-full border-ime-gray-300 dark:border-ime-gray-600 rounded-[6px] overflow-hidden']/table/tbody/tr"))

                    # Obtain the number of columns in table
                    cols = len(self.driver.find_elements(By.XPATH,
                                                         "//div[@class='border-[1px] w-full border-ime-gray-300 dark:border-ime-gray-600 rounded-[6px] overflow-hidden']/table/tbody/tr/td[2]"))

                    # Print rows and columns
                    log.logger.info("Number Of Row" + str(rows))
                    log.logger.info("Number Of Column" + str(cols))
                    log.logger.info(
                        "**||Service||**              **||Visibility||**               **||Schedule||**        "
                        "**||PreRegistration Deadline||**        **||Payment||**   **||Amount||**  **||Query EMail||**  **||Created By||**")

                    # Printing the data of the table
                    for r in range(1, rows):
                        for p in range(1, 2):
                            # obtaining the text from each column of the table
                            value = self.driver.find_element(By.XPATH,
                                                             "//div[@class='grid grid-cols-6 gap-4']/div[1]/div[1]/table/tbody/tr[" + str(
                                                                 r) + "]/td[2]").text

                            log.logger.info("" + str(value))
                            time.sleep(0.5)

                    time.sleep(0.5)
                    self.de_click(self.descriptionArrow)
                    time.sleep(0.5)
                    Description = self.get_element_text(self.Description)
                    log.logger.info("Description Of Interview Is === " + str(Description))
                    time.sleep(0.5)
                    # if invite_type == "Webinar":
                    #     link = self.get_element_text(self.webinarLink)
                    #     log.logger.info("Webinar Link Is === " + str(link))
                    #     rPeople = self.get_element_text(self.registeredPeople)
                    #     log.logger.info("Number Of People Registered In Webinar Is === " + str(rPeople))
                    #     attended = self.get_element_text(self.Attendance)
                    #     log.logger.info("Number Of People Attended Webinar  Is === " + str(attended))
                    # else:
                    #     log.logger.info("There's No Link Available For Video call")
                    self.de_click(self.backToInterviewIcon)
                    time.sleep(2)

        else:
            log.logger.info("There's No Data Available")

        # 1.4 Edit and assert the invite  Information of multiway
        log.logger.info("****==Edit and assert the invite  Information of Multiway ===***")

        time.sleep(2)

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
                elements = []
                elements = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[6]/div/button/*[local-name()='svg']")

                Type = []
                Type = self.driver.find_elements(By.XPATH,
                                                 "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[2]")
                time.sleep(0.5)
                invite_type = Type[i].text
                time.sleep(0.5)
                self.de_scroll_into_view(elements[i])
                elements[i].click()
                time.sleep(1)
                self.de_click(self.viewInviteDetailsIcon)
                time.sleep(4)
                self.de_click(self.editButton)
                time.sleep(2)
                self.do_clear_using_java_script(self.title)
                time.sleep(1)
                dateTime = self.get_date_time_using_time_zone()
                time.sleep(1)
                title = self.generate_webinar_title()
                time.sleep(0.5)
                self.do_send_key(self.title, title)
                time.sleep(1)
                visibilityDDValue = self.get_element_text(self.visibilityDD)
                time.sleep(0.5)
                self.de_click(self.visibilityDD)
                if visibilityDDValue == "Public":
                    time.sleep(0.5)
                    self.de_click(self.privateDDOption)
                elif visibilityDDValue == "Private":
                    time.sleep(0.5)
                    self.de_click(self.publicDDOption)
                else:
                    self.de_click(self.publicDDOption)
                time.sleep(1)
                self.de_click(self.serviceDD)
                time.sleep(1)
                self.de_click(self.serviceDDOption)
                time.sleep(1)
                self.do_clear_using_java_script(self.emailInput)
                time.sleep(1)
                email = self.generate_random_email()
                time.sleep(0.5)
                self.do_send_key(self.emailInput, email)
                time.sleep(1)
                self.do_clear_using_java_script(self.descriptionEdit)
                time.sleep(0.5)
                desc = self.generate_random_text()
                time.sleep(1)
                self.do_send_key(self.descriptionEdit, desc)
                time.sleep(1)
                pDD = self.driver.find_element(By.XPATH,
                                               "//div[@class='px-7 pb-[150px] overflow-y-auto']/div[2]/div[2]/div[1]/div[8]/div[1]/button")
                self.de_scroll_into_view(pDD)
                time.sleep(0.5)

                # if invite_type == "Webinar":
                #     paymentDDValue = self.get_element_text(self.paymentDD)
                #     self.de_click(self.paymentDD)
                #     if paymentDDValue == "None":
                #         time.sleep(0.5)
                #         self.de_click(self.payNowOption)
                #         time.sleep(0.5)
                #         self.do_send_key(self.amountInput, "100")
                #     else:
                #         time.sleep(0.5)
                #         self.de_click(self.noneOption)
                # else:
                #     time.sleep(1)
                #     log.logger.info("There's No Payment Option Available For Video Call")
                self.de_click(self.submit)
                time.sleep(3)
                # sType = self.get_element_text(self.serviceTypeAfterEdit)
                # assert "Awards" in sType
                # time.sleep(0.5)
                # vType = self.get_element_text(self.visibilityAfterEdit)
                # assert "Private" in vType
                # time.sleep(0.5)
                qMail = self.get_element_text(self.queryMailAfterEdit)
                assert email in qMail
                time.sleep(0.5)
                # self.de_click(self.descriptionArrow)
                # time.sleep(0.5)
                # dType = self.get_element_text(self.Description)
                # assert desc in dType
                # time.sleep(2)
                self.de_click(self.backToInterviewIcon)
                time.sleep(2)
                break


    def view_details_of_video_call_of_multiway_interview(self):

        self.de_click(self.videoCallsIcon)
        time.sleep(3)
        log.logger.info("****==View list of Multiway Video interview's details test case starts here==***")

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
            log.logger.info("**||Title||**        **||Scheduled||**  ")

            self.table_traverse_multiway_video_calls(rows, cols)
        else:
            log.logger.info("There's No Data Available")

        # # 2.1 filter list of webinar items via search box
        log.logger.info("****==Filter list of multiway Video Call details via search box using  "
                        "title test case starts here==***")

        time.sleep(1)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            is_designation_visible = self.driver.find_element(By.XPATH,
                                                              "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[1]").is_displayed()

            value = str(is_designation_visible)
            if value == "True":
                designationName = self.get_element_text(self.designationDisplayed)
                time.sleep(0.5)
            else:
                log.logger.info("No Information Available")
            time.sleep(0.5)
            self.do_send_key(self.searchBox, designationName)
            time.sleep(1.5)

            rows1 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr"))

            cols1 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row == " + str(rows1))
            log.logger.info("Number Of Column == " + str(cols1))
            log.logger.info("**||Video Call Title||** ")

            self.multiway_video_call_table_traverse_search_via_title(rows1, cols1, designationName)
            self.de_click(self.closeIconOfSearchBox)
            time.sleep(1)
        else:
            log.logger.info("There's No Data Available")

        # # 2.3 View Details of Individual Video Call

        log.logger.info("****==View Details Of individual Video Call Of Multiway ===***")

        time.sleep(2)

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
                    elements = []
                    elements = self.driver.find_elements(By.XPATH,
                                                         "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[4]/div/button/*[local-name()='svg']")
                    time.sleep(0.5)

                    self.de_scroll_into_view(elements[i])
                    elements[i].click()
                    time.sleep(1)
                    self.de_click(self.viewVideoDetailsIcon)
                    log.logger.info(
                        "!!! == User Has clicked view interview icon against interview designation == !!!")
                    time.sleep(4)

                    rows = 1 + len(self.driver.find_elements(By.XPATH,
                                                             "//div[@class='border-[1px] w-full border-ime-gray-300 dark:border-zinc-600 rounded-[6px]']/table/tbody/tr"))

                    # Obtain the number of columns in table
                    cols = len(self.driver.find_elements(By.XPATH,
                                                         "//div[@class='border-[1px] w-full border-ime-gray-300 dark:border-zinc-600 rounded-[6px]']/table/tbody/tr/td[2]"))

                    # Print rows and columns
                    log.logger.info("Number Of Row" + str(rows))
                    log.logger.info("Number Of Column" + str(cols))
                    log.logger.info(
                        "**||Video Call Title||**              **||Visibility||**               **||Service||**        "
                        "**||Query Email||**        **||Schedule||**   **||Created By||** ")

                    # Printing the data of the table
                    for r in range(1, rows):
                        for p in range(1, 2):
                            # obtaining the text from each column of the table
                            value = self.driver.find_element(By.XPATH,
                                                             "//div[@class='grid grid-cols-6 gap-4']/div[1]/div[1]/table/tbody/tr[" + str(
                                                                 r) + "]/td[2]").text

                            log.logger.info("" + str(value))
                            time.sleep(0.5)

                    time.sleep(0.5)
                    self.de_click(self.descriptionArrow)
                    time.sleep(0.5)
                    Description = self.get_element_text(self.Description)
                    log.logger.info("Description Of Interview Is === " + str(Description))
                    time.sleep(0.5)
                    # videoLink = self.get_element_text(self.webinarLink)
                    # log.logger.info("Video Link Is === " + str(videoLink))
                    # time.sleep(0.5)
                    # self.de_click(self.usersArrow)
                    # time.sleep(1)
                    # rows1 = len(self.driver.find_elements(By.XPATH,
                    #                                       "//div[@class='flex gap-4 flex-col md:flex-row']/div[1]/div[3]/div/div/div/form/div[2]/table/tbody/tr"))
                    #
                    # cols1 = len(self.driver.find_elements(By.XPATH,
                    #                                       "//div[@class='flex gap-4 flex-col md:flex-row']/div[1]/div[3]/div/div/div/form/div[2]/table/tbody/tr/td"))
                    #
                    # log.logger.info("Number Of Row == " + str(rows1))
                    # log.logger.info("Number Of Column == " + str(cols1))
                    # log.logger.info("**||Users Information||** ")
                    # self.table_traverse_for_multiway_interview_user(rows1, cols1)

                    self.de_click(self.backToInterviewIcon)
                    time.sleep(2)

        else:
            log.logger.info("There's No Data Available")

        # 2.4 Edit and assert the Video Call Information
        log.logger.info("****==Edit and assert the Video Call Information ===***")

        time.sleep(2)

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
                elements = []
                elements = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[4]/div/button/*[local-name()='svg']")
                self.de_scroll_into_view(elements[i])
                elements[i].click()
                time.sleep(1)
                self.de_click(self.viewVideoDetailsIcon)
                time.sleep(4)
                self.de_click(self.editButton)
                time.sleep(2)
                self.do_clear_using_java_script(self.title)
                time.sleep(1)
                dateTime = self.get_date_time_using_time_zone()
                time.sleep(1)
                title = self.generate_webinar_title()
                time.sleep(0.5)
                self.do_send_key(self.title, title)
                time.sleep(1)
                self.de_click(self.visibilityDD)
                time.sleep(1)
                self.de_click(self.privateDDOption)
                time.sleep(1)
                self.de_click(self.serviceDD)
                time.sleep(1)
                self.de_click(self.serviceDDOption)
                time.sleep(1)
                self.do_clear_using_java_script(self.emailInput)
                time.sleep(1)
                email = self.generate_random_email()
                time.sleep(0.5)
                self.do_send_key(self.emailInput, "")
                time.sleep(0.5)
                self.do_send_key(self.emailInput, email)
                time.sleep(1)
                self.do_clear_using_java_script(self.descriptionEdit)
                time.sleep(0.5)
                desc = self.generate_random_text()
                time.sleep(1)
                self.do_send_key(self.descriptionEdit, desc)
                time.sleep(1)
                self.de_click(self.submit)
                time.sleep(3)
                tType = self.get_element_text(self.titleTypeAfterEdit)
                assert title in tType
                time.sleep(0.5)
                # vType = self.get_element_text(self.visibilityAfterEdit)
                # assert "Private" in vType
                # time.sleep(0.5)
                # sType = self.get_element_text(self.serviceAfterEdit)
                # assert "Awards" in sType
                # time.sleep(0.5)
                qMail = self.get_element_text(self.qmailAfterEditInVideo)
                assert email in qMail
                time.sleep(0.5)
                # self.de_click(self.descriptionArrow)
                # time.sleep(0.5)
                # dType = self.get_element_text(self.Description)
                # assert desc in dType
                # time.sleep(1)
                self.de_click(self.backToInterviewIcon)
                time.sleep(2)
                break



    def view_details_of_webinar_of_multiway_interview(self):

        self.de_click(self.webinarIcon)
        time.sleep(3)
        log.logger.info("****==View list of Webinar details test case starts here==***")

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
            log.logger.info("**||Title||**    **||Visibility||**     **||Scheduled||**   **||Payment Type||** ")

            self.table_traverse_multiway_video_calls(rows, cols)
        else:
            log.logger.info("There's No Data Available")

        # 3.1 filter list of webinar  via search box
        log.logger.info("****==Filter list of webinar details via search box using webinar "
                        "title test case starts here==***")

        time.sleep(1)

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:

            is_designation_visible = self.driver.find_element(By.XPATH,
                                                              "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td[1]").is_displayed()

            value = str(is_designation_visible)
            if value == "True":
                designationName = self.get_element_text(self.designationDisplayed)
                time.sleep(0.5)
            else:
                log.logger.info("No Information Available")
            time.sleep(0.5)
            self.do_send_key(self.searchBox, designationName)
            time.sleep(1.5)

            rows1 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr"))

            cols1 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row == " + str(rows1))
            log.logger.info("Number Of Column == " + str(cols1))
            log.logger.info("**||Video Call Title||** ")

            self.multiway_video_call_table_traverse_search_via_title(rows1, cols1, designationName)
            self.de_click(self.closeIconOfSearchBox)
            time.sleep(1)
        else:
            log.logger.info("There's No Data Available")

        # 3.2 view details of individual webinar call

        log.logger.info("****==View Details Of individual Interview Of Multiway Webinar ===***")

        time.sleep(2)

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
                if i < 8:
                    elements = []
                    elements = self.driver.find_elements(By.XPATH,
                                                         "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[6]/div/button/*[local-name()='svg']")

                    visibility = []
                    visibility = self.driver.find_elements(By.XPATH,
                                                           "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[2]")
                    time.sleep(0.5)
                    visibility_type = visibility[i].text
                    time.sleep(0.5)
                    self.de_scroll_into_view(elements[i])
                    elements[i].click()
                    time.sleep(1)
                    self.de_click(self.viewWebinarDetailsIcon)
                    log.logger.info(
                        "!!! == User Has clicked view webinar icon against webinar title == !!!")
                    time.sleep(4)

                    rows = 1 + len(self.driver.find_elements(By.XPATH,
                                                             "//div[@class='border-[1px] w-full border-ime-gray-300 dark:border-ime-gray-600 rounded-[6px] overflow-hidden']/table/tbody/tr"))

                    # Obtain the number of columns in table
                    cols = len(self.driver.find_elements(By.XPATH,
                                                         "//div[@class='border-[1px] w-full border-ime-gray-300 dark:border-ime-gray-600 rounded-[6px] overflow-hidden']/table/tbody/tr/td[2]"))

                    # Print rows and columns
                    log.logger.info("Number Of Row" + str(rows))
                    log.logger.info("Number Of Column" + str(cols))
                    log.logger.info(
                        "**||Call Title||**              **||Visibility||**               **||Service||**        "
                        "**||Query Mail||**        **||Schedule||**   **||Created By||** ")

                    # Printing the data of the table
                    for r in range(1, rows):
                        for p in range(1, 2):
                            # obtaining the text from each column of the table
                            value = self.driver.find_element(By.XPATH,
                                                             "//div[@class='border-[1px] w-full border-ime-gray-300 dark:border-ime-gray-600 rounded-[6px] overflow-hidden']/table/tbody/tr[" + str(
                                                                 r) + "]/td[2]").text

                            log.logger.info("" + str(value))
                            time.sleep(0.5)

                    time.sleep(0.5)
                    self.de_click(self.descriptionArrow)
                    time.sleep(0.5)
                    Description = self.get_element_text(self.Description)
                    log.logger.info("Description Of Interview Is === " + str(Description))
                    time.sleep(0.5)
                    if visibility_type == "Public":
                        link = self.get_element_text(self.webinarLink)
                        log.logger.info("Webinar Link Is === " + str(link))
                        rPeople = self.get_element_text(self.registeredPeople)
                        log.logger.info("Number Of People Registered In Webinar Is === " + str(rPeople))
                        attended = self.get_element_text(self.Attendance)
                        log.logger.info("Number Of People Attended Webinar  Is === " + str(attended))
                    else:
                        log.logger.info("There's No Link Available For Private Webinar call")

                    self.de_click(self.backToInterviewIcon)
                    time.sleep(2)

        else:
            log.logger.info("There's No Data Available")

        # 3.3 Edit and assert the webinar Information
        log.logger.info("****==Edit Details Of individual Interview Of Multiway Webinar ===***")

        time.sleep(2)

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
                elements = []
                elements = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr/td[6]/div/button/*[local-name()='svg']")
                self.de_scroll_into_view(elements[i])
                elements[i].click()
                time.sleep(1)
                self.de_click(self.viewWebinarDetailsIcon)
                time.sleep(4)
                self.de_click(self.editButton)
                time.sleep(2)
                self.do_clear_using_java_script(self.title)
                time.sleep(1)
                dateTime = self.get_date_time_using_time_zone()
                time.sleep(1)
                title = self.generate_webinar_title()
                time.sleep(0.5)
                self.do_send_key(self.title, title)
                time.sleep(1)
                self.de_click(self.visibilityDD)
                time.sleep(1)
                self.de_click(self.privateDDOption)
                time.sleep(1)
                self.de_click(self.serviceDD)
                time.sleep(1)
                self.de_click(self.serviceDDOption)
                time.sleep(1)
                self.do_clear_using_java_script(self.emailInput)
                time.sleep(1)
                email = self.generate_random_email()
                time.sleep(0.5)
                self.do_send_key(self.emailInput, email)
                time.sleep(1)
                self.do_clear_using_java_script(self.descriptionEdit)
                time.sleep(0.5)
                desc = self.generate_random_text()
                time.sleep(1)
                self.do_send_key(self.descriptionEdit, desc)
                time.sleep(1)
                self.de_click(self.submit)
                time.sleep(3)
                # sType = self.get_element_text(self.serviceTypeAfterEdit)
                # assert "Awards" in sType
                # time.sleep(0.5)
                # vType = self.get_element_text(self.visibilityAfterEdit)
                # assert "Private" in vType
                # time.sleep(0.5)
                qMail = self.get_element_text(self.queryMailAfterEdit)
                assert email in qMail
                time.sleep(0.5)
                # self.de_click(self.descriptionArrow)
                # time.sleep(0.5)
                # dType = self.get_element_text(self.Description)
                # assert desc in dType
                time.sleep(1)
                break

        self.de_click(self.backToInterviewIcon)
        time.sleep(2)
