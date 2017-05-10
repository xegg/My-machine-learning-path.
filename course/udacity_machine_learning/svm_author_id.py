#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()





#########################################################
### your code goes here ###
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

from sklearn.svm import SVC
# for c in [10, 100, 1000, 10000]:
for c in [10000]:
    print("SVM training wich c = %s", c)
    svc = SVC(kernel='rbf', C=c)

    t0 = time()
    svc.fit(features_train, labels_train)
    print("training time with SVM's linear kernel", time() - t0)

    t1 = time()
    pred = svc.predict(features_test)
    print("prediction time with SVM's linear kernel", time() - t1)
    print("pred 10:%s 26:%s 50:%s" % (pred[10], pred[26], pred[50]))
    print("have %s is Chris" % len(list(i for i in pred if i == [1])))

    print(svc.score(features_test, labels_test))

#########################################################



