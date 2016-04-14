import sys

#Dictionaries for paramenters for different classification models. Add parameters for all other models here.

svm_params = {'C':[1,10,50,100],'shrinking':[True,False],'tol':[1e-10,1e-5,1e-2,1e-1,1],'decision_function_shape':['ovo','ovr']}
cart_param={'criterion':['gini','entropy'],'splitter':['best','random'],'max_features':[1,5,10,15,20],'max_depth':[None,10,25,50,100,500,1000,10000],'min_samples_split':[2,4,8,10,20],'min_samples_leaf':[1,2,4,8,10],'max_leaf_nodes':[None,50,100,200,500,1000,10000]}

#TODO omitting 'mahalanobis' distance metric for now as it requires an ndarray
knn_params = {'n_neighbors':[1,10,50,100,200],'weights':['uniform','distance'],'metric':['euclidean','manhattan','chebyshev','minkowski'],'p':[3,5,10],'algorithm':['auto','ball_tree','kd_tree','brute']}

