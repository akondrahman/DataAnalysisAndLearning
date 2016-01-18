# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:37:38 2016

@author: akond
"""



import sqlite3
dbFileName="/Users/akond/Documents/Spring-2016/CSC522/OSSAndroidAppDataset/androSec.db"
conn = sqlite3.connect(dbFileName)
print "Opened database successfully"

cursor = conn.execute("SELECT versionID, fuzzy_risk  from Vulnerability")
listToret=[]
for row in cursor:
   #print "ID = ", row[0]
   #print "Risk Score = ", row[1]
   tuples=(row[0], row[1])
   listToret.append(tuples)
print "The list ", listToret 
print "Operation done successfully"
conn.close()