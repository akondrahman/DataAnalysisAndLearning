# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:27:23 2016

@author: akond
"""



import  pandas as pd
from sklearn import linear_model
def performLogiRegression(fileNamaParam):
  # get test and train data together  
  test_trainData = giveMePandaDataFrame(fileNamaParam)    
  #print test_trainData.head()
  # get tarining data 
  trainingCols = test_trainData.columns[0:21]
  trainData = test_trainData[trainingCols]

  #print "<----------Training data matrix---------->"
  #print trainData.head()

  ###############
  #print trainData.describe()
  testColn = test_trainData.columns[-1]
  testData  = test_trainData[testColn]

  #print "<----------Test data column---------->"
  #print testData.head()
  #test_trainData['intercept'] = 1.0
  #################
  print "<------------ Performing Logistic Regression ------------->"

  logisticRModel = linear_model.LogisticRegression(C=1e5,  penalty='l1')
  ### if you dont fit , you will get an error 
  logisticRModel.fit(trainData, testData)
  print "Output of score (mean accuracy of test features and prediction classs) "
  print logisticRModel.score(trainData, testData)
  print "\n"
  print "Output of co-efficients ={}".format(logisticRModel.coef_)
  print "Output of intercept ={}, n_iter_ = {} ".format(logisticRModel.intercept_, logisticRModel.n_iter_)


    
def giveMePandaDataFrame(fileNamaParam):    
  '''  
  colNames=[ "versionID", "classes", "ncloc", "functions" , "duplicated_lines", "complexity", "class_complexity", "function_complexity",
           "comment_lines", "comment_lines_density", "duplicated_lines_density", "files", "directories", "file_complexity", "violations", 
           "duplicated_blocks", "duplicated_files", "lines", "blocker_violations", "critical_violations", "major_violations", "minor_violations" , "class_vscore", "END-EMPTY" ]
  #print len(colNames)
  indics=[ _ for _ in xrange(24) ]
  '''
  df = pd.read_csv(fileNamaParam, sep=",", header=None)
  #print df.head()
  #print df.describe()
  #print df.columns
  test_train_cols = df.columns[1:23]
  test_trainData  = df[test_train_cols]
  #print trainData.head()
  return test_trainData 