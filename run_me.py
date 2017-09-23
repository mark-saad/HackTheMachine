# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 11:28:13 2017

@author: Mark
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

"""
def read_csv(filepath):
    data = np.genfromtxt(filepath, delimiter=',')
    return data
"""
def read_csv(filepath):
    df = pd.read_csv(filepath)
    df.fillna(0, inplace=True)
    df.sort_values(by='DateTime')
    return df


data = read_csv("D:\HackTheMachine\hackthemachine-data\classA_ship1_allGTG.csv")
#print data.head()
unique_indicators = data.indicator.unique()
print unique_indicators
#create a data frame dictionary to store your data frames
df_dict = {elem : pd.DataFrame for elem in unique_indicators}
predict_dict = {elem : pd.DataFrame for elem in unique_indicators}

for key in df_dict.keys():
    df_dict[key] = data[:][data.indicator == key]
    df_dict[key] = df_dict[key].drop(['DateTime','indicator'], axis=1)
    clf = IsolationForest()
    clf.fit(df_dict[key])
    predict_dict[key] = clf.predict(df_dict[key])
    df = df_dict[key]
    df['outlier'] = predict_dict[key]
    print df.head()
    df.to_csv(key+'.csv', sep=',')
