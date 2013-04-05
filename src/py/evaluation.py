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


object1=open('TrainingScoreList','r')
TrainingScoreList=cPickle.load(object1)
object1.close()



object1=open('TestingScoreList','r')
TestingScoreList=cPickle.load(object1)

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







def generateROC(X_training,X_testing,y_training,y_testing,feature_label):
    clf = LinearSVC()
    classifier = svm.SVC(kernel='linear', probability=True)
    clf = clf.fit(X_training, y_training)


    probas_ = classifier.fit(X_training,y_training).predict_proba(X_testing)

    #Acc=np.mean(clf.predict(TestScores) == TestLabels)

    #Acc=np.mean(clf.predict(TestScores) == TestLabels)




    fpr, tpr, thresholds = roc_curve(y_testing, probas_[:, 1])
    roc_auc = auc(fpr, tpr)
    print("Area under the ROC curve : %f" % roc_auc)

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



for i in range(len(eval_labels)):
    generateROC(TrainingScoreList[i],TestingScoreList[i],UserLabels,TestLabels,eval_labels[i])







