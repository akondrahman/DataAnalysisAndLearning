# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:00:51 2016

@author: akond
"""



import sanityCheck, utility, IO_,  pandas as pd
dbFileName="/Users/akond/Documents/Spring-2016/CSC522/OSSAndroidAppDataset/androSec.db"
import DataExtractionFromTables as DEFT
#import correlation as corr_
versionAndCodeQualityDict =  DEFT.getValuesFrom_CodingStandard(dbFileName)
sanitizedVersions = sanityCheck.getCodeQualityofVersions(versionAndCodeQualityDict)
print "Sanitized versions that will be used in study ", len(sanitizedVersions)
#print "Sanitized versions ..." , sanitizedVersions
sanitizedVersionsWithScore = sanityCheck.getVulnerbailityScoreOfSelectedVersions(sanitizedVersions)






############################## 
sanitizedVersions_CQ = sanitizedVersions

#######  high vScore versions started  
medianScore = 51.11111
high_CQ_dict = utility.getHighVScoreVersions_CQ( sanitizedVersionsWithScore , sanitizedVersions_CQ , medianScore)
high_vScore_Dict = utility.getHighVScoreVersions_VScore(sanitizedVersionsWithScore, medianScore)
print "high_vscore_versions ", len(high_vScore_Dict)
#######  high vScore versions ended   


#######  low vScore versions started  
medianScore = 51.11111
low_CQ_dict = utility.getLowVScoreVersions_CQ( sanitizedVersionsWithScore , sanitizedVersions_CQ , medianScore)
low_vScore_Dict = utility.getLowVScoreVersions_VScore(sanitizedVersionsWithScore, medianScore)
print "len_vscore_versions ", len(low_vScore_Dict)
#######  low vScore versions ended   
##### dumpin time 
themegaFile = "all-CQ-HL.csv"
IO_.dumpIntoFile( themegaFile, high_CQ_dict, low_CQ_dict )
colNames=[ "versionID", "classes", "ncloc", "functions" , "duplicated_lines", "complexity", "class_complexity", "function_complexity",
           "comment_lines", "comment_lines_density", "duplicated_lines_density", "files", "directories", "file_complexity", "violations", 
           "duplicated_blocks", "duplicated_files", "lines", "blocker_violations", "critical_violations", "major_violations", "minor_violations" , "class_vscore", "NULL" ]
#print len(colNames)
indics=[ _ for _ in xrange(24) ]
df = pd.read_csv(themegaFile, names=colNames, usecols=indics)
#print df.head()
#print df.describe()
#print df.columns
train_cols = df.columns[1:23]
trainData  = df[train_cols]
print trainData
print "Done ;-)"
