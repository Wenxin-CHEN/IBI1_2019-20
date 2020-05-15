# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:33:20 2020

@author: 陈文心
"""

import numpy as np 
import matplotlib.pyplot as plt
population=np.zeros((100,100))
#randomly choose a outbreak point and set it to 1
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
#show the outbreak point
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest')
#beta: infection probability upon contact
beta=0.3
#gamma=recovery probability
gamma=0.05
# loop through all infected points
for i in range(1,100):
# find infected points
    infectedIndex=np.where(population==1)
    for i in range(len(infectedIndex[0])):
    # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
    # infect each neighbour with probability beta
    # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
            # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    #refresh the infected data
    infectedIndex=np.where(population==1)
    #recovery of infected ones
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        population[x,y]=np.random.choice(range(2),1,p=[1-gamma,gamma])[0]+1
    #output for each loop
    plt.figure(figsize=(6,4),dpi=150)
    plt.imshow(population,cmap='viridis',interpolation='nearest')
