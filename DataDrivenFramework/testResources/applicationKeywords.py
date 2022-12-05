from DataDrivenFramework.testResources import constants
from DataDrivenFramework.utils import conftest


class applicationkeywords:
    def __init__(self):
        self.prop = conftest.prop

    def doLogin(self, argVals):
        self.openbrowser(argVals[constants.BROWSERNAME])
        self.navigate('URL')
        self.validateTitle(self.prop['expectedTitle'])
        self.click('signin_xpath')
        self.type('email_id', self.prop['Username'])
        self.click('nextbutton_xpath')
        self.type('password_id', self.prop['Password'])
        self.click('nextbutton_xpath')