#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:21:24 2022

@author: elenauttaro
"""

import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np

depression = pd.read_csv('Depression_rates.csv',
                         skiprows = 1,
                         names = ["state","depressionrates"],
                         index_col = 'state')
state = pd.read_csv("state_code.csv",
                    skiprows = 1,
                    names = ["state",'code'],
                    index_col = 'state')




#print(depression_by_state)
sunshine = pd.read_csv("sunshine_hours_by_state.csv", 
                       skiprows = 1,
                       names = ['city', 'code',
                       'jan',	'feb',	'march',	'apr',	'may',	'june',	'july',	'aug',	'sep',	'oct',	'nov',	'dec',	'year'],
                       index_col = 'city')

sunshine_per_state = sunshine.groupby('code')

sunshine_per_state = sunshine_per_state['year'].sum()

sunshine_depression = pd.merge(pd.merge(state,depression, on= "state"),sunshine_per_state, on ='code')
                               
sunshine_depression.to_csv('sunshine_depression.csv')
#print(sunshine_depression)




x = np.array(sunshine_depression.depressionrates)
y = np.array(sunshine_depression.year)

plt.scatter(x, y, marker = '+') 
            

m,b = np.polyfit(x, y, 1) #linear fitting
plt.plot(x, m*x+b, color = 'r')

line = f'y={round(m,2)}*x+{round(b,2)}'

plt.text(.8,.2, line)

#plt.text(0.95,0.5,line)
plt.xlabel ("depressionrates")
plt.ylabel("year")
plt.title("depression vs sunshine")
plt.xticks([12,14,16,18,20,22,24],['12%','14%','16%','18%','20%','22%','24%'])


plt.show()

