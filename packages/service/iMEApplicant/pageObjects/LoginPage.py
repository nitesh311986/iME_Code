from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
from iMEApplicant.pageObjects.BasePage import BasePage
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class LoginPage(BasePage):
    applicantBlock = (By.XPATH,
                      "//button[@class='flex flex-col border border-slate-300 dark:border-slate-600 w-full h-fit "
                      "lg:h-[88px] rounded-lg p-[1.5px] lg:w-[470px] mb-3']/div/div[2]/h4")
    userEmail = (By.CSS_SELECTOR, "input[name='email']")
    userPassword = (By.CSS_SELECTOR, "input[name='password']")
    SubmitButton = (By.CSS_SELECTOR,
                    "button[class='mt-8 mx-auto w-full md:max-w-[464px] lg:w-[566px] rounded-[4px] transition-colors "
                    "h-[40px] px-6 text-sm bg-ime-accent hover:bg-blue-700 text-white']")
    dashBoradMessage = (By.XPATH,
                        "//div[@class='py-[15px] pl-[32px] flex border-b items-center bg-ime-blue-gray-50 "
                        "dark:bg-ime-blue-gray-800  border-ime-blue-gray-200 dark:border-ime-blue-gray-700 ']/h2")

    profileText = (By.XPATH, "//div[@class='ps-sidebar-container css-1sn29ar']/div/div[2]/nav/ul/li[1]/a/span[2]")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)
        # self.driver.get(TestData.BASE_URL)
        # self.driver.get(ReadConfig.getURl())

    def get_lauch_page_title(self, title):
        return self.get_title(title)

    # def select_applicant(self):
    #     self.de_click(self.applicantBlock)

    def do_login(self, username, password):
        self.de_click(self.applicantBlock)
        log.logger.info("User clicks on applicant block")
        self.do_send_key(self.userEmail, username)
        self.do_send_key(self.userPassword, password)
        self.de_click(self.SubmitButton)
        try:
            # Attempt to get the element's text
            text = self.get_element_text(self.profileText)
            return text
        except NoSuchElementException:
            # Handle the specific exception for element not found
            print("Profile text element not found.")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"An unexpected error occurred: {e}")
            return None
