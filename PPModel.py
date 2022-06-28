# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 22:37:41 2022

@author: Tarun
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/Tarun/OneDrive/Desktop/pppp/Internship_Engineering_graduate_salary - Copy (1).csv")

data = df.copy()

data.columns

data = data[['Quant', 'GraduationYear',   'experince', '12percentage', '10percentage' , 'Salary']]

from sklearn.model_selection import train_test_split

X = data.iloc[:, :-1].values
print(X.shape)


y = data.iloc[:, -1].values
print(y.shape)
y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)




# Random Forest algorithm
 
from sklearn.ensemble import RandomForestRegressor
ram_for = RandomForestRegressor()
ram_for.fit(X_train, y_train)

import pickle

with open('rfmodel_pickle', 'wb') as f:
    pickle.dump(ram_for,f)

# Linear Regression

'''
from sklearn.linear_model import LinearRegression, Lasso


lm = LinearRegression()
lm.fit(X_train, y_train)

linear_model = lm

with open('liermodel_pickle', 'wb') as f1:
    pickle.dump(linear_model,f1)



    
    '''












df = pd.read_csv("C:/Users/Tarun/OneDrive/Desktop/pppp/Internship_Engineering_graduate_salary - Copy (1).csv")

data = df.copy()

data.columns

data = data[['Quant', 'GraduationYear',   'experince', '12percentage', '10percentage' , 'Salary']]

from sklearn.model_selection import train_test_split

X = data.iloc[:, :-1]
print(X.shape)


y = data.iloc[:, -1]
print(y.shape)
y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

training_data = pd.concat([X_train, y_train],axis = 1)

testing_data = pd.concat([X_test, y_test], axis=1)

training_data.to_csv('Training_Data.csv')

testing_data.to_csv('Testing_Data.csv')