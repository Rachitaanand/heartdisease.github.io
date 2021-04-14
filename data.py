### PREPERATION ###

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#data import
df = pd.read_csv("/kaggle/input/heart-attack-analysis-prediction-dataset/heart.csv")

#shape of dataset
print("The shape of the dataset is : ", df.shape)

#Preview of the first 5 rows of the data
df.head()

#Checking the number of unique values in each column
dict = {}
for i in list(df.columns):
    dict[i] = df[i].value_counts().shape[0]

#Separating the columns in categorical and continuous
pd.DataFrame(dict,index=["unique count"]).transpose()cat_cols = ['sex','exng','caa','cp','fbs','restecg','slp','thall']
con_cols = ["age","trtbps","chol","thalachh","oldpeak"]
target_col = ["output"]
print("The categorial cols are : ", cat_cols)
print("The continuous cols are : ", con_cols)
print("The target variable is :  ", target_col)

#summary analysis
df[con_cols].describe().transpose()

#missing values
df.isnull().sum()

