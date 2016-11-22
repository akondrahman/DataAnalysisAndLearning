cat("\014") 
rm(list=ls(all=T))
library(caret)
data1407_file <-  "Exp_1_Mobilesoft_cluster_Headered_1407.csv"
data1407_data <- read.csv(data1407_file, header=TRUE, stringsAsFactors=F)
data1407_data$class_vscore     <- as.factor(data1407_data$class_vscore)

needed_data   <- data1407_data[, -c(1, 24)]
print(head(needed_data))

logireg_model1407 <- glm(class_vscore ~ ., data=needed_data, family=binomial())
### step wise selection 
# nothing_1407  <- glm(class_vscore ~ 1, data=needed_data, family=binomial())
# fullmod_1407  <- glm(class_vscore ~ ., data=needed_data, family=binomial())
# stepwise_1407 <- step(nothing_1407, scope=list(lower=formula(nothing_1407), upper=formula(fullmod_1407)), direction="forward")
###
print("***** Summary *****")
summary(logireg_model1407)
print("***** Loglikelhood ratio *****")
exp(coef(logireg_model1407))