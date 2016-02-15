# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 01:49:15 2016

@author: akond
"""



def dumpIntoFile(fileNameP,  high_CQ_dictParam, low_CQ_dictParam): 
  Str1= "versionID, classes, ncloc, functions, duplicated_lines, complexity, class_complexity, function_complexity,  "
  #Str1= " classes, ncloc, functions, duplicated_lines, complexity, class_complexity, function_complexity,  "  
  Str2= "comment_lines, comment_lines_density, duplicated_lines_density, files, directories, file_complexity, violations, "
  Str3= "duplicated_blocks, duplicated_files, lines, blocker_violations, critical_violations, major_violations, minor_violations"  
  header = Str1 + Str2 + Str3 + "," + "class_vscore" + ",NULL"
  strToWrite=""
  delimiter=","  
  allLinestr = ""
  ## gettign the high ones 
  for h_k_, h_v_ in high_CQ_dictParam.items():
    perLineStr = ""    
    perLineStr = perLineStr + str(h_k_) + delimiter
    for item  in h_v_:
      perLineStr = perLineStr  + str(item)    + delimiter
    perLineStr = perLineStr + str(1) + delimiter 
    allLinestr = allLinestr + perLineStr + "\n"
  ## gettign the low ones     
  for l_k_, l_v_ in low_CQ_dictParam.items():
    perLineStr = ""    
    perLineStr = perLineStr + str(l_k_) + delimiter
    for item  in l_v_:
      perLineStr = perLineStr  + str(item)    + delimiter
    perLineStr = perLineStr + str(0) + delimiter 
    allLinestr = allLinestr + perLineStr + "\n"    
    
  strToWrite = header + "\n"  + allLinestr  + "\n" 
  writeStrToFile(fileNameP, strToWrite)  
    
    
    
def writeStrToFile(fileName, strToWrite):
  #import os
  fileParam =  fileName 
  fileToWrite = open( fileParam, 'w')
  fileToWrite.write(strToWrite + "\n")  
  fileToWrite.close()   
    