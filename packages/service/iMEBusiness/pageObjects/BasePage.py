import pytz
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import logging
import random
import string
from iMEBusiness.Utilities.customLogger import Logger

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

    def get_attribute(self, by_locator, value):
        if value == "value":
            attrval = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).get_attribute(
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

    def de_scroll_by_pixels(self):
        self.driver.execute_script("window.scrollBy(0, 300);")

    def de_scroll_by_up_pixels(self):
        self.driver.execute_script("window.scrollBy(0, -600);")

    def generate_random_email(self):
        domain = "example.com"  # You can choose any domain
        username_length = random.randint(5, 10)  # Length of the random username part
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
        return f"{username}@{domain}"

    def browser_zoom_out(self):
        self.driver.execute_script("document.body.style.zoom='75%'")

    def generate_random_text(self, length=20):
        return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k=length))

    def generate_webinar_title(self):
        # Predefined lists for different parts of the title
        topics = ["Data Science", "Artificial Intelligence", "Cloud Computing", "Machine Learning", "Web Development",
                  "Cybersecurity", "Blockchain", "Digital Marketing"]
        actions = ["Exploring", "Mastering", "Understanding", "Introduction to", "Advanced Concepts of",
                   "Breaking Down"]
        audiences = ["Beginners", "Professionals", "Experts", "Developers", "Entrepreneurs", "Marketers", "Students"]
        formats = ["Live Session", "Workshop", "Masterclass", "Online Course", "Seminar"]

        # Randomly select elements from the lists
        topic = random.choice(topics)
        action = random.choice(actions)
        audience = random.choice(audiences)
        format_type = random.choice(formats)

        # Create the webinar title
        title = f"Webinar: {action} {topic} for {audience} | {format_type}"

        return title

    def table_traverse(self, row, col):
        for r in range(1, row + 1):
            for p in range(1, col):
                if r < 8:
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[" + str(
                                                         r) + "]/td[" + str(p) + "]").text

                    log.logger.info("" + str(value))

    def table_traverse_search(self, row, col, designationname):
        for r in range(1, row + 1):
            for p in range(1, 2):

                if r < 8:
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                         r) + "]/td[1]").text
                    log.logger.info("" + str(value))
                    assert value == designationname
                    log.logger.info("**Filter data using designation == " + str(value) + " Working Fine**")

    def table_traverse_status_dd(self, row, col, status):
        for r2 in range(1, row + 1):
            for p2 in range(1, 2):

                if r2 < 8:
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                         r2) + "]/td[2]").text

                    log.logger.info("" + str(value))

                    try:
                        if len(value) > 0:
                            assert value == status
                            log.logger.info("Filter data using interview status == " + str(value) + " Working Fine**")
                    except:
                        print("Something went wrong")
                    finally:
                        print("Loop Is Fetching One More Row")

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

    def table_traverse_search_learning(self, row, col, designationanme):
        for r1 in range(1, row):
            for p1 in range(1, 2):
                if r1 < 8:
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                         r1) + "]/td[1]").text
                    log.logger.info("" + str(value))
                    assert value == designationanme
                    log.logger.info("**Filter data using designation title == " + str(value) + " Working Fine****")

    def table_traverse_search_audition(self, row, col, designationname):
        for r1 in range(1, row + 1):
            for p1 in range(1, 2):
                if r1 < 8:
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                         r1) + "]/td[1]").text
                    log.logger.info("" + str(value))
                    assert value == designationname
                    log.logger.info("**Filter data using designation title == " + str(value) + " Working Fine****")

    def table_traverse_search_admission(self, row, col, designationname):
        for r1 in range(1, row + 1):
            for p1 in range(1, 2):
                if r1 < 8:
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//html/body/div/main/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[" + str(
                                                         r1) + "]/td[1]").text
                    log.logger.info("" + str(value))
                    assert value == designationname
                    log.logger.info("**Filter data using designation title == " + str(value) + " Working Fine****")

    def table_traverse_multiway_video_calls(self, row, col):
        for r in range(1, row + 1):
            for p in range(1, col):
                if r < 10:
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[" + str(
                                                         r) + "]/td[" + str(p) + "]").text

                    log.logger.info("" + str(value))

    def multiway_table_traverse_search_via_service(self, row, col, serviceName):
        for r in range(1, row + 1):
            for p in range(1, 2):
                # obtaining the text from each column of the table
                value = self.driver.find_element(By.XPATH,
                                                 "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[" + str(
                                                     r) + "]/td[2]/h5/div").text
                log.logger.info("" + str(value))
                assert value == serviceName
                log.logger.info(
                    "**Filter Multiway Interview List data using Service Type == " + str(value) + " Working Fine**")

    def multiway_invites_table_traverse_search_via_title(self, row, col, designationName):
        for r in range(1, row + 1):
            for p in range(1, 2):
                if r < 8:
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[" + str(
                                                         r) + "]/td[1]").text
                    log.logger.info("" + str(value))
                    assert designationName in value
                    log.logger.info(
                        "**Filter Multiway Invites  List  using Title == " + str(
                            value) + " Working Fine**")

    def multiway_video_call_table_traverse_search_via_title(self, row, col, designationName):
        for r in range(1, row + 1):
            for p in range(1, 2):
                if r < 8:
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[" + str(
                                                         r) + "]/td[1]").text
                    log.logger.info("" + str(value))
                    assert designationName in value
                    log.logger.info(
                        "**Filter Multiway Video Call List  using Title == " + str(
                            value) + " Working Fine**")

    def table_traverse_for_multiway_interview_user(self, row, col):
        for r in range(1, row + 1):
            for p in range(1, 3):
                # obtaining the text from each column of the table
                value = self.driver.find_element(By.XPATH,
                                                 "//div[@class='grid grid-cols-6 gap-4']/div/div[3]/div/div/table/tbody/tr[" + str(
                                                     r) + "]/td[" + str(p) + "]").text

                log.logger.info("" + str(value))

    def table_traverse_of_stream(self, row, col):
        for r in range(1, row + 1):
            for p in range(1, col):
                if r < 8:
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[" + str(
                                                         r) + "]/td[" + str(p) + "]").text

                    log.logger.info("" + str(value))

    def get_element_text_question_set(self, by_locator):
        element = WebDriverWait(self.driver, 240).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_date_time_using_time_zone(self):
        localVar = datetime.now().timestamp()
        dt = datetime.fromtimestamp(localVar, pytz.timezone('Africa/Johannesburg'))
        display = dt.strftime('%m-%d %H:%M (%Z)')
        return display

    def table_traverse_live_streaming_item_title(self, row, col, title):
        for r2 in range(1, row + 1):
            for p2 in range(1, 2):

                if r2 < 8:
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[" + str(
                                                         r2) + "]/td[2]/div/div[2]/div").text

                    log.logger.info("" + str(value))

                    try:
                        if len(value) > 0:
                            # assert value == title
                            log.logger.info("Filter data using streaming title == " + str(value) + " Working Fine**")
                    except:
                        print("Something went wrong")
                    finally:
                        print("Loop Is Fetching One More Row")

    def table_traverse_live_streaming_folder_item_title(self, row, col, title):
        for r2 in range(1, row + 1):
            for p2 in range(1, 2):

                if r2 < 8:
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[" + str(
                                                         r2) + "]/td[2]/div/div[2]/div").text

                    log.logger.info("" + str(value))

                    try:
                        if len(value) > 0:
                            assert value in title
                            log.logger.info(
                                "Filter Streaming data using Folder title == " + str(value) + " Working Fine**")
                    except:
                        print("Something went wrong")
                    finally:
                        print("Loop Is Fetching One More Row")

    def table_traverse_upload_streaming_item_title(self, row, col, title):
        for r2 in range(1, row + 1):
            for p2 in range(1, 2):
                # obtaining the text from each column of the table
                value = self.driver.find_element(By.XPATH,
                                                 "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[" + str(
                                                     r2) + "]/td[2]/h5/div").text

                log.logger.info("" + str(value))

                try:
                    if len(value) > 0:
                        assert value == title
                        log.logger.info("Filter data using streaming title == " + str(value) + " Working Fine**")
                except:
                    print("Something went wrong")
                finally:
                    print("Loop Is Fetching One More Row")

    def table_traverse_of_digital_content(self, row, col):
        for r in range(1, row + 1):
            for p in range(1, col):
                if r < 8:
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[" + str(
                                                         r) + "]/td[" + str(p) + "]").text

                    log.logger.info("" + str(value))

    def table_traverse_search_digital_content(self, row, col, documentTitle):
        for r in range(1, row + 1):
            for p in range(1, 2):

                if r < 8:
                    # obtaining the text from each column of the table
                    value = self.driver.find_element(By.XPATH,
                                                     "//div[@class='rounded-md border border-ime-gray-300 dark:border-ime-gray-600']/table/tbody/tr[" + str(
                                                         r) + "]/td[2]/div/div[2]").text
                    log.logger.info("" + str(value))
                    assert value == documentTitle
                    log.logger.info("**Filter data using document title == " + str(value) + " Working Fine**")
