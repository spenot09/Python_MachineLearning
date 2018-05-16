import pandas as pd
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer


train = pd.read_csv('/user/HS127/sc00858/OpenPose/Output/Train/training_set.csv', header=None)
test = pd.read_csv('/user/HS127/sc00858/OpenPose/Output/Train/training_set.csv', header=None)
#find number of rows
num_rows = len(train)

imp = Imputer(missing_values='NaN', strategy='mean', axis=0)

#extract features and targets from table
features_train = train.ix[:,:175]
target_train = train.ix[:,[176]]

features_test = test.ix[:,:175]
target_test= test.ix[:,[176]]

#convert to a numpy array
features_train_np = np.array(features_train)
target_train_np = np.array(target_train)

features_test_np = np.array(features_test)
target_test_np = np.array(target_test)

# Our dataset and targets
X = features_train_np
y = target_train_np

imp.fit(X)
X = imp.transform(X)

imp.fit(y)
y = imp.transform(y).ravel()


print X.shape, y.shape

clf = SVR(C=1.0, epsilon=0.2)
clf.fit(X, y)
clf.score(X, y)
predicted= clf.predict(features_test_np)
