import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Interview_Details(BasePage):
    videoInterviewIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/button/div")
    oneWayInterviewIcon = (
        By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/div/div/div[2]/button[3]")

    # fetch data via search box

    searchBox = (By.CSS_SELECTOR, "input[name='interviewSearch']")
    closeIconOfSearchBox = (By.XPATH,
                            "//div[@class='flex mb-4 flex-row items-center border border-ime-gray-300 dark:border-ime-gray-600 rounded-[6px] h-[36px] p-2']/*[local-name()='svg'][@class='fill-black dark:fill-white scale-[180%] cursor-pointer mt-4 h-[14px] relative right-2']")
    designationDisplayed = (By.XPATH,
                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[1]/h5/div/div[2]/button/div/div")
    statusDisplayed = (By.XPATH,
                       "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[2]/h5/div/div[1]")

    # fetch data via status DD

    statusDD = (
        By.XPATH, "//div[@class='w-full flex flex-col lg:flex-row lg:gap-[20px] rounded-[6px]']/div[2]/div[1]/button")
    activeStatusDD = (
        By.XPATH, "//div[@class='w-full flex flex-col lg:flex-row lg:gap-[20px] rounded-[6px]']/div[2]/div[1]/ul/li[1]")
    inactiveStatusDD = (
        By.XPATH, "//div[@class='w-full flex flex-col lg:flex-row lg:gap-[20px] rounded-[6px]']/div[2]/div[1]/ul/li[2]")
    expiredStatusDD = (
        By.XPATH, "//div[@class='w-full flex flex-col lg:flex-row lg:gap-[20px] rounded-[6px]']/div[2]/div[1]/ul/li[2]")
    closeIconOfStatusDD = (By.XPATH,
                           "//div[@class='w-full flex flex-col lg:flex-row lg:gap-[20px] rounded-[6px]']/div[2]/div[1]/button/*[local-name()='svg'][@class='fill-black dark:fill-white scale-[250%] cursor-pointer absolute right-10']")

    # fetch data via Department DD

    departmentDD = (
        By.XPATH,
        "//div[@class='w-full flex flex-col lg:flex-row lg:gap-[20px] rounded-[6px]']/div[2]/div[2]/div/button")
    optionOfDepartmentDD = (By.XPATH,
                            "//div[@class='w-full flex flex-col lg:flex-row lg:gap-[20px] rounded-[6px]']/div[2]/div[2]/div/ul/li[10]")

    # edit interview status
    statusOfInterview = (
        By.XPATH, "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[2]/h5/div/div")
    cogButton = (By.XPATH,
                 "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[6]/div/button")
    viewDetailOption = (By.XPATH,
                        "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[6]/div/div/button")
    editLink = (By.XPATH,
                "//div[@class='col-span-2 max-md:col-span-3 border-[1px] border-ime-gray-300 dark:border-zinc-600 rounded-[6px]']/table/tbody/tr[1]/td[2]/button")
    deactivateButton = (
        By.XPATH, "//div[@id='headlessui-portal-root']/div[1]/div/div/div/div/div/div/div[3]/div/div/button[1]")
    backButton = (By.XPATH,
                  "//div[@class='w-full h-full min-h-screen overflow-hidden duration-300 flex flex-col ml-[250px]']/div/div[2]/div/div/div[1]/div/h2")

    # Award List Sections
    awardIcon = (By.XPATH, "//div[@class='dark:bg-black w-full h-full']/div/div[1]/button[3]")
    awardTypeDD = (
        By.XPATH, "//div[@class='w-full flex flex-col lg:flex-row lg:gap-[20px] rounded-[6px]']/div[2]/div[2]/button")
    optionOfAwardTypeDD = (
        By.XPATH, "//div[@class='w-full flex flex-col lg:flex-row lg:gap-[20px] rounded-[6px]']/div[2]/div[2]/ul/li[2]")
    closeButtonOfAwardType = (By.XPATH,
                              "//div[@class='w-full flex flex-col lg:flex-row lg:gap-[20px] rounded-[6px]']/div[2]/div[2]/button/*[local-name()='svg'][@class='fill-black dark:fill-white scale-[250%] cursor-pointer absolute right-10']")

    # Marketing List Sections
    marketingIcon = (By.XPATH, "//div[@class='dark:bg-black w-full h-full']/div/div[1]/button[4]")

    # Learning List Sections
    learningIcon = (By.XPATH, "//div[@class='dark:bg-black w-full h-full']/div/div[1]/button[5]")
    optionOfDepartmentDDForLearning = (
        By.XPATH,
        "//div[@class='w-full flex flex-col lg:flex-row lg:gap-[20px] rounded-[6px]']/div[2]/div[2]/div/ul/li[2]")
    closeIconOfDepartmentDdLearning = (By.XPATH,
                                       "//div[@class='w-full flex flex-col lg:flex-row lg:gap-[20px] rounded-[6px]']/div[2]/div[2]/div/button/*[local-name()='svg'][@class='fill-black dark:fill-white scale-[250%] cursor-pointer absolute right-10']")

    # Audition List Sections

    auditionIcon = (By.XPATH, "//div[@class='dark:bg-black w-full h-full']/div/div[1]/button[6]")

    # Admission List Sections

    admissionIcon = (By.XPATH, "//div[@class='dark:bg-black w-full h-full']/div/div[1]/button[2]")
    global designationName, statusName

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_interview_icon(self):
        time.sleep(4)
        self.de_click(self.videoInterviewIcon)
        time.sleep(1)
        self.de_click(self.oneWayInterviewIcon)
        time.sleep(5)

    def fetch_recruitment_interview_details(self):
        log.logger.info("****==View list of recruitment interview's details test case starts here==***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            rows = len(self.driver.find_elements(By.XPATH,
                                                 "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr"))

            cols = len(self.driver.find_elements(By.XPATH,
                                                 "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td"))
            log.logger.info("Number Of Row == " + str(rows))
            log.logger.info("Number Of Column == " + str(cols))
            log.logger.info("**||Employment Position||**        **||Status||**        **||Interview Type||**      "
                            "**||Start Date||**         ")

            self.table_traverse(rows, cols)
        else:
            log.logger.info("There's No Data Available")

        # # 1.1 filter list of recruitment interviews via search box
        # log.logger.info("****==Filter list of recruitment interview's details via search box using employment "
        #                 "position test case starts here==***")
        #
        # time.sleep(1)
        #
        # dataAvail = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH,
        #                                     "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        # )
        # value = dataAvail.text
        # # log.logger.info("" + value)
        # if len(value) > 0:
        #
        #     is_designation_visible = self.driver.find_element(By.XPATH,
        #                                                       "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[1]/h5/div/div[1]").is_displayed()
        #
        #     value = str(is_designation_visible)
        #     if value == "True":
        #         designationName = self.get_element_text(self.designationDisplayed)
        #         time.sleep(0.5)
        #     else:
        #         log.logger.info("No Information Available")
        #     time.sleep(0.5)
        #     self.do_send_key(self.searchBox, designationName)
        #     time.sleep(1.5)
        #
        #     rows1 = len(self.driver.find_elements(By.XPATH,
        #                                           "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr"))
        #
        #     cols1 = len(self.driver.find_elements(By.XPATH,
        #                                           "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td"))
        #
        #     log.logger.info("Number Of Row == " + str(rows1))
        #     log.logger.info("Number Of Column == " + str(cols1))
        #     log.logger.info("**||Employment Position||** ")
        #
        #     self.table_traverse_search(rows1, cols1, designationName)
        #     self.de_click(self.closeIconOfSearchBox)
        #     time.sleep(1)
        # else:
        #     log.logger.info("There's No Data Available")

        # 1.2 filter list of recruitment interviews via interview status
        log.logger.info("****==Filter list of recruitment interview's details via interview status"
                        "position test case starts here==***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            is_status_visible = self.driver.find_element(By.XPATH,
                                                         "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[2]/h5/div/div[1]").is_displayed()

            value1 = str(is_status_visible)
            if value1 == "True":
                statusName = self.get_element_text(self.statusDisplayed)
                time.sleep(0.5)
            else:
                log.logger.info("No Information Available")
            time.sleep(0.5)
            self.de_click(self.statusDD)
            time.sleep(0.5)
            if statusName == "Active":
                self.de_click(self.activeStatusDD)
                time.sleep(1)
            elif statusName == "Inactive":
                self.de_click(self.inactiveStatusDD)
                time.sleep(1)
            elif statusName == "Expired":
                self.de_click(self.expiredStatusDD)
                time.sleep(1)
            rows2 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            cols2 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row == " + str(rows2))
            log.logger.info("Number Of Column == " + str(cols2))
            log.logger.info("**||Interview Status||** ")

            self.table_traverse_status_dd(rows2, cols2, statusName)
            self.de_click(self.closeIconOfStatusDD)

        else:
            log.logger.info("There's No Data Available")

        # 1.3 filter list of recruitment interviews via department
        log.logger.info("****==Filter list of recruitment interview's details via interview department"
                        "test case starts here==***")
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            time.sleep(1)
            self.de_click(self.departmentDD)
            time.sleep(0.5)
            self.de_click(self.optionOfDepartmentDD)
            time.sleep(1)

            rows3 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr"))

            cols3 = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row" + str(rows3))
            log.logger.info("Number Of Column" + str(cols3))
            log.logger.info("**||Employment Position||**        **||Status||**        **||Interview Type||**      "
                            "**||Start Date||**         ")

            self.table_traverse(rows3, cols3)
        else:
            log.logger.info("There's No Data Available")

        # 1.4 edit status of interview

        log.logger.info("****==Change the interview status and verify the same for recruitment "
                        "test case starts here==***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            status = self.get_element_text(self.statusOfInterview)
            log.logger.info("Initial status of interview === " + str(status))
            self.de_click(self.cogButton)
            time.sleep(0.5)
            self.de_click(self.viewDetailOption)
            time.sleep(2)
            self.de_click(self.editLink)
            time.sleep(1)

            deactivate = self.driver.find_element(By.XPATH,
                                                  "//div[@id='headlessui-portal-root']/div[1]/div/div/div/div/div/div/div[3]/div/div/button[1]")
            self.de_action_method(deactivate)
            time.sleep(5)
            self.de_click(self.backButton)
            time.sleep(2)
            if status == "Inactive":
                log.logger.info(
                    "Status of interview after editing === " + str(self.get_element_text(self.statusOfInterview)))
                assert self.get_element_text(self.statusOfInterview) == "Active"

            else:
                log.logger.info(
                    "Status of interview after editing === " + str(self.get_element_text(self.statusOfInterview)))
                assert self.get_element_text(self.statusOfInterview) == "Inactive"

        else:
            log.logger.info("There's No Data Available")

    #  Award vertical test scenario start here
    def fetch_award_interview_details(self):
        log.logger.info("****==View list of award interview's details test case starts here==***")
        self.de_click(self.awardIcon)
        time.sleep(7)
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            rows = len(self.driver.find_elements(By.XPATH,
                                                 "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr"))

            cols = len(self.driver.find_elements(By.XPATH,
                                                 "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row" + str(rows))
            log.logger.info("Number Of Column" + str(cols))
            log.logger.info("**||Category||**        **||Status||**        **||Interview Type||**      "
                            "**||Start Date||**         ")

            self.table_traverse(rows, cols)
        else:
            log.logger.info("There's No Data Available")

        # # 2.1 filter list of award interviews via search box using category
        # log.logger.info("****==Filter list of award interview's details via search box using category "
        #                 "test case starts here==***")
        # time.sleep(1)
        # dataAvail = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH,
        #                                     "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        # )
        # value = dataAvail.text
        # # log.logger.info("" + value)
        # if len(value) > 0:
        #
        #     is_designation_visible = self.driver.find_element(By.XPATH,
        #                                                       "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[1]/h5/div/div[1]").is_displayed()
        #
        #     value = str(is_designation_visible)
        #     if value == "True":
        #         designationName = self.get_element_text(self.designationDisplayed)
        #         time.sleep(0.5)
        #     else:
        #         log.logger.info("No Information Available")
        #     time.sleep(0.5)
        #     self.do_send_key(self.searchBox, designationName)
        #     time.sleep(1.5)
        #
        #     rows1 = len(self.driver.find_elements(By.XPATH,
        #                                           "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))
        #
        #     # Obtain the number of columns in table
        #     cols1 = len(self.driver.find_elements(By.XPATH,
        #                                           "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))
        #
        #     # Print rows and columns
        #     log.logger.info("Number Of Row" + str(rows1))
        #     log.logger.info("Number Of Column" + str(cols1))
        #     log.logger.info("**||Category||** ")
        #
        #     self.table_traverse(rows1, cols1)
        #
        #     self.de_click(self.closeIconOfSearchBox)
        #
        # else:
        #     log.logger.info("There's No Data Available")

        # 2.2 filter list of award interviews via interview status
        log.logger.info("****==Filter list of award interview's details via interview status"
                        "position test case starts here==***")

        time.sleep(1)
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            self.de_click(self.statusDD)
            time.sleep(0.5)
            is_status_visible = self.driver.find_element(By.XPATH,
                                                         "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[2]/h5/div/div[1]").is_displayed()

            value1 = str(is_status_visible)
            if value1 == "True":
                statusName = self.get_element_text(self.statusDisplayed)
                time.sleep(0.5)
            else:
                log.logger.info("No Information Available")
            time.sleep(0.5)
            if statusName == "Active":
                self.de_click(self.activeStatusDD)
                time.sleep(1)
            elif statusName == "Inactive":
                self.de_click(self.inactiveStatusDD)
                time.sleep(1)
            elif statusName == "Expired":
                self.de_click(self.expiredStatusDD)
                time.sleep(1)

            rows2 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            cols2 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row" + str(rows2))
            log.logger.info("Number Of Column" + str(cols2))
            log.logger.info("**||Interview Status||** ")

            self.table_traverse_status_dd(rows2, cols2, statusName)
            self.de_click(self.closeIconOfStatusDD)

        else:
            log.logger.info("There's No Data Available")

        # 2.3 filter list of award interviews via award type
        log.logger.info("****==Filter list of recruitment interview's details via award type"
                        "test case starts here==***")
        time.sleep(1)
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            self.de_click(self.awardTypeDD)
            time.sleep(0.5)
            self.de_click(self.optionOfAwardTypeDD)
            time.sleep(1)

            rows3 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            cols3 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row" + str(rows3))
            log.logger.info("Number Of Column" + str(cols3))
            log.logger.info("**||Category||**        **||Status||**        **||Interview Type||**      "
                            "**||Start Date||**         ")

            self.table_traverse(rows3, cols3)
            self.de_click(self.closeButtonOfAwardType)
            time.sleep(0.5)
            self.de_click(self.awardTypeDD)
            time.sleep(0.5)

        else:
            log.logger.info("There's No Data Available")

        # 2.4 edit status of interview
        log.logger.info("****==Change the interview status and verify the same for award "
                        "test case starts here==***")

        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            status = self.get_element_text(self.statusOfInterview)
            log.logger.info("Initial status of interview === " + str(status))
            self.de_click(self.cogButton)
            time.sleep(0.5)
            self.de_click(self.viewDetailOption)
            time.sleep(2)
            self.de_click(self.editLink)
            time.sleep(1)
            deactivate = self.driver.find_element(By.XPATH,
                                                  "//div[@id='headlessui-portal-root']/div[1]/div/div/div/div/div/div/div[3]/div/div/button[1]")

            self.de_action_method(deactivate)
            time.sleep(5)
            self.de_click(self.backButton)
            time.sleep(2)
            if status == "Inactive":
                log.logger.info(
                    "Status of interview after editing === " + str(self.get_element_text(self.statusOfInterview)))
                assert self.get_element_text(self.statusOfInterview) == "Active"

            else:
                log.logger.info(
                    "Status of interview after editing === " + str(self.get_element_text(self.statusOfInterview)))
                assert self.get_element_text(self.statusOfInterview) == "Inactive"

        else:
            log.logger.info("There's No Data Available")

    # Marketing vertical test scenario start here

    def fetch_marketing_interview_details(self):
        log.logger.info("****==View list of marketing interview's details test case starts here==***")
        self.de_click(self.marketingIcon)
        time.sleep(7)
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            rows = len(self.driver.find_elements(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            cols = len(self.driver.find_elements(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row" + str(rows))
            log.logger.info("Number Of Column" + str(cols))
            log.logger.info("**||Interview Title||**        **||Status||**        **||Interview Type||**      "
                            "**||Start Date||**         ")

            self.table_traverse(rows, cols)
        else:
            log.logger.info("There's No Data Available")

        # 3.1 filter list of Marketing interviews via search box using category
        # log.logger.info("****==Filter list of award interview's details via search box using interview title "
        #                 "test case starts here==***")
        # time.sleep(1)
        # dataAvail = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH,
        #                                     "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        # )
        # value = dataAvail.text
        # # log.logger.info("" + value)
        # if len(value) > 0:
        #     is_designation_visible = self.driver.find_element(By.XPATH,
        #                                                       "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[1]/h5/div/div[1]").is_displayed()
        #
        #     value = str(is_designation_visible)
        #     if value == "True":
        #         designationName = self.get_element_text(self.designationDisplayed)
        #         time.sleep(0.5)
        #     else:
        #         log.logger.info("No Information Available")
        #     time.sleep(0.5)
        #
        #     self.do_send_key(self.searchBox, designationName)
        #     time.sleep(1.5)
        #
        #     rows1 = len(self.driver.find_elements(By.XPATH,
        #                                           "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))
        #
        #     cols1 = len(self.driver.find_elements(By.XPATH,
        #                                           "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))
        #
        #     log.logger.info("Number Of Row" + str(rows1))
        #     log.logger.info("Number Of Column" + str(cols1))
        #     log.logger.info("**||Interview Title||** ")
        #     self.table_traverse_search(rows1, cols1, designationName)
        #     self.de_click(self.closeIconOfSearchBox)
        #
        # else:
        #     log.logger.info("There's No Data Available")

        # 3.2 filter list of marketing interviews via interview status
        log.logger.info("****==Filter list of marketing interview's details via interview status"
                        "position test case starts here==***")
        time.sleep(1)
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            is_status_visible = self.driver.find_element(By.XPATH,
                                                         "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[2]/h5/div/div[1]").is_displayed()

            value1 = str(is_status_visible)
            if value1 == "True":
                statusName = self.get_element_text(self.statusDisplayed)
                time.sleep(0.5)
            else:
                log.logger.info("No Information Available")
            time.sleep(0.5)
            self.de_click(self.statusDD)
            time.sleep(0.5)
            if statusName == "Active":
                self.de_click(self.activeStatusDD)
                time.sleep(1)
            elif statusName == "Inactive":
                self.de_click(self.inactiveStatusDD)
                time.sleep(1)
            elif statusName == "Expired":
                self.de_click(self.expiredStatusDD)
                time.sleep(1)

            rows2 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            cols2 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row" + str(rows2))
            log.logger.info("Number Of Column" + str(cols2))
            log.logger.info("**||Interview Status||** ")

            self.table_traverse_status_dd(rows2, cols2, statusName)
            self.de_click(self.closeIconOfStatusDD)
            time.sleep(0.5)
            self.de_click(self.statusDD)
            time.sleep(0.5)

        else:
            log.logger.info("There's No Data Available")

        # 3.3 edit status of interview
        log.logger.info("****==Change the interview status and verify the same for award "
                        "test case starts here==***")
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            status = self.get_element_text(self.statusOfInterview)
            log.logger.info("Initial status of interview === " + str(status))
            self.de_click(self.cogButton)
            time.sleep(0.5)
            self.de_click(self.viewDetailOption)
            time.sleep(2)
            self.de_click(self.editLink)
            time.sleep(1)
            deactivate = self.driver.find_element(By.XPATH,
                                                  "//div[@id='headlessui-portal-root']/div[1]/div/div/div/div/div/div/div[3]/div/div/button[1]")
            self.de_action_method(deactivate)
            time.sleep(5)
            self.de_click(self.backButton)
            time.sleep(2)
            if status == "Inactive":
                log.logger.info(
                    "Status of interview after editing === " + str(self.get_element_text(self.statusOfInterview)))
                assert self.get_element_text(self.statusOfInterview) == "Active"

            else:
                log.logger.info(
                    "Status of interview after editing === " + str(self.get_element_text(self.statusOfInterview)))
                assert self.get_element_text(self.statusOfInterview) == "Inactive"

        else:
            log.logger.info("There's No Data Available")

    # Learning vertical test scenario start here

    def fetch_learning_interview_details(self):

        log.logger.info("****==View list of list of  interview's details of learning vertical test case starts "
                        "here==***")
        self.de_click(self.learningIcon)
        time.sleep(7)
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            rows = len(self.driver.find_elements(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            cols = len(self.driver.find_elements(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row" + str(rows))
            log.logger.info("Number Of Column" + str(cols))
            log.logger.info("**||Employment Position||**        **||Status||**        **||Interview Type||**      "
                            "**||Start Date||**         ")

            self.table_traverse(rows, cols)

        else:
            log.logger.info("There's No Data Available")

        # 4.1 filter list of Learning interviews via search box using category
        # log.logger.info("****==Filter list of award interview's details via search box using interview title "
        #                 "test case starts here==***")
        # time.sleep(1)
        # dataAvail = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH,
        #                                     "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        # )
        # value = dataAvail.text
        # # log.logger.info("" + value)
        # if len(value) > 0:
        #     is_designation_visible = self.driver.find_element(By.XPATH,
        #                                                       "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[1]/h5/div/div[1]").is_displayed()
        #
        #     value = str(is_designation_visible)
        #     if value == "True":
        #         designationName = self.get_element_text(self.designationDisplayed)
        #         time.sleep(0.5)
        #     else:
        #         log.logger.info("No Information Available")
        #     time.sleep(0.5)
        #     self.do_send_key(self.searchBox, designationName)
        #     time.sleep(1.5)
        #
        #     rows1 = len(self.driver.find_elements(By.XPATH,
        #                                           "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))
        #
        #     cols1 = len(self.driver.find_elements(By.XPATH,
        #                                           "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))
        #
        #     log.logger.info("Number Of Row" + str(rows1))
        #     log.logger.info("Number Of Column" + str(cols1))
        #     log.logger.info("**||Employment Position||** ")
        #     self.table_traverse_search_learning(rows1, cols1, designationName)
        #     self.de_click(self.closeIconOfSearchBox)
        # else:
        #     log.logger.info("There's No Data Available")

        # # 4.2 filter list of learning interviews via interview status
        # log.logger.info("****==Filter list of learning interview's details via interview status"
        #                 "position test case starts here==***")
        # time.sleep(1)
        # dataAvail = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH,
        #                                     "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        # )
        # value = dataAvail.text
        # # log.logger.info("" + value)
        # if len(value) > 0:
        #     is_status_visible = self.driver.find_element(By.XPATH,
        #                                                  "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[2]/h5/div/div[1]").is_displayed()
        #
        #     value1 = str(is_status_visible)
        #     if value1 == "True":
        #         statusName = self.get_element_text(self.statusDisplayed)
        #         time.sleep(0.5)
        #     else:
        #         log.logger.info("No Information Available")
        #     time.sleep(0.5)
        #     self.de_click(self.statusDD)
        #     time.sleep(0.5)
        #     if statusName == "Active":
        #         self.de_click(self.activeStatusDD)
        #         time.sleep(1)
        #     elif statusName == "Inactive":
        #         self.de_click(self.inactiveStatusDD)
        #         time.sleep(1)
        #     elif statusName == "Active":
        #         self.de_click(self.activeStatusDD)
        #         time.sleep(1)
        #
        #     rows2 = len(self.driver.find_elements(By.XPATH,
        #                                           "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))
        #
        #     cols2 = len(self.driver.find_elements(By.XPATH,
        #                                           "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))
        #
        #     log.logger.info("Number Of Row == " + str(rows2))
        #     log.logger.info("Number Of Column == " + str(cols2))
        #     log.logger.info("**||Interview Status||** ")
        #
        #     self.table_traverse_status_dd(rows2, cols2, statusName)
        #     self.de_click(self.closeIconOfStatusDD)
        # else:
        #     log.logger.info("There's No Data Available")

        # 4.3 filter list of learning interviews via department
        # time.sleep(1)
        # dataAvail = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH,
        #                                     "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        # )
        # value = dataAvail.text
        # # log.logger.info("" + value)
        # if len(value) > 0:
        #     self.de_click(self.departmentDD)
        #     time.sleep(0.5)
        #     self.de_click(self.optionOfDepartmentDDForLearning)
        #     time.sleep(1)
        #     log.logger.info("****==Filter list of learning interview's details via interview department"
        #                     "test case starts here==***")
        #
        #     rows3 = len(self.driver.find_elements(By.XPATH,
        #                                           "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))
        #
        #     cols3 = len(self.driver.find_elements(By.XPATH,
        #                                           "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))
        #
        #     log.logger.info("Number Of Row" + str(rows3))
        #     log.logger.info("Number Of Column" + str(cols3))
        #     log.logger.info("**||Employment Position||**        **||Status||**        **||Interview Type||**      "
        #                     "**||Start Date||**         ")
        #
        #     self.table_traverse(rows3, cols3)
        #     self.de_click(self.closeIconOfDepartmentDdLearning)
        #     time.sleep(0.5)
        #     self.de_click(self.statusDD)
        #     time.sleep(0.5)
        #
        # else:
        #     log.logger.info("There's No Data Available")

        # 4.4 edit status of interview
        log.logger.info("****==Change the interview status and verify the same for learning "
                        "test case starts here==***")
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            status = self.get_element_text(self.statusOfInterview)
            log.logger.info("Initial status of interview === " + str(status))
            self.de_click(self.cogButton)
            time.sleep(0.5)
            self.de_click(self.viewDetailOption)
            time.sleep(2)
            self.de_click(self.editLink)
            time.sleep(1)
            deactivate = self.driver.find_element(By.XPATH,
                                                  "//div[@id='headlessui-portal-root']/div[1]/div/div/div/div/div/div/div[3]/div/div/button[1]")
            self.de_action_method(deactivate)
            time.sleep(5)
            self.de_click(self.backButton)
            time.sleep(2)
            if status == "Inactive":
                log.logger.info(
                    "Status of interview after editing === " + str(self.get_element_text(self.statusOfInterview)))
                assert self.get_element_text(self.statusOfInterview) == "Active"

            else:
                log.logger.info(
                    "Status of interview after editing === " + str(self.get_element_text(self.statusOfInterview)))
                assert self.get_element_text(self.statusOfInterview) == "Inactive"

        else:
            log.logger.info("There's No Data Available")

    # Audition vertical test scenario start here

    def fetch_audition_interview_details(self):

        log.logger.info("****==View list of list of  interview's details of audition vertical test case starts "
                        "here==***")
        self.de_click(self.auditionIcon)
        time.sleep(7)
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            rows = len(self.driver.find_elements(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            cols = len(self.driver.find_elements(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row" + str(rows))
            log.logger.info("Number Of Column" + str(cols))
            log.logger.info("**||Interview||**        **||Status||**        **||Interview Type||**      "
                            "**||Start Date||**         ")

            self.table_traverse(rows, cols)
        else:
            log.logger.info("There's No Data Available")

        # 5.1 filter list of Audition interviews via search box using category
        # log.logger.info("****==Filter list of audition interview's details via search box using interview title "
        #                 "test case starts here==***")
        # time.sleep(1)
        # dataAvail = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH,
        #                                     "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        # )
        # value = dataAvail.text
        # # log.logger.info("" + value)
        # if len(value) > 0:
        #     is_designation_visible = self.driver.find_element(By.XPATH,
        #                                                       "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[1]/h5/div/div[1]").is_displayed()
        #
        #     value = str(is_designation_visible)
        #     if value == "True":
        #         designationName = self.get_element_text(self.designationDisplayed)
        #         time.sleep(0.5)
        #     else:
        #         log.logger.info("No Information Available")
        #     time.sleep(0.5)
        #     self.do_send_key(self.searchBox, designationName)
        #     time.sleep(1.5)
        #
        #     rows1 = len(self.driver.find_elements(By.XPATH,
        #                                           "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))
        #
        #     cols1 = len(self.driver.find_elements(By.XPATH,
        #                                           "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))
        #
        #     log.logger.info("Number Of Row" + str(rows1))
        #     log.logger.info("Number Of Column" + str(cols1))
        #     log.logger.info("**||Employment Position||** ")
        #     self.table_traverse_search_audition(rows1, cols1, designationName)
        #     self.de_click(self.closeIconOfSearchBox)
        # else:
        #     log.logger.info("There's No Data Available")

        # 5.2 filter list of audition interviews via interview status
        log.logger.info("****==Filter list of audition interview's details via interview status"
                        "position test case starts here==***")

        time.sleep(1)
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            is_status_visible = self.driver.find_element(By.XPATH,
                                                         "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[2]/h5/div/div[1]").is_displayed()

            value1 = str(is_status_visible)
            if value1 == "True":
                statusName = self.get_element_text(self.statusDisplayed)
                time.sleep(0.5)
            else:
                log.logger.info("No Information Available")
            time.sleep(0.5)
            self.de_click(self.statusDD)
            time.sleep(0.5)
            if statusName == "Active":
                self.de_click(self.activeStatusDD)
                time.sleep(1)
            elif statusName == "Inactive":
                self.de_click(self.inactiveStatusDD)
                time.sleep(1)
            elif statusName == "Expired":
                self.de_click(self.expiredStatusDD)
                time.sleep(1)

            rows2 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            cols2 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row == " + str(rows2))
            log.logger.info("Number Of Column == " + str(cols2))
            log.logger.info("**||Interview Status||** ")

            self.table_traverse_status_dd(rows2, cols2, statusName)
            self.de_click(self.closeIconOfStatusDD)
            self.de_click(self.statusDD)

        else:
            log.logger.info("There's No Data Available")

        # 5.4 edit status of interview
        log.logger.info("****==Change the interview status and verify the same for Audition "
                        "test case starts here==***")
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            status = self.get_element_text(self.statusOfInterview)
            log.logger.info("Initial status of interview === " + str(status))
            self.de_click(self.cogButton)
            time.sleep(0.5)
            self.de_click(self.viewDetailOption)
            time.sleep(2)
            self.de_click(self.editLink)
            time.sleep(1)
            deactivate = self.driver.find_element(By.XPATH,
                                                  "//div[@id='headlessui-portal-root']/div[1]/div/div/div/div/div/div/div[3]/div/div/button[1]")
            self.de_action_method(deactivate)
            time.sleep(5)
            self.de_click(self.backButton)
            time.sleep(2)
            if status == "Inactive":
                log.logger.info(
                    "Status of interview after editing === " + str(self.get_element_text(self.statusOfInterview)))
                assert self.get_element_text(self.statusOfInterview) == "Active"

            else:
                log.logger.info(
                    "Status of interview after editing === " + str(self.get_element_text(self.statusOfInterview)))
                assert self.get_element_text(self.statusOfInterview) == "Inactive"

        else:
            log.logger.info("There's No Data Available")

    # Admission vertical test scenario start here

    def fetch_admission_interview_details(self):

        log.logger.info("****==View list of list of  interview's details of admission vertical test case starts "
                        "here==***")
        self.de_click(self.admissionIcon)
        time.sleep(7)
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            rows = len(self.driver.find_elements(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            cols = len(self.driver.find_elements(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row" + str(rows))
            log.logger.info("Number Of Column" + str(cols))
            log.logger.info("**||Interview||**        **||Status||**        **||Interview Type||**      "
                            "**||Start Date||**         ")

            self.table_traverse(rows, cols)
        else:
            log.logger.info("There's No Data Available")

        # 5.1 filter list of Admission interviews via search box using category
        # log.logger.info("****==Filter list of admission interview's details via search box using interview title "
        #                 "test case starts here==***")
        #
        # time.sleep(1)
        # dataAvail = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH,
        #                                     "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        # )
        # value = dataAvail.text
        # # log.logger.info("" + value)
        # if len(value) > 0:
        #
        #     is_designation_visible = self.driver.find_element(By.XPATH,
        #                                                       "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[1]/h5/div/div[1]").is_displayed()
        #
        #     value = str(is_designation_visible)
        #     if value == "True":
        #         designationName = self.get_element_text(self.designationDisplayed)
        #         time.sleep(0.5)
        #     else:
        #         log.logger.info("No Information Available")
        #     time.sleep(0.5)
        #     self.do_send_key(self.searchBox, designationName)
        #     time.sleep(1.5)
        #
        #     rows1 = len(self.driver.find_elements(By.XPATH,
        #                                           "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))
        #
        #     cols1 = len(self.driver.find_elements(By.XPATH,
        #                                           "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))
        #
        #     log.logger.info("Number Of Row" + str(rows1))
        #     log.logger.info("Number Of Column" + str(cols1))
        #     log.logger.info("**||Employment Position||** ")
        #     self.table_traverse_search_admission(rows1, cols1, designationName)
        #     self.de_click(self.closeIconOfSearchBox)
        #
        # else:
        #     log.logger.info("There's No Data Available")

        # 5.2 filter list of admission interviews via interview status
        log.logger.info("****==Filter list of admission interview's details via interview status"
                        "position test case starts here==***")
        time.sleep(1)
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            is_status_visible = self.driver.find_element(By.XPATH,
                                                         "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[2]/h5/div/div[1]").is_displayed()

            value1 = str(is_status_visible)
            if value1 == "True":
                statusName = self.get_element_text(self.statusDisplayed)
                time.sleep(0.5)
            else:
                log.logger.info("No Information Available")
            time.sleep(0.5)
            self.de_click(self.statusDD)
            time.sleep(0.5)
            if statusName == "Active":
                self.de_click(self.activeStatusDD)
                time.sleep(1)
            elif statusName == "Inactive":
                self.de_click(self.inactiveStatusDD)
                time.sleep(1)
            elif statusName == "Expired":
                self.de_click(self.expiredStatusDD)
                time.sleep(1)

            rows2 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

            cols2 = len(self.driver.find_elements(By.XPATH,
                                                  "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

            log.logger.info("Number Of Row == " + str(rows2))
            log.logger.info("Number Of Column == " + str(cols2))
            log.logger.info("**||Interview Status||** ")

            self.table_traverse_status_dd(rows2, cols2, statusName)
            self.de_click(self.closeIconOfStatusDD)
            self.de_click(self.statusDD)

        else:
            log.logger.info("There's No Data Available")

        # 5.4 edit status of interview
        log.logger.info("****==Change the interview status and verify the same for Admission "
                        "test case starts here==***")
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            status = self.get_element_text(self.statusOfInterview)
            log.logger.info("Initial status of interview === " + str(status))
            self.de_click(self.cogButton)
            time.sleep(0.5)
            self.de_click(self.viewDetailOption)
            time.sleep(2)
            self.de_click(self.editLink)
            time.sleep(1)
            deactivate = self.driver.find_element(By.XPATH,
                                                  "//div[@id='headlessui-portal-root']/div[1]/div/div/div/div/div/div/div[3]/div/div/button[1]")
            self.de_action_method(deactivate)
            time.sleep(5)
            self.de_click(self.backButton)
            time.sleep(2)
            if status == "Inactive":
                log.logger.info(
                    "Status of interview after editing === " + str(self.get_element_text(self.statusOfInterview)))
                assert self.get_element_text(self.statusOfInterview) == "Active"

            else:
                log.logger.info(
                    "Status of interview after editing === " + str(self.get_element_text(self.statusOfInterview)))
                assert self.get_element_text(self.statusOfInterview) == "Inactive"
        else:
            log.logger.info("There's No Data Available")
