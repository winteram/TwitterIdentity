#Evaluates Userscores using sklearn

import sklearn
import pickle
import cPickle
import numpy as np

from sklearn.metrics import roc_curve, auc

from sklearn.svm import LinearSVC


import pylab as pl
from sklearn import svm, datasets
from sklearn.utils import shuffle

from sklearn.linear_model import LogisticRegression


object1=open('TrainingScoreList','r')
TrainingScoreList=cPickle.load(object1)
object1.close()



object1=open('TestingScoreList','r')
TestingScoreList=cPickle.load(object1)

object1.close()

object1=open('IdList','r')
IdList=cPickle.load(object1)

object1.close()


object1=open('eval_labels','r')
eval_labels=cPickle.load(object1)

object1.close()


object1=open('UserLabels','r')
UserLabels=cPickle.load(object1)

object1.close()

object1=open('TestLabels','r')
TestLabels=cPickle.load(object1)

object1.close()


object1=open('Test_Count','r')
Test_Count=cPickle.load(object1)

object1.close() 


TestCount=[word for party in Test_Count for word in party]


#so we want to change X training and y training into two separate sets- 1 below the median and one above the median- or we want to do logistic regression
# where the predictor is number of tweets and the outcome is the accuracy. The later might be the best. I can actually do it in R, but maybe best in
#python. 



X= TestCount
# we want y= a vector with accuracies

# then we will do a for function with enumerate. 
# for i, value in enumerate(prediction):
    #if prediction[i]==userlabel[i]:
        #Accuracyvec.append(1)
    #else accuracyvec.append(0)

#y=A

#clf2 = LogisticRegression().fit(X, y)

#clf2.predict(X_new)


classifier = svm.SVC(kernel='linear', probability=True)




def generateROC(X_training,X_testing,y_training,y_testing,feature_label):
    clf = LinearSVC()
    classifier = svm.SVC(kernel='linear', probability=True)
    clf = clf.fit(X_training, y_training)


    probas_ = classifier.fit(X_training,y_training).predict_proba(X_testing)

    Acc=np.mean(clf.predict(X_testing) == y_testing)

    #Acc=np.mean(clf.predict(TestScores) == TestLabels)

    testing=classifier.fit(X_training,y_training).predict(X_testing)




    fpr, tpr, thresholds = roc_curve(y_testing, probas_[:, 1])
    roc_auc = auc(fpr, tpr)
    print("Area under the ROC curve : %f" % roc_auc)
    print Acc
    print testing
    print feature_label

    title="Receiver Operating Characteristic for "+feature_label

    # Plot ROC curve
    pl.clf()
    pl.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
    pl.plot([0, 1], [0, 1], 'k--')
    pl.xlim([0.0, 1.0])
    pl.ylim([0.0, 1.0])
    pl.xlabel('False Positive Rate')
    pl.ylabel('True Positive Rate')
    pl.title(title)
    pl.legend(loc="lower right")
    pl.show()



for i in range(len(eval_labels)-3):
    generateROC(TrainingScoreList[i],TestingScoreList[i],UserLabels,TestLabels,eval_labels[i])





def gentest(X_training,X_testing,y_training,y_testing,feature_label):
    clf = LinearSVC()
    classifier = svm.SVC(kernel='linear', probability=True)
    clf = clf.fit(X_training, y_training)
    testing=classifier.fit(X_training,y_training).predict(X_testing)
    return testing

i=6
predictVec=gentest(TrainingScoreList[i],TestingScoreList[i],UserLabels,TestLabels,eval_labels[i])


# we want y= a vector with accuracies

# then we will do a for function with enumerate. 

Accuracyvec=[]

for i, value in enumerate(predictVec):
    if value==TestLabels[i]:

        Accuracyvec.append(1)
    else:
        Accuracyvec.append(0)

    #else accuracyvec.append(0)

#y=A

#clf2 = LogisticRegression().fit(TestCount, Accuracyvec)


criterion=np.median(TestCount)

medianSplit=[]

AccBelow=[]
AccAbove=[]


for i,user in enumerate(TestCount):
    if user < criterion:
        #medianSplit.append(0)
        AccBelow.append(Accuracyvec[i])
    else:
        #medianSplit.append(1)
        AccAbove.append(Accuracyvec[i])


below_mean=np.mean(AccBelow)
above_mean=np.mean(AccAbove)

















