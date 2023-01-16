from _datetime import datetime
import logging

import allure
from allure_commons.types import AttachmentType

import conftest


class validationKeywords:

    def __init__(self):
        self.prop = conftest.prop

    def logging(self, message):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info(message)

    def takeScreenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "Screenshot at : " + str(datetime.now()),AttachmentType.PNG)

    def reportSuccess(self, message):
        self.logging(message)
        assert True, message

    def reportFailure(self, message):
        self.logging(message)
        self.takeScreenshot()
        assert False, message

    def validateTitle(self, expectedTitle):
        actualTitle = self.driver.title
        if (actualTitle == expectedTitle):
            self.reportSuccess("Title matched...")
        else:
            self.reportFailure("Title not matched.. expected title is -- " + expectedTitle +
                               " and actual title is -- " + actualTitle)


    def validateLogin(self, locatorKey, expectedResult):
        element = self.getElement(locatorKey)
        if (element.is_displayed() and expectedResult == 'Success'):
            self.reportSuccess("login success")
        else:
            self.reportFailure("login failure")