#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 14:59:28 2020

@author: nicobruno92
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


plt.style.use('ggplot')
fig_width = 8 # width in inches
fig_height = 6 # height in inches
fig_size = [fig_width,fig_height]
plt.rcParams['figure.figsize'] = fig_size
plt.rcParams['figure.autolayout'] = True
plt.rcParams['font.size'] = 14#9
plt.rcParams['legend.fontsize'] = 11#7.




# =============================================================================
# First model
# =============================================================================
p = np.zeros(100)

years = np.zeros(100)

def pop_fun(p, alpha = 0.1, p_zero = 2):
    p[0] = p_zero
    for i in range(len(p)-1):
        p[i+1] = p[i] + alpha*p[i]
    return p
        
for i in range(len(years)):
    years[i] = i

p1 = pop_fun(p)
plt.plot(years, p1)
plt.xlabel(r'year')
plt.ylabel(r'population')
plt.savefig('fig1_report1.png', dpi=600)
plt.show()
plt.clf()


# =============================================================================
# Testing different alphas
# =============================================================================
alphas = [0.001, 0.1, 0.11,0.12, 0.15]

p_alpha = pd.DataFrame()
for i in alphas:
    p_alpha[r'$\alpha$: {}'.format(i)] = pd.Series(pop_fun(p, alpha = i))
    
p_alpha.plot()
plt.xlabel(r'year')
plt.ylabel(r'population')
plt.legend(title= "alpha",loc='best')
plt.savefig('fig2_report1.png', dpi=600)
plt.show()
plt.clf()

# =============================================================================
# Testing different p0
# =============================================================================
p_zeros = [1, 2, 3, 5, 10]

p_zero = pd.DataFrame()
for i in p_zeros:
    p_zero[r'$p_0: {}$'.format(i)] = pd.Series(pop_fun(p, p_zero = i))
    
p_zero.plot()
plt.xlabel(r'year')
plt.ylabel(r'population')
plt.legend(title= r"$p_0$",loc='best')
plt.savefig('fig3_report1.png', dpi=600)
plt.show()
plt.clf()
# =============================================================================
# new alpha
# =============================================================================
def alpha_fun(p):
    alpha = np.zeros(500)
    for i in range(len(p)):
        p[i] = i
        alpha[i] = 200-p[i]
    return p, alpha
    
p2 = np.zeros(500)

palpha, alpha = alpha_fun(p2)

plt.plot(palpha, alpha)
plt.xlabel(r'population')
plt.ylabel(r'alpha')
plt.savefig('fig4_report1.png', dpi=600)
plt.show()
plt.clf()
# =============================================================================
# Model 2: adding beta and new alpha
# =============================================================================

def pop_fun2(p, p_zero = 2, beta =0.001):
    p[0] = p_zero
    for i in range(len(p)-1):
        p[i+1] = p[i] + beta*p[i]*(200-p[i])
    return p

p3 = pop_fun2(p)
plt.plot(years, p3)
plt.xlabel(r'year')
plt.ylabel(r'population')
plt.savefig('fig5_report1.png', dpi=600)
plt.show()
plt.clf()
# =============================================================================
# Testing different betas in model 2
# =============================================================================
betas = [0.0001, 0.001, 0.005,0.01]

p_betas = pd.DataFrame()
for i in betas:
    p_betas[r'$\beta: {}$'.format(i)] = pd.Series(pop_fun2(p, beta = i))
    
p_betas.plot()
plt.xlabel(r'year')
plt.ylabel(r'population')
plt.legend(title= "beta",loc='best')
plt.savefig('fig6_report1.png', dpi=600)
plt.show()
plt.clf()
# =============================================================================
# Testing different p0 in model 2
# =============================================================================
p_zeros = [1, 2, 3, 5, 10]

p_zero = pd.DataFrame()
for i in p_zeros:
    p_zero[r'$p_0: {}$'.format(i)] = pd.Series(pop_fun2(p, p_zero = i))
    
p_zero.plot()
plt.xlabel(r'year')
plt.ylabel(r'population')
plt.legend(title= r"$p_0$",loc='best')
plt.savefig('fig7_report1.png', dpi=600)
plt.show()
plt.clf()