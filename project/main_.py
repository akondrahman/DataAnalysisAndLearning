# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:00:51 2016

@author: akond
"""



import  experiments, IO_
print "Started at: ", IO_.giveTimeStamp()
# -----------------------------------------------------------------------
dbFileName="/Users/akond/Documents/Spring-2016/CSC522/OSSAndroidAppDataset/androSec.db"
meanFlag=False
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
	This is experiemnt # 3 where we split the vulnerability scores with clustering  


'''
#clsuterFlag = False # True means  kmeans, Flase hierarchical
#if clsuterFlag: 
#  clusterStr="K-Means"    
#else:
#  clusterStr="Aggolomerative"        
#print "########################## Applying the '"+  str_ + "' approach with " + clusterStr +  " ###############################"
#experiments.experiemnt_three(dbFileName,meanFlag, "Exp_3_" + outputStr + "_" + clusterStr, clsuterFlag )
#print "=================================================================================================================="
'''
This is experiemnt 4 : classification with  NO versions that has ZERO scores + used Median  for clustering 
'''  
#print "This is experiemnt 4 : classification with  NO versions that has ZERO scores + used Median for High and Low"
#fileNameParam="NonZeroDataset_Median.csv"
#experiments.experiemnt_svm(fileNameParam)
#print "=================================================================================================================="

'''
This is experiemnt 5 : classification with  NO versions that has ZERO scores + used K-Means  for clustering 
'''  
print "This is experiemnt 5 : classification with  NO versions that has ZERO scores + used Aggolo for High and Low"
#fileNameParam="NonZeroDataset_KMeans.csv"
fileNameParam="NonZeroDataset_Aggolo.csv"
experiments.experiemnt_svm(fileNameParam)
print "=================================================================================================================="

print "Done ;-)"
print "Ended at: ", IO_.giveTimeStamp()