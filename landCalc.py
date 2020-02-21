#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:45:23 2020

@author: Matt Harding + Jamie Garvin


"""

import numpy as np
import csv
import matplotlib.pyplot as plt

oilCSV = "Oil.csv"
wheatCSV = "Wheat.csv"
goldCSV = "ExampleGoldCsv.csv"
ironCSV =  "Iron.csv"
History = "HistoricValues.csv"

goldIDX = 2
oilIDX = 3
wheatIDX = 4
ironIDX = 5


landBorder = 10

reader = csv.reader(open(goldCSV, "r"), delimiter=",")
goldCSV = list(reader)
goldMap = np.array(goldCSV)

print(goldMap)
print(goldMap.shape)






"""  
TODO 
Parse values over time 
"""

reader = csv.reader(open(History, "r"), delimiter=",")
historyCSV = list(reader)
historyValues = np.array(historyCSV)

print(historyValues)
months = historyValues[:,1]
months = np.delete(months,0,0)

print(months)

goldHist = historyValues[:,[goldIDX]]
goldHist = np.delete(goldHist, 0, 0).astype('float')
print(goldHist)
goldMean = np.mean(goldHist)
print(goldMean)

ironHist = historyValues[:,[ironIDX]]
ironHist = np.delete(ironHist, 0, 0).astype('float')
print(ironHist)
ironMean = np.mean(ironHist)
print(ironMean)


oilHist = historyValues[:,[oilIDX]]
oilHist = np.delete(oilHist, 0, 0).astype('float')
print(oilHist)
oilMean = np.mean(oilHist)
print(oilMean)

wheatHist = historyValues[:,[wheatIDX]]
wheatHist = np.delete(wheatHist, 0, 0).astype('float')
print(wheatHist)
wheatMean = np.mean(wheatHist)
print(wheatMean)


plt.figure(figsize=(15,10))
plt.xticks(range(50),months, rotation=90)
plt.plot(goldHist, label = "Gold")
plt.plot(ironHist, label = "Iron")
plt.plot(oilHist, label = "Oil")
plt.plot(wheatHist, label = "Wheat")
plt.legend(loc = "upper right")

""" 
TODO 
Algorithm to select land
"""