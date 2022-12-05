import time

import pytest

from DataDrivenFramework.testResources import constants
from DataDrivenFramework.utils import ReadingData, conftest
from DataDrivenFramework.utils.conftest import base_fixture


@pytest.mark.run(order=1)
@pytest.mark.parametrize('argVals', ReadingData.getCellData('CreateLead', constants.TEST_CASE_FILE_PATH))
def test_createLead(argVals, base_fixture):
    testRunMode = ReadingData.isTestRunnable('CreateLead', constants.TEST_CASE_FILE_PATH)
    dataRunMode = argVals[constants.RUNMODE_COL]

    if (testRunMode):
        if (dataRunMode == constants.Y):
            base_fixture['gen'].doLogin(argVals)
            time.sleep(2)
            base_fixture['gen'].validateLogin('CRMLinkBtn_xpath', argVals[constants.EXPECTED_RESULT])
            base_fixture['gen'].wait()
            base_fixture['gen'].click('CRMLinkBtn_xpath')
            base_fixture['gen'].click('LeadsHomePageBtn_xpath')
            base_fixture['gen'].click('createLeadBtn_xpath')
            base_fixture['gen'].type('companyName_xpath', argVals[constants.COMPANYNAME])
            base_fixture['gen'].wait()
            base_fixture['gen'].type('firstName_xpath', argVals[constants.FIRSTNAME])
            base_fixture['gen'].wait()
            base_fixture['gen'].type('lastName_xpath', argVals[constants.LASTNAME])
            base_fixture['gen'].wait()
            base_fixture['gen'].click('saveBtn_id')
            base_fixture['gen'].wait()
            base_fixture['gen'].click('saveBackArrowBtn_id')
            base_fixture['gen'].wait()
            base_fixture['gen'].refresh()
            base_fixture['gen'].wait()
            base_fixture['gen'].click('LeadsHomePageBtn_xpath')
            time.sleep(2)
            rowNum = base_fixture['gen'].getRowNumberByName('nameList_xpath', argVals[constants.FIRSTNAME] + ' ' + argVals[constants.LASTNAME])

            if (rowNum == -1):
                 base_fixture['gen'].reportFailure("Lead ID " + argVals[constants.FIRSTNAME] + ' ' + argVals[constants.LASTNAME] + " not present...")
            else:
                base_fixture['gen'].reportSuccess("Lead ID " + argVals[constants.FIRSTNAME] + ' ' + argVals[constants.LASTNAME] + " is present at the row number " + str(rowNum))


        else:
            pytest.skip("Test case has been skipped...")
    else:
        pytest.skip("Test case has been skipped...")


@pytest.mark.run(order=2)
@pytest.mark.parametrize('argVals', ReadingData.getCellData('ConvertLead', constants.TEST_CASE_FILE_PATH))
def test_convertLead(argVals, base_fixture):
    testRunMode = ReadingData.isTestRunnable('ConvertLead', constants.TEST_CASE_FILE_PATH)
    dataRunMode = argVals[constants.RUNMODE_COL]

    if (testRunMode):
        if (dataRunMode == constants.Y):
            base_fixture['gen'].doLogin(argVals)
            time.sleep(2)
            base_fixture['gen'].validateLogin('CRMLinkBtn_xpath', argVals[constants.EXPECTED_RESULT])
            base_fixture['gen'].wait()
            base_fixture['gen'].click('CRMLinkBtn_xpath')
            base_fixture['gen'].click('LeadsHomePageBtn_xpath')
            base_fixture['gen'].wait()

            rowNum = base_fixture['gen'].getRowNumberByName('nameList_xpath',argVals[constants.LEADNAME])
            base_fixture['gen'].wait()

            if (rowNum == -1):
                base_fixture['gen'].reportFailure("Lead ID " + argVals[constants.LEADNAME] + " not present...")
            else:
                base_fixture['gen'].clickElementByRowNum(rowNum, 'namePart1_xpath', 'namePart2_xpath')
                base_fixture['gen'].wait()
                base_fixture['gen'].click('convertBtn_name')
                base_fixture['gen'].click('convertBtnConfirmation_id')
                base_fixture['gen'].click('goToLeadsButton_id')
                base_fixture['gen'].wait()
                base_fixture['gen'].refresh()
                base_fixture['gen'].wait()

                rowNum = base_fixture['gen'].getRowNumberByName('nameList_xpath', argVals[constants.LEADNAME])
                if (rowNum == -1):
                    base_fixture['gen'].reportSuccess("Lead ID " + argVals[constants.LEADNAME] + " not present...")
                else:
                    base_fixture['gen'].reportFailure("Lead ID " + argVals[constants.LEADNAME] + " is present at the row number " + str(rowNum))

        else:
            pytest.skip("Test case has been skipped...")
    else:
        pytest.skip("Test case has been skipped...")


@pytest.mark.run(order=3)
@pytest.mark.parametrize('argVals', ReadingData.getCellData('DeleteLead', constants.TEST_CASE_FILE_PATH))
def test_deleteLead(argVals, base_fixture):
    testRunMode = ReadingData.isTestRunnable('DeleteLead', constants.TEST_CASE_FILE_PATH)
    dataRunMode = argVals[constants.RUNMODE_COL]

    if (testRunMode):
        if (dataRunMode == constants.Y):
            base_fixture['gen'].doLogin(argVals)
            time.sleep(2)
            base_fixture['gen'].validateLogin('CRMLinkBtn_xpath', argVals[constants.EXPECTED_RESULT])
            base_fixture['gen'].wait()
            base_fixture['gen'].click('CRMLinkBtn_xpath')
            base_fixture['gen'].click('LeadsHomePageBtn_xpath')
            base_fixture['gen'].wait()

            rowNum = base_fixture['gen'].getRowNumberByName('nameList_xpath',argVals[constants.LEADNAME])
            base_fixture['gen'].wait()

            if (rowNum == -1):
                base_fixture['gen'].reportFailure("Lead ID " + argVals[constants.LEADNAME] + " not present...")
            else:
                base_fixture['gen'].clickElementByRowNum(rowNum, 'namePart1_xpath', 'namePart2_xpath')
                base_fixture['gen'].wait()
                base_fixture['gen'].click('deleteHomePageBtn_id')
                base_fixture['gen'].click('deleteActualBtn_xpath')
                base_fixture['gen'].click('deleteAlertButton_xpath')
                base_fixture['gen'].wait()
                base_fixture['gen'].refresh()
                base_fixture['gen'].wait()

                rowNum = base_fixture['gen'].getRowNumberByName('nameList_xpath', argVals[constants.LEADNAME])
                if (rowNum == -1):
                    base_fixture['gen'].reportSuccess("Lead ID " + argVals[constants.LEADNAME] + " not present...")
                else:
                    base_fixture['gen'].reportFailure("Lead ID " + argVals[constants.LEADNAME] + " is present at the row number " + str(rowNum))

        else:
            pytest.skip("Test case has been skipped...")
    else:
        pytest.skip("Test case has been skipped...")