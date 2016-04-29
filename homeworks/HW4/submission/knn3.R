rm(list=ls(all=T))
library (e1071)
library(class)

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


trainFile_1="dtr3.csv"
trainFile_2="dtr8.csv"
testFile_1="dte3.csv"
testFile_2="dte8.csv"
#### training data 
train_data = get_train_data(trainFile_1, trainFile_2)
#print(dim(train_data))
train_features = train_data[, -1]
train_class = train_data[, 1]
#print(length(train_class))
#####
##### test data 
test_data = get_test_data(testFile_1, testFile_2)
#print(dim(test_data))
test_features = test_data[, -1]
test_class = test_data[, 1]
#print(length(test_class))
#####
res_pred <- knn(train = train_features, test = test_features, cl = train_class, k=3)
#print(res_pred)
table(res_pred, test_class)