# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 21:35:19 2016

Contents of thsi file are collected from 
Dr. Tim Menzies from his CSC 591 class 

"""



class o():
  "Anonymous container"
  def __init__(i,**fields) :
    i.override(fields)
  def override(i,d): i.__dict__.update(d); return i

 # def __repr__(i):
 #   d = i.__dict__
 #   name = i.__class__.__name__
 #   return name+'{'+' '.join([':%s %s' % (k,pretty(d[k]))
 #                    for k in i.show()])+ '}'
  def show(i):
    return [k for k in sorted(i.__dict__.keys())
            if not "_" in k]


#Note: This is a12 FAST
#Oder matters ... how often more is the first list to that of the secodn list 
def doFastA12(lst1,lst2):
  """how often is lst1 often more than y in lst2?
  assumes lst1 nums are meant to be greater than lst2"""

  def loop(t,t1,t2):
    while t1.m < t1.n and t2.m < t2.n:
      h1 = t1.l[t1.m] #mth element of list 1
      h2 = t2.l[t2.m] #mth element of list 2
      h3 = t2.l[t2.m+1] if t2.m+1 < t2.n else None # next element if it is not end of list else None
      # print "h1:", h1, ""
      if h1 > h2:
        t1.m  += 1; t1.gt += t2.n - t2.m
      elif h1 == h2:
        # if h3 and gt(h1,h3) < 0:
        if h3 and h1 > h3:
            t1.gt += t2.n - t2.m  - 1
        t1.m  += 1; t1.eq += 1; t2.eq += 1
      else:
        t2,t1  = t1,t2
    return t.gt*1.0, t.eq*1.0
  #--------------------------
  lst1 = sorted(lst1,reverse=True)
  lst2 = sorted(lst2,reverse=True)
  n1   = len(lst1)
  n2   = len(lst2)
  t1   = o(l=lst1,m=0,eq=0,gt=0,n=n1)
  t2   = o(l=lst2,m=0,eq=0,gt=0,n=n2)
  # print t1
  gt,eq= loop(t1, t1, t2)
  a12_value=gt/(n1*n2) + eq/2/(n1*n2)
  return a12_value
  
  
def doSlowA12(vec1, vec2):
    ## this code is inheried from Dr. Menzies   
    ## Are eleemnts of vector 1 overall better than vector 2 ? order amtters ... see: line 42
    if (len(vec1)==0) or (len(vec2)==0):
     print "One of the vectors is invalied for A12 test !"
     return 0
    else:  
     more = same = 0.0
     for x in sorted(vec1):
      for y in sorted(vec2):
        if   x==y : 
          same += 1
        elif x > y : 
          more += 1
     return (more + 0.5*same) / (len(vec1)*len(vec2))      
     
   
   
#baal= [1, 2, 3]
#saal= [4, 5, 1]
### is saal greater than baal ? order matter s 
#A12_Output = doFastA12(  saal, baal)
#
#print "A12 output ", A12_Output   