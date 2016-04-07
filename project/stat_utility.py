# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 19:22:55 2016

@author: akond
"""



def do_T_Test_(compStrParam, vecX, vecY):
  ## order of vector, comparison string, paired=False  .... all matters  
  import rpy2.robjects as R


  #result = R.r['t.test'](R.IntVector(vecX),R.IntVector(vecY),alternative=compStrParam,paired=False,var.equal=False) 
  t_test_func_ = R.r['t.test']
  argDict  = {'var.equal':False, 'alternative':compStrParam, 'paired':False}
  result = t_test_func_(x=R.IntVector(vecX),y=R.IntVector(vecY), **argDict)  
  #print "=============================================================="
  #print result 
  #print "=============================================================="  
  #print result.r['p.value'][0][0]
  #print result.r['estimate'][0][0]
  # for paired test, if estimate > 0, then a is greater than b, else, b is greater than a (mean)
  return result[0][0],result[1][0], result[2][0]              
  
  
  
  
     