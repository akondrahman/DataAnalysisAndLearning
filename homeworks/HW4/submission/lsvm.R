rm(list=ls(all=T))
library (e1071)
### testing data 
get_test_data<- function(test_file_param1, test_file_param2)
{
  test_data_1 = read.csv(test_file_param1, sep=",", header=FALSE)
  test_data_2 = read.csv(test_file_param2, sep=",", header=FALSE)  
  #print(dim(test_data_2))
  test_data <- rbind2(test_data_1, test_data_2)
  return(test_data)
}
### training data 
get_train_data<- function(train_file_param1, train_file_param2)
{
  training_data_1 = read.csv(train_file_param1, sep=",", header=FALSE)
  training_data_2 = read.csv(train_file_param2, sep=",", header=FALSE)  
  #print(dim(training_data_2))
  training_data <- rbind2(training_data_1, training_data_2)
  return(training_data)
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
colnames(train_data) <- c("Class", paste("attrib", 2:ncol(train_data)))
#print(dim(train_data))
#train_features = train_data[, -1]
#train_class =  train_data[, 1] 
#train_class = convertToCategory( train_data[, 1] )
#print(train_class)
#####
##### test data 
test_data = get_test_data(testFile_1, testFile_2)
colnames(test_data) <- c("Class", paste("attrib", 2:ncol(train_data)))
#print(dim(test_data))
test_features = test_data[, -1]
test_class = test_data[, 1] 
#print(length(test_class))
#####


trained_svm_model <- svm(as.factor(Class)~., data=train_data, kernel="linear", cost=1)
#summary(trained_svm_model)
pred_res <- predict(trained_svm_model,test_features)
#print(pred_res)
table(pred_res, test_class)

