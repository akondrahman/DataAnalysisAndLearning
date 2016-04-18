# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:46:59 2016

@author: akond
"""



import numpy as np
import smote_utility , smote 
fileName_="13_NonZeroDataset_Aggolo.csv"
the_data_set = smote_utility.readCSVAsArray(fileName_) 
#print the_data_set
# get the distribution per clss 
counter_dict = smote_utility.getCountPerClass(the_data_set)
print counter_dict

#{0.0: 393, 1.0: 106, 2.0: 2, 3.0: 3, 4.0: 6, 5.0: 3, 6.0: 7, 7.0: 6, 8.0: 6, 9.0: 7, 10.0: 5, 11.0: 4, 12.0: 1}
print "smoting time for level 1 "
## smoting time for level 1
# get the records per sample 
classVal = float(1)
records_per_class_1 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_1)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 300
nearest_nieghbors = 10  ### Expected n_neighbors <= n_samples
smoted_dataset_1 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-1::", smoted_dataset_1.shape 
print "-----"


print "smoting time for level 2 "
## smoting time for level 2
# get the records per sample 
classVal = float(2)
records_per_class_2 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_2)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 15000
nearest_nieghbors = 2  ### Expected n_neighbors <= n_samples
smoted_dataset_2 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-2::", smoted_dataset_2.shape 
print "-----"


print "smoting time for level 3"
## smoting time for level 3
# get the records per sample 
classVal = float(3)
records_per_class_3 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_3)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 10000
nearest_nieghbors = 3  ### Expected n_neighbors <= n_samples
smoted_dataset_3 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-3::", smoted_dataset_3.shape 
print "-----"


print "smoting time for level 4"
## smoting time for level 4
# get the records per sample 
classVal = float(4)
records_per_class_4 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_4)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 5000
nearest_nieghbors = 6  ### Expected n_neighbors <= n_samples
smoted_dataset_4 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-4::", smoted_dataset_4.shape 
print "-----"


print "smoting time for level 5"
## smoting time for level 5
# get the records per sample 
classVal = float(5)
records_per_class_5 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_5)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 10000
nearest_nieghbors = 3  ### Expected n_neighbors <= n_samples
smoted_dataset_5 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-5::", smoted_dataset_5.shape 
print "-----"


print "smoting time for level 6"
## smoting time for level 6
# get the records per sample 
classVal = float(6)
records_per_class_6 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_6)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 4300
nearest_nieghbors = 7  ### Expected n_neighbors <= n_samples
smoted_dataset_6 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-6::", smoted_dataset_6.shape 
print "-----"


print "smoting time for level 7"
## smoting time for level 7
# get the records per sample 
classVal = float(7)
records_per_class_7 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_7)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 5000
nearest_nieghbors = 6  ### Expected n_neighbors <= n_samples
smoted_dataset_7 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-7::", smoted_dataset_7.shape 
print "-----"


print "smoting time for level 8"
## smoting time for level 8
# get the records per sample 
classVal = float(8)
records_per_class_8 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_8)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 5000
nearest_nieghbors = 6  ### Expected n_neighbors <= n_samples
smoted_dataset_8 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-8::", smoted_dataset_8.shape 
print "-----"


print "smoting time for level 9"
## smoting time for level 9
# get the records per sample 
classVal = float(9)
records_per_class_9 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_9)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 4300
nearest_nieghbors = 7  ### Expected n_neighbors <= n_samples
smoted_dataset_9 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-9::", smoted_dataset_9.shape 
print "-----"


print "smoting time for level 10"
## smoting time for level 10
# get the records per sample 
classVal = float(10)
records_per_class_10 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_10)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 6000
nearest_nieghbors = 5  ### Expected n_neighbors <= n_samples
smoted_dataset_10 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-10::", smoted_dataset_10.shape 
print "-----"


print "smoting time for level 11"
## smoting time for level 11
# get the records per sample 
classVal = float(11)
records_per_class_11 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_
array_shaped_record = np.array(records_per_class_11)
print "original datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 7500
nearest_nieghbors = 4  ### Expected n_neighbors <= n_samples
smoted_dataset_11 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-11::", smoted_dataset_11.shape 
print "-----"


print "smoting time for level 12"
## smoting time for level 12
# get the records per sample 
classVal = float(12)
records_per_class_12 = smote_utility.getRecordsPeClass(classVal, the_data_set)
#print records_per_class_12
### replication zone started 
## how many times to replicate? 
replCount=2
replicated_records_per_class_12 = smote_utility.replication(records_per_class_12, replCount)
### replication zone ended 
array_shaped_record = np.array(replicated_records_per_class_12)
print "original (replictaed) datatset ", array_shaped_record.shape
count_extra_synthetic_samples = 15000
nearest_nieghbors = 2  ### Expected n_neighbors <= n_samples
smoted_dataset_12 = smote.SMOTE(array_shaped_record.shape, array_shaped_record, count_extra_synthetic_samples, nearest_nieghbors)
print "smoted dataset shape: level-12::", smoted_dataset_12.shape 
print "-----"


########## dumping time 
classVal = float(0)
records_per_class_0 = smote_utility.getRecordsPeClass(classVal, the_data_set)
print "majority dataset shape: ", len(records_per_class_0)
datasets_to_write = [records_per_class_0, smoted_dataset_1, smoted_dataset_2, smoted_dataset_3, 
                     smoted_dataset_4, smoted_dataset_5, smoted_dataset_6, smoted_dataset_7, 
                     smoted_dataset_8, smoted_dataset_9, smoted_dataset_10, smoted_dataset_11, 
                     smoted_dataset_12 ]
levels=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0] 
smote_utility.write_smoted_values_to_file_13_clusters(datasets_to_write, levels , "smoted_13_clusters.csv")                    