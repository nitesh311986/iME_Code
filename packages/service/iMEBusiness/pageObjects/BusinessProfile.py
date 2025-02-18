import time
from selenium.webdriver.common.by import By
import logging
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class BusinessProfilePage(BasePage):
    # Business Profile elements
    businessProfileIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[1]/a")
    businessDetailsIcon = (By.XPATH, "//button[@id='headlessui-tabs-tab-:r47:']")
    businessName = (By.CSS_SELECTOR, "input[name='businessName']")
    businessEmail = (By.CSS_SELECTOR, "input[name='email']")
    businessContactNumber = (By.CSS_SELECTOR, "input[name='contactNumber']")
    businessLocation = (By.CSS_SELECTOR, "input[name='businessLocation']")

    # Business Subscription elements
    businessSubscriptionIcon = (By.XPATH, "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[2]")
    distributionCode = (By.XPATH,
                        "//div[@class=' md:gap-x-[2px] grid grid-cols-2 dark:bg-zinc-900 rounded-md border border-zinc-300 dark:border-zinc-600 pb-2 mb-4 lg:w-[328px] ']/div[2]")
    clientId = (By.XPATH,
                "//div[@class=' md:gap-x-[2px] grid grid-cols-2 dark:bg-zinc-900 rounded-md border border-zinc-300 dark:border-zinc-600 pb-2 mb-4 lg:w-[328px] ']/div[6]")
    planName = (By.XPATH,
                "//div[@class=' md:w-full md:h-full dark:bg-zinc-900 rounded-md border border-zinc-300 dark:border-zinc-600 mb-4 lg:w-[328px] ']/div[1]")
    billCycle = (By.XPATH,
                 "//div[@class=' md:w-full md:h-full dark:bg-zinc-900 rounded-md border border-zinc-300 dark:border-zinc-600 mb-4 lg:w-[328px] ']/div[1]/div/div")
    balance = (By.XPATH,
               "//div[@class=' md:w-full md:h-full dark:bg-zinc-900 rounded-md border border-zinc-300 dark:border-zinc-600 mb-4 lg:w-[328px] ']/div[2]/div[1]")
    renewalDetails = (By.XPATH,
                      "//div[@class=' md:w-full md:h-full dark:bg-zinc-900 rounded-md border border-zinc-300 dark:border-zinc-600 mb-4 lg:w-[328px] ']/div[2]/div[2]")
    usedVideoMinutes = (By.XPATH,
                        "//div[@class='flex flex-col items-center border border-zinc-300 bg-white h-[297px] rounded-md dark:bg-zinc-900 dark:border-zinc-600']/div[3]/div[1]/h5[2]")
    availableVideoMinutes = (By.XPATH,
                             "//div[@class='flex flex-col items-center border border-zinc-300 bg-white h-[297px] rounded-md dark:bg-zinc-900 dark:border-zinc-600']/div[3]/div[2]/h5[2]")

    # User

    businessUserIcon = (By.XPATH, "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[3]")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_profile_icon(self):
        time.sleep(3)
        self.de_click(self.businessProfileIcon)
        time.sleep(3)

    def fetch_business_details(self):
        log.logger.info("****==View Business Details Test Case Starts Here==***")
        business_Name = self.get_attribute(self.businessName, "value")
        log.logger.info("Name of business is == " + str(business_Name))
        business_Email = self.get_attribute(self.businessEmail, "value")
        log.logger.info("Email of business is == " + str(business_Email))
        business_Number = self.get_attribute(self.businessContactNumber, "value")
        log.logger.info("Contact number of business is == " + str(business_Number))
        business_Location = self.get_attribute(self.businessLocation, "value")
        log.logger.info("Location of business is == " + str(business_Location))

    def fetch_subscription_details(self):
        log.logger.info("****==View Business Subscription Test Case Starts Here==***")
        self.de_click(self.businessSubscriptionIcon)
        time.sleep(3)
        distribution_Code = self.get_element_text(self.distributionCode)
        log.logger.info("Distribution code of business subscription is == " + str(distribution_Code))
        client_Id = self.get_element_text(self.clientId)
        log.logger.info("Client Id of business subscription is == " + str(client_Id))
        plan_Name = self.get_element_text(self.planName)
        log.logger.info("Plan name of business subscription is == " + str(plan_Name))
        bill_Cycle = self.get_element_text(self.billCycle)
        log.logger.info("Bill cycle of business subscription is == " + str(bill_Cycle))
        Balance = self.get_element_text(self.balance)
        log.logger.info("Balance of business subscription is == " + str(Balance))
        renewal_Details = self.get_element_text(self.renewalDetails)
        log.logger.info("Renewal details of business subscription is == " + str(renewal_Details))
        used_Video_Minute = self.get_element_text(self.usedVideoMinutes)
        log.logger.info("Used video minute of business subscription is == " + str(used_Video_Minute))
        available_Video_Minutes = self.get_element_text(self.availableVideoMinutes)
        log.logger.info("Available video minute of business subscription is == " + str(available_Video_Minutes))

    def fetch_user_details(self):
        log.logger.info("****==View Business User details Test Case Starts Here==***")
        self.de_click(self.businessUserIcon)
        time.sleep(5)

        rows = 1 + len(self.driver.find_elements(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr"))

        # Obtain the number of columns in table
        cols = len(self.driver.find_elements(By.XPATH,
                                             "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td"))

        # Print rows and columns
        log.logger.info("Number Of Row" + str(rows))
        log.logger.info("Number Of Column" + str(cols))


        # Printing the data of the table
        for r in range(1, rows):
            for p in range(1, cols):
                # obtaining the text from each column of the table
                value = self.driver.find_element(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                     r) + "]/td[" + str(p) + "]").text

                log.logger.info("Detail Of User" + str(value))

