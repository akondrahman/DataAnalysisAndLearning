'''
Akond, Dec 22, 2016
main file to call the pca+learners
'''
import pca_mobilesoft, IO_, sys
f_ ="Exp_1_Mobilesoft_clusterified_1407.csv"
pca_mobilesoft.experiment_mobilesoft_cart(f_)
#pca_mobilesoft.experiment_mobilesoft_knn(f_)
#pca_mobilesoft.experiment_mobilesoft_random_forest(f_)
#pca_mobilesoft.experiment_mobilesoft_svm(f_)
'''
Smoted Zone
'''
print "Smoted analysis"
smoted_f = "smote/mobilesoft_smoted_5clusters.csv"
#pca_mobilesoft.experiment_mobilesoft_cart(smoted_f)
#pca_mobilesoft.experiment_mobilesoft_knn(smoted_f)
#pca_mobilesoft.experiment_mobilesoft_svm(smoted_f)
#pca_mobilesoft.experiment_mobilesoft_random_forest(smoted_f)

print "=================================================================================================================="





print "Done ;-)"
print "Ended at: ", IO_.giveTimeStamp()
