#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:21:24 2022

@author: elenauttaro
"""

import pandas as pd

depression = pd.read_csv('Depression_rates.csv',
                         skiprows = 1,
                         names = ["state","depression rate (%)"],
                         index_col = 'state')
state = pd.read_csv("state_code.csv",
                    skiprows = 1,
                    names = ["state",'code'],
                    index_col = 'state')
sunshine_by_state = pd.read_csv('sunshine_hours_by_state.csv',
                                names = ['state','rate'])

depression_by_state = pd.merge(depression, state, on ='state')