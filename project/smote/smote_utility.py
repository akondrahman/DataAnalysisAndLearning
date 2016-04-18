# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 21:20:21 2016

@author: akond
"""



import csv,numpy as np
def readCSVAsArray(CSVfileParam):
  list_to_ret = []  
  cr = csv.reader(open(CSVfileParam,"rb"))
  for row in cr:  
    sub_list = []  
    if len(row) > 0:
      for item_ in row: 
        if (len(item_) > 0 ):  
          val_ = float(item_)
          sub_list.append(val_)
    if len(sub_list) > 0:
      list_to_ret.append(sub_list)
  return list_to_ret      
  
def getRecordsPeClass(classParam, matrixParam):
  recordToret = []
  for row_ in matrixParam:
    if row_[-1]==classParam:  
      recordToret.append(row_[1:-1])
    
  return recordToret      
  
  
  
  
def getCountPerClass(dataSetAsMatrix): 
  dicToRet = {}  
  classes = []
  for row in dataSetAsMatrix: 
    classes.append(row[-1])
  no_of_classes = np.unique(classes)
  for cls in no_of_classes:
    dicToRet[cls] = len(getRecordsPeClass(cls, dataSetAsMatrix))
  return dicToRet      
def write_smoted_values_to_file_two_clusters(records_per_class_1 , majClassVal, smoted_dataset , minClassVal  , file_to_write): 
  overallStr=""  
  for rows_ in records_per_class_1: 
    per_row_str=""  
    for elem in rows_: 
      per_row_str = per_row_str + str(elem) + ","       
    per_row_str = per_row_str + str(majClassVal)     
    overallStr = overallStr + per_row_str + "\n"
    
  for rows_ in smoted_dataset: 
    per_row_str=""  
    for elem in rows_: 
      per_row_str = per_row_str + str(elem) + ","       
    per_row_str = per_row_str  + str(minClassVal)     
    overallStr = overallStr + per_row_str + "\n"    

  fileToWrite = open(file_to_write, 'w')
  fileToWrite.write(overallStr )  
  fileToWrite.close()     

def write_smoted_values_to_file_12_clusters(datasets_param, levels_param, fileParam):    
  len_label = len(levels_param)
  len_dataset = len(datasets_param)
  overallStr=""
  if len_dataset==len_label: 
    for cnt in xrange(len_label):
      level_   = levels_param[cnt]   
      dataset_ = datasets_param[cnt]
      for rows_ in dataset_: 
        per_row_str=""  
        for elem in rows_: 
          per_row_str = per_row_str + str(elem) + ","       
        per_row_str = per_row_str  + str(level_)     
        overallStr = overallStr + per_row_str + "\n"      
  fileToWrite = open(fileParam, 'w')
  fileToWrite.write(overallStr )  
  fileToWrite.close()  



def replication(recordParam, replCountParam): 
  rec_to_ret =[]  
  for row_ in recordParam: 
    for cnt in xrange(replCountParam): 
      rec_to_ret.append(row_) 
  return rec_to_ret          




def write_smoted_values_to_file_13_clusters(datasets_param, levels_param, fileParam):    
  len_label = len(levels_param)
  len_dataset = len(datasets_param)
  overallStr=""
  if len_dataset==len_label: 
    for cnt in xrange(len_label):
      level_   = levels_param[cnt]   
      dataset_ = datasets_param[cnt]
      for rows_ in dataset_: 
        per_row_str=""  
        for elem in rows_: 
          per_row_str = per_row_str + str(elem) + ","       
        per_row_str = per_row_str  + str(level_)     
        overallStr = overallStr + per_row_str + "\n"      
  fileToWrite = open(fileParam, 'w')
  fileToWrite.write(overallStr )  
  fileToWrite.close()     