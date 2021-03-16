#!/usr/bin/python3
from openpyxl import load_workbook
from matplotlib import pyplot

def getvalue(x):
    return x.value

wb = load_workbook('data_analysis_lab.xlsx')
sheet=wb['Data']

years=list(map(getvalue, sheet['A'][1:]))
temp=list(map(getvalue, sheet['B'][1:]))
actv=list(map(getvalue, sheet['D'][1:]))

pyplot.plot(years, temp, label="Изменение температуры")
pyplot.plot(years, actv, label="Активность Солнца")

pyplot.show()
