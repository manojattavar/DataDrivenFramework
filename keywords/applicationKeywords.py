import time

import conftest
from testResources import Constants

class applicationKeywords:
    def __init__(self):
        self.prop = conftest.prop

    def doLogin(self, argVals):
        self.openBrowser(argVals[Constants.BROWSERNAME])
        self.navigate('URL')
        self.validateTitle(self.prop['expectedTitle'])
        self.wait()
        self.click('signin_xpath')
        self.wait()
        self.type('email_id', self.prop['Username'])
        self.wait()
        self.click('nextbutton_xpath')
        self.wait()
        self.type('password_id', self.prop['Password'])
        self.wait()
        self.click('nextbutton_xpath')
        self.wait()