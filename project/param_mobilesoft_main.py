# -*- coding: utf-8 -*-
"""
Created on Nov 21, 2016

"""




import sys, numpy as np
import param_exp_classifier , IO_ , param_exp_analysis

def createMobileSoftFeatures(allFeatureParam, selectedIndicies):
  feature_dataset_to_ret = allFeatureParam.iloc[:, selectedIndicies]
  return feature_dataset_to_ret


def mobilesoft_random_forest(fileNameParam, fileToWriteP):
  indexVector = [0, 5, 10, 12, 13, 18, 19, 20]
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

def mobilesoft_svm(fileNameParam, fileToWriteP):
  indexVector = [0, 5, 10, 12, 13, 18, 19, 20]
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  trainData = testAndTrainData[0]
  testData  = testAndTrainData[1]
  selected_training_data = createMobileSoftFeatures(trainData, indexVector)
  print "Size of selected training data : ", np.shape(selected_training_data)
  print "="*50
  print "Glimpse at  selected features (10th entry): \n", selected_training_data.iloc[9, :]
  print "="*50
  print "Glimpse at  labels (10th entry): \n", testData.iloc[9]
  print "="*50
  dict_of_results = param_exp_classifier.runSVM(selected_training_data, testData, 0.90)
  reportStr = param_exp_analysis.analyzeThis(dict_of_results)
  IO_.writeStrToFile(fileToWriteP, reportStr)
def mobilesoft_knn(fileNameParam, fileToWriteP):
  indexVector = [0, 5, 10, 12, 13, 18, 19, 20]
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  trainData = testAndTrainData[0]
  testData  = testAndTrainData[1]
  selected_training_data = createMobileSoftFeatures(trainData, indexVector)
  print "Size of selected training data : ", np.shape(selected_training_data)
  print "="*50
  print "Glimpse at  selected features (10th entry): \n", selected_training_data.iloc[9, :]
  print "="*50
  print "Glimpse at  labels (10th entry): \n", testData.iloc[9]
  print "="*50
  dict_of_results = param_exp_classifier.runKNN(selected_training_data, testData, 0.90)
  reportStr = param_exp_analysis.analyzeThis(dict_of_results)
  IO_.writeStrToFile(fileToWriteP, reportStr)
def mobilesoft_cart(fileNameParam, fileToWriteP):
  indexVector = [0, 5, 10, 12, 13, 18, 19, 20]
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  trainData = testAndTrainData[0]
  testData  = testAndTrainData[1]
  selected_training_data = createMobileSoftFeatures(trainData, indexVector)
  print "Size of selected training data : ", np.shape(selected_training_data)
  print "="*50
  print "Glimpse at  selected features (10th entry): \n", selected_training_data.iloc[9, :]
  print "="*50
  print "Glimpse at  labels (10th entry): \n", testData.iloc[9]
  print "="*50
  # dict_of_results = param_exp_classifier.runCART(selected_training_data, testData, 0.90)
  # reportStr = param_exp_analysis.analyzeThis(dict_of_results)
  # IO_.writeStrToFile(fileToWriteP, reportStr)
print "Started at: ", IO_.giveTimeStamp()
fileNameParam="Exp_1_Mobilesoft_clusterified_1407.csv"
fileToWrite="param_exp_combo_mobilesoft_five_folds.csv"
#mobilesoft_random_forest(fileNameParam, fileToWrite)
mobilesoft_svm(fileNameParam, fileToWrite)
#mobilesoft_knn(fileNameParam, fileToWrite)
#mobilesoft_cart(fileNameParam, fileToWrite)
print "Ended at: ", IO_.giveTimeStamp()
