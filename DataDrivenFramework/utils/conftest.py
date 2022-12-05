import time

import allure
import pytest
from _overlapped import NULL
from pyjavaproperties import Properties

from DataDrivenFramework.testResources import constants
from DataDrivenFramework.testResources.genKeywords import genkeywords

prop = Properties()

@pytest.yield_fixture(scope='function', autouse=True)
def base_fixture():
    with allure.step("Initializing block..."):
        try:
            configFile = open(constants.CONFIG_FILE)
            prop.load(configFile)

            gen = genkeywords()
        except FileNotFoundError as e:
            print(e)

    yield locals()
    with allure.step("Closing block..."):
        time.sleep(2)
        gen.Quit()
