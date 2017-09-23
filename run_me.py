# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 11:28:13 2017

@author: Mark
"""

import numpy as np
import pandas as pd

"""
def read_csv(filepath):
    data = np.genfromtxt(filepath, delimiter=',')
    return data
"""
def read_csv(filepath):
    df = pd.read_csv(filepath)
    df.sort_values(by='DateTime')
    return df


data = read_csv("D:\HackTheMachine\hackthemachine-data\classA_ship1_allGTG.csv")
#print data.head()
unique_indicators = data.indicator.unique()
print unique_indicators
#create a data frame dictionary to store your data frames
df_dict = {elem : pd.DataFrame for elem in unique_indicators}

for key in df_dict.keys():
    df_dict[key] = data[:][data.indicator == key]
    
print df_dict['GTG1'].head()