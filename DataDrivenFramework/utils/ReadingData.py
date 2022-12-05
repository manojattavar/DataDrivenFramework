from DataDrivenFramework.testResources import constants
from DataDrivenFramework.utils.XLSReader import xlsReader


def getCellData(testCaseName, xlspath):
    testCaseStartRowIndex = 0

    xls = xlsReader(xlspath)

    while not (xls.getCellDataByIndex(constants.DATASHEET, testCaseStartRowIndex, 0) == testCaseName):
        testCaseStartRowIndex += 1

    testCaseColRowStartIndex = testCaseStartRowIndex + 1
    dataValRowStartIndex = testCaseStartRowIndex + 2

    maxRows = 0
    try:
        while not (xls.checkEmptyCell(constants.DATASHEET, dataValRowStartIndex + maxRows, 0)):
            maxRows += 1
    except Exception as e:
        print(e)

    maxColumns = 0
    try:
        while not (xls.checkEmptyCell(constants.DATASHEET, testCaseColRowStartIndex, maxColumns)):
            maxColumns += 1
    except Exception as e:
        print(e)

    dataList = []
    for rNum in range(dataValRowStartIndex, dataValRowStartIndex+maxRows):
        dataDict = {}
        for cNum in range(0, maxColumns):
            dataKey = xls.getCellDataByIndex(constants.DATASHEET, testCaseColRowStartIndex, cNum)
            dataValue = xls.getCellDataByIndex(constants.DATASHEET, rNum, cNum)
            dataDict[dataKey] = dataValue
        dataList.append(dataDict)
    return dataList

def isTestRunnable(testCaseName, xlspath):
    xls = xlsReader(xlspath)

    for rNum in range(0, xls.getRowCount(constants.TESTCASES)):
        testName = xls.getCellDataByColName(constants.TESTCASES, rNum, constants.TCID_COL)
        if (testName == testCaseName):
            runMode = xls.getCellDataByColName(constants.TESTCASES, rNum, constants.RUNMODE_COL)
            if (runMode == constants.Y):
                return True
            else:
                return False

isTestRunnable('LoginTest', constants.TEST_CASE_FILE_PATH)