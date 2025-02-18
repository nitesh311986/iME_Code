import time
import logging
from selenium.webdriver.common.by import By
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class LoginPage(BasePage):
    businessBlock = (By.XPATH,
                     "//button[@buttontype='business']/div/div[2]/h4")
    userEmail = (By.CSS_SELECTOR, "input[name='email']")
    userPassword = (By.CSS_SELECTOR, "input[name='password']")
    SubmitButton = (By.CSS_SELECTOR,
                    "button[type='submit']")
    dashBoradMessage = (By.XPATH,
                        "//div[@class='py-[15px] pl-[32px] flex border-b items-center bg-ime-gray-50 "
                        "dark:bg-ime-gray-900  border-ime-gray-200 dark:border-ime-gray-900 ']/h2")

    profileText = (By.XPATH,"//div[@class='ps-sidebar-container css-ztz6kr']/div/div[2]/nav/ul/li[1]/a/span[2]")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def get_launch_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        log.logger.info("****==Log In Test Case for Business Starts Here==***")
        log.logger.info("Business clicks on business block")
        self.de_click(self.businessBlock)
        time.sleep(1)
        log.logger.info("Business enters emailID == " + username)
        self.do_send_key(self.userEmail, username)
        log.logger.info("Business enters Password == " + password)
        self.do_send_key(self.userPassword, password)
        log.logger.info("Business clicks on submit button")
        self.de_click(self.SubmitButton)
        time.sleep(9)
        log.logger.info("Business successfully logged in into the system")
        return self.get_element_text(self.profileText)


