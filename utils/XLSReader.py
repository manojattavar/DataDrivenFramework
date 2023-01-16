import xlrd
from _overlapped import NULL


class XLSReader:
    def __init__(self, xlspath):
        self.xls = xlrd.open_workbook(xlspath)

    def getCellDataByIndex(self, sheetName, rowInd, colInd):
        sheet = self.xls.sheet_by_name(sheetName)
        data = sheet.cell_value(rowInd, colInd)
        if (data != NULL):
            return data
        else:
            print("Data is null")

    def checkEmptyCell(self, sheetName, rowInd, colInd):
        sheet = self.xls.sheet_by_name(sheetName)
        cellType = sheet.cell_type(rowInd, colInd)
        if (cellType == xlrd.XL_CELL_EMPTY):
            return True
        else:
            return False

    def rows(self, sheetName):
        sheet = self.xls.sheet_by_name(sheetName)
        return sheet.nrows

    def cols(self, sheetName):
        sheet = self.xls.sheet_by_name(sheetName)
        return sheet.ncols

    def getCellDataByColName(self, sheetName, rowInd, colName):
        for colNum in range(0, self.cols(sheetName)):
            extractedColName = self.getCellDataByIndex(sheetName, 0, colNum)
            if (extractedColName == colName):
                data = self.getCellDataByIndex(sheetName, rowInd, colNum)
                if (data != NULL):
                    return data
                else:
                    print("Cell data not found")