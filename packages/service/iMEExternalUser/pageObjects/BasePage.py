from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEExternalUser.Utilities.customLogger import Logger
import logging

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

    def de_scroll_into_view(self, by_locator):
        # Use JavaScript to scroll to the element
        self.driver.execute_script("arguments[0].scrollIntoView();", by_locator)
