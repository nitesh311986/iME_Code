import time
import logging

from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from iMEExternalUser.Utilities.customLogger import Logger
from iMEExternalUser.pageObjects.BasePage import BasePage

log = Logger(__name__, logging.INFO)


class Notification_Details(BasePage):
    notificationIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[3]/a")

    loadMoreIcon = (By.XPATH, "//div[@class='cursor-pointer lg-flex max-w-screen-lg mt-10 mb-10']/div")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_notificationIcon(self):
        time.sleep(1)
        try:
            # Attempt to perform the click action
            self.de_click(self.notificationIcon)
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

    def fetch_notification_details(self):
        log.logger.info("!!! == Fetch the all details of notification  == !!!")

        dataAvail = self.driver.find_element(By.XPATH,"//div[@class='last:mb-[32px]']/div").is_displayed()
        value = str(dataAvail)
        # value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) == "True":
            element_to_scroll_to = self.driver.find_element(By.XPATH,
                                                            "//div[@class='cursor-pointer lg-flex max-w-screen-lg mt-10 mb-10']/div")

            self.de_scroll_into_view(element_to_scroll_to)
            time.sleep(0.5)
            eleSelected = self.driver.find_element(By.XPATH,
                                                   "//div[@class='cursor-pointer lg-flex max-w-screen-lg mt-10 mb-10']/div").is_displayed()
            if eleSelected is True:
                self.de_click(self.loadMoreIcon)
                time.sleep(1)
                if eleSelected is True:
                    self.de_click(self.loadMoreIcon)
                    time.sleep(1)

            totalNotification = len(self.driver.find_elements(By.XPATH,
                                                              "//div[@class='last:mb-[32px]']/div"))

            Designation = []
            Designation = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='flex items-center mb-[5px] rounded-md hover:bg-zinc-100  dark:hover:bg-zinc-800']/div[2]/h2")
            Message = []
            Message = self.driver.find_elements(By.XPATH,
                                                "//div[@class='flex items-center mb-[5px] rounded-md hover:bg-zinc-100  dark:hover:bg-zinc-800']/div[2]/div")
            Date = []
            Date = self.driver.find_elements(By.XPATH,
                                             "//div[@class='flex items-center mb-[5px] rounded-md hover:bg-zinc-100  dark:hover:bg-zinc-800']/div[2]/h6")
            log.logger.info("|Designation|          |Message|        |Date|")
            for i in range(totalNotification):
                log.logger.info("Designation Of Applicant is == " + str(Designation[i].text))
                log.logger.info("Message Related To Interview is == " + str(Message[i].text))
                log.logger.info("Date of Message is  == " + str(Date[i].text))
        else:
            log.logger.info("There's No Data Available")