# -*- coding: utf-8 -*-
"""
Created on Nov 21, 2016

"""



import  exp_x_experiments, IO_
import sys




print "Started at: ", IO_.giveTimeStamp()


'''
This is experiemnt X : classification with  NO versions that has ZERO scores + used K-Means  for clustering
Classifier: Decision Tree (CART), Random Forest, SVM(rbf), Gaussian NAive Bayes , KNN
Selctive Feature
'''
print "This is experiemnt Mobilesoft: classification with ZERO scores, 5 levels using aggolo clutering"

fileNameParam="Exp_1_Mobilesoft_clusterified_1407.csv"
## Exp-1
exp_x_experiments.experiment_mobilesoft_random_forest(fileNameParam)
### Exp-2
#exp_x_experiments.experiemnt_CART(fileNameParam)
### Exp-3
#exp_x_experiments.experiemnt_SVM(fileNameParam)
### Exp-4
#exp_x_experiments.experiemnt_gaussian_naive_bayes(fileNameParam)
### Exp-5
#exp_x_experiments.experiemnt_KNN(fileNameParam)

print "=================================================================================================================="
#exp_x_experiments.experiemnt_logireg(fileNameParam)
print "=================================================================================================================="





print "Done ;-)"
print "Ended at: ", IO_.giveTimeStamp()