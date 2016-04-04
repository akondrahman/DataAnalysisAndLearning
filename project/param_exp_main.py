# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 23:45:39 2016

@author: akond
"""



import param_exp_classifier , IO_ 
def experiemnt_random_forest(fileNameParam):
  
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  print "This is 'experiemnt_random_forest' "  
  
  # settign up train data 
  trainData = testAndTrainData[0]
  original_rows = trainData.shape[0]
  original_cols =  trainData.shape[1] 
  print "Size of  training data : rows: {}, columns: {}".format( original_rows , original_cols )
  
  # settign up test data 
  testData = testAndTrainData[1]   
  param_exp_classifier.runRandomForest(trainData, testData)
  
  
  
  
  
  
print "Started at: ", IO_.giveTimeStamp()
fileNameParam="12_NonZeroDataset_Aggolo.csv"
experiemnt_random_forest(fileNameParam)


print "Done ;-)"
print "Ended at: ", IO_.giveTimeStamp()  