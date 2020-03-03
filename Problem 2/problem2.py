#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:44:40 2020

@author: nicobruno92
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


#%% defining plot function
plt.style.use('ggplot')
fig_width = 8 # width in inches
fig_height = 6 # height in inches
fig_size = [fig_width,fig_height]
plt.rcParams['figure.figsize'] = fig_size
plt.rcParams['figure.autolayout'] = True
plt.rcParams['font.size'] = 14#9
plt.rcParams['legend.fontsize'] = 11#7.
sns.set(style = 'whitegrid',context = 'poster', palette = 'viridis')

def plot(u, r, v = None):
    if v is None:
        sns.scatterplot(trials, u+0.01, alpha = 0.7)
        sns.scatterplot(trials, r-0.01, alpha = 0.7)
        plt.xlabel("Trials")
        plt.ylabel("Values")
        plt.legend(labels = ['u', 'r'], loc='best')
        sns.despine()
    else:
        sns.scatterplot(trials, u+0.01, alpha = 0.7)
        sns.scatterplot(trials, r-0.01, alpha = 0.7)
        sns.scatterplot(trials, v, alpha = 0.7)
        plt.xlabel("Trials")
        plt.ylabel("Values")
        plt.legend(labels = ['u', 'r', 'v'], loc='best')
        sns.despine()
#%% 1-A) set the initail conditions
u = np.ones(50)
r =  np.concatenate((np.ones(25), np.zeros(25)), axis  = 0)

trials = np.array(range(1, 51))

plot(u, r)
plt. show()
#%% defining Rescorla-Wagner function
def rw_fun(u, r, e = 0.1):
    v = np.zeros(50)
    w = 0
    for i in range(len(v)):
        v[i] = w*u[i]
        
        delta = r[i] - v[i]
        
        w = w + e*delta*u[i]    
    
    return v
#%% 1-B) Applying RW to the original u and r
v = rw_fun(u, r)
plot(u, r, v)
plt.show()
#%% 1-C) Trying different e
e_list = [0.05, 0.1, 0.2, 0.5]

e_df = pd.DataFrame()
e_df['trials'] = pd.Series(trials)

 
fig= plt.figure()
fig.figsize = fig_size*3
for i, e in enumerate(e_list):
    v = rw_fun(u, r, e = e)
    #e_df[r'$e: {}$'.format(i)] = pd.Series(v)
    plt.subplot(2, 2, i+1)
    plt.title(r'$e: {}$'.format(e))
    plot(u, r, v)
    plt.legend().remove()

fig.legend(labels = ['u', 'r', 'v'], loc='center right', borderaxespad=0.1)
plt.subplots_adjust(right=0.7)
plt.savefig('fig3_report2.png', dpi=600)
#e_df.plot.scatter()
plt.show()
#%%
e_list = [0.05, 0.1, 0.2, 0.5]

e_df = pd.DataFrame()

for i, e in enumerate(e_list):
    v = rw_fun(u, r, e = e)
    e_df[r'$e: {}$'.format(e)] = pd.Series(v)

e_df.plot()
plt.xlabel("Trials")
plt.ylabel("v")
sns.despine()
plt.savefig('fig3_report2.png', dpi=600)
#e_df.plot.scatter()
plt.show()

#%% 1 D) Partial reward: random reward
r2 = np.random.choice([0, 1], size=(50,), p=[0.6, 0.4])

v2 = rw_fun(u, r2) 

plot(u, r2, v2)
#%%1 E) Blocking:
