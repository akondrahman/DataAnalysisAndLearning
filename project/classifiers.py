# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:03:19 2016

@author: akond
"""



import utility 
from sklearn import cross_validation, svm
from sklearn.metrics import classification_report, roc_auc_score, mean_absolute_error, accuracy_score, hamming_loss, jaccard_similarity_score
def runSVM(fileNamaParam, trainizingSizeParam):
  # what percent will you use ? 
  testSplitSize = 1.0 - trainizingSizeParam
  # get test and train data together  
  test_trainData = utility.giveMePandaDataFrame(fileNamaParam)  
  # training data 
  trainingCols = test_trainData.columns[0:21]
  trainData = test_trainData[trainingCols]
  # test data 
  testColn = test_trainData.columns[-1]
  testData  = test_trainData[testColn]

  ### classification   
  featureSpace_train, featureSpace_test, vScore_train, vScore_test = cross_validation.train_test_split(trainData, testData, test_size=testSplitSize, random_state=0) 
  theSVMModel = svm.SVC(kernel='rbf', C=1).fit(featureSpace_train, vScore_train)   
  thePredictedScores = theSVMModel.predict(featureSpace_test)
  #print "The original vector: "
  #print vScore_test
  #print "The predicted score vector: "
  #print thePredictedScores
  evalClassifier(vScore_test, thePredictedScores) 
  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
  
  
