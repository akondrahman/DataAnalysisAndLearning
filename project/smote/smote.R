rm(list=ls(all=T))
#install.packages('DMwR')
library('DMwR')
get_data<- function(test_file_param)
{
  test_data = read.csv(test_file_param, sep=",", header=FALSE)
  return(test_data)
}

dataset_file="2_NonZeroDataset_Aggolo.csv"
dataset_ = get_data(dataset_file)
dataset_$V24 <- NULL 
cols_ = ncol(dataset_)
#print(cols_)
#print("Without headers")
#print(dataset_)
#print("-----")
#colnames(dataset_) <- c( paste("X", 1:cols_ - 1 ), "RiskScores")
#print("With headers")
#print(dataset_)
#print("-----")
smotedData <- SMOTE(V23 ~ ., dataset_, perc.over = 600,perc.under=100)
print(smotedData)
