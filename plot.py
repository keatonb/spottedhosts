# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 12:53:01 2015

@author: supernova
"""
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from planet_orbit_calculator import stellarreflextime

M = np.arange(1,5.1,1)
N = np.arange(1,5.1,1)
P = np.arange(1,5.1,1)

res = np.zeros((len(M),len(N),len(P)))
for i in range(len(M)):
    for j in range(len(N)):
        for k in range(len(P)):
            res[i,j,k] = stellarreflextime(M[i],N[j],P[k])

fig = plt.figure()
ax = fig.add_subplot(111)
plt.contourf(M,N,res[:,:,0]) #slice: for 1 year period
colorbar()
plt.show()