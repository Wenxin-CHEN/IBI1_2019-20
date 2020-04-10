# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 08:56:25 2020

@author: 陈文心
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#the code for importing the .csv file works
covid_data=pd.read_csv('full_data.csv')
#all rows and every third column between 0 and 15
print(covid_data.iloc[0:15,0:6:3])
#'total_cases' for all rows corresponding to Afghanisn
rows=[]
for i in range(0,7996):
    if covid_data.iloc[i,1]=='Afghanistan':
        rows.append(True)
    else:
        rows.append(False)
print(covid_data.loc[rows,'total_cases'])
#mean and median of new cases for the entire world
rows1=[]
for i in range(0,7996):
    if covid_data.iloc[i,1]=='World':
        rows1.append(True)
    else:
        rows1.append(False)
world_new_cases=covid_data.loc[rows1,'new_cases']
print(np.mean(world_new_cases))
print(np.median(world_new_cases))
#plot boxplot
number=world_new_cases
plt.boxplot(number,vert=True,whis=1.5,patch_artist=True,showmeans=True,meanline=True,showbox=True,showcaps=True,\
            showfliers=True,notch=False)
plt.show()
#plot x:world date y: new cases/new deathes
rows2=[]
for i in range(0,7996):
    if covid_data.iloc[i,1]=='World':
        rows2.append(True)
    else:
        rows2.append(False)
world_dates=covid_data.loc[rows2,'date']
rows3=[]
for i in range(0,7996):
    if covid_data.iloc[i,1]=='World':
        rows3.append(True)
    else:
        rows3.append(False)
world_new_deaths=covid_data.loc[rows3,'new_deaths']
plt.plot(world_dates,world_new_cases,'b+')
plt.plot(world_dates,world_new_deaths,'r+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.xlabel('date')
plt.ylabel('number of people')
plt.show()
#new question
rows4=[]
for i in range(0,7996):
    if covid_data.iloc[i,4]>=10000 and covid_data.iloc[i,0]=='2020-03-31':
        rows4.append(True)
    else:
        rows4.append(False)
print(covid_data.loc[rows4,'location'])
