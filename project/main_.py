# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:00:51 2016

@author: akond
"""



import DataExtractionFromTables as DEFT
dbFileName="/Users/akond/Documents/Spring-2016/CSC522/OSSAndroidAppDataset/androSec.db"

# table 1 
androidManifestAppList = DEFT.getValuesFrom_Android_Manifest_AppInfo(dbFileName)
#print "Output for androidManifestApp ... ", androidManifestAppList

# table 2
Android_Manifest_CommitInfoList = DEFT.getValuesFrom_Android_Manifest_CommitInfo(dbFileName)
#print "Output for Android_Manifest_CommitInfo ... ", Android_Manifest_CommitInfoList

#table 3
Android_Manifest_intent_joinList = DEFT.getValuesFrom_android_Manifest_intent_join(dbFileName)
#print "Output for android_Manifest_intent_join ... ", Android_Manifest_intent_joinList

#table 4
Android_Manifest_IntentList = DEFT.getValuesFrom_Android_Manifest_Intent(dbFileName)
#print "Output for Android_Manifest_IntentList ... ", Android_Manifest_IntentList


#table 5
Android_Manifest_IntentList = DEFT.getValuesFrom_Android_Manifest_Intent(dbFileName)
#print "Output for Android_Manifest_IntentList ... ", Android_Manifest_IntentList


#table 6
android_Manifest_permission_joinList = DEFT.getValuesFrom_android_Manifest_permission_join(dbFileName)
#print "Output for android_Manifest_permission_joinList ... ", android_Manifest_permission_joinList  


#table 7
Android_Manifest_PermissionList = DEFT.getValuesFrom_Android_Manifest_Permission(dbFileName)
#print "Output for Android_Manifest_PermissionList ... ", Android_Manifest_PermissionList


#table 8
Android_RiskRunList = DEFT.getValuesFrom_AndroriskRun(dbFileName)
#print "Output for Android_RiskRunList ... ", Android_RiskRunList


#table 9
AppDataList = DEFT.getValuesFrom_AppData(dbFileName)
#print "Output for AppDataList ... ", AppDataList


#table 10
CodingStandardList = DEFT.getValuesFrom_CodingStandard(dbFileName)
#print "Output for CodingStandardList ... ", CodingStandardList


#table 11
GitHistoryList = DEFT.getValuesFrom_GitHistory(dbFileName)
#print "Output for GitHistoryList ... ", GitHistoryList


#table 12
InentVersionList = DEFT.getValuesFrom_Intent_Version(dbFileName)
#print "Output for InentVersionList ... ", InentVersionList


#table 13
InentList = DEFT.getValuesFrom_Intent_(dbFileName)
#print "Output for InentList ... ", InentList


#table 14
OverPermissionList = DEFT.getValuesFrom_OverPermission_(dbFileName)
#print "Output for OverPermissionList ... ", OverPermissionList


#table 15
PermissionList = DEFT.getValuesFrom_Permission_(dbFileName)
#print "Output for PermissionList ... ", PermissionList


#table 16
UnderPermissionList = DEFT.getValuesFrom_UnderPermission_(dbFileName)
#print "Output for UnderPermissionList ... ", UnderPermissionList


#table 17
VersionList = DEFT.getValuesFrom_Version(dbFileName)
#print "Output for VersionList ... ", VersionList


#table 18
VulnerabilityList = DEFT.getValuesFrom_Vulnerability(dbFileName)
#print "Output for VulnerabilityList ... ", VulnerabilityList
