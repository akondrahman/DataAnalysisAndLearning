# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:28:27 2016

@author: akond
"""



import DataExtractionFromTables as DEFT, sanityCheck, utility , IO_, logiRegre as LGR
def experiemnt_one(dbFileName):
	print "Performing experiment # 1"
	#import correlation as corr_
	versionAndCodeQualityDict =  DEFT.getValuesFrom_CodingStandard(dbFileName)
	sanitizedVersions = sanityCheck.getCodeQualityofVersions(versionAndCodeQualityDict)
	print "Sanitized versions that will be used in study ", len(sanitizedVersions)
	#print "Sanitized versions ..." , sanitizedVersions
	sanitizedVersionsWithScore = sanityCheck.getVulnerbailityScoreOfSelectedVersions(sanitizedVersions)

	'''
	Stats on risk score-->len=721, median=51.1111111111,  mean=38.0255199862, max=53.3333333333, min=0.0,
	'''







	############################## 
	sanitizedVersions_CQ = sanitizedVersions

	#######  high vScore versions started  
	threshold = 51.1111111111
	high_CQ_dict = utility.getHighVScoreVersions_CQ( sanitizedVersionsWithScore , sanitizedVersions_CQ , threshold)
	high_vScore_Dict = utility.getHighVScoreVersions_VScore(sanitizedVersionsWithScore, threshold)
	print "high_vscore_versions ", len(high_vScore_Dict)
	#######  high vScore versions ended   


	#######  low vScore versions started  
	low_CQ_dict = utility.getLowVScoreVersions_CQ( sanitizedVersionsWithScore , sanitizedVersions_CQ , threshold)
	low_vScore_Dict = utility.getLowVScoreVersions_VScore(sanitizedVersionsWithScore, threshold)
	print "len_vscore_versions ", len(low_vScore_Dict)
	#######  low vScore versions ended   
	##### dumpin time 
	### three ways: first by dumping all highs then all lows 
	themegaFile_Seperated = "all-CQ-HL-Seperated.csv"
	IO_.dumpIntoFileByHighAndLow( themegaFile_Seperated, high_CQ_dict, low_CQ_dict )

	### three ways : second by dumping as it si 
	themegaFile_All = "all-CQ-HL.csv"
	IO_.dumpIntoFile( themegaFile_All,sanitizedVersions_CQ , sanitizedVersionsWithScore, threshold, False )
	LGR.performLogiRegression(themegaFile_All)
 




def experiemnt_two(dbFileName):

	print "Performing experiemnt # 2"
	#import correlation as corr_
	versionAndCodeQualityDict =  DEFT.getValuesFrom_CodingStandard(dbFileName)
	sanitizedVersions = sanityCheck.getCodeQualityofVersions(versionAndCodeQualityDict)
	print "Sanitized versions that will be used in study ", len(sanitizedVersions)
	#print "Sanitized versions ..." , sanitizedVersions
	NonZero_sanitizedVersionsWithScore = sanityCheck.getNonZeroVulnerbailityScoreOfSelectedVersions(sanitizedVersions)

	'''
	  Stats on risk score (non-zero elemnts)-->len=549, median=51.1111111111,  mean=49.9387976503, max=53.3333333333, min=15.0	
	'''

	############################## 
	sanitizedVersions_CQ = sanitizedVersions

	#######  high vScore versions started  
	threshold = 51.1111111111
	high_CQ_dict = utility.getHighVScoreVersions_CQ( NonZero_sanitizedVersionsWithScore , sanitizedVersions_CQ , threshold)
	high_vScore_Dict = utility.getHighVScoreVersions_VScore(NonZero_sanitizedVersionsWithScore, threshold)
	print "non zero high_vscore_versions ", len(high_vScore_Dict)
	#######  high vScore versions ended   


	#######  low vScore versions started  
	low_CQ_dict = utility.getLowVScoreVersions_CQ( NonZero_sanitizedVersionsWithScore , sanitizedVersions_CQ , threshold)
	low_vScore_Dict = utility.getLowVScoreVersions_VScore(NonZero_sanitizedVersionsWithScore, threshold)
	print "non zero  len_vscore_versions ", len(low_vScore_Dict)
	#######  low vScore versions ended   
	##### dumpin time 
	### three ways: first by dumping all highs then all lows 
	themegaFile_Seperated = "non_zero_all-CQ-HL-Seperated.csv"
	IO_.dumpIntoFileByHighAndLow( themegaFile_Seperated, high_CQ_dict, low_CQ_dict )

	### three ways : second by dumping as it si 
	themegaFile_All = "non_zero_all-CQ-HL.csv"
	IO_.dumpIntoFile( themegaFile_All,sanitizedVersions_CQ , NonZero_sanitizedVersionsWithScore, threshold, False )
	LGR.performLogiRegression(themegaFile_All)  
