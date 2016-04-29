rm(list=ls(all=T))
#install.packages("ROCR")
#library(Rcpp)
library(monmlp)
library(RSNNS)
library(nnet)
library(ROCR)
#require(mlbench)
#require(mxnet)
### testing data 
get_test_data<- function(test_file_param1, test_file_param2)
{
  test_data_1 = read.csv(test_file_param1, sep=",", header=FALSE)
  test_data_2 = read.csv(test_file_param2, sep=",", header=FALSE)  
  #print(dim(test_data_2))
  test_data <- rbind2(test_data_1, test_data_2)
  test_data_mat <- as.matrix(test_data)
  return(test_data_mat)
}
### training data 
get_train_data<- function(train_file_param1, train_file_param2)
{
  training_data_1 = read.csv(train_file_param1, sep=",", header=FALSE)
  training_data_2 = read.csv(train_file_param2, sep=",", header=FALSE)  
  #print(dim(training_data_2))
  training_data <- rbind2(training_data_1, training_data_2)
  train_data_matrix<-as.matrix(training_data)
  return(train_data_matrix)
}

convertToCategory<- function(vectorParam)
{
  listToRet<- list()
  for( index in 1:length(vectorParam))
  {
    elem = vectorParam[index]
    strElem = toString(elem)
    listToRet[index]<-strElem
    #print(listToRet)
  }
  return(listToRet)
}


trainFile_1="dtr3.csv"
trainFile_2="dtr8.csv"
testFile_1="dte3.csv"
testFile_2="dte8.csv"
#### training data 
train_data = get_train_data(trainFile_1, trainFile_2)
#colnames(train_data) <- c("Class", paste("attrib", 2:ncol(train_data)))
#print(dim(train_data))
train_features = train_data[, -1]
train_class = as.matrix( train_data[, 1] )
#print(dim(train_class))
#train_class = convertToCategory( train_data[, 1] )
#print(train_class)
#####
##### test data 
test_data = get_test_data(testFile_1, testFile_2)
#colnames(test_data) <- c("Class", paste("attrib", 2:ncol(train_data)))
#print(dim(test_data))
test_features = test_data[, -1]
test_class = test_data[, 1] 
#print(length(test_class))
#####

### decode 
#decoded_train_class <- decodeClassLabels(train_class)
#decoded_test_class <- decodeClassLabels(test_class)
#print(length(decoded_test_class))
###

#trained_mnnet <- monmlp.fit(train_features, train_class, hidden1=3, n.ensemble=5, monotone=1, bag=TRUE)
trained_nnet <- mlp(train_features, train_class, size=50, learnFuncParams=c(0.1), maxit=100)
#trained_mnnet <- nnet(Surv~Sex+Age+Class, train_class, size=10, softmax=TRUE)
#mx.set.seed(0)
#trained_mnnet <- mx.mlp(train_features, train_class, hidden_node=10, out_node=2, out_activation="softmax",
#                num.round=20, array.batch.size=15, learning.rate=0.07, momentum=0.9, 
#                eval.metric=mx.metric.accuracy)

#summary(trained_mnnet)

#test_res <- monmlp.predict(x = test_features, weights = trained_mnnet)
predictions <- encodeClassLabels(predict(trained_nnet, test_features,  type = "class"))
#print(predictions)
#test_res <- predict(trained_mnnet,test_features)
#print(test_res)
#fitted_value = fitted.values(trained_mnnet)
#print(fitted_value)
#performance( prediction( trained_mnnet, test_class ))
#confusionMatrix(test_features, fitted.values(trained_nnet))

table(predictions, test_class)
#encoded_stuff <- encodeClassLabels(fitted.values(trained_nnet),  method = "402040", l = 0.4, h = 0.6)
#print(encoded_stuff)

 