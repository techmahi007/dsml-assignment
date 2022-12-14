# -*- coding: utf-8 -*-
"""324032_ShardulJoshi_Assgn3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eu80eyLoN5YeCDWF9QFpsfe3hAOuLiYU
"""

import pandas as pd
import numpy as np

data=pd.read_csv("Decision.csv")
data=data.drop(['Id'], axis=1)
print(data)

data.describe()

data['Buys'].value_counts()

from sklearn.preprocessing import LabelEncoder
l=LabelEncoder();

from tables.table import Column
x=data.iloc[:,:-1]  #last Column not included
x=x.apply(l.fit_transform)

print("Age with encoded value:",list(zip(data.iloc[:,0],x.iloc[:,0])))
print("\nIncome with encoded value:",list(zip(data.iloc[:,1],x.iloc[:,1])))
print("\nGender with encoded value:",list(zip(data.iloc[:,2],x.iloc[:,2])))
print("\nMaritialStatus with encoded value:",list(zip(data.iloc[:,3],x.iloc[:,3])))

y=data.iloc[:,-1]

from sklearn.tree import DecisionTreeClassifier 
classifier=DecisionTreeClassifier(criterion='entropy')
classifier.fit(x,y)

test_x=np.array([1,1,0,0])
pred_y=classifier.predict([test_x])
print("decision for the test data: [Age < 21, Income = Low, Gender = Female, Marital Status = Married] :",pred_y[0])