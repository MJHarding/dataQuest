#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:45:23 2020

@author: Matt Harding + Jamie Garvin


"""

import numpy as np
import csv

oilCSV = "Oil.csv"
wheatCSV = "Wheat.csv"
goldCSV = "ExampleGoldCsv.csv"
ironCSV =  "Iron.csv"

reader = csv.reader(open(goldCSV, "rb"), delimiter=",")
x = list(reader)
result = np.array(x).astype("float")

print(result)

landBorder = 10






"""  
TODO 
Parse values over time 
"""



""" 
TODO 
Algorithm to select land
"""