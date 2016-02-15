# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:00:51 2016

@author: akond
"""



import sanityCheck
dbFileName="/Users/akond/Documents/Spring-2016/CSC522/OSSAndroidAppDataset/androSec.db"
import DataExtractionFromTables as DEFT
#import correlation as corr_
versionAndCodeQualityDict =  DEFT.getValuesFrom_CodingStandard(dbFileName)
sanitizedVersions = sanityCheck.getCodeQualityofVersions(versionAndCodeQualityDict)
print "Sanitized versions that will be used in study ", len(sanitizedVersions)
#print "Sanitized versions ..." , sanitizedVersions
sanitizedVersionsWithScore = sanityCheck.getVulnerbailityScoreOfSelectedVersions(sanitizedVersions)





