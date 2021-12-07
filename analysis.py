# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:03:35 2021

@author: Student
"""
import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

#reading in the data
data = pd.read_csv(r'C:\Users\Student\OneDrive - University of Virginia\Desktop\College\Fall 2021\DS 3002\api_results.csv', index_col=False)
#replacing the str time with epoch time
t = data['time']

i = 0

for i in range(0,60):
    tparsed = t[i][10:]
    minute = int(tparsed[2:4])
    timeMin = minute
    data.loc[i,'time'] = timeMin

data.sort_values(by='time')
time_data = data['time']
pi = data['pi']
factor = data['factor']

plt.figure(1)
plt.scatter(time_data,factor)
plt.xlabel('Time (min)')
plt.ylabel('Factor')

plt.figure(2)
plt.scatter(time_data,pi,label='Series')
length = len(time_data)
pi_array = np.pi*np.ones((length,1))

plt.plot(time_data, pi_array, label='Actual', color = 'orange')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Pi')
plt.ylim(top=3.15)
plt.ylim(bottom=3.13)

plt.figure(3)
plt.scatter(factor,pi)
plt.xlabel('Factor')
plt.ylabel('Pi')
plt.ylim(top=3.15)
plt.ylim(bottom=3.13)