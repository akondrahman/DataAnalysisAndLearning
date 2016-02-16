# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:36:44 2016

@author: akond
"""



dbFileName="/Users/akond/Documents/Spring-2016/CSC522/OSSAndroidAppDataset/androSec.db"
import DataExtractionFromTables as DEFT
import numpy as np




def getCodeQualityofVersions(dictParam, meanFlag=True):
  versionDictToRet = {}
  versionRiskDict = DEFT.getValuesFrom_Vulnerability(dbFileName)
  ### 
  fileList = []
  for k_, v_ in versionRiskDict.items():
    versionIDInRiskDict = k_ 
    ## let us first check if the vulnerabilites scores are there for all versions if not then excluded 
    if versionIDInRiskDict in dictParam:
      fileCount =  dictParam[versionIDInRiskDict][10]
      if fileCount!=None:
        fileList.append(fileCount)  
        #print "Version #{} has #{} files".format(versionIDInRiskDict, fileCount) 
  print "Stats on file count : len={}, median={},  mean={}, max={}, min={},".format(len(fileList), np.median(fileList), np.mean(fileList), max(fileList), min(fileList))  
  

  if meanFlag: 
    thres = np.mean(fileList)
  else:
    thres = np.median(fileList)      
  for k_, v_ in versionRiskDict.items():
    versionIDInRiskDict = k_ 
    if versionIDInRiskDict in dictParam:
      fileCount =  dictParam[versionIDInRiskDict][10]
      # then lets check if the file coutn is at least the mdian file count 
      if fileCount >= thres : 
        versionDictToRet[versionIDInRiskDict] = dictParam[versionIDInRiskDict]      
  return versionDictToRet

def getVulnerbailityScoreOfSelectedVersions(dictParam):
  validDictToret={}  
  riskList=[]
  original_versionRiskDict = DEFT.getValuesFrom_Vulnerability(dbFileName)
  for k_, v_ in dictParam.items():
    ## get the scores for the valid versions 
    riskScore = original_versionRiskDict[k_]
    validDictToret[k_] = riskScore
    riskList.append(riskScore)
  print "Stats on risk score-->len={}, median={},  mean={}, max={}, min={},".format(len(riskList), np.median(riskList), np.mean(riskList), max(riskList), min(riskList))      
  return validDictToret     
        




def getNonZeroVulnerbailityScoreOfSelectedVersions(dictParam):
  validDictToret={}  
  riskList=[]
  original_versionRiskDict = DEFT.getValuesFrom_Vulnerability(dbFileName)
  for k_, v_ in dictParam.items():
    ## get the scores for the valid versions 
    riskScore = original_versionRiskDict[k_]
    if riskScore > 0:
      validDictToret[k_] = riskScore
      riskList.append(riskScore)
  print "Stats on risk score (non-zero elemnts)-->len={}, median={},  mean={}, max={}, min={},".format(len(riskList), np.median(riskList), np.mean(riskList), max(riskList), min(riskList))      
  return validDictToret         

def getVulnerbailityScoreStatus(dictParam):
  riskList=[]
  original_versionRiskDict = DEFT.getValuesFrom_Vulnerability(dbFileName)
  for k_, v_ in dictParam.items():
    ## get the scores for the valid versions 
    riskScore = original_versionRiskDict[k_]
    riskList.append(riskScore)
  return np.mean(riskList), np.median(riskList)     
#versionAndCodeQualityDict =  DEFT.getValuesFrom_CodingStandard(dbFileName)
#sanitizedVersions = getCodeQualityofVersions(versionAndCodeQualityDict)
#print "Sanitized versions that will be used in study ", len(sanitizedVersions)
##print "Sanitized versions ..." , sanitizedVersions
#sanitizedVersionsWithScore =  getVulnerbailityScoreOfSelectedVersions(sanitizedVersions)
#print "Sanitized version with contents "
#print len(sanitizedVersionsWithScore)


