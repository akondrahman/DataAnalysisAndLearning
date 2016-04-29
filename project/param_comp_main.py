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



def getData(fileNameParam): 
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  
  trainData = testAndTrainData[0]
  testData = testAndTrainData[1]    
 
  return trainData, testData   
  
def evalClassifier(vScore_test, thePredictedScores):  
    

    #target_names_2_aggolo = [ 'L', 'H']  ## same thing for kmeans and aggolo    
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






def perform_cross_validation(classiferP, trainingP, testP, cross_vali_param):
  #print "||||| ----- Performing cross validation (start) -----  |||||"  
  predicted_via_cv = cross_validation.cross_val_predict(classiferP, trainingP , testP , cv=cross_vali_param)  
  res_tuple = evalClassifier(testP, predicted_via_cv)
  #print "||||| ----- Performing cross validation (end) -----  |||||"  
  return res_tuple  


def runRFTest(fileParam, itnParam, cv_param):
 
  ### init 
  mae_list_1 = [] 
  mae_list_2 = []   
  time_list_1 = [] 
  time_list_2 = []     
  ### 
  testAndTrainData  = getData(fileParam)  
  trainingData = testAndTrainData[0]
  testData = testAndTrainData[1]
   
  for cnt in xrange(itnParam):
    t1 = time.time()  
    theModel_1 = RandomForestClassifier()  
    mae_for_param_combo_1 =  perform_cross_validation(theModel_1, trainingData, testData, cv_param)[1]
    t2 = time.time()    
    time_for_param_comb_1 =  t2 - t1 
    mae_list_1.append(mae_for_param_combo_1) 
    time_list_1.append(time_for_param_comb_1)
    
    t2, t1 = 0, 0 

    #n_estimators=10, criterion=entropy, max_features=sqrt, max_dept=15, max_leaf_nodes=75
    #bootstrap=False, min-sample-split=1, oob_score=False, min-wt-frac=0.3, warm-start=False
    t1 = time.time()         
    theModel_2     =  RandomForestClassifier(n_estimators=10, criterion='entropy', max_features='sqrt',  
                                                            max_depth=15, max_leaf_nodes=75, 
                                                            bootstrap=False, min_samples_split=1,  
                                                            oob_score=False, min_weight_fraction_leaf=0.3,  
                                                            n_jobs=-1 , warm_start=False)    

    mae_for_param_combo_2 =  perform_cross_validation(theModel_2, trainingData, testData, cv_param)[1]
    t2 = time.time()  
    time_for_param_comb_2 =  t2 - t1
    mae_list_2.append(mae_for_param_combo_2) 
    time_list_2.append(time_for_param_comb_2)    
    
    
    
  mae_a12_ = a12_utility.doSlowA12(mae_list_1, mae_list_2)    
  time_a12_ = a12_utility.doSlowA12(time_list_2, time_list_1)   
  print "MAE  comaprison: is default worse than 'best combo' ?", mae_a12_  
  print "time comaprison: is 'best' combo slower than default ?", time_a12_      





def runknnTest(fileParam, itnParam, cv_param):
 
  ### init 
  mae_list_1 = [] 
  mae_list_2 = []   
  time_list_1 = [] 
  time_list_2 = []     
  ### 
  testAndTrainData  = getData(fileParam)  
  trainingData = testAndTrainData[0]
  testData = testAndTrainData[1]
   
  for cnt in xrange(itnParam):
    t1 = time.time()  
    the_Model_1 = KNeighborsClassifier()
    mae_for_param_combo_1 =  perform_cross_validation(the_Model_1, trainingData, testData, cv_param)[1]
    t2 = time.time()    
    time_for_param_comb_1 =  t2 - t1 
    mae_list_1.append(mae_for_param_combo_1) 
    time_list_1.append(time_for_param_comb_1)
    
    t2, t1 = 0, 0 

    t1 = time.time()         
    # n_neighbors=10 weights=distance metric=minkowski p=3 algorithm=brute
    the_Model_2 = KNeighborsClassifier(n_neighbors=10, weights='distance', metric='minkowski', p=3, algorithm='brute')   

    mae_for_param_combo_2 =  perform_cross_validation(the_Model_2, trainingData, testData, cv_param)[1]
    t2 = time.time()  
    time_for_param_comb_2 =  t2 - t1
    mae_list_2.append(mae_for_param_combo_2) 
    time_list_2.append(time_for_param_comb_2)    
    
    
    
  mae_a12_ = a12_utility.doSlowA12(mae_list_1, mae_list_2)    
  time_a12_ = a12_utility.doSlowA12(time_list_2, time_list_1)   
  print "MAE  comaprison: is default worse than 'best combo' ?", mae_a12_  
  print "time comaprison: is 'best' combo slower than default ?", time_a12_      






def runsvmTest(fileParam, itnParam, cv_param):
 
  ### init 
  mae_list_1 = [] 
  mae_list_2 = []   
  time_list_1 = [] 
  time_list_2 = []     
  ### 
  testAndTrainData  = getData(fileParam)  
  trainingData = testAndTrainData[0]
  testData = testAndTrainData[1]
   
  for cnt in xrange(itnParam):
    t1 = time.time()  
    the_Model_1 = svm.SVC(kernel='rbf')
    mae_for_param_combo_1 =  perform_cross_validation(the_Model_1, trainingData, testData, cv_param)[1]
    t2 = time.time()    
    time_for_param_comb_1 =  t2 - t1 
    mae_list_1.append(mae_for_param_combo_1) 
    time_list_1.append(time_for_param_comb_1)
    
    t2, t1 = 0, 0 

    # C=10 shrinking=False tol=1e-05 decision_function_shape=ovr
    t1 = time.time()         
    the_Model_2  =  svm.SVC(kernel='rbf', C=10, shrinking = False, tol =1e-05, decision_function_shape = 'ovr') 

    mae_for_param_combo_2 =  perform_cross_validation(the_Model_2, trainingData, testData, cv_param)[1]
    t2 = time.time()  
    time_for_param_comb_2 =  t2 - t1
    mae_list_2.append(mae_for_param_combo_2) 
    time_list_2.append(time_for_param_comb_2)    
    
    
    
  mae_a12_ = a12_utility.doSlowA12(mae_list_1, mae_list_2)    
  time_a12_ = a12_utility.doSlowA12(time_list_2, time_list_1)   
  print "MAE  comaprison: is default worse than 'best combo' ?", mae_a12_  
  print "time comaprison: is 'best' combo slower than default ?", time_a12_      






def runCARTTest(fileParam, itnParam, cv_param):
 
  ### init 
  mae_list_1 = [] 
  mae_list_2 = []   
  time_list_1 = [] 
  time_list_2 = []     
  ### 
  testAndTrainData  = getData(fileParam)  
  trainingData = testAndTrainData[0]
  testData = testAndTrainData[1]
   
  for cnt in xrange(itnParam):
    t1 = time.time()  
    the_Model_1 = DecisionTreeClassifier()
    mae_for_param_combo_1 =  perform_cross_validation(the_Model_1, trainingData, testData, cv_param)[1]
    t2 = time.time()    
    time_for_param_comb_1 =  t2 - t1 
    mae_list_1.append(mae_for_param_combo_1) 
    time_list_1.append(time_for_param_comb_1)
    
    t2, t1 = 0, 0 
    #criterion=entropy splitter=random max_features=10 max_depth=25 min_samples_split=4 min_samples_leaf=2 
    #max_leaf_nodes=10000

    t1 = time.time()         
    the_Model_2=DecisionTreeClassifier(criterion='entropy',splitter='random',max_features=10,max_depth=25,min_samples_split=4,min_samples_leaf=2,max_leaf_nodes=10000)  

    mae_for_param_combo_2 =  perform_cross_validation(the_Model_2, trainingData, testData, cv_param)[1]
    t2 = time.time()  
    time_for_param_comb_2 =  t2 - t1
    mae_list_2.append(mae_for_param_combo_2) 
    time_list_2.append(time_for_param_comb_2)    
    
    
    
  mae_a12_ = a12_utility.doSlowA12(mae_list_1, mae_list_2)    
  time_a12_ = a12_utility.doSlowA12(time_list_2, time_list_1)   
  print "MAE  comaprison: is default worse than 'best combo' ?", mae_a12_  
  print "time comaprison: is 'best' combo slower than default ?", time_a12_      



datasetFileName="13_NonZeroDataset_Aggolo.csv"
iterations=10000
cv_param = 5
print "========== Random Forest =========="
with IO_.duration():
  runRFTest(datasetFileName, iterations, cv_param)
print "========== KNN =========="  
with IO_.duration():
  runknnTest(datasetFileName, iterations, cv_param) 
print "========== SVM =========="    
with IO_.duration():
  runsvmTest(datasetFileName, iterations, cv_param) 
print "========== CART =========="    
with IO_.duration():
  runCARTTest(datasetFileName, iterations, cv_param)   
