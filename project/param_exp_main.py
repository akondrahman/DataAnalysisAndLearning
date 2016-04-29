# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 21:05:17 2016

@author: akond
"""



import sys
import param_exp_classifier , IO_ , param_exp_analysis 

def experiemnt_random_forest(fileNameParam, fileToWriteP):
  
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  print "This is 'experiemnt_random_forest' "  
  
  # settign up train data 
  trainData = testAndTrainData[0]
  original_rows = trainData.shape[0]
  original_cols =  trainData.shape[1] 
  print "Size of  training data : rows: {}, columns: {}".format( original_rows , original_cols )
  
  # settign up test data 
  testData = testAndTrainData[1]   
  dict_of_results = param_exp_classifier.runRandomForest(trainData, testData)
  reportStr = param_exp_analysis.analyzeThis(dict_of_results)
  IO_.writeStrToFile(fileToWriteP, reportStr)
  
def experiemnt_KNN(fileNameParam):
  import exp_x_classifiers , IO_ 
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  print "This is 'experiemnt_KNN' "      
  
  # settign up train data 
  trainData = testAndTrainData[0]
  original_rows = trainData.shape[0]
  original_cols =  trainData.shape[1] 
  print "Size of  training data : rows: {}, columns: {}".format( original_rows , original_cols )
  
  # settign up test data 
  testData = testAndTrainData[1]
   
  for selCount in xrange(original_cols):
    count_ = selCount + 1 
    if count_ <= original_cols:      
      slected_training_data = giveSelectedTrainingData(trainData, testData, count_ ) 
      print "#################  No. of features to work with={}  ############".format(count_)
      print "Size of selected training data : ", slected_training_data.shape
      emperiemntSplitters=[float(x)/float(10) for x in xrange(10) if x > 0] 
      for elem in emperiemntSplitters:
        #print "Training size: {} %".format(float(elem*100))
        param_exp_classifier.runKNN(slected_training_data, testData, elem)
        #print "---------------------------------------------------------------"	 

def experiemnt_SVM(fileNameParam):
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  print "This is 'experiemnt_SVM' "    
  
  # settign up train data 
  trainData = testAndTrainData[0]
  original_rows = trainData.shape[0]
  original_cols =  trainData.shape[1] 
  print "Size of  training data : rows: {}, columns: {}".format( original_rows , original_cols )
  
  # settign up test data 
  testData = testAndTrainData[1]   
  for selCount in xrange(original_cols):
    count_ = selCount + 1 
    if count_ <= original_cols:      
      slected_training_data = giveSelectedTrainingData(trainData, testData, count_ ) 
      print "#################  No. of features to work with={}  ############".format(count_)
      print "Size of selected training data : ", slected_training_data.shape
      emperiemntSplitters=[float(x)/float(10) for x in xrange(10) if x > 0] 
      for elem in emperiemntSplitters:
        #print "Training size: {} %".format(float(elem*100))
        param_exp_classifier.runSVM(slected_training_data, testData, elem)
        #print "---------------------------------------------------------------"	 


def experiemnt_CART(fileNameParam):
  import exp_x_classifiers , IO_ 
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  print "This is 'experiemnt_CART' "      
  
  # settign up train data 
  trainData = testAndTrainData[0]
  original_rows = trainData.shape[0]
  original_cols =  trainData.shape[1] 
  print "Size of  training data : rows: {}, columns: {}".format( original_rows , original_cols )
  
  # settign up test data 
  testData = testAndTrainData[1]   
#  for selCount in xrange(original_cols):
#    count_ = selCount + 1 
#    if count_ < original_cols:      
  slected_training_data = giveSelectedTrainingData(trainData, testData, original_cols ) 
  print "#################  No. of features to work with={}  ############".format(original_cols)
  print "Size of selected training data : ", slected_training_data.shape
  emperiemntSplitters=[float(x)/float(10) for x in xrange(10) if x > 0] 
  for elem in emperiemntSplitters:
	#print "Training size: {} %".format(float(elem*100))
	param_exp_classifier.runCART(slected_training_data, testData, elem)
	#print "---------------------------------------------------------------"	 

def giveSelectedTrainingData(trainParam, testParam, no_of_chices_param): 
  from sklearn.feature_selection import SelectKBest
  from sklearn.feature_selection import chi2

  train_data_new = SelectKBest(chi2, k=no_of_chices_param).fit_transform(trainParam, testParam)
  return train_data_new

####### Open loggger ####
old_stdout = sys.stdout
output_file_name="param_exp_random_forest_500_two_folds.txt"
log_file = open( output_file_name,  "w")
sys.stdout = log_file  
  
  
print "Started at: ", IO_.giveTimeStamp()
fileNameParam="13_NonZeroDataset_Aggolo.csv"
fileToWrite="param_exp_combo_report_500_two_folds.csv"
experiemnt_random_forest(fileNameParam, fileToWrite)
#experiemnt_SVM(fileNameParam)
#experiemnt_KNN(fileNameParam)
#experiemnt_CART(fileNameParam)


print "Done ;-)"
print "Ended at: ", IO_.giveTimeStamp()  

#### close logger       
sys.stdout = old_stdout
log_file.close()     