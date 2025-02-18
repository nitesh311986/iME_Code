import os
import logging
import time
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iMEApplicant.pageObjects.BasePage import BasePage
from iMEApplicant.utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Create_ContentLibrary(BasePage):
    contentLibrary = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[3]/a")
    uploadButton = (By.XPATH, "//div[@class='flex space-x-4 ml-auto mt-4']/button[1]")
    fileName = (By.CSS_SELECTOR, "input[name='fileName']")
    saveButton = (
        By.XPATH,
        "//div[@class='flex flex-col w-full text-ime-gray-500 dark:text-ime-gray-400 text-[14px]']/form/button")

    inputCheckBox = (By.XPATH,
                     "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr[1]/td[1]/div/div/div/input")
    deleteButton = (By.XPATH, "//div[@class='flex space-x-4 ml-auto mt-4']/button[2]")
    popUpDeleteButton = (By.XPATH,
                         "//div[@class='flex flex-col w-full text-ime-gray-500 dark:text-ime-gray-400 text-[14px]']/div/div[2]/button[1]")

    def __init__(self, driver, environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_content_Library(self):
        time.sleep(1)
        self.de_click(self.contentLibrary)
        time.sleep(4)

    def create_content_library(self):
        log.logger.info("****==Create Content Library Test Case Starts Here==***")
        dataAvail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody"))
        )
        value = dataAvail.text
        # log.logger.info("" + value)
        if len(value) > 0:
            totalItem = len(self.driver.find_elements(By.XPATH,
                                                      "//div[@class='border-[1px] border-ime-blue-gray-300 dark:border-ime-blue-gray-600 mt-[10px] rounded-md mb-20']/table/tbody/tr"))
            if totalItem == 10:
                for j in range(2):
                    time.sleep(1.5)
                    self.de_click(self.inputCheckBox)
                    time.sleep(2)
                    self.de_click(self.deleteButton)
                    time.sleep(2)
                    self.de_click(self.popUpDeleteButton)
                    time.sleep(3)
                    log.logger.info("Item Has been deleted successfully form content library")
                time.sleep(2)
                self.create_item()
            else:
                self.create_item()
                # for i in range(2):
                #     self.de_click(self.uploadButton)
                #     file_input = self.driver.find_element(By.XPATH,
                #                                           "//div[@class='cursor-pointer w-full h-20 border-dashed border-gray-300 dark:border-gray-500 border  rounded-md flex items-center justify-center text-ime-blue-gray-500']/input")
                #
                #     # Replace with the path to the video file you want to upload
                #     base_dir = os.path.dirname(__file__)
                #     relative_file_path = os.path.join(base_dir, '../Document/07.png')
                #     absolute_file_path = os.path.abspath(relative_file_path)
                #
                #     # Check if the file input element accepts the desired file types
                #     accept_attribute = file_input.get_attribute('accept')
                #
                #     # Define accepted types
                #     accepted_types = [
                #         '.mp4', 'video/*', 'image/jpeg', '.jpeg', '.jpg', 'image/png', '.png',
                #         'application/pdf', '.pdf', 'audio/mpeg', '.mp3', 'audio/wav', '.wav',
                #         'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                #         '.docx', 'application/vnd.ms-powerpoint', '.ppt',
                #         'application/vnd.openxmlformats-officedocument.presentationml.presentation', '.pptx',
                #         'application/vnd.ms-excel', '.xls',
                #         'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', '.xlsx'
                #     ]
                #
                #     # Extract the file extension and MIME type from the file path
                #     file_extension = os.path.splitext(absolute_file_path)[1].lower()
                #     mime_type = None
                #
                #     # Determine the MIME type for common file extensions (you may need to adjust this for your use case)
                #     mime_type_mapping = {
                #         '.mp4': 'video/mp4',
                #         '.jpeg': 'image/jpeg',
                #         '.jpg': 'image/jpeg',
                #         '.png': 'image/png',
                #         '.pdf': 'application/pdf',
                #         '.mp3': 'audio/mpeg',
                #         '.wav': 'audio/wav',
                #         '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                #         '.ppt': 'application/vnd.ms-powerpoint',
                #         '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                #         '.xls': 'application/vnd.ms-excel',
                #         '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                #
                #     }
                #
                #     if file_extension in mime_type_mapping:
                #         mime_type = mime_type_mapping[file_extension]
                #
                #     # Function to check if file type is accepted
                #     def is_accepted(file_extension, mime_type, accepted_types):
                #         for accepted_type in accepted_types:
                #             if file_extension == accepted_type or mime_type == accepted_type:
                #                 return True
                #             if '*' in accepted_type and file_extension in accepted_type:
                #                 return True
                #             if '*' in accepted_type and mime_type and mime_type.startswith(accepted_type.split('/')[0]):
                #                 return True
                #
                #         return False
                #
                #     # Check if the file type is accepted
                #     if is_accepted(file_extension, mime_type, accepted_types):
                #         # Send the file path to the file input element
                #         file_input.send_keys(absolute_file_path)
                #         log.logger.info("User Has Uploaded Video For Stream")
                #     else:
                #         log.logger.info("File input does not accept the file type or format: " + accept_attribute)
                #
                #     time.sleep(2)
                #     # dateTime = self.get_date_time_using_time_zone()
                #     random_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
                #     self.do_send_key(self.fileName, random_name)
                #     time.sleep(1)
                #     self.de_click(self.saveButton)
                #     time.sleep(10)


    def create_item(self):
        self.de_click(self.uploadButton)
        file_input = self.driver.find_element(By.XPATH,
                                              "//div[@class='cursor-pointer w-full h-20 border-dashed border-gray-300 dark:border-gray-500 border  rounded-md flex items-center justify-center text-ime-blue-gray-500']/input")

        # Replace with the path to the video file you want to upload
        base_dir = os.path.dirname(__file__)
        relative_file_path = os.path.join(base_dir, '../Document/07.png')
        absolute_file_path = os.path.abspath(relative_file_path)

        # Check if the file input element accepts the desired file types
        accept_attribute = file_input.get_attribute('accept')

        # Define accepted types
        accepted_types = [
            '.mp4', 'video/*', 'image/jpeg', '.jpeg', '.jpg', 'image/png', '.png',
            'application/pdf', '.pdf', 'audio/mpeg', '.mp3', 'audio/wav', '.wav',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            '.docx', 'application/vnd.ms-powerpoint', '.ppt',
            'application/vnd.openxmlformats-officedocument.presentationml.presentation', '.pptx',
            'application/vnd.ms-excel', '.xls',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', '.xlsx'
        ]

        # Extract the file extension and MIME type from the file path
        file_extension = os.path.splitext(absolute_file_path)[1].lower()
        mime_type = None

        # Determine the MIME type for common file extensions (you may need to adjust this for your use case)
        mime_type_mapping = {
            '.mp4': 'video/mp4',
            '.jpeg': 'image/jpeg',
            '.jpg': 'image/jpeg',
            '.png': 'image/png',
            '.pdf': 'application/pdf',
            '.mp3': 'audio/mpeg',
            '.wav': 'audio/wav',
            '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            '.ppt': 'application/vnd.ms-powerpoint',
            '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
            '.xls': 'application/vnd.ms-excel',
            '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

        }

        if file_extension in mime_type_mapping:
            mime_type = mime_type_mapping[file_extension]

        # Function to check if file type is accepted
        def is_accepted(file_extension, mime_type, accepted_types):
            for accepted_type in accepted_types:
                if file_extension == accepted_type or mime_type == accepted_type:
                    return True
                if '*' in accepted_type and file_extension in accepted_type:
                    return True
                if '*' in accepted_type and mime_type and mime_type.startswith(accepted_type.split('/')[0]):
                    return True

            return False

        # Check if the file type is accepted
        if is_accepted(file_extension, mime_type, accepted_types):
            # Send the file path to the file input element
            file_input.send_keys(absolute_file_path)
            log.logger.info("User Has Uploaded Video For Stream")
        else:
            log.logger.info("File input does not accept the file type or format: " + accept_attribute)

        time.sleep(2)
        # dateTime = self.get_date_time_using_time_zone()
        random_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
        self.do_send_key(self.fileName, random_name)
        time.sleep(1)
        self.de_click(self.saveButton)
        time.sleep(10)