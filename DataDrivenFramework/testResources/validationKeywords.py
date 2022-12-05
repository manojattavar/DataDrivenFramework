import _datetime as dt
from _datetime import datetime
import logging

import allure
from allure_commons.types import AttachmentType

from DataDrivenFramework.utils import conftest


class validationkeywords:

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
        if (expectedTitle == actualTitle):
            self.reportSuccess("Title matched...")
        else:
            self.reportFailure("Title does not match. actual title is " + actualTitle + " and expected is " + expectedTitle)


    def validateLogin(self, locatorKey, expectedResult):

        element = self.getElement(locatorKey)
        if (element.is_displayed() and expectedResult == 'Success'):
            self.reportSuccess("login successfull...")
        else:
            self.reportFailure("login has failed...")