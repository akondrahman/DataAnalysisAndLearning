# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 18:39:50 2016

@author: akond
"""

from sklearn import cross_validation, svm
from sklearn.metrics import  mean_absolute_error, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier 
from sklearn.naive_bayes import GaussianNB
#from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier



def evalClassifier(vScore_test, thePredictedScores):  
  #target_names_3_aggolo = [ 'H', 'L', 'M']  ## same thing for kmeans and aggolo
  #target_names_5_aggolo = [ 'VL', 'VH', 'L', 'M', 'H']  #4=50, 1=51.11, 0=15, 2=30, 3=44.61
  #target_names_10_aggolo = [ '51_1', '20', '30', '44_61', '15', '50_0', '52_29', '43_33', '53_22', '50_67']
  #target_names_10_aggolo = ['L9' , 'L8', 'L3' , 'L7', 'L5', 'L1', 'L2', 'L0', 'L4', 'L6']  

  ### 10 clusters 
  ##3=51.1, 4=50.0, 1=52.00, 5=20.0, 0=53.33, 9=50.667, 8=44.61, 6=30, 7=15, 2=43.33 
  ##0=53.33, 1=52.00, 2=43.33, 3=51.1, 4=50.0,  5=20.0, 6=30, 7=15, 8=44.61,  9=50.667,

  ### 13 clusters  
  ##  0=51.11, 1=50.0,  12=52.0, 11=20.0, 4=53.33, 
  ##  6=30.0, 9=50.67, 8=44.615, 7=15.0, 3=53.0,  
  ##  10= 52.22 , 5=43.33 , 2=52.631     
  #target_names_13_aggolo = ['L7', 'L5', 'L10', 'L11', 'L12', 'L3', 'L2', 'L0', 'L4', 'L6', 'L9', 'L1', 'L8']  

  ### 12 clusters  
  ## 1=51.11, 4=50.0, 0=52.0, 11=20.0, 
  ## 10=53.33, 6=30.0, 9=50.67, 8=44.61, 
  ##  3=53.0, 5=43.33, 2=52.63, 7=15.0 
  #target_names_12_aggolo = [ 'L8', 'L7', 'L9', 'L10', 'L5', 'L3', 'L2', 'L0', 'L4', 'L6', 'L11' , 'L1']  
    
  #target_names_5_kmeans = [ 'H', 'VL', 'L', 'VH', 'M']

  '''
    the way skelarn treats is the following: first index -> lower index -> 0 -> 'Low'
    the way skelarn treats is the following: next index after first  -> next lower index -> 1 -> 'high'    
  '''
  #print "precison, recall, F-stat"
  #print(classification_report(vScore_test, thePredictedScores, target_names=target_names_12_aggolo))
  #print"*********************"
  # preserve the order first test(real values from dataset), then predcited (from the classifier )
  '''
    are under the curve values .... reff: http://gim.unmc.edu/dxtests/roc3.htm 
    0.80~0.90 -> good, any thing less than 0.70 bad , 0.90~1.00 -> excellent 
  '''
  #area_roc_output = roc_auc_score(vScore_test, thePredictedScores)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
  #print "Area under the ROC curve is ", area_roc_output
  #print"*********************"  
  '''
    mean absolute error (mae) values .... reff: http://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html
    the smaller the better , ideally expect 0.0 
  '''
  mae_output = mean_absolute_error(vScore_test, thePredictedScores)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
  #print "Mean absolute errro output  is ", mae_output  
  #print"*********************"  
  
  '''
  accuracy_score ... reff: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter .... percentage of correct predictions 
  ideally 1.0, higher the better 
  '''
  accuracy_score_output = accuracy_score(vScore_test, thePredictedScores)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
  #print "Accuracy output  is ", accuracy_score_output   
  #print"*********************"  
  

  
  return  accuracy_score_output, mae_output

#  avg_precision_output = average_precision_score(vScore_test, thePredictedScores)    
#  # preserve the order first test(real values from dataset), then predcited (from the classifier )  
#  print "Avg. precision score is", avg_precision_output  
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






def perform_cross_validation(classiferP, trainingP, testP, cross_vali_param):
  #print "||||| ----- Performing cross validation (start) -----  |||||"  
  predicted_via_cv = cross_validation.cross_val_predict(classiferP, trainingP , testP , cv=cross_vali_param)  
  res_tuple = evalClassifier(testP, predicted_via_cv)
  #print "||||| ----- Performing cross validation (end) -----  |||||"  
  return res_tuple    
  
  
  
  
def runRandomForest(trainDataParam, testDataParam):
  theRndForestModel = RandomForestClassifier(n_estimators=50)
  accu_, moea_ = perform_cross_validation(theRndForestModel, trainDataParam, testDataParam, 5)
  return accu_, moea_

    
def runSVM(trainDataParam, testDataParam):
  theSVMModel = svm.SVC(kernel='rbf') 
  accu_, moea_ = perform_cross_validation(theSVMModel, trainDataParam, testDataParam, 5)
  return accu_, moea_
  
def runCART(trainDataParam, testDataParam):  
  theCARTModel = DecisionTreeClassifier()
  accu_, moea_ = perform_cross_validation(theCARTModel, trainDataParam, testDataParam, 5)
  return accu_, moea_     
  
def runGNB(trainDataParam, testDataParam):  
  theGNBModel = GaussianNB()
  accu_, moea_ = perform_cross_validation(theGNBModel, trainDataParam, testDataParam, 5)
  return accu_, moea_

def runKNN(trainDataParam, testDataParam):  
  theKNNModel = KNeighborsClassifier()
  accu_, moea_ = perform_cross_validation(theKNNModel, trainDataParam, testDataParam, 5)
  return accu_, moea_
  