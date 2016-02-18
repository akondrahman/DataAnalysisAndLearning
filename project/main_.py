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
Classifier: SVM 
'''  
#print "This is experiemnt 4 : classification with  NO versions that has ZERO scores + used Median for High and Low"
#fileNameParam="NonZeroDataset_Median.csv"
#experiments.experiemnt_svm(fileNameParam)
#print "=================================================================================================================="

'''
This is experiemnt 5 : classification with  NO versions that has ZERO scores + used K-Means  for clustering 
Classifier: SVM
'''  
#print "This is experiemnt 5 : classification with  NO versions that has ZERO scores + used Aggolo for High and Low"
##fileNameParam="NonZeroDataset_KMeans.csv"
#fileNameParam="NonZeroDataset_Aggolo.csv"
#experiments.experiemnt_svm(fileNameParam)
#print "=================================================================================================================="



'''
This is experiemnt 6 : correlation : different to that of 4 and 5 , and 6 and 7 
'''  
#clsuterFlag = True # True means  kmeans, Flase hierarchical
#if clsuterFlag: 
#  clusterStr="K-Means"    
#else:
#  clusterStr="Aggolomerative"        
#print "This is experiemnt 6 : 'correlation' different to that of 4 and 5 "
#experiments.experiemnt_correlation(dbFileName,meanFlag, "Exp_6_" + outputStr + "_" + clusterStr, clsuterFlag)
'''
Only foudn one metric that has a Spearman correlation p-value < 0.05 for high defect scores. it was func_complexity  
Found no  metric that has a Pearson correlation p-value < 0.05 for high defect scores. 
Almost all metrics shows shome valeu for MIC and non-linearity. 
Can be preneted in paper as learning curve and say the imprtance of simple logistic regression analysis 

'''
#print "=================================================================================================================="
'''
This is experiemnt 7 : classification with  NO versions that has ZERO scores + used Median  for clustering
Classifier: RandmonForests 
'''  
#print "This is experiemnt 7 : classification (Random Forests) with  NO versions that has ZERO scores + used Median for High and Low"
#fileNameParam="NonZeroDataset_Median.csv"
#experiments.experiemnt_random_forest(fileNameParam)
#print "=================================================================================================================="

'''
This is experiemnt 8 : classification with  NO versions that has ZERO scores + used K-Means  for clustering 
Classifier: RandmonForests
'''  
#print "This is experiemnt 8 : classification (Random Forests) with  NO versions that has ZERO scores + used K-Means for High and Low"
#fileNameParam="NonZeroDataset_KMeans.csv"
##fileNameParam="NonZeroDataset_Aggolo.csv"
#experiments.experiemnt_random_forest(fileNameParam)
#print "=================================================================================================================="
'''
This is experiemnt 9 : classification with  NO versions that has ZERO scores + used Median  for clustering
Classifier: Quadratic Determinsitic Analysis  (QDA)
As thsi expeirment gives bad results , we will not use it 
'''  
#print "This is experiemnt 9 : classification  (QDA) with  NO versions that has ZERO scores + used Median for High and Low"
#fileNameParam="NonZeroDataset_Median.csv"
#experiments.experiemnt_qda(fileNameParam)
#print "=================================================================================================================="

'''
This is experiemnt 10 : classification with  NO versions that has ZERO scores + used K-Means  for clustering 
Classifier: Quadratic Determinsitic Analysis 
As thsi expeirment gives bad results , we will not use it 
'''  
#print "This is experiemnt 10 : classification (QDA) with  NO versions that has ZERO scores + used Aggolo for High and Low"
##fileNameParam="NonZeroDataset_KMeans.csv"
#fileNameParam="NonZeroDataset_Aggolo.csv"
#experiments.experiemnt_qda(fileNameParam)
#print "=================================================================================================================="
'''
This is experiemnt 11: classification with  NO versions that has ZERO scores + used Median  for clustering
Classifier: Decision Tree (CART)
'''  
#print "This is experiemnt 11 : classification  (CART) with  NO versions that has ZERO scores + used Median for High and Low"
#fileNameParam="NonZeroDataset_Median.csv"
#experiments.experiemnt_cart(fileNameParam)
#print "=================================================================================================================="

'''
This is experiemnt 12 : classification with  NO versions that has ZERO scores + used K-Means  for clustering 
Classifier: Decision Tree (CART)
'''  
#print "This is experiemnt 12 : classification (CART) with  NO versions that has ZERO scores + used K-Means for High and Low"
#fileNameParam="NonZeroDataset_KMeans.csv"
##fileNameParam="NonZeroDataset_Aggolo.csv"
#experiments.experiemnt_cart(fileNameParam)
#print "=================================================================================================================="

print "Done ;-)"
print "Ended at: ", IO_.giveTimeStamp()