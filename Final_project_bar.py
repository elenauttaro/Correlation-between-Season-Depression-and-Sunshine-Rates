#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:10:23 2022

@author: elenauttaro
"""

import random 
import matplotlib.pyplot as plt

inpf = open('Depression_rates.txt')

state = []
depressionrates = []

for rec in inpf:
    
    rec = rec.strip()
    cols = rec.split()
    state.append(cols[0])
    depressionrates.append(float(cols[0]))

inpf.close()

##x_pos specifices the x coordiantes of abrs starting from 0
x_pos = [i for i in range(len(state))]
for i in range(len(state)):
    x_pos.append(i)

yerr = []
for i in range(len(state)):
    yerr.append(random.gauss(2,1))



## through xticks()
plt.xticks(x_pos, state, rotation = 60, ha = 'right')

plt.bar(x_pos, depressionrates, yerr=yerr, alpha = 0.4)
plt.xlabel("states")
plt.ylabel("depression")
plt.title("depression by state")
plt.show()