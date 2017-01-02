# -*- coding: utf-8 -*-
"""
Created on Nov 21, 2016

"""




import sys, numpy as np
import param_exp_classifier , IO_ , param_exp_analysis, pca_mobilesoft

def createMobileSoftFeatures(allFeatureParam, selectedIndicies):
  feature_dataset_to_ret = allFeatureParam.iloc[:, selectedIndicies]
  return feature_dataset_to_ret


def mobilesoft_random_forest(fileNameParam, fileToWriteP):

  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  trainData = testAndTrainData[0]
  testData  = testAndTrainData[1]
  #print trainData
  selected_training_data = pca_mobilesoft.getPCAedFeatures(trainData)
  print "Size of selected training data : ", np.shape(selected_training_data)
  print "="*50

  dict_of_results = param_exp_classifier.runRandomForest(selected_training_data, testData)
  reportStr = param_exp_analysis.analyzeThis(dict_of_results)
  IO_.writeStrToFile(fileToWriteP, reportStr)

def mobilesoft_svm(fileNameParam, fileToWriteP):

  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  trainData = testAndTrainData[0]
  testData  = testAndTrainData[1]
  selected_training_data = pca_mobilesoft.getPCAedFeatures(trainData)
  print "Size of selected training data : ", np.shape(selected_training_data)
  print "="*50

  dict_of_results = param_exp_classifier.runSVM(selected_training_data, testData, 0.90)
  reportStr = param_exp_analysis.analyzeThis(dict_of_results)
  IO_.writeStrToFile(fileToWriteP, reportStr)
def mobilesoft_knn(fileNameParam, fileToWriteP):

  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  trainData = testAndTrainData[0]
  testData  = testAndTrainData[1]
  selected_training_data = pca_mobilesoft.getPCAedFeatures(trainData)
  print "Size of selected training data : ", np.shape(selected_training_data)
  print "="*50

  dict_of_results = param_exp_classifier.runKNN(selected_training_data, testData, 0.90)
  reportStr = param_exp_analysis.analyzeThis(dict_of_results)
  IO_.writeStrToFile(fileToWriteP, reportStr)
def mobilesoft_cart(fileNameParam, fileToWriteP):
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  trainData = testAndTrainData[0]
  testData  = testAndTrainData[1]
  selected_training_data = pca_mobilesoft.getPCAedFeatures(trainData)
  print "Size of selected training data : ", np.shape(selected_training_data)
  print "="*50

  dict_of_results = param_exp_classifier.runCART(selected_training_data, testData, 0.90)
  reportStr = param_exp_analysis.analyzeThis(dict_of_results)
  IO_.writeStrToFile(fileToWriteP, reportStr)
print "Started at: ", IO_.giveTimeStamp()
#fileNameParam="Exp_1_Mobilesoft_clusterified_1407.csv"
#fileToWrite="param_exp_combo_mobilesoft_ten_folds.csv"
smoted_fileToWrite="param_smoted_combo_.csv"
smoted_f = "smote/mobilesoft_smoted_5clusters.csv"
mobilesoft_random_forest(smoted_f, 'rf_'+smoted_fileToWrite)
#mobilesoft_svm(smoted_f, 'svm_'+smoted_fileToWrite)
#mobilesoft_knn(smoted_f, 'knn_'+smoted_fileToWrite)
#mobilesoft_cart(smoted_f, 'cart_'+smoted_fileToWrite)
print "Ended at: ", IO_.giveTimeStamp()
