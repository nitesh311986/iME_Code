import time
import logging

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from iMEExternalUser.Utilities.customLogger import Logger
from iMEExternalUser.pageObjects.BasePage import BasePage


log = Logger(__name__, logging.INFO)


class LoginPage(BasePage):
    applicantBlock = (By.XPATH,
                      "//button[@class='flex flex-col border border-slate-300 dark:border-slate-600 w-full h-fit lg:h-[88px] rounded-lg p-[1.5px] lg:w-[470px]']/div/div[2]/h4"
                      )
    userEmail = (By.CSS_SELECTOR, "input[name='email']")
    userPassword = (By.CSS_SELECTOR, "input[name='password']")
    SubmitButton = (By.CSS_SELECTOR,
                    "button[class='mt-8 mx-auto w-full md:max-w-[464px] lg:w-[566px] rounded-[4px] transition-colors "
                    "h-[40px] px-6 text-sm bg-ime-accent hover:bg-blue-700 text-white']")
    dashBoardMessage = (By.XPATH,
                        "//div[@class='py-[15px] pl-[32px] flex border-b items-center bg-ime-gray-50 dark:bg-ime-gray-900  border-ime-gray-200 dark:border-ime-gray-900 ']/h2")
    imEQueueText = (By.XPATH,"//div[@class='ps-sidebar-container css-ztz6kr']/div/div[2]/nav/ul/li[1]/a/span[2]")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)
        # self.driver.get(TestData.BASE_URL)
        # self.driver.get(ReadConfig.getURl())

    def get_launch_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.de_click(self.applicantBlock)
        log.logger.info("User clicks on applicant block")
        self.do_send_key(self.userEmail, username)
        self.do_send_key(self.userPassword, password)
        self.de_click(self.SubmitButton)
        time.sleep(5)
        try:
            # Attempt to get the element's text
            text = self.get_element_text(self.imEQueueText)
            return text
        except NoSuchElementException:
            # Handle the specific exception for element not found
            print("Profile text element not found.")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"An unexpected error occurred: {e}")
            return None


