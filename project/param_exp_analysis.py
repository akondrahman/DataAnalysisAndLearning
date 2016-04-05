# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:09:13 2016

@author: akond
"""



def getDictKey(indexToLookParam, dictToLookParam): 
   try:
       return list(dictToLookParam)[indexToLookParam] 
   except IndexError:
       print 'That is weird ... how did this happen?'
    
def analyzeThis(dictParam): 
  acc_ = []
  moea = []  
  for k_,v_ in dictParam.items():
    acc_.append(v_[0])   
    moea.append(v_[1]) 
  

  
  acc_high_index = acc_.index( max(acc_) )     
  acc_low_index  = acc_.index( min(acc_) )  

  moea_high_index = moea.index( max(moea) )     
  moea_low_index  = moea.index( min(moea) ) 


  
  acc_high_combo = getDictKey(acc_high_index, dictParam)     
  acc_low_combo  = getDictKey(acc_low_index, dictParam)       
  
  moea_high_combo = getDictKey(moea_high_index, dictParam)     
  moea_low_combo  = getDictKey(moea_low_index, dictParam)    

  headerForReport="Name,"+"Highest,"+"Lowest" + "\n"
  entry2="Avg.Accuracy," +str(acc_high_combo) + "," + str(acc_low_combo) + "\n"
  entry3="MAE," + str(moea_high_combo) + "," + str(moea_low_combo) + "\n"
  strToWrite = headerForReport +  entry2 + entry3 
  return strToWrite
      