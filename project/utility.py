# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 00:18:43 2016

@author: akond
"""


import  pandas as pd
def getHighVScoreVersions_CQ(vScoreDictParam, codeQualityDictParam, medianVScoreParam):
  dictToret = {}  
  for k_, v_ in vScoreDictParam.items():
    vscore_ =  vScoreDictParam[k_]    
    if vscore_ >= medianVScoreParam:
      dictToret[k_] = codeQualityDictParam[k_]
      
  return dictToret  
  
  
def getLowVScoreVersions_CQ(vScoreDictParam, codeQualityDictParam, medianVScoreParam):
  dictToret = {}  
  for k_, v_ in vScoreDictParam.items():
    vscore_ =  vScoreDictParam[k_]    
    if vscore_ < medianVScoreParam:
      dictToret[k_] = codeQualityDictParam[k_]
      
  return dictToret  
  
  
def getHighVScoreVersions_VScore(vScoreDictParam, medianVScoreParam):
  dictToret = {}  
  for k_, v_ in vScoreDictParam.items():
    vscore_ =  vScoreDictParam[k_]    
    if vscore_ >= medianVScoreParam:
      dictToret[k_] = vScoreDictParam[k_]
      
  return dictToret  
  
  
def getLowVScoreVersions_VScore(vScoreDictParam, medianVScoreParam):
  dictToret = {}  
  for k_, v_ in vScoreDictParam.items():
    vscore_ =  vScoreDictParam[k_]    
    if vscore_ < medianVScoreParam:
      dictToret[k_] = vScoreDictParam[k_]
      
  return dictToret    
  
  
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
  