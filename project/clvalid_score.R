cat("\014") 
rm(list=ls(all=T))
#install.packages("clValid")  
library(clValid)
risk_score = read.csv("1407_scores_for_clustering_measure.csv", header = T)

risk_score_value=risk_score$V1
#summary(risk_score_value)
#print(risk_score_value)
df_risk_score_value <- as.data.frame(risk_score_value)
head(df_risk_score_value)
summary(df_risk_score_value)
#print(nrow(risk_score))
#print(ncol(risk_score))

print("##### Cluster Analysis: Internal Validity #####")
cluster_range <-  seq(from = 2, to = 100, by = 3)
internal_summary <- clValid(df_risk_score_value, cluster_range, maxitems=nrow(df_risk_score_value),  clMethods=c("hierarchical"), validation="internal")

print("----- Summary -----")
summary(internal_summary)
print("----- Details -----")
print(internal_summary)