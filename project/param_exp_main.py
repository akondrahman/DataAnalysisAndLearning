# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 23:45:39 2016

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
  
  
  
####### Open loggger ####
old_stdout = sys.stdout
output_file_name="V2_output/chrome-ff-topics_1000_missing.txt"
log_file = open( output_file_name,  "w")
sys.stdout = log_file  
  
  
print "Started at: ", IO_.giveTimeStamp()
fileNameParam="12_NonZeroDataset_Aggolo.csv"
fileToWrite="param_exp_combo_report.csv"
experiemnt_random_forest(fileNameParam, fileToWrite)


print "Done ;-)"
print "Ended at: ", IO_.giveTimeStamp()  

#### close logger       
sys.stdout = old_stdout
log_file.close()      