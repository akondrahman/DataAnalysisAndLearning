#dataList<-{55, 23, 28, 32, 18, 68, 72, 89, 98, 100}
dataVal <- c(55, 23, 28, 32, 18, 68, 72, 89, 98, 100)
#print(dataVal)

doMinMaxNormalization<- function(dataListParam) 
{
  normalizedDataVal=NULL
  minRange=min(dataListParam)
  maxRange=max(dataListParam)
  newMinRange=0
  newMaxRange=255
  #print(minRange)
  for (i in 1:length(dataListParam) ) 
  {
    normalizedDataVal[i] =  (((dataListParam[i] - minRange)/(maxRange - minRange)) * (newMaxRange - newMinRange)) + newMinRange
  }
  returnMinMaxList<-normalizedDataVal
}

print("original list")
print(dataVal)
minMaxNormalizedDataList<-doMinMaxNormalization(dataVal)
print("After min-max normalization the list becomes: ")
print(minMaxNormalizedDataList)
doZScoreNormalization<- function(dataListParam) 
{
  normalizedTempDataVal=NULL
  mean_ = mean(dataListParam)
  stdDev_ = sd(dataListParam, na.rm = TRUE)
  for (i in 1:length(dataListParam) ) 
  {
    normalizedTempDataVal[i] =  (dataListParam[i] - mean_) / stdDev_
  }
  returnZList<-normalizedTempDataVal
}
print("Another transformation ...")
print("original list")
print(dataVal)
zNormalizedDataList=NULL
zNormalizedDataList<-doZScoreNormalization(dataVal)
print("After Z-Score normalization the list becomes: ")
print(zNormalizedDataList)


print("#####################Plotting Time###############")
heightVec<-c(5.6, 5.8, 5.4, 6.1, 5.9)
weightVec<-c(150, 155, 145, 180, 175)
print("Plotting Normal Vectors")
plot(heightVec, weightVec, main="HeightVs.Weight",
     xlab="Height ", ylab="Weight", pch=19) 
nrmHeightvec<-doZScoreNormalization(heightVec)
nrmWeightvec<-doZScoreNormalization(weightVec)  
#print("Normalized vectors ....") 
#print(nrmHeightvec)
#print(nrmWeightvec)
#plot(nrmHeightvec, nrmWeightvec, main="HeightVs.Weight",
#     xlab="Height ", ylab="Weight", pch=19) 
print("################Pair Wise Distance############")
createMatrix<- function(heightVecP, weightVecP) 
{
  tempMat<- matrix(nrow=5, ncol=2)
  returnMat<- matrix(nrow=5, ncol=2)
  for (j in 1:length(heightVecP) ) 
  {
    tempMat[j,1] = heightVecP[j]    
    tempMat[j,2] = weightVecP[j]        
  }
  returnMat<-tempMat
}
theMatrix<-createMatrix(heightVec, weightVec)
normMatrix<-createMatrix(nrmHeightvec, nrmWeightvec)
print("The matrix is: ")
print(theMatrix)
print("Normalized  matrix is: ")
print(normMatrix)
#install.packages("flexclust")  
library(flexclust)
#pDistOutput<-dist(theMatrix, method = "euclidean", diag = FALSE, upper = FALSE)
pDistOutput <-dist2(theMatrix, theMatrix, method = "euclidean", p=2)
pNormDistOutput <-dist2(normMatrix, normMatrix, method = "euclidean", p=2)
print("P dist output for original matrix is ...")
print(pDistOutput)
print("P dist output for normalized matrix is ...")
print(pNormDistOutput)