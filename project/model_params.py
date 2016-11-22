import sys

#Dictionaries for paramenters for different classification models. Add parameters for all other models here.

svm_params = {'C':         [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
              'shrinking': [True,False],
              'tol':       [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
              'decision_function_shape':['ovo','ovr']}

cart_param = {'criterion':         ['gini','entropy'],
              'splitter':          ['best','random'],
              'max_features':      [None, 'auto', 'sqrt', 'log2', 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
              'max_depth':         [None, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
              'min_samples_split': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
              'min_samples_leaf':  [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
              'max_leaf_nodes':    [None, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]}



knn_params = {'n_neighbors':[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
               'weights':['uniform','distance'],
               'metric':['euclidean','manhattan','chebyshev','minkowski'],
               'algorithm':['auto','ball_tree','kd_tree','brute']}
