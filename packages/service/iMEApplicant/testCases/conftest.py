import os
import allure
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from iMEApplicant.Config.config import TestData
from iMEApplicant.utilities.customLogger import Logger
import logging

log = Logger(__name__, logging.INFO)

@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request, environment):
    global driver
    if request.param == "chrome":
        # Set up FirefoxOptions with desired capabilities
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')  # Optional: For Linux systems
        chrome_options.add_argument('--window-size=1920x1080')
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1
        })


        try:
            # Attempt to initialize Chrome WebDriver normally
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

            # If the above initialization is successful, proceed with browser interaction
            request.cls.driver = driver
            driver.maximize_window()  # Optional: Maximize the browser window
            if environment == "UTA":
                driver.get(TestData.UTA_URL)
            else:
                driver.get(TestData.BASE_URL)

        except OSError as e:
            print(f"First attempt failed with OSError: {e}")

            # Secondary approach
            try:
                # Manually specify the path to chromedriver.exe
                chromedriver_path = ChromeDriverManager().install()
                print(f"ChromeDriver installed at: {chromedriver_path}")

                # Ensure the path is pointing to the chromedriver executable
                if not chromedriver_path.endswith("chromedriver.exe"):
                    chromedriver_path = os.path.join(os.path.dirname(chromedriver_path), "chromedriver.exe")
                    print(f"Updated ChromeDriver path: {chromedriver_path}")

                # Initialize WebDriver with the correct path
                driver = webdriver.Chrome(service=ChromeService(chromedriver_path), options=chrome_options)

                # Interact with the browser
                request.cls.driver = driver
                driver.maximize_window()  # Optional: Maximize the browser window
                if environment == "UTA":
                    driver.get(TestData.UTA_URL)
                else:
                    driver.get(TestData.BASE_URL)

            except Exception as e:
                print(f"Secondary attempt failed: {e}")

    yield driver
    driver.quit()




def pytest_addoption(parser):
    # Check if --env is already added
    existing_options = [option.dest for option in parser._anonymous.options]
    if 'env' not in existing_options:
        parser.addoption("--env", action="store", default="stage", help="Environment to run tests against: stage or UTA")


@pytest.fixture(scope="class")
def environment(request):
    return request.config.getoption("--env")



# allure report
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def failed_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        # Capture screenshot with a unique name (e.g., test name + timestamp)
        screenshot_filename = f"{item.nodeid.replace('::', '_').replace('/', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        screenshot_path = f"reports/screenshots/{screenshot_filename}"
        allure.attach(driver.get_screenshot_as_png(), name="FailedTest", attachment_type=allure.attachment_type.PNG)
        driver.save_screenshot(screenshot_path)
        log.logger.error(f"Test failed: {item.nodeid}. Screenshot saved at {screenshot_path}")


@pytest.fixture(scope="function")
def wait_for_page_load(request):
    def _wait_for_page_loaded():
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )

    return _wait_for_page_loaded


def pytest_collection_modifyitems(config, items):
    order = [
        "testCases/test_LoginPage.py",
        "testCases/test_Profile.py",
        "testCases/test_iME_Queue_Page.py",
        "testCases/test_Recruitment_page.py",
        "testCases/test_Awards_Page.py",
        "testCases/test_Marketing_Page.py",
        "testCases/test_Learning_Page.py",
        "testCases/test_Auditions_Page.py",
        "testCases/test_Admission_Page.py",
        "testCases/test_iME_Queue_Multiway.py",
        "testCases/test_Multiway_Details.py",
        "testCases/test_create_content_library.py",
        "testCases/test_Content_Page.py",
        "testCases/test_iMe_Hub_View.py",
    ]

    def get_order(item):
        # Extract the file name from the item location
        file_name = item.location[0].split('/')[-1]
        # Provide a high order number if the file is not in the order list
        return order.index(file_name) if file_name in order else len(order)

    items.sort(key=get_order)



# log = Logger(__name__, logging.INFO)
#
#
# @pytest.fixture(params=["chrome"], scope="class")
# def init_driver(request, environment):
#     global driver
#     if request.param == "chrome":
#         # Set up FirefoxOptions with desired capabilities
#         chrome_options = ChromeOptions()
#         chrome_options.add_argument('--headless')
#         chrome_options.add_argument('--no-sandbox')
#         chrome_options.add_argument('--disable-dev-shm-usage')
#         chrome_options.add_argument('--disable-gpu')  # Optional: For Linux systems
#         chrome_options.add_argument('--window-size=1920x1080')
#         chrome_options.add_experimental_option("prefs", {
#             "profile.default_content_setting_values.media_stream_mic": 1,
#             "profile.default_content_setting_values.media_stream_camera": 1
#         })
#
#         try:
#             # Attempt to initialize Chrome WebDriver normally
#             driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
#                                       options=chrome_options)
#
#             # If the above initialization is successful, proceed with browser interaction
#             request.cls.driver = driver
#             driver.maximize_window()  # Optional: Maximize the browser window
#             if environment == "UTA":
#                 driver.get(TestData.UTA_URL)
#             else:
#                 driver.get(TestData.BASE_URL)
#
#         except OSError as e:
#             print(f"First attempt failed with OSError: {e}")
#
#             # Secondary approach
#             try:
#                 # Manually specify the path to chromedriver.exe
#                 chromedriver_path = ChromeDriverManager().install()
#                 print(f"ChromeDriver installed at: {chromedriver_path}")
#
#                 # Ensure the path is pointing to the chromedriver executable
#                 if not chromedriver_path.endswith("chromedriver.exe"):
#                     chromedriver_path = os.path.join(os.path.dirname(chromedriver_path), "chromedriver.exe")
#                     print(f"Updated ChromeDriver path: {chromedriver_path}")
#
#                 # Initialize WebDriver with the correct path
#                 driver = webdriver.Chrome(service=ChromeService(chromedriver_path), options=chrome_options)
#
#                 # Interact with the browser
#                 request.cls.driver = driver
#                 driver.maximize_window()  # Optional: Maximize the browser window
#                 if environment == "UTA":
#                     driver.get(TestData.UTA_URL)
#                 else:
#                     driver.get(TestData.BASE_URL)
#
#             except Exception as e:
#                 print(f"Secondary attempt failed: {e}")
#
#     yield driver
#     driver.quit()
#
#
# def pytest_addoption(parser):
#     parser.addoption("--env", action="store", default="stage", help="Environment to run tests: stage or UTA")
#     parser.addoption("--test_classes", action="store", default=None,
#                      help="Comma-separated list of test classes to run (e.g., test_LoginPage,test_Notification_Details)")
#
#
# @pytest.fixture(scope="class")
# def environment(request):
#     return request.config.getoption("--env")
#
#
# @pytest.fixture(scope="class")
# def selected_test_classes(request):
#     """
#     Fixture to get the test classes specified in the command line option.
#     If no classes are specified, all tests run.
#     """
#     test_classes = request.config.getoption("--test_classes")
#     if test_classes:
#         return test_classes.split(",")
#     return None
#
#
# def pytest_collection_modifyitems(config, items):
#     """
#     Modify the order of test collection and handle the selection of specific test classes.
#     """
#     # Retrieve test class selection and markers from the command line
#     selected_classes = config.getoption("--test_classes")
#     selected_classes_list = selected_classes.split(",") if selected_classes else None
#
#     # Test order defined in confset.py
#
#     default_order = [
#         "testCases/test_LoginPage.py",
#         "testCases/test_Profile.py",
#         "testCases/test_iME_Queue_Page.py",
#         "testCases/test_Recruitment_page.py",
#         "testCases/test_Awards_Page.py",
#         "testCases/test_Marketing_Page.py",
#         "testCases/test_Learning_Page.py",
#         "testCases/test_Auditions_Page.py",
#         "testCases/test_Admission_Page.py",
#         "testCases/test_iME_Queue_Multiway.py",
#         "testCases/test_Multiway_Details.py",
#         "testCases/test_create_content_library.py",
#         "testCases/test_Content_Page.py",
#         "testCases/test_iMe_Hub_View.py",
#     ]
#
#     def get_order(item):
#         file_name = item.location[0].split('/')[-1]
#         return default_order.index(file_name) if file_name in default_order else len(default_order)
#
#     # Filter tests if specific classes are provided
#     if selected_classes_list:
#         items[:] = [item for item in items if item.cls and item.cls.__name__ in selected_classes_list]
#
#     # Sort remaining tests by the predefined order
#     items.sort(key=get_order)
#
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
#
#
# @pytest.fixture()
# def failed_on_failure(request):
#     yield
#     item = request.node
#     if item.rep_call.failed:
#         screenshot_filename = f"{item.nodeid.replace('::', '_').replace('/', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
#         screenshot_path = f"reports/screenshots/{screenshot_filename}"
#         allure.attach(driver.get_screenshot_as_png(), name="FailedTest", attachment_type=allure.attachment_type.PNG)
#         driver.save_screenshot(screenshot_path)
#         log.logger.error(f"Test failed: {item.nodeid}. Screenshot saved at {screenshot_path}")
#
#
# @pytest.fixture(scope="function")
# def wait_for_page_load(request):
#     def _wait_for_page_loaded():
#         WebDriverWait(driver, 30).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
#         )
#
#     return _wait_for_page_loaded


