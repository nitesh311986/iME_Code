import time
import logging
import pytest
from selenium.webdriver.common.by import By
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.pageObjects.BasePage import BasePage

log = Logger(__name__, logging.INFO)


class Faq(BasePage):
    faqIcon = (By.XPATH, "//div[@class='framer-1id1vs8']/div[1]/div[5]/p/a")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    @pytest.mark.smoke
    def click_on_faq(self):
        time.sleep(2)
        self.de_click(self.faqIcon)
        time.sleep(3)
        totalFAQ = len(self.driver.find_elements(By.XPATH,
                                                 "//div[@class='framer-libcqa']/div/div/div/div/div/div/div/div[2]/h5"))
        FAQ = []
        FAQ = self.driver.find_elements(By.XPATH,
                                        "//div[@class='framer-libcqa']/div/div/div/div/div/div/div/div[2]/h5")

        for i in range(totalFAQ):
            if i == 4:
                self.driver.execute_script("window.scrollTo(0,300)")
                FAQ[i].click()
                time.sleep(0.5)
                FAQ[i].click()
                time.sleep(0.5)
            elif i == 9:
                self.driver.execute_script("window.scrollTo(0,500)")
                FAQ[i].click()
                time.sleep(0.5)
                FAQ[i].click()
                time.sleep(0.5)
            elif i == 13:
                self.driver.execute_script("window.scrollTo(0,700)")
                FAQ[i].click()
                time.sleep(0.5)
                FAQ[i].click()
                time.sleep(0.5)
            elif i == 16:
                self.driver.execute_script("window.scrollTo(0,900)")
                FAQ[i].click()
                time.sleep(0.5)
                FAQ[i].click()
                time.sleep(0.5)
            elif i == 19:
                self.driver.execute_script("window.scrollTo(0,1100)")
                FAQ[i].click()
                time.sleep(0.5)
                FAQ[i].click()
                time.sleep(0.5)
            else:
                FAQ[i].click()
                time.sleep(0.5)
                FAQ[i].click()
                time.sleep(0.5)
