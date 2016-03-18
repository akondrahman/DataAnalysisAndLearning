# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:02:00 2016

@author: akond
"""



import  exp_x_experiments, IO_
print "Started at: ", IO_.giveTimeStamp()


'''
This is experiemnt X : classification with  NO versions that has ZERO scores + used K-Means  for clustering 
Classifier: Decision Tree (CART), Random Forest, SVM(rbf), Gaussian NAive Bayes , KNN
Selctive Feature 
'''  
print "This is experiemnt X : classification with  NO versions that has ZERO scores + used K-Means for High and Low + Selectiev Feature "
print "Classifier: Decision Tree (CART), Random Forest, SVM(rbf), Gaussian NAive Bayes , KNN"
##fileNameParam="NonZeroDataset_KMeans.csv"
fileNameParam="NonZeroDataset_Aggolo.csv"
exp_counts=2

for cnt in xrange(exp_counts):
  itn = cnt + 1   
  print "----------------------------- Iteration # {} Starts ------------------------------".format(itn) 
  ### Exp-1   
  #exp_x_experiments.experiemnt_CART(fileNameParam)
  ### Exp-2
  #exp_x_experiments.experiemnt_random_forest(fileNameParam)
  ### Exp-3
  #exp_x_experiments.experiemnt_SVM(fileNameParam)
  ### Exp-4
  #exp_x_experiments.experiemnt_gaussian_naive_bayes(fileNameParam)
  ### Exp-5
  #exp_x_experiments.experiemnt_KNN(fileNameParam)  

  
  
  print "----------------------------- Iteration # {} Ends ------------------------------".format(itn)      
print "=================================================================================================================="
exp_x_experiments.experiemnt_logireg(fileNameParam)
print "=================================================================================================================="






print "Done ;-)"
print "Ended at: ", IO_.giveTimeStamp()