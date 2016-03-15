# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:02:00 2016

@author: akond
"""



import  exp_x_experiments, IO_
print "Started at: ", IO_.giveTimeStamp()


'''
This is experiemnt X : classification with  NO versions that has ZERO scores + used K-Means  for clustering 
Classifier: Decision Tree (CART)
Selctive Feature 
'''  
print "This is experiemnt X : classification (RandomForests) with  NO versions that has ZERO scores + used K-Means for High and Low + Selectiev Feature "
##fileNameParam="NonZeroDataset_KMeans.csv"
fileNameParam="NonZeroDataset_Aggolo.csv"
#exp_x_experiments.experiemnt_decision_tree(fileNameParam)
#exp_x_experiments.experiemnt_SVM(fileNameParam)
exp_x_experiments.experiemnt_CART(fileNameParam)
print "=================================================================================================================="
exp_x_experiments.experiemnt_logireg(fileNameParam)
print "=================================================================================================================="






print "Done ;-)"
print "Ended at: ", IO_.giveTimeStamp()