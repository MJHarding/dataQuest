#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:45:23 2020

@author: Matt Harding + Jamie Garvin


"""

import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()


History = "HistoricValues.csv"
oilCSV = "OilCsv.csv"
wheatCSV = "WheatCsv.csv"
goldCSV = "GoldCsv.csv"
ironCSV =  "IronCsv.csv"

goldIDX = 2
oilIDX = 3
wheatIDX = 4
ironIDX = 5

#reader = csv.reader(open(goldCSV, "r"), delimiter=",")
#goldCSV = list(reader)
#goldMap = np.array(goldCSV)



goldReader = csv.reader(open(goldCSV, "r"), delimiter=",")
wheatReader = csv.reader(open(wheatCSV, "r"), delimiter=",")
ironReader = csv.reader(open(ironCSV, "r"), delimiter=",")
oilReader = csv.reader(open(oilCSV, "r"), delimiter=",")
goldCSV = list(goldReader)
wheatCSV = list(wheatReader)
ironCSV = list(ironReader)
oilCSV = list(oilReader)
goldMap = np.array(goldCSV).astype("float")
goldArray = np.array(goldCSV).astype(int)
wheatArray = np.array(wheatCSV).astype(int)
oilArray = np.array(oilCSV).astype(int)
ironArray = np.array(ironCSV).astype(int)
finalArray = np.empty([1000,1000], dtype=float)
coords = []


"""  
Parse values over time 
"""

reader = csv.reader(open(History, "r"), delimiter=",")
historyCSV = list(reader)
historyValues = np.array(historyCSV)

#print(historyValues)
months = historyValues[:,1]
months = np.delete(months,0,0)

#print(months)

goldHist = historyValues[:,[goldIDX]]
goldHist = np.delete(goldHist, 0, 0).astype('float')
print(goldHist)
goldMean = np.mean(goldHist)
print("gold", goldMean)

ironHist = historyValues[:,[ironIDX]]
ironHist = np.delete(ironHist, 0, 0).astype('float')
print(ironHist)
ironMean = np.mean(ironHist)
print("iron ", ironMean)


oilHist = historyValues[:,[oilIDX]]
oilHist = np.delete(oilHist, 0, 0).astype('float')
print(oilHist)
oilMean = np.mean(oilHist)
print("oil", oilMean)

wheatHist = historyValues[:,[wheatIDX]]
wheatHist = np.delete(wheatHist, 0, 0).astype('float')
print(wheatHist)
wheatMean = np.mean(wheatHist)
print(wheatMean)
#
#
plt.figure(figsize=(15,10))
plt.xticks(range(50),months, rotation=90)
plt.plot(goldHist, label = "Gold")
plt.plot(ironHist, label = "Iron")
plt.plot(oilHist, label = "Oil")
plt.plot(wheatHist, label = "Wheat")
plt.legend(loc = "upper right")

""" 
Algorithm to select land
"""


def concatArr():
    array = np.dstack((goldArray, wheatArray, oilArray, ironArray))
    return array
    
def applyWeight(goldWeight, ironWeight, wheatWeight, oilWeight):
    for i in range(1000):
        goldArray[i] = goldArray[i] * goldWeight
        ironArray[i]= ironArray[i] * ironWeight
        oilArray[i]= oilArray[i] * oilWeight
        wheatArray[i] = wheatArray[i] * wheatWeight        
        finalArray[i] = goldArray[i] + ironArray[i] + oilArray[i] + wheatArray[i]

def showHeatMap(x, y, array):
    plt.imshow(array[x:(x+11),y:(y+11)], cmap='RdPu')
    plt.figure(figsize=(20,20))
    plt.show()
    
    
def findSubScore(arr):
    x = 0
    y = 0
    z = 0
    
    while(x < 989 and y < 989 and z < 4):
        for x in range(x + 9) :
            for y in range (y + 9):
                for z in range (z + 3):
                    sum = arr[x] + arr[y] + arr[z]
                    coords.append((sum, (x, y)))
#                    print(coords[x])
                    

applyWeight(10.04,6.92,3.02,14.2)
array = concatArr()


def printSumSimple(mat, k): 
    list = []
    n = 5
    if (k > n): 
        return
  
    # row number of first cell in current 
    # sub-square of size k x k 
    for i in range(n - k + 1): 
      
        # column of first cell in current  
        # sub-square of size k x k 
        for j in range(n - k + 1): 
              
            # Calculate and print sum 
            sum = 0
            for p in range(i, k + i): 
                for q in range(j, k + j): 
                    sum += mat[p][q] 
            list.append((sum, (p,q)))
       
            print() 
            sortedList = sorted(list, reverse = True ,key = lambda x: x[0])
            print(sortedList[0:100])   
        
        
printSumSimple(finalArray, 10)

#showHeatMap(9,254, finalArray)

