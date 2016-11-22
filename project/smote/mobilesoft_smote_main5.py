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
