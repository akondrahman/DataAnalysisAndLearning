# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:04:49 2016

@author: akond
"""



import logiRegre as LGR
def experiemnt_logireg(fileNameParam):
  print "Performing experiemnt # X:LGR: LGR with class lebals : 1 and 0   "  
  LGR.performLogiRegression(fileNameParam)  
     
def experiemnt_random_forest(fileNameParam):
  import exp_x_classifiers , IO_ 
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  print "This is 'experiemnt_random_forest' "  
  
  # settign up train data 
  trainData = testAndTrainData[0]
  original_rows = trainData.shape[0]
  original_cols =  trainData.shape[1] 
  print "Size of  training data : rows: {}, columns: {}".format( original_rows , original_cols )
  
  # settign up test data 
  testData = testAndTrainData[1]   
  for selCount in xrange(original_cols):
    count_ = selCount + 1 
    if count_ < original_cols:      
      slected_training_data = giveSelectedTrainingData(trainData, testData, count_ ) 
      print "#################  No. of features to work with={}  ############".format(count_)
      print "Size of selected training data : ", slected_training_data.shape
      emperiemntSplitters=[float(x)/float(10) for x in xrange(10) if x > 0] 
      for elem in emperiemntSplitters:
	  print "Training size: {} %".format(float(elem*100))
	  exp_x_classifiers.runRandomForest(slected_training_data, testData, elem)
	  print "---------------------------------------------------------------"	 
   
   
def experiemnt_gaussian_naive_bayes(fileNameParam):
  import exp_x_classifiers , IO_ 
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  print "This is 'experiemnt_gaussian_naive_bayes' "  
  
  # settign up train data 
  trainData = testAndTrainData[0]
  original_rows = trainData.shape[0]
  original_cols =  trainData.shape[1] 
  print "Size of  training data : rows: {}, columns: {}".format( original_rows , original_cols )
  
  # settign up test data 
  testData = testAndTrainData[1]   
  for selCount in xrange(original_cols):
    count_ = selCount + 1 
    if count_ < original_cols:      
      slected_training_data = giveSelectedTrainingData(trainData, testData, count_ ) 
      print "#################  No. of features to work with={}  ############".format(count_)
      print "Size of selected training data : ", slected_training_data.shape
      emperiemntSplitters=[float(x)/float(10) for x in xrange(10) if x > 0] 
      for elem in emperiemntSplitters:
	  print "Training size: {} %".format(float(elem*100))
	  exp_x_classifiers.runGNB(slected_training_data, testData, elem)
	  print "---------------------------------------------------------------"	    
  
  
def experiemnt_SVM(fileNameParam):
  import exp_x_classifiers , IO_ 
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
    if count_ < original_cols:      
      slected_training_data = giveSelectedTrainingData(trainData, testData, count_ ) 
      print "#################  No. of features to work with={}  ############".format(count_)
      print "Size of selected training data : ", slected_training_data.shape
      emperiemntSplitters=[float(x)/float(10) for x in xrange(10) if x > 0] 
      for elem in emperiemntSplitters:
	  print "Training size: {} %".format(float(elem*100))
	  exp_x_classifiers.runSVM(slected_training_data, testData, elem)
	  print "---------------------------------------------------------------"	 


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
  for selCount in xrange(original_cols):
    count_ = selCount + 1 
    if count_ < original_cols:      
      slected_training_data = giveSelectedTrainingData(trainData, testData, count_ ) 
      print "#################  No. of features to work with={}  ############".format(count_)
      print "Size of selected training data : ", slected_training_data.shape
      emperiemntSplitters=[float(x)/float(10) for x in xrange(10) if x > 0] 
      for elem in emperiemntSplitters:
	  print "Training size: {} %".format(float(elem*100))
	  exp_x_classifiers.runCART(slected_training_data, testData, elem)
	  print "---------------------------------------------------------------"	 



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
    if count_ < original_cols:      
      slected_training_data = giveSelectedTrainingData(trainData, testData, count_ ) 
      print "#################  No. of features to work with={}  ############".format(count_)
      print "Size of selected training data : ", slected_training_data.shape
      emperiemntSplitters=[float(x)/float(10) for x in xrange(10) if x > 0] 
      for elem in emperiemntSplitters:
	  print "Training size: {} %".format(float(elem*100))
	  exp_x_classifiers.runKNN(slected_training_data, testData, elem)
	  print "---------------------------------------------------------------"	 




def giveSelectedTrainingData(trainParam, testParam, no_of_chices_param): 
  from sklearn.feature_selection import SelectKBest
  from sklearn.feature_selection import chi2

  train_data_new = SelectKBest(chi2, k=no_of_chices_param).fit_transform(trainParam, testParam)
  return train_data_new
  
  
  
  
#def experiemnt_x_lgr(dbFileName, meanFlag):
#  import DataExtractionFromTables as DEFT, sanityCheck,  IO_ 
#
#
#
#  print "Performing experiemnt # X:LGR: LGR with raw scores  "
#  versionAndCodeQualityDict =  DEFT.getValuesFrom_CodingStandard(dbFileName)
#  sanitizedVersions = sanityCheck.getCodeQualityofVersions(versionAndCodeQualityDict, meanFlag)
#  sanitizedVersions_CQ = sanitizedVersions
#  #print "Sanitized versions that will be used in study ", len(sanitizedVersions)
#  #print "Sanitized versions ..." , sanitizedVersions
#  NonZero_sanitizedVersionsWithScore = sanityCheck.getNonZeroVulnerbailityScoreOfSelectedVersions(sanitizedVersions)
#  #print "zzzz", len(NonZero_sanitizedVersionsWithScore)
#
#
#
#
#  ############################## 
#  themegaFile_All =  "_exp_x_lgr_.csv"
#  IO_.dumpIntoClusterifiedFile( themegaFile_All,sanitizedVersions_CQ , NonZero_sanitizedVersionsWithScore, False )
#  LGR.performLogiRegression(themegaFile_All)    
      