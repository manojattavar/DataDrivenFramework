import time

import pytest

from conftest import gList
from testResources import Constants
from utils import ReadingData


@pytest.mark.parametrize('argVals', ReadingData.getCellData('DeleteDeal', Constants.TEST_CASE_FILE_PATH))
def testDeleteDeal(argVals):
    testCaseRunMode = ReadingData.isTestRunnable('DeleteDeal', Constants.TEST_CASE_FILE_PATH)
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
            time.sleep(2)

            rowNum = gList[i].getRowNumberByName('dealNameList_xpath', argVals[Constants.DEALNAME])
            if (rowNum != -1):
                gList[i].clickElementByRowNumber(rowNum, 'dealButtonXpath1_xpath', 'dealButtonXpath2_xpath')
                gList[i].wait()
                gList[i].click('deleteHomePageBtn_id')
                gList[i].wait()
                gList[i].click('deleteActualBtn_xpath')
                gList[i].wait()
                gList[i].click('deleteAlertButton_xpath')
                time.sleep(2)

                rowNum = gList[i].getRowNumberByName('dealNameList_xpath', argVals[Constants.DEALNAME])
                if (rowNum == -1):
                    gList[i].reportSuccess("Deal ID " + argVals[Constants.DEALNAME] + " not found")
                else:
                    gList[i].reportFailure("Deal ID " + argVals[Constants.DEALNAME] + " found and the row number is  " + str(i))
            else:
                gList[i].reportFailure("Deal ID " + argVals[Constants.DEALNAME] + " not found ")

        else:
            pytest.skip("Test Case is skipped")
    else:
        pytest.skip("Test Case is skipped")