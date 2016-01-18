# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:26:34 2016

@author: akond
"""



def getValuesFrom_Android_Manifest_AppInfo(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"

  cursor = conn.execute("SELECT AppID, AppName FROM Android_Manifest_AppInfo")
  dictToret={}
  for row in cursor:
     dictToret[row[0]] = row[1]

  conn.close()    
  return dictToret
  




def getValuesFrom_Android_Manifest_CommitInfo(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"
  queryStr1= "Commit_val, Author_Name, Author_Email, Commit_Date, AppID, Commit_Order, Commit_ID, "
  queryStr2= "Commit_Message, VersionCode, VersionName, minSDK, targetSDK "
  queryStr = "SELECT " + queryStr1 + queryStr2 +   " FROM Android_Manifest_CommitInfo"
  cursor = conn.execute(queryStr)
  dictToret={}
  for row in cursor:
      
     tuples=(row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
     dictToret[row[4]] = tuples 
  #print "The list ", listToret 
  #print "Operation done successfully"
  conn.close()    
  return dictToret
  
  


def getValuesFrom_android_Manifest_intent_join(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"

  cursor = conn.execute("SELECT Commit_ID, Intent_ID FROM android_Manifest_intent_join")
  dictToret={}
  for row in cursor:
     dictToret[row[0]] = row[1]

  conn.close()    
  return dictToret  
def getValuesFrom_Android_Manifest_Intent(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"

  cursor = conn.execute("SELECT Intent_ID, Intent FROM Android_Manifest_Intent")
  dictToret={}
  for row in cursor:
      dictToret[row[0]] = row[1]

  conn.close()    
  return dictToret    
  
def getValuesFrom_android_Manifest_permission_join(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"

  cursor = conn.execute("SELECT Commit_ID, Permission_ID FROM android_Manifest_permission_join")
  dictToret={}
  for row in cursor:
      dictToret[row[0]] = row[1]
  conn.close()    
  return dictToret    
  
def getValuesFrom_Android_Manifest_Permission(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"

  cursor = conn.execute("SELECT Permission_ID, Permission FROM Android_Manifest_Permission")
  dictToret={}
  for row in cursor:
      dictToret[row[0]] = row[1]
  conn.close()    
  return dictToret    
  
def  getValuesFrom_AndroriskRun(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"

  cursor = conn.execute("SELECT versionID FROM AndroriskRun")
  listToret=[]
  for row in cursor:
     tuples=row[0]
     listToret.append(tuples)
  #print "The list ", listToret 
  #print "Operation done successfully"
  conn.close()    
  return listToret       
  
def getValuesFrom_AppData(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"
  

  queryStr1= "appId, name,  categories, license, auto_name, source_code,  "
  queryStr2= "  summary,  repo_type,  "
  queryStr3= " current_version, current_build_number "  
  queryStr = "SELECT " + queryStr1 + queryStr2 +  queryStr3 + " FROM AppData"
  cursor = conn.execute(queryStr)
  dictToret={}
  for row in cursor:
     tuples=( row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
     dictToret[row[0]] = tuples 
  conn.close()    
  return dictToret
  
def getValuesFrom_CodingStandard(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"


  queryStr1= "versionID, classes, ncloc, functions, duplicated_lines, complexity, class_complexity, function_complexity,  "
  queryStr2= "comment_lines, comment_lines_density, duplicated_lines_density, files, directories, file_complexity, violations, "
  queryStr3= "duplicated_blocks, duplicated_files, lines, blocker_violations, critical_violations, major_violations, minor_violations"  
  queryStr = "SELECT " + queryStr1 + queryStr2 +  queryStr3 + " FROM CodingStandard"
  cursor = conn.execute(queryStr)
  dictToret={}
  for row in cursor:
     tuples=(
             row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], 
             row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], 
             row[19], row[20], row[21] 
            )
     dictToret[row[0]] = tuples 
  #print "The list ", listToret 
  #print "Operation done successfully"
  conn.close()    
  return dictToret  
  
  
def getValuesFrom_GitHistory(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"
  

  queryStr1= "commitID, appID,  author, email, time, summary "
  queryStr = "SELECT " + queryStr1  + " FROM GitHistory"
  cursor = conn.execute(queryStr)
  dictToret={}
  for row in cursor:
     tuples=(row[1], row[2], row[3], row[4], row[5])
     dictToret[row[0]] = tuples 
  #print "The list ", listToret 
  #print "Operation done successfully"
  conn.close()    
  return dictToret



def getValuesFrom_Intent_Version(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"

  cursor = conn.execute("SELECT intentID, versionID FROM Intent_Version")
  dictToret={}
  for row in cursor:
      dictToret[row[1]] = row[0]
  conn.close()    
  return dictToret  



  
def getValuesFrom_Intent_(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"

  cursor = conn.execute("SELECT intentID, name FROM Intent")
  dictToret={}
  for row in cursor:
      dictToret[row[0]] = row[1]
  conn.close()    
  return dictToret    
  
  
  
  
def getValuesFrom_OverPermission_(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"

  cursor = conn.execute("SELECT permissionID, versionID FROM OverPermission")
  dictToret={}
  for row in cursor:
      dictToret[row[1]] = row[0]
  conn.close()    
  return dictToret    
  
  
  
  
def getValuesFrom_Permission_(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"

  cursor = conn.execute("SELECT permissionID, name FROM Permission")
  dictToret={}
  for row in cursor:
      dictToret[row[0]] = row[1]
  conn.close()    
  return dictToret    




def getValuesFrom_UnderPermission_(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"

  cursor = conn.execute("SELECT permissionID, versionID FROM UnderPermission")
  dictToret={}
  for row in cursor:
      dictToret[row[1]] = row[0]
  conn.close()    
  return dictToret    
  
  
  
 
def getValuesFrom_Version(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"
  

  queryStr1= "versionID, appID, version, build_number, build_commit, isAPKExists  "
  queryStr = "SELECT " + queryStr1  + " FROM Version"
  cursor = conn.execute(queryStr)
  dictToret={}
  for row in cursor:
     tuples=(row[0], row[2], row[3], row[4], row[5])
     dictToret[row[1]] = tuples 

  conn.close()    
  return dictToret
  
  
  
  
def getValuesFrom_Vulnerability(dbFileParam):
  import sqlite3
  conn = sqlite3.connect(dbFileParam)
  #print "Opened database successfully"

  cursor = conn.execute("SELECT versionID, fuzzy_risk FROM Vulnerability")
  dictToret={}
  for row in cursor:
      dictToret[row[0]] = row[1]
  conn.close()    
  return dictToret 