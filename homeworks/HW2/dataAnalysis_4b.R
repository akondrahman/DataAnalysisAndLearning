temp = read.csv("hw2-data.csv", sep=",", row.names=1)
data_ <- as.matrix(temp) 
print("Hierarchical Clustering started ... ")
hc_data_ <- hclust(dist(data_), method = "average")
groups <- cutree(hc_data_, h=20) # cut tree into 4 clusters
plot(hc_data_, main = "Cluster Plot: Parameter='Centroid'", labels = as.character(groups))


