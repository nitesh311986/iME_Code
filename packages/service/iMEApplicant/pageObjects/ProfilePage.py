import time
import pytest
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from iMEApplicant.pageObjects.BasePage import BasePage
from iMEApplicant.Config.config import TestData


class ProfilePage(BasePage):
    profileIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/li[2]/a")

    # personal information page
    firstName = (By.CSS_SELECTOR, "input[name='firstName']")
    contactNumber = (By.CSS_SELECTOR, "input[name='contactNumber']")
    lastName = (By.CSS_SELECTOR, "input[name='lastName']")
    preferredName = (By.CSS_SELECTOR, "input[name='preferredName']")
    dateOfBirth = (By.CSS_SELECTOR, "input[name='dateOfBirth']")
    genderDropDown = (By.XPATH,
                      "//div[@class='mt-[32px] flex flex-col md:grid sm:grid-cols-2 md:grid-cols-3 sm:gap-x-[16px]']/div[3]/button")
    optionOfGebderDropDown = (By.XPATH,
                              "//div[@class='mt-[32px] flex flex-col md:grid sm:grid-cols-2 md:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li[2]")
    physicalAddress = (
        By.CSS_SELECTOR, "input[class='w-full bg-transparent outline-none overflow-ellipsis pac-target-input']")
    region = (By.CSS_SELECTOR, "input[name='region']")
    residentialStatusDD = (By.XPATH,
                           "//div[@class='mt-[32px] flex flex-col md:grid sm:grid-cols-2 md:grid-cols-3 sm:gap-x-[16px]']/div[7]/button")
    optionOfresidentialStatusDD = (By.XPATH,
                                   "//div[@class='mt-[32px] flex flex-col md:grid sm:grid-cols-2 md:grid-cols-3 sm:gap-x-[16px]']/div[7]/ul/li[3]")
    ethinicityDD = (By.XPATH,
                    "//div[@class='mt-[32px] flex flex-col md:grid sm:grid-cols-2 md:grid-cols-3 sm:gap-x-[16px]']/div[8]/button")
    optionOfethnicityDD = (By.XPATH,
                           "//div[@class='mt-[32px] flex flex-col md:grid sm:grid-cols-2 md:grid-cols-3 sm:gap-x-[16px]']/div[8]/ul/li[2]")
    disabilitiesDDClear = (By.XPATH,
                           "//div[@class='mt-[32px] flex flex-col md:grid sm:grid-cols-2 md:grid-cols-3 sm:gap-x-[16px]']/div[9]/button/div/div/div/div")
    disabilitiesDD = (By.XPATH,
                      "//div[@class='mt-[32px] flex flex-col md:grid sm:grid-cols-2 md:grid-cols-3 sm:gap-x-[16px]']/div[9]/button/div")
    optionOfdisabilitiesDD = (By.XPATH,
                              "//div[@class='mt-[32px] flex flex-col md:grid sm:grid-cols-2 md:grid-cols-3 sm:gap-x-[16px]']/div[9]/ul/li[3]")
    clickonDiv = (By.XPATH, "//div[@class='mt-8 mx-auto w-full mb-[30px] flex flex-row-reverse']")
    saveInformationButton = (By.CSS_SELECTOR,
                             "button[class='m-[1px] w-full bg-white dark:bg-ime-dark !text-ime-dark hover:!text-white dark:!text-white rounded-[6px] hover:bg-transparent rounded-[4px] transition-colors h-[40px] px-6 text-sm bg-ime-accent hover:bg-blue-700 text-white']")

    # About Me page

    aboutMeIcon = (By.XPATH,
                   "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[2]")
    height = (By.CSS_SELECTOR, "input[name='height']")
    garmentSizeDD = (By.XPATH, "//div[@class='mb-4 relative lg:max-w-[328px]']/button")
    optionOfGarmentSizeDD = (By.XPATH, "//div[@class='mb-4 relative lg:max-w-[328px]']/ul/li[4]")
    dietaryRequirementClear = (
        By.XPATH, "//form[@class='w-full flex flex-col']/div[1]/div/div[3]/button/div/div/div/div")
    dietaryRequirementDD = (By.XPATH, "//form[@class='w-full flex flex-col']/div[1]/div/div[3]/button/div")
    optionOfDietaryRequirementDD = (By.XPATH, "//form[@class='w-full flex flex-col']/div[1]/div/div[3]/ul/li[1]")
    allergiesClear = (By.XPATH, "//form[@class='w-full flex flex-col']/div[1]/div/div[4]/button/div/div/div/div")
    allergies = (By.XPATH, "//form[@class='w-full flex flex-col']/div[1]/div/div[4]/button/div/input")
    hobbiesClear = (By.XPATH, "//form[@class='w-full flex flex-col']/div[1]/div/div[5]/button/div/div/div/div")
    hobbies = (By.XPATH, "//form[@class='w-full flex flex-col']/div[1]/div/div[5]/button/div/input")
    fluentLanguageClear = (By.XPATH, "//form[@class='w-full flex flex-col']/div[1]/div/div[6]/button/div/div/div/div")
    fluentLanguageDD = (By.XPATH, "//form[@class='w-full flex flex-col']/div[1]/div/div[6]/button")
    optionOfFluentLanguageDD = (By.XPATH, "//form[@class='w-full flex flex-col']/div[1]/div/div[6]/ul/li[3]")
    linkedIn = (By.CSS_SELECTOR, "input[name='links.linkedin']")
    faceBook = (By.CSS_SELECTOR, "input[name='links.facebook']")
    twitter = (By.CSS_SELECTOR, "input[name='links.twitter']")
    instagram = (By.CSS_SELECTOR, "input[name='links.instagram']")
    youTube = (By.CSS_SELECTOR, "input[name='links.youtube']")
    tickTok = (By.CSS_SELECTOR, "input[name='links.ticktok']")
    webSite = (By.CSS_SELECTOR, "input[name='links.personalWebsite']")

    # Additional Information
    additionalInformationIcon = (By.XPATH,
                                 "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[3]")
    emergencyContactName = (By.CSS_SELECTOR, "input[name = 'emergencyContactName']")
    emergencyContactNumber = (By.CSS_SELECTOR, "input[name = 'emergencyContactNumber']")
    emergencyContactRelationshipDD = (
        By.XPATH, "//form[@class='w-full flex flex-col gap-y-6']/div[1]/div/div[3]/button")
    optionOfEmergencyContactRelationshipDD = (
        By.XPATH, "//form[@class='w-full flex flex-col gap-y-6']/div[1]/div/div[3]/ul/li[4]")
    identityTypeDD = (By.XPATH, "//form[@class='w-full flex flex-col gap-y-6']/div[2]/div/div[1]/div/button")
    optionOfIdentityTypeDD = (By.XPATH, "//form[@class='w-full flex flex-col gap-y-6']/div[2]/div/div[1]/div/ul/li[1]")
    firstIdentityNumber = (By.CSS_SELECTOR, "input[name='identities.0.identityNumber']")
    maritalStatusDD = (By.XPATH, "//form[@class='w-full flex flex-col gap-y-6']/div[3]/div/div[1]/button")
    optionOfMaritalStatusDD = (By.XPATH, "//form[@class='w-full flex flex-col gap-y-6']/div[3]/div/div[1]/ul/li[1]")
    drivingLicence = (By.XPATH, "//form[@class='w-full flex flex-col gap-y-6']/div[4]/div/div[1]/button")
    optionOfDrivingLicence = (By.XPATH, "//form[@class='w-full flex flex-col gap-y-6']/div[4]/div/div[1]/ul/li[2]")

    # Education

    educationIcon = (By.XPATH,
                     "//div[@class='ime-tab-group w-full font-semibold flex flex-row [&::-webkit-scrollbar]:hidden']/button[4]")
    addEducationIcon = (By.XPATH,
                        "//div[@class='mr-[48px] h-[72px] bg-slate-100 dark:bg-slate-800 border border-slate-300 dark:border-slate-600 slate-600 font-semibold border-dashed flex flex-row justify-center items-center rounded-[6px] text-slate-500 dark:text-slate-400 text-[16px] cursor-pointer mt-[10px]']")
    qualificationDD = (By.XPATH,
                       "//div[@class='flex flex-col md:grid md:grid-rows-4 md:grid-flow-col md:h-[296px] md:gap-x-[16px] md:mb-[28px]']/div[1]/button")
    optionOfQualificationDD = (By.XPATH,
                               "//div[@class='flex flex-col md:grid md:grid-rows-4 md:grid-flow-col md:h-[296px] md:gap-x-[16px] md:mb-[28px]']/div[1]/ul/li[4]")
    qualificationName = (By.CSS_SELECTOR, "input[name='qualification']")
    instituteName = (By.CSS_SELECTOR, "input[name='institute']")
    startDate = (By.CSS_SELECTOR, "input[name='startDate']")
    endDate = (By.CSS_SELECTOR, "input[name='endDate']")
    saveEducationButton = (By.CSS_SELECTOR,
                           "button[class='bg-clip-border bg-white dark:bg-slate-800 !text-ime-dark hover:!text-white dark:!text-white rounded-[6px] hover:bg-transparent w-[122px] rounded-[4px] transition-colors h-[40px] px-6 text-sm bg-ime-accent hover:bg-blue-700 text-white']")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    # Click on profile section
    def click_on_profile_icon(self):
        time.sleep(3)
        currentURL = self.driver.current_url

        try:
            # Attempt to perform the click action
            self.de_click(self.profileIcon)
        except NoSuchElementException:
            # Handle case where the element is not found
            print("The element to click was not found.")
        except ElementNotInteractableException:
            # Handle case where the element is present but not clickable
            print("The element is not interactable.")
        except Exception as e:
            # Handle any other unexpected exceptions
            print(f"An unexpected error occurred while clicking the element: {e}")
        time.sleep(3)

    # Fill all personal information
    def fill_personal_information(self):
        # self.do_clear(self.firstName)
        # time.sleep(1)
        # self.do_send_key(self.firstName, "Viral")
        # self.do_clear(self.contactNumber)
        # time.sleep(1)
        # self.do_send_key(self.contactNumber, "8511654575")
        # self.do_clear(self.lastName)
        # time.sleep(1)
        # self.do_send_key(self.lastName, "Barot")
        # self.do_clear(self.dateOfBirth)
        # time.sleep(1)
        # self.do_send_key(self.dateOfBirth, "31/01/1988")
        time.sleep(3)
        self.do_clear_using_java_script(self.preferredName)
        time.sleep(1)
        self.do_send_key(self.preferredName, "Viral")
        time.sleep(1)
        self.de_click(self.genderDropDown)
        time.sleep(1)
        self.de_click(self.optionOfGebderDropDown)
        time.sleep(1)
        self.do_clear_using_java_script(self.physicalAddress)
        time.sleep(1)
        self.do_send_key(self.physicalAddress, "United Kingdom")
        time.sleep(1)
        self.de_click(self.region)
        time.sleep(1)
        self.de_click(self.residentialStatusDD)
        time.sleep(1)
        self.de_click(self.optionOfresidentialStatusDD)
        time.sleep(1)
        self.de_click(self.ethinicityDD)
        time.sleep(1)
        self.de_click(self.optionOfethnicityDD)
        time.sleep(1)
        self.de_click(self.disabilitiesDDClear)
        time.sleep(1)
        self.de_click(self.disabilitiesDD)
        time.sleep(1)
        self.de_click(self.optionOfdisabilitiesDD)
        time.sleep(1)
        self.de_click(self.clickonDiv)
        time.sleep(1)
        self.de_click(self.saveInformationButton)
        time.sleep(3)

    # Fill About Me Information
    def fill_about_me_information(self):
        self.de_click(self.aboutMeIcon)
        time.sleep(1)
        self.do_clear_using_java_script(self.height)
        time.sleep(1)
        self.do_send_key(self.height, "6.8")
        time.sleep(1)
        self.de_click(self.garmentSizeDD)
        time.sleep(1)
        self.de_click(self.optionOfGarmentSizeDD)
        time.sleep(1)
        self.de_click(self.dietaryRequirementClear)
        time.sleep(1)
        self.de_click(self.dietaryRequirementDD)
        time.sleep(1)
        self.de_click(self.optionOfDietaryRequirementDD)
        time.sleep(1)
        self.de_click(self.height)
        time.sleep(1)
        self.de_click(self.allergiesClear)
        time.sleep(1)
        self.do_send_key(self.allergies, "Nuts")
        time.sleep(1)
        self.de_click(self.hobbiesClear)
        time.sleep(1)
        self.do_send_key(self.hobbies, "Painting")
        time.sleep(1)
        self.de_click(self.fluentLanguageClear)
        time.sleep(1)
        self.de_click(self.fluentLanguageDD)
        time.sleep(1)
        self.de_click(self.optionOfFluentLanguageDD)
        time.sleep(1)
        self.de_click(self.height)
        time.sleep(1)
        self.do_clear_using_java_script(self.linkedIn)
        time.sleep(1)
        self.do_send_key(self.linkedIn, "LinkedInAccount")
        time.sleep(1)
        self.do_clear_using_java_script(self.faceBook)
        time.sleep(1)
        self.do_send_key(self.faceBook, "faceBookAccount")
        time.sleep(1)
        self.do_clear_using_java_script(self.twitter)
        time.sleep(1)
        self.do_send_key(self.twitter, "twitterAccount")
        time.sleep(1)
        self.do_clear_using_java_script(self.instagram)
        time.sleep(1)
        self.do_send_key(self.instagram, "instagramAccount")
        time.sleep(1)
        self.do_clear_using_java_script(self.youTube)
        time.sleep(1)
        self.do_send_key(self.youTube, "youtubeAccount")
        time.sleep(1)
        self.do_clear_using_java_script(self.tickTok)
        time.sleep(1)
        self.do_send_key(self.tickTok, "tickTockAccount")
        time.sleep(1)
        self.do_clear_using_java_script(self.webSite)
        time.sleep(1)
        self.do_send_key(self.webSite, "www.nitesh.com")
        time.sleep(1)
        self.de_click(self.saveInformationButton)
        time.sleep(3)

    def fill_additional_information(self):
        self.de_click(self.additionalInformationIcon)
        time.sleep(1)
        self.do_clear_using_java_script(self.emergencyContactName)
        time.sleep(1)
        self.do_send_key(self.emergencyContactName, "Vishal")
        time.sleep(1)
        self.do_clear_using_java_script(self.emergencyContactNumber)
        time.sleep(1)
        self.do_send_key(self.emergencyContactNumber, "9090909090")
        time.sleep(1)
        self.de_click(self.emergencyContactRelationshipDD)
        time.sleep(1)
        self.de_click(self.optionOfEmergencyContactRelationshipDD)
        time.sleep(1)
        self.de_click(self.identityTypeDD)
        time.sleep(1)
        self.de_click(self.optionOfIdentityTypeDD)
        time.sleep(1)
        self.do_clear_using_java_script(self.firstIdentityNumber)
        time.sleep(1)
        self.do_send_key(self.firstIdentityNumber, "F6589900")
        time.sleep(1)
        self.de_click(self.maritalStatusDD)
        time.sleep(1)
        self.de_click(self.optionOfMaritalStatusDD)
        time.sleep(1)
        self.de_click(self.drivingLicence)
        time.sleep(1)
        self.de_click(self.optionOfDrivingLicence)
        time.sleep(1)
        self.de_click(self.saveInformationButton)
        time.sleep(3)

        # Fill education Information

    # def fill_educational_information(self):
    #     self.de_click(self.educationIcon)
    #     time.sleep(2)
    #     self.de_click(self.addEducationIcon)
    #     time.sleep(1)
    #     self.de_click(self.qualificationDD)
    #     time.sleep(1)
    #     self.de_click(self.optionOfQualificationDD)
    #     time.sleep(1)
    #     self.do_send_key(self.qualificationName,"Master Of Computer Science")
    #     time.sleep(1)
    #     self.do_send_key(self.instituteName, "DDIT")
    #     time.sleep(0.5)
    #     self.do_clear(self.startDate)
    #
    #     time.sleep(1)
    #     self.do_send_key(self.startDate,"12")
    #     time.sleep(0.5)
    #     self.do_send_key(self.startDate, "09")
    #     time.sleep(0.5)
    #     self.do_send_key(self.startDate, "2002")
    #     time.sleep(0.5)
    #     time.sleep(1)
    #
    #     self.do_clear(self.endDate)
    #     time.sleep(0.5)
    #
    #     self.do_send_key(self.endDate, "12")
    #     time.sleep(0.5)
    #     self.do_send_key(self.endDate, "09")
    #     time.sleep(0.5)
    #     self.do_send_key(self.endDate, "2008")
    #     time.sleep(0.5)
    #     self.de_click(self.saveEducationButton)
    #     time.sleep(2)
