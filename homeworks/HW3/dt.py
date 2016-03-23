# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 21:13:03 2016

@author: akond
"""



import pydot 
from sklearn.externals.six import StringIO  
from sklearn import tree
clf = tree.DecisionTreeClassifier()
X=[[2, 0, 1], [0, 1, 0], [1, 0, 1], [1, 1, 1], [2, 0, 1], 
   [2, 2, 1], [1, 2, 1], [0, 2, 0], [0, 2, 0], [0, 0, 0], 
   [1, 2, 0], [1, 0, 0], [1, 2, 1], [2, 2, 0] ]
Y=[0, 0, 0, 0,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
clf = clf.fit(X, Y)



dot_data = StringIO() 
#tree.export_graphviz(clf, out_file=dot_data) 
tree.export_graphviz(clf, out_file=dot_data,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = pydot.graph_from_dot_data(dot_data.getvalue())  
with open("the-tree.dot", 'w') as f:
  f = tree.export_graphviz(clf, out_file=f, filled=True, rounded=True,  special_characters=True) 
                         
#graph = pydot.graph_from_dot_data(dot_data.getvalue())
#graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
#graph.write_pdf("thetree.pdf") 
#graph = pydot.graph_from_dot_file('the-tree.dot')
#graph.write_png('the-tree.png')                         
                         
