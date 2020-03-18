# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:36:52 2020

@author: 陈文心
"""

gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
#range from the laegest number to the smallest and delete the last(smallest) number
gene_lengths.reverse()
gene_lengths.pop()
#range from the smallest number to the largest and delete the last(largest) number
gene_lengths.sort()
gene_lengths.pop()
#use data from gene_lengths to draw boxplot
import matplotlib.pyplot as plt
score=gene_lengths
plt.boxplot(score,vert=True,whis=1.5,patch_artist=True,
            meanline=True,showbox=True,showcaps=True,showfliers=True,notch=False)
plt.show()
