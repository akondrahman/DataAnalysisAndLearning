#hw2_data = read.csv("hw2-data.csv", header=TRUE)
# print("the data is ")
# #hw2_data
# x1<-hw2_data[2]
# #print("is this x1?")
# #x1
# x2<-hw2_data[3]
# #x2
# 
# x1_ = matrix( x1, nrow=length(x1), ncol=1) 
# theMatrix = cbind(x1_, x2) 
# length(theMatrix)
temp = read.csv("hw2-data.csv", sep=",", row.names=1)
data_ <- as.matrix(temp) 
#temp1[450,2]
print("Clustering started ... ")
cluster_no = 6
theCluster <- kmeans(data_,cluster_no)
#theCluster$cluster
plot(data_[,1], data_[,2],col=theCluster$cluster)
points(theCluster$centers, pch=15)
###
wss <- (nrow(data_)-1)*sum(apply(data_,2,var))
for (i in 2:6) wss[i] <- sum(kmeans(data_,
                                     centers=i)$withinss)
plot(1:6, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares") 
print("6 is teh best")

