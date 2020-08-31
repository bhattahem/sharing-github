# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 08:05:33 2020

@author: hbhatt
"""
import pandas as pd
import matplotlib.pyplot as plt
#%%

df = pd.read_csv(r'C:\Users\hbhatt\Desktop\Microfinance for energy\project works\project_data_python_version2.1.csv')
df.head()
#%%
data = df.iloc[df.shape[0]-2,3:]
T0 = 0;
T1 = 0;
T2 =0;
T3 = 0;
T4 = 0;
T5 = 0;

for each in data:
    if (each<12):
        T0 = T0 +1;
    elif (each>=12 and each<200):
        T1 = T1 +1;
    elif (each>=200 and each<1000):
        T2 = T2+1;
    elif (each>=1000 and each<3400):
        T3 = T3 +1;
    elif (each>=3400 and each<8200):
        T4 = T4 +1;
    else:
        T5 = T5 + 1;
    
T =[ T0, T1, T2, T3, T4, T5]
Names =['Tier-0','Tier-1','Tier-2','Tier-3','Tier-4','Tier-5']

#%%
import numpy as np
Names =['Tier-0','Tier-1','Tier-2','Tier-3','Tier-4','Tier-5']
line = plt.bar(Names,T)
plt.ylabel('Number of Household')
plt.xlabel('MTF label')

for i in range(len(T)):
    plt.annotate(str(T[i]), xy=(Names[i],T[i]))

plt.show()

plt.show()
#%%
#df1 = pd.read_csv(r'C:\Users\hbhatt\Desktop\Microfinance for energy\project works\projectdata_python.csv')
#df.head()