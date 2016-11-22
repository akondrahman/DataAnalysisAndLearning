# -*- coding: utf-8 -*-
"""
Created on Nov 22, 2016

@author: akond
"""



import numpy as np
import smote_utility , smote
fileName_="Exp_1_Mobilesoft_clusterified_1407.csv"
the_data_set = smote_utility.readCSVAsArray(fileName_)
counter_dict = smote_utility.getCountPerClass(the_data_set)
print counter_dict
#{0.0: 10, 1.0: 417, 2.0: 7, 3.0: 9, 4.0: 106 }
'''
formula to fix no. of samples: no_of_samples_you_want = x * no. of neighbors / 100
you have to provide x , x must be < 100 or multiple of 100
'''
print "smoting time for level 0 "
## smoting time for level 0
# get the records per sample
classVal = float(0)
records_per_class_0 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_0)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 50 ## as this is the majorityy class, nothing will be added and so, less than 100
nearest_nieghbors = 10 ### Expected n_neighbors <= n_samples, level 0 has 10 samples
smoted_dataset_0 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-0::(majority class)", smoted_dataset_0.shape
print "-----"

print "smoting time for level 1 "
## smoting time for level 1
# get the records per sample
classVal = float(1)
records_per_class_1 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_1)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 2200
nearest_nieghbors = 10 ### Expected n_neighbors <= n_samples : level has 417 samples, going with 10
smoted_dataset_2 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-2::(minority class)", smoted_dataset_2.shape
print "-----"


print "smoting time for level 2 "
## smoting time for level 2
# get the records per sample
classVal = float(2)
records_per_class_2 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_2)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 50 ## as this is the 75% of the majority class, nothing will be added and so, less than 100
nearest_nieghbors = 10 ### Expected n_neighbors <= n_samples
smoted_dataset_3 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-2::", smoted_dataset_3.shape
print "-----"


print "smoting time for level 3"
## smoting time for level 3
# get the records per sample
classVal = float(3)
records_per_class_3 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_3)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 6200
nearest_nieghbors = 10  ### Expected n_neighbors <= n_samples
smoted_dataset_3 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-3::", smoted_dataset_3.shape
print "-----"


print "smoting time for level 4 "
## smoting time for level 4
# get the records per sample
classVal = float(4)
records_per_class_4 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_4)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 5200  ##N must be < 100 or multiple of 100
nearest_nieghbors = 10  ### Expected n_neighbors <= n_samples
smoted_dataset_4 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-4::", smoted_dataset_4.shape
print "-----"
