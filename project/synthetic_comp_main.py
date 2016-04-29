# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:04:44 2016

@author: akond
"""



import time, a12_utility , IO_
from sklearn import cross_validation, svm
from sklearn.metrics import  mean_absolute_error, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


def getData(fileNameParam): 
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  
  trainData = testAndTrainData[0]
  testData = testAndTrainData[1]    
 
  return trainData, testData   
  
def evalClassifier(vScore_test, thePredictedScores):  

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






def perform_cross_validation(classiferP, trainingP, testP, cross_vali_param):
  #print "||||| ----- Performing cross validation (start) -----  |||||"  
  predicted_via_cv = cross_validation.cross_val_predict(classiferP, trainingP , testP , cv=cross_vali_param)  
  res_tuple = evalClassifier(testP, predicted_via_cv)
  #print "||||| ----- Performing cross validation (end) -----  |||||"  
  return res_tuple  


def runRFTest(orig_fileParam, synth_fileParam, itnParam, cv_param):
 
  ### init 
  mae_list_1 = [] 
  mae_list_2 = []   
  time_list_1 = [] 
  time_list_2 = []     
  ### 
  orig_testAndTrainData  = getData(orig_fileParam)  
  orig_trainingData = orig_testAndTrainData[0]
  orig_testData = orig_testAndTrainData[1]
  ### 
  synth_testAndTrainData  = getData(synth_fileParam)  
  synth_trainingData = synth_testAndTrainData[0]
  synth_testData = synth_testAndTrainData[1]  
  
   
  for cnt in xrange(itnParam):
    t1 = time.time()  
    theModel_orig = RandomForestClassifier(n_estimators=50)  
    mae_for_orig =  perform_cross_validation(theModel_orig, orig_trainingData, orig_testData, cv_param)[1]
    t2 = time.time()    
    time_for_orig =  t2 - t1 
    mae_list_1.append(mae_for_orig) 
    time_list_1.append(time_for_orig)
    
    t2, t1 = 0, 0 


    t1 = time.time()         
    theModel_synth =  RandomForestClassifier(n_estimators=50)    
    mae_for_synth =  perform_cross_validation(theModel_synth, synth_trainingData, synth_testData, cv_param)[1]
    t2 = time.time()  
    time_for_synth =  t2 - t1
    mae_list_2.append(mae_for_synth) 
    time_list_2.append(time_for_synth)    
    
    
    
  mae_a12_ = a12_utility.doSlowA12(mae_list_1, mae_list_2)    
  time_a12_ = a12_utility.doSlowA12(time_list_2, time_list_1)   
  print "MAE  comparison: is original worse than synthetic ?", mae_a12_  
  print "time comparison: is synthetic slower than original ?", time_a12_      





def runknnTest(orig_fileParam, synth_fileParam, itnParam, cv_param):

  ### init 
  mae_list_1 = [] 
  mae_list_2 = []   
  time_list_1 = [] 
  time_list_2 = []     
  ### 
  orig_testAndTrainData  = getData(orig_fileParam)  
  orig_trainingData = orig_testAndTrainData[0]
  orig_testData = orig_testAndTrainData[1]
  ### 
  synth_testAndTrainData  = getData(synth_fileParam)  
  synth_trainingData = synth_testAndTrainData[0]
  synth_testData = synth_testAndTrainData[1]  
  
   
  for cnt in xrange(itnParam):
    t1 = time.time()  
    theModel_orig = KNeighborsClassifier()
    mae_for_orig =  perform_cross_validation(theModel_orig, orig_trainingData, orig_testData, cv_param)[1]
    t2 = time.time()    
    time_for_orig =  t2 - t1 
    mae_list_1.append(mae_for_orig) 
    time_list_1.append(time_for_orig)
    
    t2, t1 = 0, 0 


    t1 = time.time()         
    theModel_synth =  KNeighborsClassifier()
    mae_for_synth =  perform_cross_validation(theModel_synth, synth_trainingData, synth_testData, cv_param)[1]
    t2 = time.time()  
    time_for_synth =  t2 - t1
    mae_list_2.append(mae_for_synth) 
    time_list_2.append(time_for_synth)    
    
    
    
  mae_a12_ = a12_utility.doSlowA12(mae_list_1, mae_list_2)    
  time_a12_ = a12_utility.doSlowA12(time_list_2, time_list_1)   
  print "MAE  comparison: is original worse than synthetic ?", mae_a12_  
  print "time comparison: is synthetic slower than original ?", time_a12_  





def runsvmTest(orig_fileParam, synth_fileParam, itnParam, cv_param):

  ### init 
  mae_list_1 = [] 
  mae_list_2 = []   
  time_list_1 = [] 
  time_list_2 = []     
  ### 
  orig_testAndTrainData  = getData(orig_fileParam)  
  orig_trainingData = orig_testAndTrainData[0]
  orig_testData = orig_testAndTrainData[1]
  ### 
  synth_testAndTrainData  = getData(synth_fileParam)  
  synth_trainingData = synth_testAndTrainData[0]
  synth_testData = synth_testAndTrainData[1]  
  
   
  for cnt in xrange(itnParam):
    t1 = time.time()  
    theModel_orig = svm.SVC(kernel='rbf')
    mae_for_orig =  perform_cross_validation(theModel_orig, orig_trainingData, orig_testData, cv_param)[1]
    t2 = time.time()    
    time_for_orig =  t2 - t1 
    mae_list_1.append(mae_for_orig) 
    time_list_1.append(time_for_orig)
    
    t2, t1 = 0, 0 


    t1 = time.time()         
    theModel_synth =  svm.SVC(kernel='rbf')
    mae_for_synth =  perform_cross_validation(theModel_synth, synth_trainingData, synth_testData, cv_param)[1]
    t2 = time.time()  
    time_for_synth =  t2 - t1
    mae_list_2.append(mae_for_synth) 
    time_list_2.append(time_for_synth)    
    
    
    
  mae_a12_ = a12_utility.doSlowA12(mae_list_1, mae_list_2)    
  time_a12_ = a12_utility.doSlowA12(time_list_2, time_list_1)   
  print "MAE  comparison: is original worse than synthetic ?", mae_a12_  
  print "time comparison: is synthetic slower than original ?", time_a12_  






def runCARTTest(orig_fileParam, synth_fileParam, itnParam, cv_param):
  ### init 
  mae_list_1 = [] 
  mae_list_2 = []   
  time_list_1 = [] 
  time_list_2 = []     
  ### 
  orig_testAndTrainData  = getData(orig_fileParam)  
  orig_trainingData = orig_testAndTrainData[0]
  orig_testData = orig_testAndTrainData[1]
  ### 
  synth_testAndTrainData  = getData(synth_fileParam)  
  synth_trainingData = synth_testAndTrainData[0]
  synth_testData = synth_testAndTrainData[1]  
  
   
  for cnt in xrange(itnParam):
    t1 = time.time()  
    theModel_orig = DecisionTreeClassifier()
    mae_for_orig =  perform_cross_validation(theModel_orig, orig_trainingData, orig_testData, cv_param)[1]
    t2 = time.time()    
    time_for_orig =  t2 - t1 
    mae_list_1.append(mae_for_orig) 
    time_list_1.append(time_for_orig)
    
    t2, t1 = 0, 0 


    t1 = time.time()         
    theModel_synth =  DecisionTreeClassifier()
    mae_for_synth =  perform_cross_validation(theModel_synth, synth_trainingData, synth_testData, cv_param)[1]
    t2 = time.time()  
    time_for_synth =  t2 - t1
    mae_list_2.append(mae_for_synth) 
    time_list_2.append(time_for_synth)    
    
    
    
  mae_a12_ = a12_utility.doSlowA12(mae_list_1, mae_list_2)    
  time_a12_ = a12_utility.doSlowA12(time_list_2, time_list_1)   
  print "MAE  comparison: is original worse than synthetic ?", mae_a12_  
  print "time comparison: is synthetic slower than original ?", time_a12_  




def runGNBTest(orig_fileParam, synth_fileParam, itnParam, cv_param):
  ### init 
  mae_list_1 = [] 
  mae_list_2 = []   
  time_list_1 = [] 
  time_list_2 = []     
  ### 
  orig_testAndTrainData  = getData(orig_fileParam)  
  orig_trainingData = orig_testAndTrainData[0]
  orig_testData = orig_testAndTrainData[1]
  ### 
  synth_testAndTrainData  = getData(synth_fileParam)  
  synth_trainingData = synth_testAndTrainData[0]
  synth_testData = synth_testAndTrainData[1]  
  
   
  for cnt in xrange(itnParam):
    t1 = time.time()  
    theModel_orig = GaussianNB()
    mae_for_orig =  perform_cross_validation(theModel_orig, orig_trainingData, orig_testData, cv_param)[1]
    t2 = time.time()    
    time_for_orig =  t2 - t1 
    mae_list_1.append(mae_for_orig) 
    time_list_1.append(time_for_orig)
    
    t2, t1 = 0, 0 


    t1 = time.time()         
    theModel_synth =  GaussianNB()
    mae_for_synth =  perform_cross_validation(theModel_synth, synth_trainingData, synth_testData, cv_param)[1]
    t2 = time.time()  
    time_for_synth =  t2 - t1
    mae_list_2.append(mae_for_synth) 
    time_list_2.append(time_for_synth)    
    
    
    
  mae_a12_ = a12_utility.doSlowA12(mae_list_1, mae_list_2)    
  time_a12_ = a12_utility.doSlowA12(time_list_2, time_list_1)   
  print "MAE  comparison: is original worse than synthetic ?", mae_a12_  
  print "time comparison: is synthetic slower than original ?", time_a12_  


orig_datasetFileName="13_NonZeroDataset_Aggolo.csv"
synth_datasetFileName="smote/smoted_13_clusters.csv"
iterations=10000
cv_param_items = [2, 5]


for cv_param in cv_param_items:
  print "*************************** {} fold ***************************".format(cv_param)  
  print "========== CART =========="    
  with IO_.duration():
    runCARTTest(orig_datasetFileName, synth_datasetFileName, iterations, cv_param)   
  print "========== GNB =========="    
  with IO_.duration():
    runGNBTest(orig_datasetFileName, synth_datasetFileName, iterations, cv_param)   
  print "========== KNN =========="  
  with IO_.duration():
    runknnTest(orig_datasetFileName, synth_datasetFileName, iterations, cv_param) 
  print "========== SVM =========="    
  with IO_.duration():
    runsvmTest(orig_datasetFileName, synth_datasetFileName, iterations, cv_param) 
  print "========== Random Forest =========="
  with IO_.duration():
    runRFTest(orig_datasetFileName, synth_datasetFileName, iterations, cv_param)