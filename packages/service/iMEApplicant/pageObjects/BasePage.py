from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from iMEApplicant.utilities.customLogger import Logger

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

    def do_clear_using_java_script(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(by_locator)
        )

        # Use JavaScript to clear the input value
        self.driver.execute_script("arguments[0].value = '';", element)

    def de_scroll_into_view(self, by_locator):
        # Use JavaScript to scroll to the element
        self.driver.execute_script("arguments[0].scrollIntoView();", by_locator)

    def table_traverse(self, row, col):
        for r in range(1, row):
            for p in range(1, col):
                # obtaining the text from each column of the table

                if r <= 10:
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                         r) + "]/td[" + str(p) + "]").text

                    log.logger.info("" + str(value))

                else:
                    break

    def filter_via_designation(self, row, col, designation):

        for r2 in range(1, row):
            for p2 in range(1, 2):
                # obtaining the text from each column of the table
                if r2 <= 8:
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                         r2) + "]/td[1]/div/div[1]/div[1]").text

                    log.logger.info("" + str(value))
                    assert designation in value
                    log.logger.info(
                        "<< !! Filter multiway interview list using Search box via designation ===  "
                        "!!>>" + str(value) + " === executed Successfully")
                else:
                    break

    def filter_via_company_name(self, row, col, cname):

        for r2 in range(1, row):
            for p2 in range(1, 2):
                # obtaining the text from each column of the table
                if r2 < 10:
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                         r2) + "]/td[2]/div").text

                    log.logger.info("" + str(value))
                    assert cname in value
                    log.logger.info(
                        "<< !! Filter multiway interview list using Search box via company name ===  "
                        "!!>>" + str(value) + " === executed Successfully")
                else:
                    break

    def filter_via_designation_multiway(self, row, col, designation):

        for r2 in range(1, row):
            for p2 in range(1, 2):
                # obtaining the text from each column of the table

                if r2 <= 10:
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                         r2) + "]/td[1]/div/div[1]").text

                    log.logger.info("" + str(value))
                    assert designation in value
                    log.logger.info(
                        "<< !! Filter multiway interview list using Search box via designation ===  "
                        "!!>>" + str(value) + " === executed Successfully")

                else:
                    break

    def filter_via_interview_status(self, row, col, status):

        for r2 in range(1, row):
            for p2 in range(1, 2):
                # obtaining the text from each column of the table
                if r2 <= 10:
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md overflow-hidden']/table/tbody/tr[" + str(
                                                         r2) + "]/td[5]/div/div[1]").text

                    log.logger.info("" + str(value))
                    assert status in value
                    log.logger.info(
                        "<< !! Filter multiway interview list using Search box via interview status ===  "
                        "!!>>" + str(value) + " === executed Successfully")

                else:
                    break
