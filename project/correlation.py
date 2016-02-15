# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 23:09:46 2016

@author: akond
"""



def doCorrelation(vectorX, vectorY):
    corrList_=[]
    #from minepy import minepy
    from scipy import stats
    import minepy
    ## do not chnage alpha and c in the following line     
    minedValue  = minepy.minestats(vectorX, vectorY, alpha=0.6, c=15)
    spearmanValue = stats.spearmanr(vectorX, vectorY)
    pearsonValue = stats.pearsonr(vectorX, vectorY)
    corrList_ =[pearsonValue[0] , pearsonValue[1],  spearmanValue[0], spearmanValue[1], minedValue['mic'], minedValue['nonlinearity']]

    return corrList_       
    


def performCorrBasedOnIndiMetrics(sanitizedVersionsWithVScoreParam, sanitizedVersionsWithCodeQParam):
############################CORRRELATION ZONE ##############################
  sanitizedVersionsWithScore = sanitizedVersionsWithVScoreParam 
  sanitizedVersions = sanitizedVersionsWithCodeQParam
  vScoreList=[]
  classCountList = []
  lineOfStringsList = []
  funcList  =  []
  dupl_LineList = []
  #
  tot_complexityList, class_complexityList, function_complexityList, commentLinesList=[], [], [], []
  comment_lines_densityList, duplicated_lines_densityList, filesCountList, directoriesCountList = [], [], [], []
  file_complexityList, violationsCountList, duplicated_blocksCntList, duplicated_filesCntList = [], [], [], []
  linesCntList, blocker_violationsCntList, critical_violationsCntList, major_violationsCntList = [], [], [], []
  #
  minor_violationsCntList = []

  for k_, v_ in  sanitizedVersionsWithScore.items():
    vScoreList.append(v_)
    
    classCountList.append(sanitizedVersions[k_][0])      
    lineOfStringsList.append(sanitizedVersions[k_][1])
    funcList.append(sanitizedVersions[k_][2])      
    dupl_LineList.append(sanitizedVersions[k_][3])  
    
    tot_complexityList.append(sanitizedVersions[k_][4])      
    class_complexityList.append(sanitizedVersions[k_][5])
    function_complexityList.append(sanitizedVersions[k_][6])      
    commentLinesList.append(sanitizedVersions[k_][7])  
    
    comment_lines_densityList.append(sanitizedVersions[k_][8])      
    duplicated_lines_densityList.append(sanitizedVersions[k_][9])
    filesCountList.append(sanitizedVersions[k_][10])      
    directoriesCountList.append(sanitizedVersions[k_][11])    
    
    file_complexityList.append(sanitizedVersions[k_][12])      
    violationsCountList.append(sanitizedVersions[k_][13])
    duplicated_blocksCntList.append(sanitizedVersions[k_][14])      
    duplicated_filesCntList.append(sanitizedVersions[k_][15])  
    
    linesCntList.append(sanitizedVersions[k_][16])      
    blocker_violationsCntList.append(sanitizedVersions[k_][17])
    critical_violationsCntList.append(sanitizedVersions[k_][18])      
    major_violationsCntList.append(sanitizedVersions[k_][19])    

    minor_violationsCntList.append(sanitizedVersions[k_][20])  

  print "------------------"  
  print "Correlating vScore and classCount" 
  _corr_score = doCorrelation(classCountList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and lineWithStrings " 
  _corr_score = doCorrelation(lineOfStringsList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and noOfFunctions " 
  _corr_score = doCorrelation(funcList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and noOfDuplicatedLines " 
  _corr_score = doCorrelation(dupl_LineList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])    
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and totComplexity " 
  _corr_score = doCorrelation(tot_complexityList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])    
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and classComplexity " 
  _corr_score = doCorrelation(class_complexityList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and funcCmplexity " 
  _corr_score = doCorrelation(function_complexityList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and commentsLines " 
  _corr_score = doCorrelation(commentLinesList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and commentsLineDensity " 
  _corr_score = doCorrelation(comment_lines_densityList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and duplicatedLineDensity " 
  _corr_score = doCorrelation(duplicated_lines_densityList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and no of Files " 
  _corr_score = doCorrelation(filesCountList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and no. of directories  " 
  _corr_score = doCorrelation(directoriesCountList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and fileComplexity " 
  _corr_score = doCorrelation(file_complexityList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and no. of violations  " 
  _corr_score = doCorrelation(violationsCountList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5]) 
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and duplicated block count  " 
  _corr_score = doCorrelation(duplicated_blocksCntList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])   
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and duplicated files count " 
  _corr_score = doCorrelation(duplicated_filesCntList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and total lines " 
  _corr_score = doCorrelation(linesCntList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and blocker violations count " 
  _corr_score = doCorrelation(blocker_violationsCntList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and critical violations " 
  _corr_score = doCorrelation(critical_violationsCntList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and major violations  " 
  _corr_score = doCorrelation( major_violationsCntList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
  _corr_score = []
  print "------------------"    
  print "Correlating vScore and minor violations  " 
  _corr_score = doCorrelation( minor_violationsCntList, vScoreList)  
  print "Pearson:{}, P-P:{}, Spaeramn:{}, S-P:{}, MIC:{}, Non-Linearity:{}".format(_corr_score[0], _corr_score[1], _corr_score[2], _corr_score[3], _corr_score[4], _corr_score[5])  
############################CORRRELATION ZONE ##############################   



import sanityCheck, utility
dbFileName="/Users/akond/Documents/Spring-2016/CSC522/OSSAndroidAppDataset/androSec.db"
import DataExtractionFromTables as DEFT
#import correlation as corr_
versionAndCodeQualityDict =  DEFT.getValuesFrom_CodingStandard(dbFileName)
sanitizedVersions_CQ = sanityCheck.getCodeQualityofVersions(versionAndCodeQualityDict)
print "Sanitized versions that will be used in study ", len(sanitizedVersions_CQ)
#print "Sanitized versions ..." , sanitizedVersions
##### all the vulnerability versions started 
sanitizedVersionsWithScore = sanityCheck.getVulnerbailityScoreOfSelectedVersions(sanitizedVersions_CQ)
### call for correlation 
#performCorrBasedOnIndiMetrics(sanitizedVersionsWithScore, sanitizedVersions_CQ)
##### all the vulnerability versions ended 



#######  high vScore versions started  
medianScore = 51.11111
high_CQ_dict = utility.getHighVScoreVersions_CQ( sanitizedVersionsWithScore , sanitizedVersions_CQ , medianScore)
high_vScore_Dict = utility.getHighVScoreVersions_VScore(sanitizedVersionsWithScore, medianScore)
### call for correlation 
#performCorrBasedOnIndiMetrics(high_vScore_Dict, high_CQ_dict)
#######  high vScore versions ended   


#######  low vScore versions started  
medianScore = 51.11111
low_CQ_dict = utility.getLowVScoreVersions_CQ( sanitizedVersionsWithScore , sanitizedVersions_CQ , medianScore)
low_vScore_Dict = utility.getLowVScoreVersions_VScore(sanitizedVersionsWithScore, medianScore)
### call for correlation 
performCorrBasedOnIndiMetrics(low_vScore_Dict, low_CQ_dict)
#######  low vScore versions ended    