import allure
import pytest
from pyjavaproperties import Properties

from keywords.genKeywords import genKeywords
from testResources import Constants

prop = Properties()
gList = []

@pytest.yield_fixture(scope='function', autouse=True)
def base_fixture():
    with allure.step("Initialization block..."):
        try:
            configFile = open(Constants.CONFIG_FILE)
            prop.load(configFile)

            gen = genKeywords()
            gList.append(gen)
        except Exception as e:
            print(e)

        yield locals()

    with allure.step("Finishing block..."):
        gen.Quit()