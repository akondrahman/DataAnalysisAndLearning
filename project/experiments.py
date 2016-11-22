# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:28:27 2016

@author: akond
"""


from sklearn.metrics import silhouette_samples, silhouette_score
import DataExtractionFromTables as DEFT, sanityCheck, utility , IO_, logiRegre as LGR, numpy as np
def experiemnt_one(dbFileName, meanFlag, outputStrParam):
	print "Performing experiment # 1"
	#import correlation as corr_
	versionAndCodeQualityDict =  DEFT.getValuesFrom_CodingStandard(dbFileName)
	sanitizedVersions = sanityCheck.getCodeQualityofVersions(versionAndCodeQualityDict, meanFlag)
	print "Sanitized versions that will be used in study ", len(sanitizedVersions)
	#print "Sanitized versions ..." , sanitizedVersions
	sanitizedVersionsWithScore = sanityCheck.getVulnerbailityScoreOfSelectedVersions(sanitizedVersions)

	'''
	Stats on risk score-->len=721, median=51.1111111111,  mean=38.0255199862, max=53.3333333333, min=0.0,
	'''


	riskStatus = sanityCheck.getVulnerbailityScoreStatus(sanitizedVersionsWithScore)
	if meanFlag:
	 threshold = riskStatus[0]   ## first returned index is mean
	else:
	 threshold = riskStatus[1]




	##############################
	sanitizedVersions_CQ = sanitizedVersions

	#######  high vScore versions started

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
	themegaFile_Seperated = outputStrParam + "_" + "all-CQ-HL-Seperated.csv"
	IO_.dumpIntoFileByHighAndLow( themegaFile_Seperated, high_CQ_dict, low_CQ_dict )

	### three ways : second by dumping as it si
	themegaFile_All = outputStrParam + "_" + "all-CQ-HL.csv"
	IO_.dumpIntoFile( themegaFile_All,sanitizedVersions_CQ , sanitizedVersionsWithScore, threshold, False )
	LGR.performLogiRegression(themegaFile_All)





def experiemnt_two(dbFileName, meanFlag, outputStrParam ):
	print "Performing experiemnt # 2"



	#import correlation as corr_
	versionAndCodeQualityDict =  DEFT.getValuesFrom_CodingStandard(dbFileName)
	sanitizedVersions = sanityCheck.getCodeQualityofVersions(versionAndCodeQualityDict, meanFlag)
	print "Sanitized versions that will be used in study ", len(sanitizedVersions)
	#print "Sanitized versions ..." , sanitizedVersions
	NonZero_sanitizedVersionsWithScore = sanityCheck.getNonZeroVulnerbailityScoreOfSelectedVersions(sanitizedVersions)

	'''
	Stats on risk score (non-zero elemnts)-->len=549, median=51.1111111111,  mean=49.9387976503, max=53.3333333333, min=15.0
	'''

	##############################
	sanitizedVersions_CQ = sanitizedVersions


	riskStatus = sanityCheck.getVulnerbailityScoreStatus(NonZero_sanitizedVersionsWithScore)
	if meanFlag:
	 threshold = riskStatus[0]   ## first returned index is mean
	else:
	 threshold = riskStatus[1]


	#######  high vScore versions started

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
	themegaFile_Seperated = outputStrParam + "_" + "non_zero_all-CQ-HL-Seperated.csv"
	IO_.dumpIntoFileByHighAndLow( themegaFile_Seperated, high_CQ_dict, low_CQ_dict )

	### three ways : second by dumping as it si
	themegaFile_All = outputStrParam + "_" + "non_zero_all-CQ-HL.csv"
	IO_.dumpIntoFile( themegaFile_All,sanitizedVersions_CQ , NonZero_sanitizedVersionsWithScore, threshold, False )
	LGR.performLogiRegression(themegaFile_All)

def experiemnt_three(dbFileName, meanFlag, outputStrParam, clusterFlag):
	from sklearn import cluster
	import plotter
	clusteringType = None
	if clusterFlag:
		clusteringType = cluster.KMeans(n_clusters=13)
	else:
		clusteringType = cluster.AgglomerativeClustering(n_clusters=13)


	print "Performing experiemnt # 3: Clustering score into two clusters "
	versionAndCodeQualityDict =  DEFT.getValuesFrom_CodingStandard(dbFileName)
	sanitizedVersions = sanityCheck.getCodeQualityofVersions(versionAndCodeQualityDict, meanFlag)
	sanitizedVersions_CQ = sanitizedVersions
	#print "Sanitized versions that will be used in study ", len(sanitizedVersions)
	#print "Sanitized versions ..." , sanitizedVersions
	NonZero_sanitizedVersionsWithScore = sanityCheck.getNonZeroVulnerbailityScoreOfSelectedVersions(sanitizedVersions)
	#print "zzzz", len(NonZero_sanitizedVersionsWithScore)
	### dyumping scores ...

	brokenDict = utility.getVScoreList(NonZero_sanitizedVersionsWithScore)
	onlyTheNonZeroSanitizedVersionIDs, onlyTheNonZeroSanitizedVScores = brokenDict[0], brokenDict[1]
	#print "lalalaa ", onlyTheNonZeroSanitizedVScores

	#strOfScoresToDump=""
	#for elem in onlyTheNonZeroSanitizedVScores:
	#  strOfScoresToDump = strOfScoresToDump + str(elem) +  "," + "\n"

	###
	#IO_.writeStrToFile("scores_for_clustering_measure.csv", strOfScoresToDump)

	reshapedNonZerSanitizedScores = np.reshape(onlyTheNonZeroSanitizedVScores, (-1, 1))
	clusteringType.fit(reshapedNonZerSanitizedScores)
	labelsFroVersions = clusteringType.labels_
	if clusterFlag:
		centroids = clusteringType.cluster_centers_
		print "And the centroids are .... ", centroids
		NonZer_Santized_versionDictWithLabels = utility.clusterByKmeansLabel( onlyTheNonZeroSanitizedVersionIDs , labelsFroVersions)
		##### plotting clusters start
		#low_cluster_y, high_cluster_y = utility.plotClusterByLabel( onlyTheNonZeroSanitizedVersionIDs , labelsFroVersions, NonZero_sanitizedVersionsWithScore)
		#low_cluster_x = [ 22.35294118 for x in low_cluster_y]
		#hig_cluster_x = [ 50.82030058 for x in high_cluster_y]
		#plotter.createClusterPlots(low_cluster_x, low_cluster_y, hig_cluster_x, high_cluster_y)
    ##### plottign clusters end
	else:
		print "No centroids for Aggolomerative clustering"
		NonZer_Santized_versionDictWithLabels = utility.clusterByAggoloLabel( onlyTheNonZeroSanitizedVersionIDs , labelsFroVersions)
	print "And the labels are .... "
	print len(labelsFroVersions)
	cluster_labels = clusteringType.fit_predict(reshapedNonZerSanitizedScores)
	silhouette_avg = silhouette_score(reshapedNonZerSanitizedScores, cluster_labels)
	print "Silhouette average---> ", silhouette_avg




	##############################
	themegaFile_All = outputStrParam + "_" + "culsterified_non_zero_all-CQ-HL.csv"
	IO_.dumpIntoClusterifiedFile( themegaFile_All,sanitizedVersions_CQ , NonZer_Santized_versionDictWithLabels, False )
	#LGR.performLogiRegression(themegaFile_All)






def experiemnt_svm(fileNameParam):
	import classifiers
	emperiemntSplitters=[float(x)/float(10) for x in xrange(10) if x > 0]
	for elem in emperiemntSplitters:
		print "Training size: {} %".format(float(elem*100))
		classifiers.runSVM(fileNameParam, elem)
		print "---------------------------------------------------------------"



def experiemnt_correlation(dbFileName, meanFlag, outputStrParam, clusterFlag):
	import correlation
	from sklearn import cluster
	clusteringType = None
	if clusterFlag:
		clusteringType = cluster.KMeans(n_clusters=2)
	else:
		clusteringType = cluster.AgglomerativeClustering(n_clusters=2)


	print "Performing experiemnt # Correlation: Clustering score into two clusters "
	versionAndCodeQualityDict =  DEFT.getValuesFrom_CodingStandard(dbFileName)
	sanitizedVersions = sanityCheck.getCodeQualityofVersions(versionAndCodeQualityDict, meanFlag)
	sanitizedVersions_CQ = sanitizedVersions
	#print "Sanitized versions that will be used in study ", len(sanitizedVersions)
	#print "Sanitized versions ..." , sanitizedVersions
	NonZero_sanitizedVersionsWithScore = sanityCheck.getNonZeroVulnerbailityScoreOfSelectedVersions(sanitizedVersions)
	#print "zzzz", len(NonZero_sanitizedVersionsWithScore)
	brokenDict = utility.getVScoreList(NonZero_sanitizedVersionsWithScore)
	onlyTheNonZeroSanitizedVersionIDs, onlyTheNonZeroSanitizedVScores = brokenDict[0], brokenDict[1]
	#print "lalalaa ", onlyTheNonZeroSanitizedVScores
	reshapedNonZerSanitizedScores = np.reshape(onlyTheNonZeroSanitizedVScores, (-1, 1))
	clusteringType.fit(reshapedNonZerSanitizedScores)
	labelsFroVersions = clusteringType.labels_
	if clusterFlag:
		centroids = clusteringType.cluster_centers_
		print "And the centroids are .... ", centroids
		NonZer_Santized_versionDictWithLabels = utility.clusterByKmeansLabel( onlyTheNonZeroSanitizedVersionIDs , labelsFroVersions)
	else:
		print "No centroids for Aggolomerative clustering"
		NonZer_Santized_versionDictWithLabels = utility.clusterByAggoloLabel( onlyTheNonZeroSanitizedVersionIDs , labelsFroVersions)
	#print "And the labels are .... "
	#print labelsFroVersions


	#print "versionDictWithLabels"
	#print len(versionDictWithLabels)
	onlyHighV_Scores_Dict = utility.getH_Scores_ForCorr(NonZer_Santized_versionDictWithLabels, NonZero_sanitizedVersionsWithScore)
	correlation.performCorrBasedOnIndiMetrics(onlyHighV_Scores_Dict, sanitizedVersions_CQ)
def experiemnt_random_forest(fileNameParam):
	import classifiers
	emperiemntSplitters=[float(x)/float(10) for x in xrange(10) if x > 0]
	for elem in emperiemntSplitters:
		print "Training size: {} %".format(float(elem*100))
		classifiers.runRandomForest(fileNameParam, elem)
		print "---------------------------------------------------------------"



def experiemnt_qda(fileNameParam):
	import classifiers
	emperiemntSplitters=[float(x)/float(10) for x in xrange(10) if x > 0]
	for elem in emperiemntSplitters:
		print "Training size: {} %".format(float(elem*100))
		classifiers.runQDA(fileNameParam, elem)
		print "---------------------------------------------------------------"



def experiemnt_cart(fileNameParam):
	import classifiers
	emperiemntSplitters=[float(x)/float(10) for x in xrange(10) if x > 0]
	for elem in emperiemntSplitters:
		print "Training size: {} %".format(float(elem*100))
		classifiers.runCART(fileNameParam, elem)
		print "---------------------------------------------------------------"




'''
Mobilesoft zone
'''
def experiemnt_mobilesoft(dbFileName,  outputStrParam):
	from sklearn import cluster
	import plotter
	clusteringType = cluster.AgglomerativeClustering(n_clusters=5)


	print "Performing experiemnt # Mobilesoft"
	versionAndCodeQualityDict =  DEFT.getValuesFrom_CodingStandard(dbFileName)
	sanitizedVersions = sanityCheck.getMobilesoftCodeQualityVersions(versionAndCodeQualityDict, 1.00)
	sanitizedVersions_CQ = sanitizedVersions

	NonZero_sanitizedVersionsWithScore = sanityCheck.getAllVulnerbailityScoreOfSelectedVersions(sanitizedVersions)


	brokenDict = utility.getVScoreList(NonZero_sanitizedVersionsWithScore)
	onlyTheNonZeroSanitizedVersionIDs, onlyTheNonZeroSanitizedVScores = brokenDict[0], brokenDict[1]


	# strOfScoresToDump=""
	# for elem in onlyTheNonZeroSanitizedVScores:
	#   strOfScoresToDump = strOfScoresToDump + str(elem) +  "," + "\n"
	#
	# ##
	# IO_.writeStrToFile("scores_for_clustering_measure.csv", strOfScoresToDump)

	reshapedNonZerSanitizedScores = np.reshape(onlyTheNonZeroSanitizedVScores, (-1, 1))
	clusteringType.fit(reshapedNonZerSanitizedScores)
	labelsFroVersions = clusteringType.labels_
	print "No centroids for Aggolomerative clustering"
	NonZer_Santized_versionDictWithLabels = utility.clusterByAggoloLabel( onlyTheNonZeroSanitizedVersionIDs , labelsFroVersions)
	print "And the labels are .... "
	print len(labelsFroVersions)
	cluster_labels = clusteringType.fit_predict(reshapedNonZerSanitizedScores)
	silhouette_avg = silhouette_score(reshapedNonZerSanitizedScores, cluster_labels)
	print "Silhouette average---> ", silhouette_avg




	##############################
	themegaFile_All = outputStrParam + "_" + "cluster_Headered_1407.csv"
	IO_.dumpIntoClusterifiedFile( themegaFile_All,sanitizedVersions_CQ , NonZer_Santized_versionDictWithLabels )
	'''
	if you don't want headers
	'''
	# themegaFile_All = outputStrParam + "_" + "clusterified_1407.csv"
	# IO_.dumpIntoClusterifiedFile( themegaFile_All,sanitizedVersions_CQ , NonZer_Santized_versionDictWithLabels, False )
	#LGR.performLogiRegression(themegaFile_All)


def experiemnt_select_classifier(dbFileName, meanFlag, outputStrParam, clusterFlag, scoreTypeParam):
	from sklearn import cluster
	from sklearn.metrics import silhouette_samples, silhouette_score, v_measure_score, adjusted_mutual_info_score, completeness_score

	scoreListToret=[]
	print "Performing experiemnt: Select Classifier"
	clusters=[x for x in xrange(100) if x > 1 ]
	#clusters=[2]
	for clsuter_cnt in clusters:
		print "this is iteration #", clsuter_cnt
		versionAndCodeQualityDict =  DEFT.getValuesFrom_CodingStandard(dbFileName)
		sanitizedVersions = sanityCheck.getCodeQualityofVersions(versionAndCodeQualityDict, meanFlag)
		sanitizedVersions_CQ = sanitizedVersions

		NonZero_sanitizedVersionsWithScore = sanityCheck.getNonZeroVulnerbailityScoreOfSelectedVersions(sanitizedVersions)
		#print "zzzz", len(NonZero_sanitizedVersionsWithScore)
		brokenDict = utility.getVScoreList(NonZero_sanitizedVersionsWithScore)
		onlyTheNonZeroSanitizedVersionIDs, onlyTheNonZeroSanitizedVScores = brokenDict[0], brokenDict[1]
		#print "lalalaa ", onlyTheNonZeroSanitizedVScores
		reshapedNonZerSanitizedScores = np.reshape(onlyTheNonZeroSanitizedVScores, (-1, 1))
		clusteringType = None
		if clusterFlag:
			clusteringType = cluster.KMeans(n_clusters=clsuter_cnt)
		else:
			clusteringType = cluster.AgglomerativeClustering(n_clusters=clsuter_cnt)

		cluster_labels = clusteringType.fit_predict(reshapedNonZerSanitizedScores)
		scores=0
		if scoreTypeParam==0:
			scores = silhouette_score(reshapedNonZerSanitizedScores, cluster_labels)
			score_type='Silhouette'
		# elif scoreTypeParam==1:
		# 	scores = v_measure_score(reshapedNonZerSanitizedScores, cluster_labels)
		# 	score_type='V-measure'
		# elif scoreTypeParam==2:
		# 	scores = adjusted_mutual_info_score(reshapedNonZerSanitizedScores, cluster_labels)
		# 	score_type='adjusted mutual info'
		# elif scoreTypeParam==3:
		# 	scores = completeness_score(reshapedNonZerSanitizedScores, cluster_labels)
		# 	score_type='completeness'
		score_combo = (clsuter_cnt, scores)
		scoreListToret.append(score_combo)
		print "::::: score_type={}, For n_clusters ={}, The clustering _score is ={} :::::".format(score_type, clsuter_cnt, scores)


	return scoreListToret
