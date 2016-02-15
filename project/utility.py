# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 00:18:43 2016

@author: akond
"""



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