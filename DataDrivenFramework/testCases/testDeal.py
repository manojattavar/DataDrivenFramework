import time

import pytest

from DataDrivenFramework.testResources import constants
from DataDrivenFramework.utils import ReadingData, conftest
from DataDrivenFramework.utils.conftest import base_fixture


@pytest.mark.run(order=1)
@pytest.mark.parametrize('argVals', ReadingData.getCellData('CreateDeal', constants.TEST_CASE_FILE_PATH))
def test_createDeal(argVals, base_fixture):
    testRunMode = ReadingData.isTestRunnable('CreateDeal', constants.TEST_CASE_FILE_PATH)
    dataRunMode = argVals[constants.RUNMODE_COL]

    if (testRunMode):
        if (dataRunMode == constants.Y):
            base_fixture['gen'].doLogin(argVals)
            # time.sleep(2)
            # base_fixture['gen'].validateLogin('CRMLinkBtn_xpath', argVals[constants.EXPECTED_RESULT])
            base_fixture['gen'].wait()
            base_fixture['gen'].click('CRMLinkBtn_xpath')
            base_fixture['gen'].click('dealHomePageBtn_xpath')
            base_fixture['gen'].click('createDeal_xpath')
            base_fixture['gen'].type('dealName_id', argVals[constants.DEALNAME])
            base_fixture['gen'].wait()
            base_fixture['gen'].click('dealAccountNameWindow_xpath')
            base_fixture['gen'].wait()
            rowNum = base_fixture['gen'].getRowNumberByName('dealAccountNamesList_xpath', argVals[constants.ACCOUNTNAME])

            base_fixture['gen'].clickElementByRowNum(rowNum, 'accuntNamePart1_xpath', 'accuntNamePart2_xpath')
            base_fixture['gen'].wait()
            base_fixture['gen'].enterClosingDate(argVals[constants.CLOSINGDATE])
            base_fixture['gen'].wait()

            base_fixture['gen'].click('saveBtn_id')
            base_fixture['gen'].click('saveBackArrowBtn_id')
            base_fixture['gen'].wait()

            rowNum = base_fixture['gen'].getRowNumberByName('dealNameList_xpath', argVals[constants.DEALNAME])

            if (rowNum == -1):
                 base_fixture['gen'].reportFailure("Deal ID " + argVals[constants.DEALNAME] + " not present...")
            else:
                base_fixture['gen'].reportSuccess("Deal ID " + argVals[constants.DEALNAME] + " is present at the row number " + str(rowNum))


        else:
            pytest.skip("Test case has been skipped...")
    else:
        pytest.skip("Test case has been skipped...")


@pytest.mark.run(order=2)
@pytest.mark.parametrize('argVals', ReadingData.getCellData('DeleteDeal', constants.TEST_CASE_FILE_PATH))
def test_deleteDeal(argVals, base_fixture):
    testRunMode = ReadingData.isTestRunnable('DeleteDeal', constants.TEST_CASE_FILE_PATH)
    dataRunMode = argVals[constants.RUNMODE_COL]

    if (testRunMode):
        if (dataRunMode == constants.Y):
            base_fixture['gen'].doLogin(argVals)
            # base_fixture['gen'].validateLogin('CRMLinkBtn_xpath', argVals[constants.EXPECTED_RESULT])
            base_fixture['gen'].wait()
            base_fixture['gen'].click('CRMLinkBtn_xpath')
            base_fixture['gen'].click('dealHomePageBtn_xpath')
            base_fixture['gen'].wait()

            rowNum = base_fixture['gen'].getRowNumberByName('dealNameList_xpath',argVals[constants.DEALNAME])
            base_fixture['gen'].wait()

            if (rowNum == -1):
                base_fixture['gen'].reportFailure("Deal ID " + argVals[constants.DEALNAME] + " not present...")
            else:
                base_fixture['gen'].clickElementByRowNum(rowNum, 'dealButtonXpath1_xpath', 'dealButtonXpath2_xpath')
                base_fixture['gen'].wait()
                base_fixture['gen'].click('deleteHomePageBtn_id')
                base_fixture['gen'].click('deleteActualBtn_xpath')
                base_fixture['gen'].click('deleteAlertButton_xpath')
                base_fixture['gen'].wait()
                base_fixture['gen'].refresh()
                base_fixture['gen'].wait()

                rowNum = base_fixture['gen'].getRowNumberByName('dealNameList_xpath', argVals[constants.DEALNAME])
                if (rowNum == -1):
                    base_fixture['gen'].reportSuccess("Deal ID " + argVals[constants.DEALNAME] + " not present...")
                else:
                    base_fixture['gen'].reportFailure("Deal ID " + argVals[constants.DEALNAME] + " is present at the row number " + str(rowNum))

        else:
            pytest.skip("Test case has been skipped...")
    else:
        pytest.skip("Test case has been skipped...")