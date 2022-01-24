from asyncore import read
from multiprocessing.sharedctypes import Value
#from email.header import Header
from numpy import NaN
import numpy as np
import pandas
import csv
from typing import List
import glob
import time
import json






def ReadIntoTable(fileName):

    #f = open ('test.Csv','r',delimiter =' ')
    trend_data = pandas.read_csv(fileName, sep = ';', header = 0)
    #reader = csv.reader(f)
    #print(trend_data)
    points = {}
    newList = list()
    points =trend_data['Data Source'].unique()
    uni_dates =  trend_data['DateTime'].unique()
    
    #print(uni_dates)
    
    trend_data['DateTime'] = pandas.to_datetime(trend_data['DateTime'])
    #pivot = pandas.pivot_table(trend_data,index = 'DateTime',columns = 'Data Source')
    
    #print (trend_data)

    noDup = trend_data.drop_duplicates(subset=['DateTime','Data Source'], keep='first')
    #trend_data.reset_index()
    
    #print (noDup)
    
    #print(trend_data)

    pivot = pandas.pivot(noDup,index = 'DateTime',columns = 'Data Source', values = 'Value')
    #pivot = pivot.fillna(0)
    #pivot = pivot.dropna(axis='columns')
    
    
    print('######################################## PIVOT #############################')
    #print(trend_data['Value'])
    print(pivot)
    print('######################################## END PIVOT #############################')
    #print(test_pivot)
    

    oldNames = []
    colNames = pivot.columns
    pivot = pivot.loc[:, pivot.columns.notnull()]

    #pivot = pivot.round(5)
    tmp = pivot.select_dtypes(include=[np.number])
    #pivot.loc[:, tmp.columns] = np.round(tmp)
    #print (pivot.loc[:, tmp.columns])
    pivot = pivot.resample('15min').pad()
    pivot.ffill(inplace = True)
    #df = pivot.set_index('DateTime').resample('15M').pad()


    print (pivot)

    
    for col in pivot.columns:
        pivot[col] = pandas.to_numeric(pivot[col], errors = 'ignore')
    print('========= Data Types ======')
    print(pivot.index.dtype)
    print(pivot.dtypes)
    print('========= End Data Types ======')
    
    #pivot.index.resample('15M')

    print (pivot)
    for col in colNames:
        print (col)
        oldNames.append(col)

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

def SaveProcessed():
    json_process = json.dumps(processed, indent=2)

    with open('processed.json','w') as f:
        f.write(json_process)
    

#Get files in the directory
path = 'c:/trends'
processed = {}
while True:

    files = glob.glob(path+'/*.csv')
    #print(files)

    #Processed needs to be stored in the file, in case the program was restarted, it will not process all files over again
    
    pivot = pandas.DataFrame

    for file in files:
        if not processed.get(file):
            processed[file] = True
            pivot = ReadIntoTable(file)

            newName = file.lower().replace('.csv','_modified.csv')
            newName = newName.replace(path,path+'/excel')
            print (newName + "  Has been processed!")
            #pivot.to_csv(newName)
            exec_name = newName.replace('.csv','.xlsx')
            pivot.to_excel(exec_name)
            SaveProcessed()
    print (processed)
    
    time.sleep(10)







