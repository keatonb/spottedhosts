# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 12:53:01 2015

@author: supernova
"""
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import *
from planet_orbit_calculator.py import stellarreflextime
from mpl_toolkits.mplot3d import Axes3D


M = np.arange(1,5.1,1)
N = np.arange(1,5.1,1)
P = np.arange(1,5.1,1)

def time_delay(M,N,P):
    for stellar_mass in M:
        for planet_mass in N:
            for period in P:
                res = [stellarreflextime(stellar_mass,planet_mass, period) for stellar_mass in M for planet_mass in N for period in P]         
                return res
                
res = np.zeros(x,y,z)
for i in range(len(M)):
    for j in range(len(N)):
        for k in range(len(P)):
            return res[i,j,k]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.contourf(M,N,time_delay(M,N,P)[:,:,0]) #slice: for 1 year period
plt.show()