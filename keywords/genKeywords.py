import time
import _datetime as dt

import allure
from _overlapped import NULL
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import conftest
from keywords.applicationKeywords import applicationKeywords
from keywords.validationKeywords import validationKeywords
from testResources import Constants


class genKeywords(validationKeywords, applicationKeywords):

    def __init__(self):
        self.prop = conftest.prop

    def browserOptions(self, browserName):
        if (browserName == Constants.CHROME):
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            options.add_argument("--disable-notifications")
            return options

    def openBrowser(self, browserName):
        if (browserName == Constants.CHROME):
            options = self.browserOptions(browserName)
            self.driver = webdriver.Chrome(options=options, executable_path=Constants.EXECUTABLE_DRIVER_CHROME)
            self.driver.maximize_window()

    def navigate(self, url):
        URL = self.prop[url]
        self.driver.get(URL)

    def click(self, locatorKey):
        with allure.step("Clicking an element"):
            element = self.getElement(locatorKey)
            element.click()

    def type(self, locatorKey, data):
        with allure.step("Typing input field"):
            element = self.getElement(locatorKey)
            element.send_keys(data)

    def wait(self):
        time.sleep(1)

    def Quit(self):
        try:
            if (self.driver != '' or self.driver != NULL):
                self.driver.quit()
        except Exception as e:
            print(e)

    def waitForPageToBeLoaded(self):
        i = 0
        while (i < 10):
            status = self.driver.execute_script("return document.readyState")
            if (status == 'complete'):
                break
            else:
                self.wait()
                i += 1

    def isElementPresent(self, locatorKey):
        obj = self.prop[locatorKey]
        self.waitForPageToBeLoaded()

        wait = WebDriverWait(self.driver, 20)

        if (locatorKey.endswith("xpath")):
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, obj)))
        elif (locatorKey.endswith("id")):
            elements = wait.until(EC.presence_of_all_elements_located((By.ID, obj)))
        elif (locatorKey.endswith("name")):
            elements = wait.until(EC.presence_of_all_elements_located((By.NAME, obj)))
        else:
            elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, obj)))

        if (len(elements) != 0):
            return True
        else:
            return False


    def isElementVisible(self, locatorKey):
        obj = self.prop[locatorKey]
        self.waitForPageToBeLoaded()

        wait = WebDriverWait(self.driver, 20)

        if (locatorKey.endswith("xpath")):
            elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, obj)))
        elif (locatorKey.endswith("id")):
            elements = wait.until(EC.visibility_of_all_elements_located((By.ID, obj)))
        elif (locatorKey.endswith("name")):
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
            if (locatorKey.endswith("xpath")):
                element = self.driver.find_element(By.XPATH, obj)
            elif (locatorKey.endswith("id")):
                element = self.driver.find_element(By.ID, obj)
            elif (locatorKey.endswith("name")):
                element = self.driver.find_element(By.NAME, obj)
            else:
                element = self.driver.find_element(By.CSS_SELECTOR, obj)

            if (element != '' or element != NULL):
                return element
            else:
                print("Element not found")


    def getRowNumberByName(self, locatorKey, username):
        if (self.isElementPresent(locatorKey) and self.isElementVisible(locatorKey)):
            obj = self.prop[locatorKey]
            if (locatorKey.endswith("xpath")):
                elements = self.driver.find_elements(By.XPATH, obj)
            elif (locatorKey.endswith("id")):
                elements = self.driver.find_elements(By.ID, obj)
            elif (locatorKey.endswith("name")):
                elements = self.driver.find_elements(By.NAME, obj)
            else:
                elements = self.driver.find_elements(By.CSS_SELECTOR, obj)

            for i in range(0, len(elements)):
                if (elements[i].text == username):
                    return i+1
            return -1

        else:
            print("Element not present or visible")
            self.reportFailure("Element not present or visible")

    def clickElementByRowNumber(self, rowNum, locatorKey1, locatorKey2):
        obj1 = self.prop[locatorKey1]
        obj2 = self.prop[locatorKey2]

        if (locatorKey1.endswith("xpath")):
            element = self.driver.find_element(By.XPATH, obj1 + str(rowNum) + obj2)
        elif (locatorKey1.endswith("id")):
            element = self.driver.find_element(By.ID, obj1 + str(rowNum) + obj2)
        elif (locatorKey1.endswith("name")):
            element = self.driver.find_element(By.NAME, obj1 + str(rowNum) + obj2)
        else:
            element = self.driver.find_element(By.CSS_SELECTOR, obj1 + str(rowNum) + obj2)

        element.click()


    def enterClosingDate(self, closingDate):
        closingDate = '04-01-2023'
        format = dt.datetime.strptime(closingDate, '%d-%m-%Y')

        year = format.year
        month = format.month
        day = format.day

        desiredMonth = format.strftime('%b')
        expectedMonth = format.strftime('%B')

        desiredFormat = str(desiredMonth) + " " + str(day) + ", " + str(year)
        expectedFormat = str(expectedMonth) + " " + str(year)

        element = self.driver.find_element(By.XPATH, "//*[@id='Crm_Potentials_CLOSINGDATE_LInput']")
        element.send_keys(desiredFormat)

        self.wait()

        while True:
            displayedMonth = self.driver.find_element(By.XPATH, "//*[@id='lyteCalendar']/lyte-calendar/div/div/div[1]/div/span[5]/lyte-dropdown[1]/div[1]/lyte-drop-button/span").text
            self.wait()
            displayedYear = self.driver.find_element(By.XPATH, "//*[@id='lyteCalendar']/lyte-calendar/div/div/div[1]/div/span[5]/lyte-dropdown[2]/div[1]/lyte-drop-button/span").text
            self.wait()
            displayedFormat = str(displayedMonth) + " " + str(displayedYear)

            if (expectedFormat > displayedFormat):
                element = self.driver.find_element(By.XPATH,
                                                   "//*[@id='lyteCalendar']/lyte-calendar/div/div/div[1]/div/span[1]")
                element.click()
                self.wait()
                displayedMonth = self.driver.find_element(By.CSS_SELECTOR,
                                                          "#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalMonthDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
                self.wait()
                displayedYear = self.driver.find_element(By.CSS_SELECTOR,
                                                         "#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalYearDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
                self.wait()
                displayedFormat = str(displayedMonth) + " " + str(displayedYear)

                if (expectedFormat == displayedFormat):
                    element = self.driver.find_element(By.XPATH, "//*[@id='Lyte_Calendar_Day_975']/span")
                    element.click()
                    self.wait()
                    break

            elif (expectedFormat < displayedFormat):
                element = self.driver.find_element(By.XPATH,
                                                   "//*[@id='lyteCalendar']/lyte-calendar/div/div/div[1]/div/span[6]")
                element.click()
                self.wait()
                displayedMonth = self.driver.find_element(By.CSS_SELECTOR,
                                                          "#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalMonthDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
                self.wait()
                displayedYear = self.driver.find_element(By.CSS_SELECTOR,
                                                         "#lyteCalendar > lyte-calendar > div > div > div:nth-child(1) > div > span.lyteCalsCalMon > lyte-dropdown.lyteCalYearDD > div.lyteDummyEventContainer > lyte-drop-button > span").text
                self.wait()
                displayedFormat = str(displayedMonth) + " " + str(displayedYear)

                if (expectedFormat == displayedFormat):
                    element = self.driver.find_element(By.XPATH, "//*[@id='Lyte_Calendar_Day_975']/span")
                    element.click()
                    self.wait()
                    break

            else:
                break








