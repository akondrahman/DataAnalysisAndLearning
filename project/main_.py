# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:00:51 2016

@author: akond
"""



import  experiments, IO_
print "Started at: ", IO_.giveTimeStamp()
# -----------------------------------------------------------------------
dbFileName="/Users/akond/Documents/Spring-2016/CSC522/OSSAndroidAppDataset/androSec.db"
meanFlag=True
# -----------------------------------------------------------------------
if meanFlag:
  str_ = "M-E-A-N" 
  outputStr="AVG"   
else:
  str_ = "M-E-D-I-A-N"      
  outputStr="MEDI"  
'''
This is experiemnt 1 : there are versions with ZERO scores 
'''  
#print "########################## Applying the '"+  str_ + "' approach ###############################"
#experiments.experiemnt_one(dbFileName, meanFlag, "Exp_1_" + outputStr)
#print "=================================================================================================================="
'''
This is experiemnt 2 : there are NO versions with ZERO scores 
'''  
#experiments.experiemnt_two(dbFileName, meanFlag, "Exp_2_" + outputStr)
#print "=================================================================================================================="
'''
	This experiemnt is abandones because logistic reression si a binary classifier 
	and not an estmator 

experiments.experiemnt_three(dbFileName, meanFlag)
print "=================================================================================================================="
'''
'''
This is experiemnt 4 : classification with  NO versions that has ZERO scores 
'''  
fileNameParam="TheNonZeroDataset.csv"
experiments.experiemnt_four(fileNameParam)
print "=================================================================================================================="
print "Done ;-)"
print "Ended at: ", IO_.giveTimeStamp()