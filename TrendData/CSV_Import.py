from asyncore import read
from email.header import Header
from numpy import NaN
import pandas
import csv
from typing import List
import glob

#Get files in the directory
path = 'c:/trends'
files = glob.glob(path+'/*.csv')
print(files)

#Processed needs to be stored in the file, in case the program was restarted, it will not process all files over again
processed = {}
pivot = pandas.DataFrame



def ReadIntoTable(fileName):

    #f = open ('test.Csv','r',delimiter =' ')
    trend_data = pandas.read_csv(files[0], sep = ';', header = 0)
    #reader = csv.reader(f)

    points = {}
    newList = list()
    points =trend_data['Data Source'].unique() 

    trend_data['DateTime'] = pandas.to_datetime(trend_data['DateTime'])
    pivot = pandas.pivot_table(trend_data,index = 'DateTime',columns = 'Data Source')
    
    oldNames = []
    colNames = pivot.columns
    for col in colNames:
        oldNames.append(col[1])

    newNames = CleanName(oldNames)
    pivot.columns = newNames
    return pivot

def CleanName(names):
    newNames = []
    #newNames.append('DateTime')
    for nam in names:
        if nam == None or len (str(nam)) < 5: continue
        pLeft = str(nam).rfind('.')
        sLeft = str(nam)[:pLeft]
        pRight = sLeft.rfind('.')+1
        sRight = sLeft[pRight:]
        newName = sRight
        newNames.append(newName)
    return newNames


pivot = ReadIntoTable(files[1])





newName = files[0].lower().replace('.csv','_modified.csv')
newName = newName.replace(path,path+'/excel')
print (newName)
pivot.to_csv(newName)

