# -*- coding: utf-8 -*-
"""
Created on Nov 21, 2016

"""




import sys
import param_exp_classifier , IO_ , param_exp_analysis

def mobilesoft_random_forest(fileNameParam, fileToWriteP):
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  trainData = testAndTrainData[0]
  testData  = testAndTrainData[1]
  #print trainData
  selected_training_data = createMobileSoftFeatures(trainData, indexVector)
  print "Size of selected training data : ", np.shape(selected_training_data)
  print "="*50
  print "Glimpse at  selected features (10th entry): \n", selected_training_data.iloc[9, :]
  print "="*50
  print "Glimpse at  labels (10th entry): \n", testData.iloc[9]
  print "="*50
  # dict_of_results = param_exp_classifier.runRandomForest(selected_training_data, testData)
  # reportStr = param_exp_analysis.analyzeThis(dict_of_results)
  # IO_.writeStrToFile(fileToWriteP, reportStr)


print "Started at: ", IO_.giveTimeStamp()
fileNameParam="Exp_1_Mobilesoft_clusterified_1407.csv"
fileToWrite="param_exp_combo_mobilesoft_five_folds.csv"
mobilesoft_random_forest(fileNameParam, fileToWrite)
print "Ended at: ", IO_.giveTimeStamp()
