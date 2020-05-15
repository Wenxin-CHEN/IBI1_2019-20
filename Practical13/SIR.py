# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:26:00 2020

@author: 陈文心
"""
#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
inf=[1]
sus=[9999]
rec=[0]
#total number of people
N=10000
#beta: infection probability upon contact
beta=0.3
#gamma=recovery probability
gamma=0.05
#store the time for x
T=[0]
#loop over 1000 time points
for t in range(0,1000):
    a=np.random.choice(range(2),sus[t],p=[1-beta*(inf[t]/N),beta*(inf[t]/N)])
    #count the number of infected people
    num_inf=np.sum(a==1)
    b=np.random.choice(range(2),inf[t],p=[1-gamma,gamma])
    #count the number of people recovered
    num_rec=np.sum(b==1)
    #record the output of each time step
    sus.append(sus[t]-num_inf)
    inf.append(inf[t]+num_inf-num_rec)
    rec.append(rec[t]+num_rec)
    T.append(t+1)
#plot the picture
plt.plot(T,inf,label='infected')
plt.plot(T,sus,label='susceptibles')
plt.plot(T,rec,label='recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend(loc='upper right')
plt.show()
plt.figure(figsize=(6,4),dpi=150)
plt.savefig('the SRI model',type='png')