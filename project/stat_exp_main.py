# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 18:52:13 2016

@author: akond
"""



import stat_exp_classifiers , IO_, stat_utility , a12_utility 
import sys 



def getData(fileNameParam): 
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  
  trainData = testAndTrainData[0]
  testData = testAndTrainData[1]    
 
  return trainData, testData   

def runs(runCntParam, file_Param):
  all_accu_lists, all_moea_lists = []   , []
  
  rndfor_accu , rndfor_moea =[], []
  svm_accu , svm_moea =[], []
  knn_accu , knn_moea =[], []
  cart_accu , cart_moea =[], []
  gnb_accu , gnb_moea =[], []
  
  testAndTrainData  = getData(file_Param)  
  trainingData = testAndTrainData[0]
  testData = testAndTrainData[1]
  #print runCntParam
  for cnt_index in xrange(runCntParam):
      
    #print "This is 'experiemnt_random_forest' "    
    accu, moea = stat_exp_classifiers.runRandomForest(trainingData, testData) 
    rndfor_accu.append(accu) 
    rndfor_moea.append(moea)
    accu, moea = 0,0     
    
    #print "This is 'experiemnt_svm' "    
    accu, moea = stat_exp_classifiers.runSVM(trainingData, testData) 
    svm_accu.append(accu) 
    svm_moea.append(moea)  
    accu, moea = 0,0          
    
    #print "This is 'experiemnt_knn' "    
    accu, moea = stat_exp_classifiers.runKNN(trainingData, testData) 
    knn_accu.append(accu) 
    knn_moea.append(moea)  
    accu, moea = 0,0             
    
    
    #print "This is 'experiemnt_CART' "    
    accu, moea = stat_exp_classifiers.runCART(trainingData, testData) 
    cart_accu.append(accu) 
    cart_moea.append(moea)  
    accu, moea = 0,0                
    
    #print "This is 'experiemnt_GNB' "    
    accu, moea = stat_exp_classifiers.runGNB(trainingData, testData) 
    gnb_accu.append(accu) 
    gnb_moea.append(moea)  
    accu, moea = 0,0    

  ## appending all 
  all_accu_lists.append( rndfor_accu ) 
  all_accu_lists.append(svm_accu) 
  all_accu_lists.append(knn_accu) 
  all_accu_lists.append(cart_accu) 
  all_accu_lists.append( gnb_accu )
  
  all_moea_lists.append(rndfor_moea) 
  all_moea_lists.append(svm_moea) 
  all_moea_lists.append(knn_moea) 
  all_moea_lists.append(cart_moea) 
  all_moea_lists.append(gnb_moea)
  
  return all_accu_lists, all_moea_lists 



def stat_hypo_test_(valueListParam): 
  for value_for_one_classifier in valueListParam: 
    comparer = value_for_one_classifier  
    comparees = [x for x in valueListParam if x!=value_for_one_classifier] 
    for comparee_item in comparees: 
      #print "comparer: {}, comapree: {}".format(comparer, comparee_item)  
      t_test_results = stat_utility.do_T_Test_("greater", comparer, comparee_item)
      print "-----"          
      print "Two sample t-test results : (TS, df, p-value) "
      print t_test_results   
      print "-----"                



def stat_a12_test_(valueListParam): 
  for value_for_one_classifier in valueListParam: 
    comparer = value_for_one_classifier  
    comparees = [x for x in valueListParam if x!=value_for_one_classifier] 
    print "---"
    for comparee_item in comparees: 
      #print "comparer: {}, comapree: {}".format(comparer, comparee_item)  
      a12_results = a12_utility.doSlowA12(comparer, comparee_item)
      print "----->", a12_results   

####### Open loggger ####
old_stdout = sys.stdout
output_file_name="a12_res_.txt"
log_file = open( output_file_name,  "w")
sys.stdout = log_file  

print "Started at: ", IO_.giveTimeStamp()
count=100000
file_="12_NonZeroDataset_Aggolo.csv"
all_accu_moea = runs(count, file_)
all_acuu = all_accu_moea[0]
all_moea = all_accu_moea[1]
#print "**************** Hypo. tests for Accuracy  ****************"
#stat_hypo_test_(all_acuu)
#print "**************** Hypo. tests for Mean Abs. Error  ****************"
#stat_hypo_test_(all_moea)
print "**************** A12 tests for Accuracy  ****************"
stat_a12_test_(all_acuu)
print "**************** A12 tests for Mean Abs. Error  ****************"
stat_a12_test_(all_moea)
print "Ended at: ", IO_.giveTimeStamp() 




#### close logger       
sys.stdout = old_stdout
log_file.close()        