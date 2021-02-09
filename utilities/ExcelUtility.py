
import openpyexcel

# workbook = openpyexcel.load_workbook("E:\pythonProject\Framefork1\TestData\TestData_NopAdmin.xlsx")
# sheet = workbook["ProfileDetails"]
# value = sheet.cell(row = 2, column = 6).value
# strval = str(value)
# ret = strval.split(" ")
# print(ret[0])




def getRowcount (filepath, sheetname):
    workbook = openpyexcel.load_workbook(filepath)
    sheet = workbook[sheetname]
    return (sheet.max_row)

def getColumncount (filepath , sheetname):
    workbook = openpyexcel.load_workbook(filepath)
    sheet = workbook[sheetname]
    return (sheet.max_column)

def readData (filepath, sheetname, rownum, colnum):
    workbook = openpyexcel.load_workbook(filepath)
    sheet = workbook[sheetname]
    return sheet.cell(row=rownum, column = colnum).value




