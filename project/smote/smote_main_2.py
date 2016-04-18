# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 21:09:09 2016

@author: akond
"""



import numpy as np
import smote_utility , smote 
fileName_="2_NonZeroDataset_Aggolo.csv"
the_data_set = smote_utility.readCSVAsArray(fileName_) 
#print the_data_set
# get the distribution per clss 
counter_dict = smote_utility.getCountPerClass(the_data_set)
print counter_dict
# get the records per sample 
classVal = float(0)
records_per_class_0 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_0)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 3000
nearest_nieghbors = 10 
smoted_dataset = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: ", smoted_dataset.shape 
#print "smoted dataset .... \n ", smoted_dataset
classVal = float(1)
records_per_class_1 = smote_utility.getRecordsPeClass(classVal, the_data_set)
print "majority dataset shape: ", len(records_per_class_1)
smote_utility.write_smoted_values_to_file_two_clusters( records_per_class_1 , 1, 
                                                       smoted_dataset , 0  , "smoted_2_clusters.csv")
