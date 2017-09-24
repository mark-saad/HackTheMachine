# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 11:28:13 2017

@author: Mark
"""

# import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

def read_csv(filepath):
    df = pd.read_csv(filepath, parse_dates=True, index_col='DateTime')
    print(df.shape)
    df = df.drop_duplicates()
    print(df.shape)
#    df.fillna(0, inplace=True)
    df.fillna(df.mean(), inplace=True)
    df.sort_index()
    return df




# MRG Files selected columns to be dropped for clustering
# 'TURB OVER TEMP', 'TURN GR ENGAGED', 'TURN GR DISENGD',\
mrg_drop_columns = ['indicator']


data = read_csv("D:\HackTheMachine\hackthemachine-data\gas\classB_ship2_allGTM_sorted_rmDUPs.csv")
#print data.head()

unique_indicators = data.indicator.unique()
#print unique_indicators
# create a data frame dictionary to store your data frames
df_dict = {elem : pd.DataFrame for elem in unique_indicators}
predict_dict = {elem : pd.DataFrame for elem in unique_indicators}

for key in df_dict.keys():
    df_dict[key] = data[:][data.indicator == key]
    #df_dict[key] = df_dict[key].drop(gtg_drop, axis=1)
    X = df_dict[key].drop(mrg_drop_columns, axis=1)
    # change the contamination percentage to have more or less outliers
    clf = IsolationForest(contamination=0.1)
    clf.fit(X)
    predict_dict[key] = clf.predict(X)
    df = df_dict[key]
    # this is the output field to tell if it's an outlier
    df['normal'] = predict_dict[key]
    #print df.head()
    ax = df.plot(kind='line',logy=True, title='classB_ship2_meanfilled_'+key).legend(loc='center left', bbox_to_anchor=(1, 0.5))
    fig = ax.get_figure()
    fig.savefig('classB_ship2_meanfilled_' + key + '.png')
    df.to_csv('classB_ship2_meanfilled_' + key + '.csv', sep=',')