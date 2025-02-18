import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from iMEWebsite.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class BasePage:

    def __int__(self, driver):
        self.driver = driver

    def de_click(self, by_locator):
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).click()
        except TimeoutException as e:
            log.logger.error(f"Timeout: Unable to click element located by {by_locator}. Retrying...")
            # Retry after waiting for some time or refresh page
            self.driver.refresh()  # Example of recovery action (could be other actions)
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).click()
        except NoSuchElementException as e:
            log.logger.error(f"Element not found: Unable to find element located by {by_locator}.")
            raise e

    def do_send_key(self, by_locator, text):
        # WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).clear()
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except TimeoutException as e:
            log.logger.error(f"Timeout: Unable to send text in to element located by {by_locator}. Retrying...")
            # Retry after waiting for some time or refresh page
            self.driver.refresh()  # Example of recovery action (could be other actions)
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except NoSuchElementException as e:
            log.logger.error(f"Element not found: Unable to find element located by {by_locator}.")
            raise e

    def get_element_text(self, by_locator):
        # element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        try:
            element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        except TimeoutException as e:
            log.logger.error(f"Timeout: Unable to find element located by {by_locator}. Retrying...")
            # Retry after waiting for some time or refresh page
            self.driver.refresh()  # Example of recovery action (could be other actions)
            element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        except NoSuchElementException as e:
            log.logger.error(f"Element not found: Unable to find element located by {by_locator}.")
            raise e
        return element.text

    def is_enable(self, by_locator):
        # element = WebDriverWait(self.driver, 60).until((EC.visibility_of_element_located(by_locator)))
        try:
            element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        except TimeoutException as e:
            log.logger.error(f"Timeout: Unable to find element located by {by_locator}. Retrying...")
            # Retry after waiting for some time or refresh page
            self.driver.refresh()  # Example of recovery action (could be other actions)
            element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        except NoSuchElementException as e:
            log.logger.error(f"Element not found: Unable to find element located by {by_locator}.")
            raise e
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 60).until(EC.title_is(title))
        try:
            WebDriverWait(self.driver, 60).until(EC.title_is(title))
        except TimeoutException as e:
            log.logger.error(f"Timeout: No Title Found Retrying...")
            # Retry after waiting for some time or refresh page
            self.driver.refresh()  # Example of recovery action (could be other actions)
            WebDriverWait(self.driver, 60).until(EC.title_is(title))
        except NoSuchElementException as e:
            log.logger.error(f"Title Not Fount")
            raise e
        return self.driver.title

    def do_clear(self, by_locator):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).clear()
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).clear()
        except TimeoutException as e:
            log.logger.error(f"Timeout: Unable to find element located by {by_locator}. Retrying...")
            # Retry after waiting for some time or refresh page
            self.driver.refresh()  # Example of recovery action (could be other actions)
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).clear()
        except NoSuchElementException as e:
            log.logger.error(f"Element not found: Unable to find element located by {by_locator}.")
            raise e

    def get_attribute(self, by_locator, value):
        if value == "value":
            attrval = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).get_attribute(
                "value")
            return attrval

    def de_action_method(self, by_locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(by_locator)
        actions.click(by_locator)
        actions.perform()

    def de_scroll_into_view(self, by_locator):
        # Use JavaScript to scroll to the element
        self.driver.execute_script("arguments[0].scrollIntoView();", by_locator)

    def table_traverse(self, row, col):
        for r in range(1, row + 1):
            for p in range(1, col):
                # obtaining the text from each column of the table
                value = self.driver.find_element(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                     r) + "]/td[" + str(p) + "]").text

                log.logger.info("" + str(value))

    def table_traverse_search(self, row, col):
        for r in range(1, row + 1):
            for p in range(1, 2):
                # obtaining the text from each column of the table
                value = self.driver.find_element(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                     r) + "]/td[1]").text
                log.logger.info("" + str(value))
                assert value == "Lead Qa"
                log.logger.info("**Filter Options Working Fine**")

    def table_traverse_status_dd(self, row, col):
        for r2 in range(1, row + 1):
            for p2 in range(1, 2):
                # obtaining the text from each column of the table
                value = self.driver.find_element(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                     r2) + "]/td[2]").text

                log.logger.info("" + str(value))
                assert value == "Active"
                log.logger.info("**Filter Options Working Fine**")

    def table_traverse_search_award(self, row, col):
        for r1 in range(1, row + 1):
            for p1 in range(1, 2):
                # obtaining the text from each column of the table
                value = self.driver.find_element(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                     r1) + "]/td[1]").text
                log.logger.info("" + str(value))
                assert value == "Admin"
                log.logger.info("**Filter Options Working Fine**")

    def table_traverse_search_marketing(self, row, col):
        for r1 in range(1, row + 1):
            for p1 in range(1, 2):
                # obtaining the text from each column of the table
                value = self.driver.find_element(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                     r1) + "]/td[1]").text
                log.logger.info("" + str(value))
                assert value == "podcast intern"
                log.logger.info("**Filter Options Working Fine**")

    def table_traverse_search_learning(self, row, col):
        for r1 in range(1, row + 1):
            for p1 in range(1, 2):
                # obtaining the text from each column of the table
                value = self.driver.find_element(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                     r1) + "]/td[1]").text
                log.logger.info("" + str(value))
                assert value == "Counselor"
                log.logger.info("**Filter Options Working Fine**")

    def table_traverse_search_audition(self, row, col):
        for r1 in range(1, row + 1):
            for p1 in range(1, 2):
                # obtaining the text from each column of the table
                value = self.driver.find_element(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                     r1) + "]/td[1]").text
                log.logger.info("" + str(value))
                assert value == "podcast intern"
                log.logger.info("**Filter Options Working Fine**")

    def table_traverse_search_admission(self, row, col):
        for r1 in range(1, row + 1):
            for p1 in range(1, 2):
                # obtaining the text from each column of the table
                value = self.driver.find_element(By.XPATH,
                                                 "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                     r1) + "]/td[1]").text
                log.logger.info("" + str(value))
                assert value == "Asst.Professor"
                log.logger.info("**Filter Options Working Fine**")

    def get_element_text_question_set(self, by_locator):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def moveToElement(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)
