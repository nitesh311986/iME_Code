import os
import time
import logging
from selenium.webdriver.common.by import By
from iMEWebsite.pageObjects.BasePage import BasePage
from iMEWebsite.Utilities.customLogger import Logger
from iMEWebsite.Utilities.excelReader import excel_Data

log = Logger(__name__, logging.INFO)


class PricingPage(BasePage):
    UK = (By.XPATH, "//div[@class='framer-1kev92k']/div/div[1]/div/div[1]/div/div/p")
    SA = (By.XPATH, "//div[@class='framer-1kev92k']/div/div[1]/div/div[2]/div/div/p")
    UAE = (By.XPATH, "//div[@class='framer-1kev92k']/div/div[1]/div/div[3]/div/div/p")
    Silver = (By.XPATH, "//div[@class='framer-129ouxm']/div[1]/h3")
    dSilver = (By.XPATH, "//div[@class='framer-1vvz6o2']/div[1]")
    Gold = (By.XPATH, "//div[@class='framer-iaovrk']/h3")
    dGold = (By.XPATH, "//div[@class='framer-18mdhjb']/div[1]")
    Platinum = (By.XPATH, "//div[@class='framer-19cs2dh']/h3")
    dPlatinum = (By.XPATH, "//div[@class='framer-1ni84sq']/div[1]")
    Dimond = (By.XPATH, "//div[@class='framer-93561r']/h3")
    dDimond = (By.XPATH, "//div[@class='framer-skzti0']/div[1]")

    def __init__(self, driver,environment):
        self.environment = environment
        super().__int__(driver)

    def verify_pricing_of_countries(self):
        global Plan, Price
        log.logger.info("****==Verify Functions Of iME Pricing Page Functions==***")
        time.sleep(4)
        iMeIcon = self.driver.find_element(By.XPATH, "//div[@class='framer-1id1vs8']/div[1]/div[1]/div/div[1]/p")
        self.moveToElement(iMeIcon)
        time.sleep(2)
        # log.logger.info("User Clicks On About Us Link")
        # about = self.driver.find_element(By.XPATH, "//div[@role='dialog' and @class='framer-1nhn8ey']/div/div/div[1]/p/a")
        # self.de_action_method(about)
        # time.sleep(1)
        # self.driver.back()
        # iMeIcon = self.driver.find_element(By.XPATH, "//div[@class='framer-1id1vs8']/div[1]/div[1]/div/div[1]/p")
        # self.moveToElement(iMeIcon)
        # time.sleep(1)
        log.logger.info("User Clicks On iME Pricing Link")
        price = self.driver.find_element(By.XPATH,
                                         "//div[@role='dialog' and @class='framer-1nhn8ey']/div/div/div[4]/p/a")
        self.de_action_method(price)
        time.sleep(2)
        priceUrl = self.driver.current_url
        log.logger.info("User will redirect to page with url == " + str(priceUrl))
        # assert priceUrl == "https://reservation-sack-316416.framer.app/pricing"
        if self.environment == "stage":
            assert priceUrl == "https://reservation-sack-316416.framer.app/pricing"
        elif self.environment == "UTA":
            assert priceUrl == "https://i-me.tech/pricing"  # Adjust this URL as necessary
        time.sleep(2)

        # Pricing For UK
        self.de_click(self.UK)
        time.sleep(1)
        silverUK = self.get_element_text(self.Silver)
        amount1UK = self.get_element_text(self.dSilver)

        goldUK = self.get_element_text(self.Gold)
        amount2UK = self.get_element_text(self.dGold)

        platinumUK = self.get_element_text(self.Platinum)
        amount3UK = self.get_element_text(self.dPlatinum)

        dimondUK = self.get_element_text(self.Dimond)
        amount4UK = self.get_element_text(self.dDimond)

        time.sleep(2)
        log.logger.info("Current working directory:" + str(os.getcwd()))
        base_dir = os.path.dirname(__file__)

        # Define the relative path to the Pricing.xlsx file
        relative_path = os.path.join(base_dir, '../excel/Pricing.xlsx')

        # Get the absolute path
        path = os.path.abspath(relative_path)
        print("Absolute path:", path)

        # Check if the file exists
        if os.path.exists(path):
            print("File found!")
            # Proceed with file operations
        else:
            raise FileNotFoundError(f"File not found: {path}")
        sheetName = 'UK'
        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))

        for j in range(2, row + 1):
            for k in range(1, col + 1, 3):
                Plan = excel_Data.getCellData(path, sheetName, j, 1)
                Price = excel_Data.getCellData(path, sheetName, j, 2)
                if Plan == silverUK and Price == amount1UK:
                    log.logger.info("Plans is " + str(silverUK) + " And Price Is == " + str(amount1UK))
                elif Plan == goldUK and Price == amount2UK:
                    log.logger.info("Plans is " + str(goldUK) + " And Price Is == " + str(amount2UK))
                elif Plan == platinumUK and Price == amount3UK:
                    log.logger.info("Plans is " + str(platinumUK) + " And Price Is == " + str(amount3UK))
                elif Plan == dimondUK and Price == amount4UK:
                    log.logger.info("Plans is " + str(dimondUK) + " And Price Is == " + str(amount4UK))
                else:
                    assert False

        # Pricing For SA
        self.de_click(self.SA)
        time.sleep(1)
        silverSA = self.get_element_text(self.Silver)
        amount1SA = self.get_element_text(self.dSilver)

        goldSA = self.get_element_text(self.Gold)
        amount2SA = self.get_element_text(self.dGold)

        PlatinumSA = self.get_element_text(self.Platinum)
        amount3SA = self.get_element_text(self.dPlatinum)

        DimondSA = self.get_element_text(self.Dimond)
        amount4SA = self.get_element_text(self.dDimond)

        time.sleep(2)

        base_dir = os.path.dirname(__file__)

        # Define the relative path to the Pricing.xlsx file
        relative_path = os.path.join(base_dir, '../excel/Pricing.xlsx')

        # Get the absolute path
        path = os.path.abspath(relative_path)
        print("Absolute path:", path)

        # Check if the file exists
        if os.path.exists(path):
            print("File found!")
            # Proceed with file operations
        else:
            raise FileNotFoundError(f"File not found: {path}")
        sheetName = 'SA'
        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))

        for j in range(2, row + 1):
            for k in range(1, col + 1, 3):
                Plan = excel_Data.getCellData(path, sheetName, j, 1)
                Price = excel_Data.getCellData(path, sheetName, j, 2)
                if Plan == silverSA and Price == amount1SA:
                    log.logger.info("Plans is " + str(silverSA) + " And Price Is == " + str(amount1SA))
                elif Plan == goldSA and Price == amount2SA:
                    log.logger.info("Plans is " + str(goldSA) + " And Price Is == " + str(amount2SA))
                elif Plan == PlatinumSA and Price == amount3SA:
                    log.logger.info("Plans is " + str(PlatinumSA) + " And Price Is == " + str(amount3SA))
                elif Plan == DimondSA and Price == amount4SA:
                    log.logger.info("Plans is " + str(DimondSA) + " And Price Is == " + str(amount4SA))
                else:
                    assert False

        # Pricing For UAE
        self.de_click(self.UAE)
        time.sleep(1)
        silverUAE = self.get_element_text(self.Silver)
        amount1UAE = self.get_element_text(self.dSilver)

        goldUAE = self.get_element_text(self.Gold)
        amount2UAE = self.get_element_text(self.dGold)

        PlatinumUAE = self.get_element_text(self.Platinum)
        amount3UAE = self.get_element_text(self.dPlatinum)

        DimondUAE = self.get_element_text(self.Dimond)
        amount4UAE = self.get_element_text(self.dDimond)

        time.sleep(2)

        base_dir = os.path.dirname(__file__)

        # Define the relative path to the Pricing.xlsx file
        relative_path = os.path.join(base_dir, '../excel/Pricing.xlsx')

        # Get the absolute path
        path = os.path.abspath(relative_path)
        print("Absolute path:", path)

        # Check if the file exists
        if os.path.exists(path):
            print("File found!")
            # Proceed with file operations
        else:
            raise FileNotFoundError(f"File not found: {path}")
        sheetName = 'UAE'
        row = excel_Data.getRowCount(path, sheetName)
        log.logger.info("" + str(row))
        col = excel_Data.getColCount(path, sheetName)
        log.logger.info("" + str(col))

        for j in range(2, row + 1):
            for k in range(1, col + 1, 3):
                Plan = excel_Data.getCellData(path, sheetName, j, 1)
                Price = excel_Data.getCellData(path, sheetName, j, 2)
                if Plan == silverUAE and Price == amount1UAE:
                    log.logger.info("Plans is " + str(silverUAE) + " And Price Is == " + str(amount1UAE))
                elif Plan == goldUAE and Price == amount2UAE:
                    log.logger.info("Plans is " + str(goldUAE) + " And Price Is == " + str(amount2UAE))
                elif Plan == PlatinumUAE and Price == amount3UAE:
                    log.logger.info("Plans is " + str(PlatinumUAE) + " And Price Is == " + str(amount3UAE))
                elif Plan == DimondUAE and Price == amount4UAE:
                    log.logger.info("Plans is " + str(DimondUAE) + " And Price Is == " + str(amount4UAE))
                else:
                    assert False
