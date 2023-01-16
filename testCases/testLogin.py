import pytest

from conftest import gList
from testResources import Constants
from utils import ReadingData


@pytest.mark.parametrize('argVals', ReadingData.getCellData('LoginTest', Constants.TEST_CASE_FILE_PATH))
def testLogin(argVals):
    testCaseRunMode = ReadingData.isTestRunnable('LoginTest', Constants.TEST_CASE_FILE_PATH)
    dataRunMode = argVals['RunMode']

    if (testCaseRunMode):
        if (dataRunMode == Constants.Y):
            for i in range(0, len(gList)):
                pass

            gList[i].doLogin(argVals)
            gList[i].validateLogin('CRMLinkBtn_xpath', argVals[Constants.EXPECTED_RESULT])

        else:
            pytest.skip("Test Case is skipped")
    else:
        pytest.skip("Test Case is skipped")