# -*- coding: utf-8 -*-
"""DIABETES_PRED.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FMDwcT07XB8R5_Z4m2NauujU-PepCMN6
"""

import pandas as pd

data = pd.read_csv('/content/sample_data/diabetes.csv')

data.head()

X = data.drop('Outcome', axis=1)
Y = data['Outcome']

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y, random_state=3)

from sklearn.linear_model import LogisticRegression

Lmodel = LogisticRegression()

Lmodel.fit(X_train, Y_train)

from sklearn import svm

Smodel = svm.SVC()

Smodel.fit(X_train, Y_train)

from sklearn.metrics import accuracy_score

Lpred = Lmodel.predict(X_train)
Laccuracy = accuracy_score(Lpred,Y_train)
print(Laccuracy)


Spred = Smodel.predict(X_train)
Saccuracy = accuracy_score(Spred, Y_train)
print(Saccuracy)

