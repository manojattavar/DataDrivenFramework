import time
import _datetime as dt

import allure
from _overlapped import NULL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from DataDrivenFramework.testResources import constants
from DataDrivenFramework.testResources.applicationKeywords import applicationkeywords
from DataDrivenFramework.testResources.validationKeywords import validationkeywords
from DataDrivenFramework.utils import conftest


class genkeywords(validationkeywords, applicationkeywords):

    def __init__(self):
        self.prop = conftest.prop
        # self.driver = NULL

    def getBrowserOptions(self, browserName):
        if (browserName == constants.CHROME):
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            options.add_argument("--disable-notifications")
            return options
        elif (browserName == constants.FIREFOX):
            options = Options()
            options.set_preference("dom.webnotifications.enabled", True)
            return options

    def openbrowser(self, browserName):
        if (browserName == constants.CHROME):
            options = self.getBrowserOptions(browserName)
            self.driver = webdriver.Chrome(options=options)
        elif (browserName == constants.FIREFOX):
            options = self.getBrowserOptions(browserName)
            self.driver = webdriver.Firefox(options=options)

    def navigate(self, url):
        with allure.step("Navigating..."):
            URL = self.prop[url]
            self.driver.get(URL)
            self.driver.maximize_window()

    def click(self, locatorKey):
        with allure.step("Clicking an element..."):
            element = self.getElement(locatorKey)
            element.click()

    def type(self, locatorKey, data):
        with allure.step("Typing..."):
            element = self.getElement(locatorKey)
            element.send_keys(data)


    def wait(self):
        time.sleep(1)

    def refresh(self):
        self.driver.refresh()


    def getRowNumberByName(self, locatorKey, userName):
        obj = self.prop[locatorKey]

        if (self.isElementPresent(locatorKey) and self.isElementVisible(locatorKey)):

            if (locatorKey.endswith('xpath')):
                elements = self.driver.find_elements(By.XPATH, obj)
            elif (locatorKey.endswith('id')):
                elements = self.driver.find_elements(By.ID, obj)
            elif (locatorKey.endswith('name')):
                elements = self.driver.find_elements(By.NAME, obj)
            else:
                elements = self.driver.find_elements(By.CSS_SELECTOR, obj)

            for index in range(0, len(elements)):
                if (elements[index].text == userName):
                    return index+1
            return -1

    def clickElementByRowNum(self, rowNum, locatorKey1, locatorKey2):
        obj1 = self.prop[locatorKey1]
        obj2 = self.prop[locatorKey2]

        if (locatorKey1.endswith('xpath')):
            element = self.driver.find_element(By.XPATH, obj1 + str(rowNum) + obj2)
        elif (locatorKey1.endswith('id')):
            element = self.driver.find_element(By.ID, obj1 + str(rowNum) + obj2)
        elif (locatorKey1.endswith('name')):
            element = self.driver.find_element(By.NAME, obj1 + str(rowNum) + obj2)
        else:
            element = self.driver.find_element(By.CSS_SELECTOR, obj1 + str(rowNum) + obj2)

        element.click()


    def Quit(self):
        try:
            if (self.driver != '' or self.driver != NULL):
                self.driver.quit()
        except Exception as e:
            print("Session not found...")

    def WaitForPageToBeLoaded(self):
        i = 1
        while (i != 10):
            load_status = self.driver.execute_script("return document.readyState")
            if (load_status == 'complete'):
                break
            else:
                time.sleep(2)
                i += 1


    def isElementPresent(self, locatorKey):
        obj = self.prop[locatorKey]

        self.WaitForPageToBeLoaded()

        wait = WebDriverWait(self.driver, 20)

        if (locatorKey.endswith('xpath')):
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, obj)))
        elif (locatorKey.endswith('id')):
            elements = wait.until(EC.presence_of_all_elements_located((By.ID, obj)))
        elif (locatorKey.endswith('name')):
            elements = wait.until(EC.presence_of_all_elements_located((By.NAME, obj)))
        else:
            elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, obj)))

        if (len(elements) != 0):
            return True
        else:
            return False

    def isElementVisible(self, locatorKey):
        obj = self.prop[locatorKey]

        self.WaitForPageToBeLoaded()

        wait = WebDriverWait(self.driver, 20)

        if (locatorKey.endswith('xpath')):
            elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, obj)))
        elif (locatorKey.endswith('id')):
            elements = wait.until(EC.visibility_of_all_elements_located((By.ID, obj)))
        elif (locatorKey.endswith('name')):
            elements = wait.until(EC.visibility_of_all_elements_located((By.NAME, obj)))
        else:
            elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, obj)))

        if (len(elements) != 0):
            return True
        else:
            return False

    def getElement(self, locatorKey):

        obj = self.prop[locatorKey]
        if (self.isElementPresent(locatorKey) and self.isElementVisible(locatorKey)):

            if (locatorKey.endswith('xpath')):
                element = self.driver.find_element(By.XPATH, obj)
            elif (locatorKey.endswith('id')):
                element = self.driver.find_element(By.ID, obj)
            elif (locatorKey.endswith('name')):
                element = self.driver.find_element(By.NAME, obj)
            else:
                element = self.driver.find_element(By.CSS_SELECTOR, obj)

            if (element != NULL):
                return element
            else:
                print("Element not found...")

    def enterClosingDate(self, closingDate):
        closingDate = '04-12-2022'
        formatted = dt.datetime.strptime(closingDate, '%d-%m-%Y')
        year = formatted.year
        month = formatted.month
        day = formatted.day

        formatted_month = formatted.strftime('%b')

        desiredDateMonthYear = str(formatted_month) + ' ' + str(day) + ', ' + str(year)
        desiredMonthYear = str(formatted.strftime('%B')) + ' ' + str(year)

        element = self.driver.find_element(By.XPATH, "//*[@id='Crm_Potentials_CLOSINGDATE_LInput']")
        time.sleep(1)
        element.send_keys(desiredDateMonthYear)
        time.sleep(1)

        month = self.driver.find_element(By.CSS_SELECTOR, "#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalMonthDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
        time.sleep(1)
        year = self.driver.find_element(By.CSS_SELECTOR, "#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalYearDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
        time.sleep(1)

        displayedMonthYear = str(month) + ' ' + str(year)

        while True:
            if (desiredMonthYear > displayedMonthYear):
                self.driver.find_element(By.XPATH,"//*[@id='lyteCalendar']/lyte-calendar/div/div/div[1]/div/span[1]").click()
                time.sleep(1)
                modifiedMonth = self.driver.find_element(By.CSS_SELECTOR, "#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalMonthDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
                time.sleep(1)
                modifiedyear = self.driver.find_element(By.CSS_SELECTOR,"#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalMonthDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
                time.sleep(1)
                modifiedMonthYear = str(modifiedMonth) + ' ' + str(modifiedyear)

                if (desiredMonthYear == modifiedMonthYear):
                    self.driver.find_element(By.XPATH, "//*[@id='Lyte_Calendar_Day_404']").click()
                    break

            elif (desiredMonthYear < displayedMonthYear):
                self.driver.find_element(By.XPATH, "//*[@id='lyteCalendar']/lyte-calendar/div/div/div[1]/div/span[6]").click()
                time.sleep(1)
                modifiedMonth = self.driver.find_element(By.CSS_SELECTOR, "#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalMonthDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
                time.sleep(1)
                modifiedyear = self.driver.find_element(By.CSS_SELECTOR,"#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalMonthDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
                time.sleep(1)
                modifiedMonthYear = str(modifiedMonth) + ' ' + str(modifiedyear)

                if (desiredMonthYear == modifiedMonthYear):
                    self.driver.find_element(By.XPATH, "//*[@id='Lyte_Calendar_Day_404']").click()
                    break
            else:
                break