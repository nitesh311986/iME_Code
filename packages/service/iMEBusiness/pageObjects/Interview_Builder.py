import os
import time
import logging
from selenium.webdriver.common.by import By
from iMEBusiness.Utilities.excelReader import excel_Data
from iMEBusiness.pageObjects.BasePage import BasePage
from iMEBusiness.Utilities.customLogger import Logger

log = Logger(__name__, logging.INFO)


class Interview_Builder(BasePage):
    videoInterviewIcon = (By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/button/div")
    interviewBuilderIcon = (
        By.XPATH, "//div[@data-testid='ps-sidebar-container-test-id']/div/div[2]/nav/ul/div/div/div[2]/button[2]")

    # Information Section

    serviceDD = (By.XPATH, "//div[@class='flex flex-row md:flex-row items-baseline']/div/button")
    recruitmentService = (By.XPATH, "//div[@class='flex flex-row md:flex-row items-baseline']/div/ul/li[1]")
    awardService = (By.XPATH, "//div[@class='flex flex-row md:flex-row items-baseline']/div/ul/li[2]")
    marketingService = (By.XPATH, "//div[@class='flex flex-row md:flex-row items-baseline']/div/ul/li[3]")
    learningService = (By.XPATH, "//div[@class='flex flex-row md:flex-row items-baseline']/div/ul/li[4]")
    auditionService = (By.XPATH, "//div[@class='flex flex-row md:flex-row items-baseline']/div/ul/li[5]")
    admissionService = (By.XPATH, "//div[@class='flex flex-row md:flex-row items-baseline']/div/ul/li[6]")

    jobTitle = (By.CSS_SELECTOR, "input[name='interviewTitle']")
    # Department
    departmentDD = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/button")
    Marketing = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[1]")
    Operations = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[2]")
    Legal = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[3]")
    CustomerService = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[4]")
    ResearchDevelopment = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[5]")
    Administration = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[6]")
    ProductDevelopment = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[7]")
    QualityAssurance = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[8]")
    Sales = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[9]")
    informationAndTech = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[10]")
    Finance = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[11]")
    BusinessDevelopment = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[12]")
    SupplyChainManagement = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[13]")
    Communications = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[14]")
    HumanResources = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[15]")
    PublicRelations = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[16]")

    # Employment
    employmentTypeDD = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/button")
    fullTime = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li[1]")
    partTime = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li[2]")
    Freelance = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li[3]")
    Contract = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li[4]")
    Internship = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li[5]")
    Apprenticeship = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li[6]")
    Seasonal = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li[7]")

    # Work Model
    workModelDD = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[4]/button")
    onSite = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[4]/ul/li[1]")
    Remote = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[4]/ul/li[2]")
    Hybrid = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[4]/ul/li[3]")

    Location = (By.CSS_SELECTOR, "input[name='location']")
    queryMail = (By.CSS_SELECTOR, "input[name='queryEmail']")

    # Open or Close Interview
    interViewTypeDD = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[8]/button")
    openInterview = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[8]/ul/li[1]")
    closeInterview = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[8]/ul/li[2]")

    Description = (By.CSS_SELECTOR, "textarea[name='description']")
    nextButton = (By.XPATH,
                  "//div[@class='mt-8 self-end mb-[30px] flex flex-row-reverse w-full max-sm:relative bottom-0']/div/button")

    # Payment Option

    paymentTypeDD = (By.XPATH, "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/button")
    nonePaymentOption = (
        By.XPATH, "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/ul/li[1]")
    payNowPaymentOption = (
        By.XPATH, "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/ul/li[2]")

    amountDD = (
        By.XPATH, "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/button")
    gbpOption = (
        By.XPATH, "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div[1]")
    zarOption = (
        By.XPATH, "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div[2]")
    usdOption = (
        By.XPATH, "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div[3]")
    eurOption = (
        By.XPATH, "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div[4]")
    amountInput = (
        By.XPATH, "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[2]/input")

    # Minimum requirements
    searchMinimumRequirement = (
        By.XPATH, "//div[@class='relative w-full md:w-[350px] overflow-visible']/div/div[1]/input")
    optionOfMinimumRequirements = (By.XPATH, "//div[@class='absolute max-h-[40vh] origin-top-right rounded-md shadow-lg ring-1 ring-black ring-opacity-5 overflow-y-auto overflow-x-hidden border mt-4 border-ime-gray-300 text-ime-gray-800 dark:border-ime-gray-600 bg-white dark:bg-gray-800 __variable_6ba5be font-sans']/div[1]")
    nextButton1 = (
        By.XPATH, "//div[@class='self-end mb-[30px] mt-[30px] flex flex-row-reverse w-full bottom-0']/div[1]/button")
    nextDesignation = (By.XPATH, "//div[@class='mt-8 self-end mb-[30px] flex flex-row-reverse w-full bottom-0']/div["
                                 "1]/button")
    nextButtonVideo = (By.XPATH, "//div[@class='mt-8 self-end mb-[30px] flex justify-end w-full']/button[2]")
    nextMultimediaButton = (
        By.XPATH, "//div[@class='self-end mb-[30px] mt-[30px] flex flex-row-reverse w-full bottom-0']/div[1]/button")
    nextUserButton = (
        By.XPATH, "//div[@class='mt-8 self-end mb-[30px] flex flex-row-reverse w-full bottom-0']/div[1]/button")

    # intro/outro

    introVideo = (By.XPATH,
                  "//div[@class='top-[40px] h-full md:justify-center flex flex-col']/form/div[2]/div[1]/div/div[1]/div/div/input")
    outroVideo = (By.XPATH,
                  "//div[@class='top-[40px] h-full md:justify-center flex flex-col']/form/div[4]/div[1]/div/div[1]/div/div/input")

    # Add Applicant

    addApplicantButton = (By.XPATH, "//form[@class='w-full flex flex-col']/div[1]/button")
    Name = (By.CSS_SELECTOR, "input[name='firstName']")
    lastName = (By.CSS_SELECTOR, "input[name='lastName']")
    Contact = (By.CSS_SELECTOR, "input[name='contact']")
    Email = (By.CSS_SELECTOR, "input[name='email']")
    templateDD = (By.XPATH, "//div[@class='mb-4 relative w-full md:w-[584px]']/button")
    optionOfTemplateDD = (By.XPATH, "//div[@class='mb-4 relative w-full md:w-[584px]']/ul/li[1]")
    saveApplicantButton = (By.XPATH, "//div[@class='w-full flex flex-row-reverse']/button")
    nextButtonApplicant = (
        By.XPATH, "//div[@class='flex justify-center items-center w-full sm:w-[117px] rounded-[6px]']/button")

    saveInterView = (By.XPATH, "//div[@class='w-full flex flex-row justify-end my-[32px]']/button")
    addInterview = (By.XPATH, "//div[@class='flex flex-col w-full items-center h-fit']/div/button[1]")

    # Award Interview

    awardTypeDD = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/button")
    individualTYpe = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[1]")
    teamTYpe = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[2]")
    companyTYpe = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li[3]")

    interviewTypeOFAwardDD = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/button")
    openInterviewType = (By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li[1]")
    closeInterviewType = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li[2]")

    generatedInterview = (By.XPATH,
                          "//div[@class='border border-ime-gray-300 dark:border-zinc-600 mt-[10px] rounded-md']/table/tbody/tr[1]/td[1]/h5/div/div[1]")

    # Marketing Interview

    interviewTypeOfMarketingDD = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/button")

    # Learning Interview

    interviewTypeOfLearningDD = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/button")
    openInterviewTypeOfLearning = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li[1]")
    closeInterviewTypeOfLearning = (
        By.XPATH, "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li[2]")

    global sheetName

    def __init__(self, driver, environment):
        self.environment = environment
        super().__int__(driver)

    def click_on_interview_builder_icon(self):
        time.sleep(5)
        self.de_click(self.videoInterviewIcon)
        time.sleep(1)
        self.de_click(self.interviewBuilderIcon)
        time.sleep(4)

    # Create Interview For Recruitment Starts from here
    def create_interview_for_recruitment(self):
        global position
        global department
        global employment

        log.logger.info("****==Create Interview For Recruitment Services ==***")

        self.de_click(self.serviceDD)
        time.sleep(0.5)
        self.de_click(self.recruitmentService)
        time.sleep(0.5)

        log.logger.info("Current working directory:" + str(os.getcwd()))
        base_dir = os.path.dirname(__file__)

        # Define the relative path to the Pricing.xlsx file
        relative_path = os.path.join(base_dir, '../excel/interview_builder_information.xlsx')
        sheetName = 'Recruitment'

        # Get the absolute path
        path = os.path.abspath(relative_path)
        print("Absolute path:", path)

        # Check if the file exists
        if os.path.exists(path):
            print("File found!")
            # Proceed with file operations
        else:
            raise FileNotFoundError(f"File not found: {path}")

        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))

        for j in range(2, row + 1):
            for k in range(1, col + 1):
                position = excel_Data.getCellData(path, sheetName, j, 1)
                department = excel_Data.getCellData(path, sheetName, j, 2)
                employment = excel_Data.getCellData(path, sheetName, j, 3)
                model = excel_Data.getCellData(path, sheetName, j, 4)
                location = excel_Data.getCellData(path, sheetName, j, 5)
                email = excel_Data.getCellData(path, sheetName, j, 6)
                interviewType = excel_Data.getCellData(path, sheetName, j, 7)
                description = excel_Data.getCellData(path, sheetName, j, 8)
                designation = excel_Data.getCellData(path, sheetName, j, 9)
                service = excel_Data.getCellData(path, sheetName, j, 10)
                payment_type = excel_Data.getCellData(path, sheetName, j, 11)
                currency_method = excel_Data.getCellData(path, sheetName, j, 12)
                amount = excel_Data.getCellData(path, sheetName, j, 13)

        # Get Current Date Time Using Time Zone
        dateTime = self.get_date_time_using_time_zone()

        time.sleep(0.5)
        self.do_send_key(self.jobTitle, position + dateTime)
        time.sleep(0.5)
        self.de_click(self.departmentDD)
        time.sleep(0.5)

        totalJobDepartment = len(self.driver.find_elements(By.XPATH,
                                                           "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li"))
        JobTitle = []
        JobTitle = self.driver.find_elements(By.XPATH,
                                             "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li")
        for i in range(totalJobDepartment):

            title = str(JobTitle[i].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(department))
            if department == "Marketing":
                self.de_click(self.Marketing)
                break
            elif department == "Operations":
                self.de_click(self.Operations)
                break
            elif department == "Legal":
                self.de_click(self.Legal)
                break
            elif department == "Customer Service":
                self.de_click(self.CustomerService)
                break
            elif department == "Research and Development":
                self.de_click(self.ResearchDevelopment)
                break
            elif department == "Administration":
                self.de_click(self.Administration)
                break
            elif department == "Product Development":
                self.de_click(self.ProductDevelopment)
                break
            elif department == "Quality Assurance":
                self.de_click(self.QualityAssurance)
                break
            elif department == "Sales":
                self.de_click(self.Sales)
                break
            elif department == "Information Technology":
                self.de_click(self.informationAndTech)
                break
            elif department == "Finance":
                self.de_click(self.Finance)
                break
            elif department == "Business Development":
                self.de_click(self.BusinessDevelopment)
                break
            elif department == "Supply Chain Management":
                self.de_click(self.SupplyChainManagement)
                break
            elif department == "Communications":
                self.de_click(self.Communications)
                break
            elif department == "Human Resources":
                self.de_click(self.HumanResources)
                break
            elif department == "Public Relations":
                self.de_click(self.PublicRelations)
                break

        time.sleep(0.5)
        self.de_click(self.employmentTypeDD)
        time.sleep(0.5)
        totalEmployment = len(self.driver.find_elements(By.XPATH,
                                                        "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li"))
        employmentType = []
        employmentType = self.driver.find_elements(By.XPATH,
                                                   "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li")

        for m in range(totalEmployment):

            title = str(employmentType[m].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(employment))
            if employment == "Full-time":
                self.de_click(self.fullTime)
                break
            elif employment == "Part-time":
                self.de_click(self.partTime)
                break
            elif employment == "Freelance":
                self.de_click(self.Freelance)
                break
            elif employment == "Contract":
                self.de_click(self.Contract)
                break
            elif employment == "Internship":
                self.de_click(self.Internship)
                break
            elif employment == "Apprenticeship":
                self.de_click(self.Apprenticeship)
                break
            elif employment == "Seasonal":
                self.de_click(self.Seasonal)
                break

        time.sleep(0.5)
        self.de_click(self.workModelDD)
        time.sleep(0.5)
        totalWorkModel = len(self.driver.find_elements(By.XPATH,
                                                       "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[4]/ul/li"))
        workModel = []
        workModel = self.driver.find_elements(By.XPATH,
                                              "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[4]/ul/li")

        for n in range(totalWorkModel):

            model1 = str(workModel[n].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(model))
            if model == "On Site":
                self.de_click(self.onSite)
                break
            elif model == "Remote":
                self.de_click(self.Remote)
                break
            elif model == "Hybrid":
                self.de_click(self.Hybrid)
                break

        time.sleep(0.5)
        self.do_send_key(self.Location, location)
        time.sleep(0.5)
        self.do_send_key(self.queryMail, email)
        time.sleep(0.5)
        self.do_send_key(self.Location, location)
        time.sleep(0.5)

        time.sleep(0.5)
        self.de_click(self.interViewTypeDD)
        time.sleep(0.5)
        totalInterviewType = len(self.driver.find_elements(By.XPATH,
                                                           "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[8]/ul/li"))
        interviewType1 = []
        interviewType1 = self.driver.find_elements(By.XPATH,
                                                   "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[8]/ul/li")

        for p in range(totalInterviewType):

            interviewtype = str(interviewType1[p].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(interviewType))
            if interviewType == "Open Interview":
                self.de_click(self.openInterview)
                break
            elif interviewType == "Closed Interview":
                self.de_click(self.closeInterview)
                break

        time.sleep(0.5)
        self.do_send_key(self.Description, description)
        time.sleep(0.5)
        self.de_click(self.paymentTypeDD)
        time.sleep(0.5)
        total_payment_type = len(self.driver.find_elements(By.XPATH,
                                                           "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/ul/li"))
        payment_method = []
        payment_method = self.driver.find_elements(By.XPATH,
                                                   "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/ul/li")
        for i in range(total_payment_type):

            p_type = str(payment_method[i].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(p_type))
            if payment_type == "NO":
                self.de_click(self.nonePaymentOption)
                break
            elif payment_type == "Pay Now":
                self.de_click(self.payNowPaymentOption)
                time.sleep(1)
                self.de_click(self.amountDD)
                time.sleep(1)
                currency_type = len(self.driver.find_elements(By.XPATH,
                                                              "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div"))
                currency = []
                currency = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div")

                for j in range(currency_type):
                    c_type = str(currency[j].text)
                    # log.logger.info("" + str(title))
                    log.logger.info("" + str(c_type))
                    if currency_method == "GBP":
                        self.de_click(self.gbpOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "ZAR":
                        self.de_click(self.zarOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "USD":
                        self.de_click(self.usdOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "EUR":
                        self.de_click(self.eurOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    else:
                        self.de_click(self.gbpOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                break
            else:
                self.de_click(self.nonePaymentOption)
                break
        time.sleep(1)

        self.de_click(self.nextButton)
        time.sleep(3)

        # Minimum Requirement
        self.minimum_Requirement(sheetName)

        # Application requirements
        self.application_Requirement(sheetName)

        # Question Set
        self.question_Set(sheetName)

        # Intro Outro Video
        self.intro_Outro_Video()

        # Multimedia
        self.multiMedia(sheetName)

        # Add User
        self.addUser()

        # Add Applicant
        self.add_Applicant()

        # Save Interview
        self.save_Interview()

        # code goes here

    # Create Interview For Award Starts from here

    def create_interview_for_award(self):

        global position
        global department
        global employment

        log.logger.info("****==Create Interview For Award Services ==***")

        self.de_click(self.serviceDD)
        time.sleep(0.5)
        self.de_click(self.awardService)
        time.sleep(0.5)
        log.logger.info("Current working directory:" + str(os.getcwd()))
        base_dir = os.path.dirname(__file__)

        # Define the relative path to the Pricing.xlsx file
        relative_path = os.path.join(base_dir, '../excel/interview_builder_information.xlsx')
        sheetName = 'Awards'

        # Get the absolute path
        path = os.path.abspath(relative_path)
        print("Absolute path:", path)

        # Check if the file exists
        if os.path.exists(path):
            print("File found!")
            # Proceed with file operations
        else:
            raise FileNotFoundError(f"File not found: {path}")

        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))

        for j in range(2, row + 1):
            for k in range(1, col + 1):
                position = excel_Data.getCellData(path, sheetName, j, 1)
                awardType = excel_Data.getCellData(path, sheetName, j, 2)
                interviewType = excel_Data.getCellData(path, sheetName, j, 3)
                email = excel_Data.getCellData(path, sheetName, j, 4)
                description = excel_Data.getCellData(path, sheetName, j, 5)
                designation = excel_Data.getCellData(path, sheetName, j, 6)
                payment_type = excel_Data.getCellData(path, sheetName, j, 7)
                currency_method = excel_Data.getCellData(path, sheetName, j, 8)
                amount = excel_Data.getCellData(path, sheetName, j, 9)

        # Get Current Date Time Using Time Zone
        dateTime = self.get_date_time_using_time_zone()

        time.sleep(0.5)
        self.do_send_key(self.jobTitle, position + dateTime)
        time.sleep(0.5)
        self.de_click(self.awardTypeDD)
        time.sleep(0.5)

        totalAwardType = len(self.driver.find_elements(By.XPATH,
                                                       "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li"))
        awardType1 = []
        awardType1 = self.driver.find_elements(By.XPATH,
                                               "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li")
        for i in range(totalAwardType):

            title = str(awardType1[i].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(awardType))
            if awardType == "Individual":
                self.de_click(self.individualTYpe)
                break
            elif awardType == "Team":
                self.de_click(self.teamTYpe)
                break
            elif awardType == "Company":
                self.de_click(self.companyTYpe)
                break

        time.sleep(0.5)
        self.de_click(self.interviewTypeOFAwardDD)
        time.sleep(0.5)
        totalInterviewTypeOfAward = len(self.driver.find_elements(By.XPATH,
                                                                  "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li"))
        interviewTypeOfAward = []
        interviewTypeOfAward = self.driver.find_elements(By.XPATH,
                                                         "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li")

        for m in range(totalInterviewTypeOfAward):

            title = str(interviewTypeOfAward[m].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(interviewType))
            if interviewType == "Open Interview":
                self.de_click(self.fullTime)
                break
            elif interviewType == "Closed Interview":
                self.de_click(self.partTime)
                break

        self.do_send_key(self.queryMail, email)
        time.sleep(0.5)

        time.sleep(0.5)
        self.do_send_key(self.Description, description)
        time.sleep(0.5)
        self.de_click(self.paymentTypeDD)
        time.sleep(0.5)
        total_payment_type = len(self.driver.find_elements(By.XPATH,
                                                           "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/ul/li"))
        payment_method = []
        payment_method = self.driver.find_elements(By.XPATH,
                                                   "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/ul/li")
        for i in range(total_payment_type):

            p_type = str(payment_method[i].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(p_type))
            if payment_type == "NO":
                self.de_click(self.nonePaymentOption)
                break
            elif payment_type == "Pay Now":
                self.de_click(self.payNowPaymentOption)
                time.sleep(1)
                self.de_click(self.amountDD)
                time.sleep(1)
                currency_type = len(self.driver.find_elements(By.XPATH,
                                                              "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div"))
                currency = []
                currency = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div")

                for j in range(currency_type):
                    c_type = str(currency[j].text)
                    # log.logger.info("" + str(title))
                    log.logger.info("" + str(c_type))
                    if currency_method == "GBP":
                        self.de_click(self.gbpOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "ZAR":
                        self.de_click(self.zarOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "USD":
                        self.de_click(self.usdOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "EUR":
                        self.de_click(self.eurOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    else:
                        self.de_click(self.gbpOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                break
            else:
                self.de_click(self.nonePaymentOption)
                break
        self.de_click(self.nextButton)
        time.sleep(3)

        # Create Minimum Requirement
        self.minimum_Requirement(sheetName)

        # Application requirements
        self.application_Requirement(sheetName)

        # Create Question Set
        self.question_Set(sheetName)

        # Intro/Outro Video
        self.intro_Outro_Video()

        # Multimedia
        self.multiMedia(sheetName)

        # Add Internal External User
        self.addUser()

        # Add Applicant
        self.add_Applicant()

        # Save Interview
        self.save_Interview()

    # Create Interview For Marketing Service Starts from here

    def create_interview_for_marketing(self):
        global position
        global department
        global employment

        log.logger.info("****==Create Interview For Marketing Services ==***")

        self.de_click(self.serviceDD)
        time.sleep(0.5)
        self.de_click(self.marketingService)
        time.sleep(0.5)

        log.logger.info("Current working directory:" + str(os.getcwd()))
        base_dir = os.path.dirname(__file__)

        # Define the relative path to the Pricing.xlsx file
        relative_path = os.path.join(base_dir, '../excel/interview_builder_information.xlsx')
        sheetName = 'Marketing'

        # Get the absolute path
        path = os.path.abspath(relative_path)
        print("Absolute path:", path)

        # Check if the file exists
        if os.path.exists(path):
            print("File found!")
            # Proceed with file operations
        else:
            raise FileNotFoundError(f"File not found: {path}")

        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))

        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))

        for j in range(2, row + 1):
            for k in range(1, col + 1):
                position = excel_Data.getCellData(path, sheetName, j, 1)
                email = excel_Data.getCellData(path, sheetName, j, 2)
                interviewType = excel_Data.getCellData(path, sheetName, j, 3)
                description = excel_Data.getCellData(path, sheetName, j, 4)
                designation = excel_Data.getCellData(path, sheetName, j, 5)
                payment_type = excel_Data.getCellData(path, sheetName, j, 6)
                currency_method = excel_Data.getCellData(path, sheetName, j, 7)
                amount = excel_Data.getCellData(path, sheetName, j, 8)

        # Get Current Date Time Using Time Zone
        dateTime = self.get_date_time_using_time_zone()

        time.sleep(0.5)
        self.do_send_key(self.jobTitle, position + dateTime)
        time.sleep(0.5)
        self.do_send_key(self.queryMail, email)
        time.sleep(0.5)

        time.sleep(0.5)
        self.de_click(self.interviewTypeOFAwardDD)
        time.sleep(0.5)
        totalInterviewTypeOfMarketing = len(self.driver.find_elements(By.XPATH,
                                                                      "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li"))
        interviewTypeOfMarketing = []
        interviewTypeOfMarketing = self.driver.find_elements(By.XPATH,
                                                             "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li")

        for m in range(totalInterviewTypeOfMarketing):

            title = str(interviewTypeOfMarketing[m].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(interviewType))
            if interviewType == "Open Interview":
                self.de_click(self.openInterviewType)
                break
            elif interviewType == "Closed Interview":
                self.de_click(self.closeInterviewType)
                break

        time.sleep(0.5)
        self.do_send_key(self.Description, description)
        time.sleep(0.5)
        time.sleep(0.5)
        self.de_click(self.paymentTypeDD)
        time.sleep(0.5)
        total_payment_type = len(self.driver.find_elements(By.XPATH,
                                                           "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/ul/li"))
        payment_method = []
        payment_method = self.driver.find_elements(By.XPATH,
                                                   "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/ul/li")
        for i in range(total_payment_type):

            p_type = str(payment_method[i].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(p_type))
            if payment_type == "NO":
                self.de_click(self.nonePaymentOption)
                break
            elif payment_type == "Pay Now":
                self.de_click(self.payNowPaymentOption)
                time.sleep(1)
                self.de_click(self.amountDD)
                time.sleep(1)
                currency_type = len(self.driver.find_elements(By.XPATH,
                                                              "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div"))
                currency = []
                currency = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div")

                for j in range(currency_type):
                    c_type = str(currency[j].text)
                    # log.logger.info("" + str(title))
                    log.logger.info("" + str(c_type))
                    if currency_method == "GBP":
                        self.de_click(self.gbpOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "ZAR":
                        self.de_click(self.zarOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "USD":
                        self.de_click(self.usdOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "EUR":
                        self.de_click(self.eurOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    else:
                        self.de_click(self.gbpOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                break
            else:
                self.de_click(self.nonePaymentOption)
                break
        self.de_click(self.nextButton)
        time.sleep(3)

        # Create Minimum Requirement
        self.minimum_Requirement(sheetName)

        # Application requirements
        self.application_Requirement(sheetName)

        # Create Question Set
        self.question_Set(sheetName)

        # Create Intro Outro Video
        self.intro_Outro_Video()

        # Create Multimedia Video
        self.multiMedia(sheetName)

        # Add  User
        self.addUser()

        # Add Applicants List
        self.add_Applicant()

        # Save Interview
        self.save_Interview()

    # Create Interview For Learning Service Starts from here

    def create_interview_for_learning(self):
        global position
        global department
        global employment

        log.logger.info("****==Create Interview For Learning Services ==***")

        self.de_click(self.serviceDD)
        time.sleep(0.5)
        self.de_click(self.learningService)
        time.sleep(0.5)
        log.logger.info("Current working directory:" + str(os.getcwd()))
        base_dir = os.path.dirname(__file__)

        # Define the relative path to the Pricing.xlsx file
        relative_path = os.path.join(base_dir, '../excel/interview_builder_information.xlsx')
        sheetName = 'Learning'

        # Get the absolute path
        path = os.path.abspath(relative_path)
        print("Absolute path:", path)

        # Check if the file exists
        if os.path.exists(path):
            print("File found!")
            # Proceed with file operations
        else:
            raise FileNotFoundError(f"File not found: {path}")

        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))

        for j in range(2, row + 1):
            for k in range(1, col + 1):
                position = excel_Data.getCellData(path, sheetName, j, 1)
                department = excel_Data.getCellData(path, sheetName, j, 2)
                email = excel_Data.getCellData(path, sheetName, j, 3)
                interviewType = excel_Data.getCellData(path, sheetName, j, 4)
                description = excel_Data.getCellData(path, sheetName, j, 5)
                designation = excel_Data.getCellData(path, sheetName, j, 6)
                payment_type = excel_Data.getCellData(path, sheetName, j, 7)
                currency_method = excel_Data.getCellData(path, sheetName, j, 8)
                amount = excel_Data.getCellData(path, sheetName, j, 9)

        # Get Current Date Time Using Time Zone
        dateTime = self.get_date_time_using_time_zone()

        time.sleep(0.5)
        self.do_send_key(self.jobTitle, position + dateTime)
        time.sleep(0.5)
        # self.de_click(self.departmentDD)
        # time.sleep(0.5)

        # totalJobDepartment = len(self.driver.find_elements(By.XPATH,
        #                                                    "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li"))
        # JobTitle = []
        # JobTitle = self.driver.find_elements(By.XPATH,
        #                                      "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[2]/ul/li")
        # for i in range(totalJobDepartment):
        #
        #     title = str(JobTitle[i].text)
        #     # log.logger.info("" + str(title))
        #     log.logger.info("" + str(department))
        #     if department == "Marketing":
        #         self.de_click(self.Marketing)
        #         break
        #     elif department == "Operations":
        #         self.de_click(self.Operations)
        #         break
        #     elif department == "Legal":
        #         self.de_click(self.Legal)
        #         break
        #     elif department == "Customer Service":
        #         self.de_click(self.CustomerService)
        #         break
        #     elif department == "Research and Development":
        #         self.de_click(self.ResearchDevelopment)
        #         break
        #     elif department == "Administration":
        #         self.de_click(self.Administration)
        #         break
        #     elif department == "Product Development":
        #         self.de_click(self.ProductDevelopment)
        #         break
        #     elif department == "Quality Assurance":
        #         self.de_click(self.QualityAssurance)
        #         break
        #     elif department == "Sales":
        #         self.de_click(self.Sales)
        #         break
        #     elif department == "Information Technology":
        #         self.de_click(self.informationAndTech)
        #         break
        #     elif department == "Finance":
        #         self.de_click(self.Finance)
        #         break
        #     elif department == "Business Development":
        #         self.de_click(self.BusinessDevelopment)
        #         break
        #     elif department == "Supply Chain Management":
        #         self.de_click(self.SupplyChainManagement)
        #         break
        #     elif department == "Communications":
        #         self.de_click(self.Communications)
        #         break
        #     elif department == "Human Resources":
        #         self.de_click(self.HumanResources)
        #         break
        #     elif department == "Public Relations":
        #         self.de_click(self.PublicRelations)
        #         break

        self.do_send_key(self.queryMail, email)
        time.sleep(0.5)
        self.de_click(self.interviewTypeOfLearningDD)
        time.sleep(0.5)
        totalInterviewTypeOfLearning = len(self.driver.find_elements(By.XPATH,
                                                                     "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[4]/ul/li"))
        interviewTypeOfMarketing = []
        interviewTypeOfLearning = self.driver.find_elements(By.XPATH,
                                                            "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[4]/ul/li")

        for m in range(totalInterviewTypeOfLearning):

            title = str(interviewTypeOfLearning[m].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(interviewType))
            if interviewType == "Open Interview":
                self.de_click(self.openInterviewTypeOfLearning)
                break
            elif interviewType == "Closed Interview":
                self.de_click(self.closeInterviewTypeOfLearning)
                break

        time.sleep(0.5)
        self.do_send_key(self.Description, description)
        time.sleep(0.5)
        time.sleep(0.5)
        self.de_click(self.paymentTypeDD)
        time.sleep(0.5)
        total_payment_type = len(self.driver.find_elements(By.XPATH,
                                                           "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/ul/li"))
        payment_method = []
        payment_method = self.driver.find_elements(By.XPATH,
                                                   "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/ul/li")
        for i in range(total_payment_type):

            p_type = str(payment_method[i].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(p_type))
            if payment_type == "NO":
                self.de_click(self.nonePaymentOption)
                break
            elif payment_type == "Pay Now":
                self.de_click(self.payNowPaymentOption)
                time.sleep(1)
                self.de_click(self.amountDD)
                time.sleep(1)
                currency_type = len(self.driver.find_elements(By.XPATH,
                                                              "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div"))
                currency = []
                currency = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div")

                for j in range(currency_type):
                    c_type = str(currency[j].text)
                    # log.logger.info("" + str(title))
                    log.logger.info("" + str(c_type))
                    if currency_method == "GBP":
                        self.de_click(self.gbpOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "ZAR":
                        self.de_click(self.zarOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "USD":
                        self.de_click(self.usdOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "EUR":
                        self.de_click(self.eurOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    else:
                        self.de_click(self.gbpOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                break
            else:
                self.de_click(self.nonePaymentOption)
                break
        self.de_click(self.nextButton)
        time.sleep(3)

        # Create Minimum Requirement
        self.minimum_Requirement(sheetName)

        # Application requirements
        self.application_Requirement(sheetName)

        # Create Question Set
        self.question_Set(sheetName)

        # Create Intro Outro Video
        self.intro_Outro_Video()

        # Create Multimedia Video
        self.multiMedia(sheetName)

        # Add User
        self.addUser()

        # Add Applicants List
        self.add_Applicant()

        # Save and create interview
        self.save_Interview()

    # Create Interview For Audition Service Starts from here

    def create_interview_for_audition(self):

        global position
        global department
        global employment

        log.logger.info("****==Create Interview For Audition Services ==***")

        self.de_click(self.serviceDD)
        time.sleep(0.5)
        self.de_click(self.auditionService)
        time.sleep(0.5)
        log.logger.info("Current working directory:" + str(os.getcwd()))
        base_dir = os.path.dirname(__file__)

        # Define the relative path to the Pricing.xlsx file
        relative_path = os.path.join(base_dir, '../excel/interview_builder_information.xlsx')
        sheetName = 'Auditions'

        # Get the absolute path
        path = os.path.abspath(relative_path)
        print("Absolute path:", path)

        # Check if the file exists
        if os.path.exists(path):
            print("File found!")
            # Proceed with file operations
        else:
            raise FileNotFoundError(f"File not found: {path}")

        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))

        for j in range(2, row + 1):
            for k in range(1, col + 1):
                position = excel_Data.getCellData(path, sheetName, j, 1)
                email = excel_Data.getCellData(path, sheetName, j, 2)
                interviewType = excel_Data.getCellData(path, sheetName, j, 3)
                description = excel_Data.getCellData(path, sheetName, j, 4)
                designation = excel_Data.getCellData(path, sheetName, j, 5)
                payment_type = excel_Data.getCellData(path, sheetName, j, 6)
                currency_method = excel_Data.getCellData(path, sheetName, j, 7)
                amount = excel_Data.getCellData(path, sheetName, j, 8)

        # Get Current Date Time Using Time Zone
        dateTime = self.get_date_time_using_time_zone()

        time.sleep(0.5)
        self.do_send_key(self.jobTitle, position + dateTime)
        time.sleep(0.5)
        self.do_send_key(self.queryMail, email)
        time.sleep(0.5)

        time.sleep(0.5)
        self.de_click(self.interviewTypeOFAwardDD)
        time.sleep(0.5)
        totalInterviewTypeOfMarketing = len(self.driver.find_elements(By.XPATH,
                                                                      "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li"))
        interviewTypeOfMarketing = []
        interviewTypeOfMarketing = self.driver.find_elements(By.XPATH,
                                                             "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li")

        for m in range(totalInterviewTypeOfMarketing):

            title = str(interviewTypeOfMarketing[m].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(interviewType))
            if interviewType == "Open Interview":
                self.de_click(self.openInterviewType)
                break
            elif interviewType == "Closed Interview":
                self.de_click(self.closeInterviewType)
                break

        time.sleep(0.5)
        self.do_send_key(self.Description, description)
        time.sleep(0.5)
        time.sleep(0.5)
        self.de_click(self.paymentTypeDD)
        time.sleep(0.5)
        total_payment_type = len(self.driver.find_elements(By.XPATH,
                                                           "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/ul/li"))
        payment_method = []
        payment_method = self.driver.find_elements(By.XPATH,
                                                   "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/ul/li")
        for i in range(total_payment_type):

            p_type = str(payment_method[i].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(p_type))
            if payment_type == "NO":
                self.de_click(self.nonePaymentOption)
                break
            elif payment_type == "Pay Now":
                self.de_click(self.payNowPaymentOption)
                time.sleep(1)
                self.de_click(self.amountDD)
                time.sleep(1)
                currency_type = len(self.driver.find_elements(By.XPATH,
                                                              "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div"))
                currency = []
                currency = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div")

                for j in range(currency_type):
                    c_type = str(currency[j].text)
                    # log.logger.info("" + str(title))
                    log.logger.info("" + str(c_type))
                    if currency_method == "GBP":
                        self.de_click(self.gbpOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "ZAR":
                        self.de_click(self.zarOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "USD":
                        self.de_click(self.usdOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "EUR":
                        self.de_click(self.eurOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    else:
                        self.de_click(self.gbpOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                break
            else:
                self.de_click(self.nonePaymentOption)
                break
        self.de_click(self.nextButton)
        time.sleep(3)

        # Create Minimum Requirement
        self.minimum_Requirement(sheetName)

        # Application requirements
        self.application_Requirement(sheetName)

        # Create Question Set
        self.question_Set(sheetName)

        # Create Intro Outro Video
        self.intro_Outro_Video()

        # Create Multimedia Video
        self.multiMedia(sheetName)
        #
        # # Add  User
        self.addUser()
        #
        # # Add Applicants List
        self.add_Applicant()

        # # Save and Create Interview
        self.save_Interview()

    # Create Interview For Admission Service Starts from here

    def create_interview_for_admission(self):

        global position
        global department
        global employment

        log.logger.info("****==Create Interview For Admission Services ==***")

        self.de_click(self.serviceDD)
        time.sleep(0.5)
        self.de_click(self.admissionService)
        time.sleep(0.5)
        log.logger.info("Current working directory:" + str(os.getcwd()))
        base_dir = os.path.dirname(__file__)

        # Define the relative path to the Pricing.xlsx file
        relative_path = os.path.join(base_dir, '../excel/interview_builder_information.xlsx')
        sheetName = 'Admissions'

        # Get the absolute path
        path = os.path.abspath(relative_path)
        print("Absolute path:", path)

        # Check if the file exists
        if os.path.exists(path):
            print("File found!")
            # Proceed with file operations
        else:
            raise FileNotFoundError(f"File not found: {path}")

        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))

        for j in range(2, row + 1):
            for k in range(1, col + 1):
                position = excel_Data.getCellData(path, sheetName, j, 1)
                email = excel_Data.getCellData(path, sheetName, j, 2)
                interviewType = excel_Data.getCellData(path, sheetName, j, 3)
                description = excel_Data.getCellData(path, sheetName, j, 4)
                designation = excel_Data.getCellData(path, sheetName, j, 5)
                payment_type = excel_Data.getCellData(path, sheetName, j, 6)
                currency_method = excel_Data.getCellData(path, sheetName, j, 7)
                amount = excel_Data.getCellData(path, sheetName, j, 8)

        # Get Current Date Time Using Time Zone
        dateTime = self.get_date_time_using_time_zone()
        time.sleep(0.5)

        self.do_send_key(self.jobTitle, position + dateTime)
        time.sleep(0.5)
        self.do_send_key(self.queryMail, email)
        time.sleep(0.5)

        time.sleep(0.5)
        self.de_click(self.interviewTypeOFAwardDD)
        time.sleep(0.5)
        totalInterviewTypeOfMarketing = len(self.driver.find_elements(By.XPATH,
                                                                      "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li"))
        interviewTypeOfMarketing = []
        interviewTypeOfMarketing = self.driver.find_elements(By.XPATH,
                                                             "//div[@class='grid md:grid-cols-2 lg:grid-cols-3 sm:gap-x-[16px]']/div[3]/ul/li")

        for m in range(totalInterviewTypeOfMarketing):

            title = str(interviewTypeOfMarketing[m].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(interviewType))
            if interviewType == "Open Interview":
                self.de_click(self.openInterviewType)
                break
            elif interviewType == "Closed Interview":
                self.de_click(self.closeInterviewType)
                break

        time.sleep(0.5)
        self.do_send_key(self.Description, description)
        time.sleep(0.5)
        time.sleep(0.5)
        self.de_click(self.paymentTypeDD)
        time.sleep(0.5)
        total_payment_type = len(self.driver.find_elements(By.XPATH,
                                                           "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/ul/li"))
        payment_method = []
        payment_method = self.driver.find_elements(By.XPATH,
                                                   "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[1]/ul/li")
        for i in range(total_payment_type):

            p_type = str(payment_method[i].text)
            # log.logger.info("" + str(title))
            log.logger.info("" + str(p_type))
            if payment_type == "NO":
                self.de_click(self.nonePaymentOption)
                break
            elif payment_type == "Pay Now":
                self.de_click(self.payNowPaymentOption)
                time.sleep(1)
                self.de_click(self.amountDD)
                time.sleep(1)
                currency_type = len(self.driver.find_elements(By.XPATH,
                                                              "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div"))
                currency = []
                currency = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='flex flex-row max-md:flex-col gap-x-2 sm:gap-x-[16px]']/div[2]/div[1]/div/div")

                for j in range(currency_type):
                    c_type = str(currency[j].text)
                    # log.logger.info("" + str(title))
                    log.logger.info("" + str(c_type))
                    if currency_method == "GBP":
                        self.de_click(self.gbpOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "ZAR":
                        self.de_click(self.zarOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "USD":
                        self.de_click(self.usdOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    elif currency_method == "EUR":
                        self.de_click(self.eurOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                    else:
                        self.de_click(self.gbpOption)
                        time.sleep(0.5)
                        self.do_send_key(self.amountInput, amount)
                        break
                break
            else:
                self.de_click(self.nonePaymentOption)
                break
        self.de_click(self.nextButton)
        time.sleep(3)

        # Create Minimum Requirement
        self.minimum_Requirement(sheetName)

        # Application requirements
        self.application_Requirement(sheetName)

        # Create Question Set
        self.question_Set(sheetName)

        # Create Intro Outro Video
        self.intro_Outro_Video()

        # Create Multimedia Video
        self.multiMedia(sheetName)
        #
        # # Add  User
        self.addUser()
        #
        # # Add Applicants List
        self.add_Applicant()

        self.save_Interview()

    # common Function for All Services

    def minimum_Requirement(self, sheet):
        global row, col, path, sheetName
        if sheet == "Recruitment":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/template_creation.xlsx')
            sheetName = 'Recruitment'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Awards":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/template_creation.xlsx')
            sheetName = 'Awards'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Marketing":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/template_creation.xlsx')
            sheetName = 'Marketing'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Learning":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/template_creation.xlsx')
            sheetName = 'Learning'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Auditions":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/template_creation.xlsx')
            sheetName = 'Auditions'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Admissions":
            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/template_creation.xlsx')
            sheetName = 'Admissions'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))
        for j in range(2, row + 1):
            for k in range(1, col + 1, 3):
                question = excel_Data.getCellData(path, sheetName, j, k)
                cellData1 = excel_Data.getCellData(path, sheetName, j, 2)
                time.sleep(0.5)
                log.logger.info("" + str(question))
                log.logger.info("" + str(cellData1))
                time.sleep(0.5)
                if j < row:
                    self.do_send_key(self.searchMinimumRequirement, question)
                    time.sleep(0.5)
                    self.de_click(self.searchMinimumRequirement)
                    time.sleep(0.5)
                    self.de_click(self.optionOfMinimumRequirements)
                    time.sleep(1)
                else:
                    break

        self.de_click(self.nextButton1)
        time.sleep(3)

    def application_Requirement(self, sheet):
        global row, col, path, sheetName
        if sheet == "Recruitment":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/application_requirement_creation.xlsx')
            sheetName = 'Recruitment'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Awards":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/application_requirement_creation.xlsx')
            sheetName = 'Awards'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Marketing":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/application_requirement_creation.xlsx')
            sheetName = 'Marketing'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Learning":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/application_requirement_creation.xlsx')
            sheetName = 'Learning'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Auditions":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/application_requirement_creation.xlsx')
            sheetName = 'Auditions'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Admissions":
            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/application_requirement_creation.xlsx')
            sheetName = 'Admissions'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))
        for j in range(2, row + 1):
            for k in range(1, col + 1):
                requirementType = excel_Data.getCellData(path, sheetName, j, k)
                cellData1 = excel_Data.getCellData(path, sheetName, j, 2)
                time.sleep(0.5)
                log.logger.info("" + str(requirementType))
                log.logger.info("" + str(cellData1))
                time.sleep(0.5)
                if j < row:
                    self.do_send_key(self.searchMinimumRequirement, cellData1)
                    time.sleep(0.5)
                    self.de_click(self.searchMinimumRequirement)
                    time.sleep(0.5)
                    self.de_click(self.optionOfMinimumRequirements)
                    time.sleep(1)
                    break
                else:
                    break

            break

        self.de_click(self.nextButton1)
        time.sleep(3)

    def question_Set(self, sheet):
        global row, col, path, sheetName
        if sheet == "Recruitment":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/interview_builder_information.xlsx')
            sheetName = 'Recruitment'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")



        elif sheet == "Awards":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/interview_builder_information.xlsx')
            sheetName = 'Awards'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Marketing":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/interview_builder_information.xlsx')
            sheetName = 'Marketing'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")



        elif sheet == "Learning":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/interview_builder_information.xlsx')
            sheetName = 'Learning'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Auditions":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/interview_builder_information.xlsx')
            sheetName = 'Auditions'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Admissions":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/interview_builder_information.xlsx')
            sheetName = 'Admissions'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))
        for j in range(2, row + 1):
            for k in range(1, col + 1):
                designation = excel_Data.getCellData(path, sheetName, j, 1)

            log.logger.info("" + str(designation))
            self.do_send_key(self.searchMinimumRequirement, designation)
            time.sleep(0.5)
            self.de_click(self.searchMinimumRequirement)
            time.sleep(0.5)
            self.de_click(self.optionOfMinimumRequirements)
            time.sleep(1)
            self.de_click(self.nextDesignation)
            time.sleep(3)

    def intro_Outro_Video(self):
        self.de_click(self.nextButtonVideo)
        time.sleep(3)

    def multiMedia(self, sheet):
        global row, col, path, sheetName
        if sheet == "Recruitment":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/multimedia_creation.xlsx')
            sheetName = 'Recruitment'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Awards":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/multimedia_creation.xlsx')
            sheetName = 'Awards'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Marketing":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/multimedia_creation.xlsx')
            sheetName = 'Marketing'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Learning":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/multimedia_creation.xlsx')
            sheetName = 'Learning'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Auditions":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/multimedia_creation.xlsx')
            sheetName = 'Auditions'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        elif sheet == "Admissions":

            log.logger.info("Current working directory:" + str(os.getcwd()))
            base_dir = os.path.dirname(__file__)

            # Define the relative path to the Pricing.xlsx file
            relative_path = os.path.join(base_dir, '../excel/multimedia_creation.xlsx')
            sheetName = 'Admissions'

            # Get the absolute path
            path = os.path.abspath(relative_path)
            print("Absolute path:", path)

            # Check if the file exists
            if os.path.exists(path):
                print("File found!")
                # Proceed with file operations
            else:
                raise FileNotFoundError(f"File not found: {path}")

        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))

        for j in range(2, row + 1):
            for k in range(1, col + 1, 3):
                requestDocument = excel_Data.getCellData(path, sheetName, j, k)
                documentType = excel_Data.getCellData(path, sheetName, j, 2)
                time.sleep(0.5)
                log.logger.info("" + str(requestDocument))
                log.logger.info("" + str(documentType))
                time.sleep(0.5)
                if j <= row:
                    self.do_clear(self.searchMinimumRequirement)
                    time.sleep(0.5)
                    self.do_send_key(self.searchMinimumRequirement, requestDocument)
                    time.sleep(0.5)
                    self.de_click(self.searchMinimumRequirement)
                    time.sleep(0.5)
                    self.de_click(self.optionOfMinimumRequirements)
                    time.sleep(1)
                else:
                    break

        self.de_click(self.nextMultimediaButton)
        time.sleep(3)

    def addUser(self):
        self.de_click(self.searchMinimumRequirement)
        time.sleep(1)
        totalUser = len(self.driver.find_elements(By.XPATH,
                                                  "//div[@class='relative w-full md:w-[350px] overflow-visible']/div/div[2]"))

        for i in range(totalUser):
            self.de_click(self.searchMinimumRequirement)
            time.sleep(0.5)
            self.de_click(self.optionOfMinimumRequirements)
            time.sleep(1)

        self.de_click(self.nextUserButton)
        time.sleep(3)

    def add_Applicant(self):

        log.logger.info("Current working directory:" + str(os.getcwd()))
        base_dir = os.path.dirname(__file__)

        # Define the relative path to the Pricing.xlsx file
        relative_path = os.path.join(base_dir, '../excel/Applicant_List.xlsx')
        sheetName = 'Applicant'

        # Get the absolute path
        path = os.path.abspath(relative_path)
        print("Absolute path:", path)

        # Check if the file exists
        if os.path.exists(path):
            print("File found!")
            # Proceed with file operations
        else:
            raise FileNotFoundError(f"File not found: {path}")

        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))

        for j in range(2, row + 1):
            for k in range(1, col + 1, 5):
                name = excel_Data.getCellData(path, sheetName, j, 1)
                LastName = excel_Data.getCellData(path, sheetName, j, 2)
                contact = excel_Data.getCellData(path, sheetName, j, 3)
                email = excel_Data.getCellData(path, sheetName, j, 4)
                log.logger.info("" + str(name))
                log.logger.info("" + str(LastName))
                log.logger.info("" + str(contact))
                log.logger.info("" + str(email))
                time.sleep(0.5)
                self.de_click(self.addApplicantButton)
                time.sleep(1)
                self.do_send_key(self.Name, name)
                time.sleep(0.5)
                self.do_send_key(self.lastName, LastName)
                time.sleep(0.5)
                self.do_send_key(self.Contact, contact)
                time.sleep(0.5)
                self.do_send_key(self.Email, email)
                time.sleep(0.5)
                self.de_click(self.templateDD)
                time.sleep(0.5)
                self.de_click(self.optionOfTemplateDD)
                time.sleep(0.5)
                self.de_click(self.saveApplicantButton)
                time.sleep(1)

        self.de_click(self.nextButtonApplicant)
        time.sleep(3)

    def save_Interview(self):
        button = self.driver.find_element(By.XPATH, "//div[@class='w-full flex flex-row justify-end my-[32px]']/button")
        self.de_scroll_into_view(button)
        time.sleep(0.5)
        self.de_click(self.saveInterView)
        time.sleep(0.5)
        self.de_click(self.addInterview)
        time.sleep(15)
        title = self.get_element_text(self.generatedInterview)
        log.logger.info("Interview Generated With Title" + str(title))
        time.sleep(4)
        self.de_click(self.interviewBuilderIcon)
        time.sleep(4)
