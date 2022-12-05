import xlrd
from _overlapped import NULL


class xlsReader:

    def __init__(self, xlspath):
        self.xlspath = xlspath
        self.xls = xlrd.open_workbook(xlspath)

    def getCellDataByIndex(self, sheetName, rowIndex, colIndex):
        sheet = self.xls.sheet_by_name(sheetName)
        cell = sheet.cell_value(rowIndex, colIndex)
        return cell

    def checkEmptyCell(self, sheetName, rowIndex, colIndex):
        sheet = self.xls.sheet_by_name(sheetName)
        cell_type = sheet.cell_type(rowIndex, colIndex)
        if (cell_type == xlrd.XL_CELL_EMPTY):
            return True
        else:
            return False

    def getCellDataByColName(self, sheetName, rowNum, columnName):
        for cNum in range(0, self.getColCount(sheetName)):
            extractedColName = self.getCellDataByIndex(sheetName, 0, cNum)
            if (extractedColName == columnName):
                data = self.getCellDataByIndex(sheetName, rowNum, cNum)
                if (data != '' or data != NULL):
                    return data
                else:
                    return ''

    def getRowCount(self, sheetName):
        sheet = self.xls.sheet_by_name(sheetName)
        return sheet.nrows

    def getColCount(self, sheetName):
        sheet = self.xls.sheet_by_name(sheetName)
        return sheet.ncols