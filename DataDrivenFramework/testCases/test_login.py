import time

import pytest

from DataDrivenFramework.testResources import constants
from DataDrivenFramework.utils import ReadingData, conftest
from DataDrivenFramework.utils.conftest import base_fixture


@pytest.mark.parametrize('argVals', ReadingData.getCellData('LoginTest', constants.TEST_CASE_FILE_PATH))
def test_login(argVals, base_fixture):
    testRunMode = ReadingData.isTestRunnable('LoginTest', constants.TEST_CASE_FILE_PATH)
    dataRunMode = argVals[constants.RUNMODE_COL]

    if (testRunMode):
        if (dataRunMode == constants.Y):
            base_fixture['gen'].doLogin(argVals)
            # time.sleep(2)
            # base_fixture['gen'].validateLogin('CRMLinkBtn_xpath', argVals[constants.EXPECTED_RESULT])

        else:
            pytest.skip("Test case has been skipped...")
    else:
        pytest.skip("Test case has been skipped...")