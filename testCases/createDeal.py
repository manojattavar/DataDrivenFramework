import time

import pytest

from conftest import gList
from testResources import Constants
from utils import ReadingData


@pytest.mark.parametrize('argVals', ReadingData.getCellData('CreateDeal', Constants.TEST_CASE_FILE_PATH))
def testCreateDeal(argVals):
    testCaseRunMode = ReadingData.isTestRunnable('CreateDeal', Constants.TEST_CASE_FILE_PATH)
    dataRunMode = argVals['RunMode']

    if (testCaseRunMode):
        if (dataRunMode == Constants.Y):
            for i in range(0, len(gList)):
                pass

            gList[i].doLogin(argVals)
            gList[i].validateLogin('CRMLinkBtn_xpath', argVals[Constants.EXPECTED_RESULT])
            gList[i].click('CRMLinkBtn_xpath')
            gList[i].wait()
            gList[i].click('dealHomePageBtn_xpath')
            gList[i].wait()
            gList[i].click('createDeal_xpath')
            gList[i].wait()
            gList[i].type('dealName_id', argVals[Constants.DEALNAME])
            gList[i].wait()
            gList[i].click('dealAccountNameWindow_xpath')

            rowNum = gList[i].getRowNumberByName('dealAccountNamesList_xpath', argVals[Constants.ACCOUNTNAME])

            if (rowNum != -1):
                gList[i].clickElementByRowNumber(rowNum, 'accuntNamePart1_xpath', 'accuntNamePart2_xpath')
            else:
                gList[i].reportFailure("Deal ID " + argVals[Constants.DEALNAME] + " not found ")

            gList[i].wait()
            gList[i].enterClosingDate(argVals[Constants.CLOSINGDATE])
            gList[i].click('saveBtn_id')
            gList[i].wait()
            gList[i].click('saveBackArrowBtn_id')
            gList[i].wait()

            rowNum = gList[i].getRowNumberByName('dealNameList_xpath', argVals[Constants.DEALNAME])

            if (rowNum != -1):
                gList[i].reportSuccess("Deal ID " + argVals[Constants.DEALNAME] +
                                       " found and the row number is  " + str(i))
            else:
                gList[i].reportFailure("Deal ID " + argVals[Constants.DEALNAME] +
                                       " not found ")


        else:
            pytest.skip("Test Case is skipped")
    else:
        pytest.skip("Test Case is skipped")