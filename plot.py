#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from planet_orbit_calculator import stellarreflextime

M = np.arange(0.2,5.1,0.1)
N = np.arange(0.5,3000,10)
P = np.arange(0.1,10.1,0.1)

res = np.zeros((len(M),len(N),len(P)))
for i in range(len(M)):
    for j in range(len(N)):
        for k in range(len(P)):
            res[i,j,k] = stellarreflextime(M[i],N[j],P[k])

fig = plt.figure()
ax = fig.add_subplot(111)
plt.contourf(N,M,res[:,:,-1])
plt.colorbar()
plt.show()