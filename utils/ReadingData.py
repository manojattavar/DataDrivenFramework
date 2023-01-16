from testResources import Constants
from utils.XLSReader import XLSReader


def getCellData(testCaseName, xlspath):
    xls = XLSReader(xlspath)

    testCaseStartRowIndex = 0

    try:
        while not (xls.getCellDataByIndex(Constants.DATASHEET, testCaseStartRowIndex, 0) == testCaseName):
            testCaseStartRowIndex += 1
    except Exception as e:
        print(e)

    testCaseNameStartRowIndex = testCaseStartRowIndex + 1
    testDataValueStartRowIndex = testCaseStartRowIndex + 2

    maxRows = 0
    try:
        while not (xls.checkEmptyCell(Constants.DATASHEET, testDataValueStartRowIndex + maxRows, 0)):
            maxRows += 1
    except Exception as e:
        print(e)


    maxCols = 0
    try:
        while not (xls.checkEmptyCell(Constants.DATASHEET, testCaseNameStartRowIndex, maxCols)):
            maxCols += 1
    except Exception as e:
        print(e)

    dataList = []
    for rowNum in range(testDataValueStartRowIndex, testDataValueStartRowIndex+maxRows):
        dataDict = {}
        for colNum in range(0, maxCols):
            dataKey = xls.getCellDataByIndex(Constants.DATASHEET, testCaseNameStartRowIndex, colNum)
            dataValue = xls.getCellDataByIndex(Constants.DATASHEET, rowNum, colNum)
            dataDict[dataKey] = dataValue
        dataList.append(dataDict)
    return dataList

def isTestRunnable(testCaseName, xlspath):
    xls = XLSReader(xlspath)
    rows = xls.rows(Constants.TESTCASES)
    for rowNum in range(0, rows):
        testName = xls.getCellDataByColName(Constants.TESTCASES, rowNum, Constants.TCID_COL)
        if (testName == testCaseName):
            runMode = xls.getCellDataByColName(Constants.TESTCASES, rowNum, Constants.RUNMODE_COL)
            if (runMode == Constants.Y):
                return True
            else:
                return False