# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:06:14 2016

@author: akond
"""



#import IO_ 
from sklearn import cross_validation, svm
from sklearn.metrics import classification_report, roc_auc_score, mean_absolute_error, accuracy_score, hamming_loss, jaccard_similarity_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier 
from sklearn.naive_bayes import GaussianNB
#from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier




def runRandomForest(trainDataParam, testDataParam, trainizingSizeParam):
  # what percent will you use ? 
  testSplitSize = 1.0 - trainizingSizeParam

  ### classification   

  featureSpace_train, featureSpace_test, vScore_train, vScore_test = cross_validation.train_test_split(trainDataParam, testDataParam, test_size=testSplitSize, random_state=0) 
  ## fire up the model   
  theRndForestModel = RandomForestClassifier(n_estimators=10)
  theRndForestModel.fit(featureSpace_train, vScore_train)
  thePredictedScores = theRndForestModel.predict(featureSpace_test)

  evalClassifier(vScore_test, thePredictedScores) 
  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
  
  
  
  
  
def runSVM(trainDataParam, testDataParam, trainizingSizeParam):
  # what percent will you use ? 
  testSplitSize = 1.0 - trainizingSizeParam

  ### classification   
  ## get the test and training sets   
  featureSpace_train, featureSpace_test, vScore_train, vScore_test = cross_validation.train_test_split(trainDataParam, testDataParam, test_size=testSplitSize, random_state=0) 
  ## fire up the model 
  theSVMModel = svm.SVC(kernel='rbf', C=1).fit(featureSpace_train, vScore_train)   
  thePredictedScores = theSVMModel.predict(featureSpace_test)

  evalClassifier(vScore_test, thePredictedScores) 
  # preserve the order first test(real values from dataset), then predcited (from the classifier )    
  
  
def runCART(trainDataParam, testDataParam, trainizingSizeParam):  
  # what percent will you use ? 
  testSplitSize = 1.0 - trainizingSizeParam

  ### classification   

  featureSpace_train, featureSpace_test, vScore_train, vScore_test = cross_validation.train_test_split(trainDataParam, testDataParam, test_size=testSplitSize, random_state=0) 
  ## fire up the model   
  theCARTModel = DecisionTreeClassifier()
  theCARTModel.fit(featureSpace_train, vScore_train)
  thePredictedScores = theCARTModel.predict(featureSpace_test)

  evalClassifier(vScore_test, thePredictedScores) 
  # preserve the order first test(real values from dataset), then predcited (from the classifier )            
  
def runGNB(trainDataParam, testDataParam, trainizingSizeParam):  
  # what percent will you use ? 
  testSplitSize = 1.0 - trainizingSizeParam

  ### classification   

  featureSpace_train, featureSpace_test, vScore_train, vScore_test = cross_validation.train_test_split(trainDataParam, testDataParam, test_size=testSplitSize, random_state=0) 
  ## fire up the model   
  theGNBModel = GaussianNB()
  theGNBModel.fit(featureSpace_train, vScore_train)
  thePredictedScores = theGNBModel.predict(featureSpace_test)

  evalClassifier(vScore_test, thePredictedScores) 
  # preserve the order first test(real values from dataset), then predcited (from the classifier ) 

def runKNN(trainDataParam, testDataParam, trainizingSizeParam):  
  # what percent will you use ? 
  testSplitSize = 1.0 - trainizingSizeParam

  ### classification   

  featureSpace_train, featureSpace_test, vScore_train, vScore_test = cross_validation.train_test_split(trainDataParam, testDataParam, test_size=testSplitSize, random_state=0) 
  ## fire up the model   
  theKNNModel = KNeighborsClassifier()
  theKNNModel.fit(featureSpace_train, vScore_train)
  thePredictedScores = theKNNModel.predict(featureSpace_test)

  evalClassifier(vScore_test, thePredictedScores) 
  # preserve the order first test(real values from dataset), then predcited (from the classifier )

  
# def runMLP(trainDataParam, testDataParam, trainizingSizeParam):  
#   # what percent will you use ? 
#   testSplitSize = 1.0 - trainizingSizeParam

#   ### classification   

#   featureSpace_train, featureSpace_test, vScore_train, vScore_test = cross_validation.train_test_split(trainDataParam, testDataParam, test_size=testSplitSize, random_state=0) 
#   ## fire up the model   
#   theMLPModel = MLPClassifier()
#   theMLPModel.fit(featureSpace_train, vScore_train)
#   thePredictedScores = theMLPModel.predict(featureSpace_test)

#   evalClassifier(vScore_test, thePredictedScores) 
#   # preserve the order first test(real values from dataset), then predcited (from the classifier )              


def evalClassifier(vScore_test, thePredictedScores):  
  target_names = ['Low_Risk', 'High_Risk']
  '''
    the way skelarn treats is the following: first index -> lower index -> 0 -> 'Low'
    the way skelarn treats is the following: next index after first  -> next lower index -> 1 -> 'high'    
  '''
  print "precison, recall, F-stat"
  print(classification_report(vScore_test, thePredictedScores, target_names=target_names))
  print"*********************"
  # preserve the order first test(real values from dataset), then predcited (from the classifier )
  '''
    are under the curve values .... reff: http://gim.unmc.edu/dxtests/roc3.htm 
    0.80~0.90 -> good, any thing less than 0.70 bad , 0.90~1.00 -> excellent 
  '''
  area_roc_output = roc_auc_score(vScore_test, thePredictedScores)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
  print "Area under the ROC curve is ", area_roc_output
  print"*********************"  
  '''
    mean absolute error (mae) values .... reff: http://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html
    the smaller the better , ideally expect 0.0 
  '''
  mae_output = mean_absolute_error(vScore_test, thePredictedScores)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
  print "Mean absolute errro output  is ", mae_output  
  print"*********************"  
  
#  '''
#  accuracy_score ... reff: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter .... percentage of correct predictions 
#  ideally 1.0, higher the better 
#  '''
#  accuracy_score_output = accuracy_score(vScore_test, thePredictedScores)
#  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
#  print "Accuracy output  is ", accuracy_score_output   
#  print"*********************"  
#  
#  '''
#  hamming_loss ... reff: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter .... percentage of correct predictions 
#  ideally 0.0, lower the better 
#  '''
#  hamming_loss_output = hamming_loss(vScore_test, thePredictedScores)
#  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
#  print "Hamming loss output  is ", hamming_loss_output    
#  print"*********************"  
#  
#  
#  '''
#  jaccardian score ... reff: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter .... percentage of correct predictions 
#  ideally 1.0, higher the better 
#  '''
#  jaccardian_output = jaccard_similarity_score(vScore_test, thePredictedScores)
#  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
#  print "Jaccardian output  is ", jaccardian_output     
#  print"*********************" 