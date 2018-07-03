

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neural_network import MLPRegressor
from keras.models import Sequential
from keras.layers import Dense

# Create first network with Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy


randomseed = np.random.seed(0)
# Importing the dataset


feature_dataset = pd.read_csv(r'D:\Personal\Techgig\result.csv',parse_dates=['Built_Date','Priced_Date'])
target_dataset =  pd.read_csv(r'D:\Personal\Techgig\Predicting Housing Prices\Housing Prices data\house_prices.csv')
missing_id = pd.read_csv(r'D:\Personal\Techgig\Predicting Housing Prices\Housing Prices data\missing.csv')



dataset = pd.merge(feature_dataset,target_dataset,on='House ID')

#Handling Missiing values.

X = dataset.iloc[:,3:-1]

#Fill categorical data with most frequent
X = X.apply(lambda x:x.fillna(x.value_counts().index[0]))

# encode df.famhist as a numeric via pd.Factor
df['famhist_ord'] = pd.Categorical(df.famhist).labels

#result_df  = pd.get_dummies(X)
# Importing the dataset
X = result_df.values
y = dataset.iloc[:, -1].values
