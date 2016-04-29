rm(list=ls(all=T))
library (e1071)

### testing data 
get_test_data<- function(test_file_param)
{
  test_data = read.csv(test_file_param, sep=",")
  #test_data_matrix <- matrix(test_data, ncol = ncol(test_data), dimnames = NULL)
  return(test_data)
}
### training data 
get_train_data<- function(train_file_param)
{
  training_data = read.csv(train_file_param, sep=",")
  #training_data_matrix <- matrix(training_data, ncol = ncol(training_data), dimnames = NULL)  
  return(training_data)
}


trainFile="img-train.txt"
testFile="img-test.txt"
train_data = get_train_data(trainFile)


#print(train_data)
nb_model <- naiveBayes(as.factor(Class)~., data=train_data, laplace = 0.0)
#print(nb_model)
test_data = get_test_data(testFile)
#print(test_data)
test_features = test_data[, -4]
test_class = test_data[, 4]
#print(test_features)
predicted_res <- predict(nb_model, test_features)
#print(predicted_res)
#print(test_class)
table(predicted_res, test_class)



###### Plotting #######
# print("Plotting Red vs Green")
# redVector  <-  train_data$R
# greebVector <- train_data$G  
# 
# #plot(greebVector, redVector, main="Red vs. Green", xlab="Green ", ylab="Red", pch=19) 
# #plot( redVector, greebVector, main="Green vs. Red", xlab="Red", ylab="Green", pch=19) 