'''
Akond, Dec 22, 2016
'''

from sklearn import decomposition
import IO_, sys, exp_x_classifiers
import numpy as np, pandas as pd
def getPCAedFeatures(all_features):
    '''
    PCA reff:
    1. http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.fit
    2. http://scikit-learn.org/dev/tutorial/statistical_inference/unsupervised_learning.html#principal-component-analysis-pca
    '''
    #print all_features
    pcaObj = decomposition.PCA(n_components=21)
    pcaObj.fit(all_features)
    # variance of features
    variance_of_features = pcaObj.explained_variance_
    # how much variance is explained each component
    variance_ratio_of_features = pcaObj.explained_variance_ratio_
    print "Explained varaince ratio"
    for index_ in xrange(len(variance_ratio_of_features)):
        print "Principal component#{}, explained variance:{}".format(index_+1, variance_ratio_of_features[index_])
    #print variance_ratio_of_features
    print "-"*50
    getPCAInsights(pcaObj)
    selective_feature_indices = [x_ for x_ in variance_of_features if x_ > float(1) ]
    no_features_to_use = len(selective_feature_indices)
    # see how much explained variance is covered by the number of compoenents , and set the number
    no_features_to_use = 1 #using one PCA we get >95% variance
    print "Of all the features, we will use:", no_features_to_use
    print "-"*50
    pcaObj.n_components=no_features_to_use
    selected_features = pcaObj.fit_transform(all_features)
    print "Selected feature dataset size:", np.shape(selected_features)
    print "-"*50

    return selected_features

def getPCAInsights(pcaParamObj):
    '''
    reff-1: http://stackoverflow.com/questions/22348668/pca-decomposition-with-python-features-relevances
    reff-2: http://stackoverflow.com/questions/22984335/recovering-features-names-of-explained-variance-ratio-in-pca-with-sklearn
    '''
    #print pd.DataFrame(pcaParamObj.components_)
    #lol = np.abs(pcaParamObj.components_[10]).argsort()[::-1][:3]
    #print lol
    for row_ in pcaParamObj.components_:
        print row_
        print "~"*25
def experiment_mobilesoft_random_forest(fileNameParam):
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  trainData = testAndTrainData[0]
  testData  = testAndTrainData[1]
  #print trainData
  selected_training_data = getPCAedFeatures(trainData)
  print "Size of selected training data : ", np.shape(selected_training_data)
  print "="*50
  exp_x_classifiers.runRandomForest(selected_training_data, testData, 0.90)
  print "="*50

def experiment_mobilesoft_cart(fileNameParam):
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  trainData = testAndTrainData[0]
  testData  = testAndTrainData[1]
  #print trainData
  selected_training_data = getPCAedFeatures(trainData)
  print "Size of selected training data : ", np.shape(selected_training_data)
  print "="*50
  exp_x_classifiers.runCART(selected_training_data, testData, 0.90)
  print "="*50

def experiment_mobilesoft_svm(fileNameParam):
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  trainData = testAndTrainData[0]
  testData  = testAndTrainData[1]
  #print trainData
  selected_training_data = getPCAedFeatures(trainData)
  print "Size of selected training data : ", np.shape(selected_training_data)
  print "="*50
  exp_x_classifiers.runSVM(selected_training_data, testData, 0.90)
  print "="*50

def experiment_mobilesoft_knn(fileNameParam):
  testAndTrainData = IO_.giveTestAndTrainingData(fileNameParam)
  trainData = testAndTrainData[0]
  testData  = testAndTrainData[1]
  #print trainData
  selected_training_data = getPCAedFeatures(trainData)
  print "Size of selected training data : ", np.shape(selected_training_data)
  print "="*50
  exp_x_classifiers.runKNN(selected_training_data, testData, 0.90)
  print "="*50
