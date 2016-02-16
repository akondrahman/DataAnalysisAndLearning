# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:00:51 2016

@author: akond
"""



import  experiments
dbFileName="/Users/akond/Documents/Spring-2016/CSC522/OSSAndroidAppDataset/androSec.db"
experiments.experiemnt_one(dbFileName)
print "========================================================="
experiments.experiemnt_two(dbFileName)
print "========================================================="
'''
	This experiemnt is abandones because logistic reression si a binary classifier 
	and not an estmator 

experiments.experiemnt_three(dbFileName)
print "========================================================="
'''

print "Done ;-)"
