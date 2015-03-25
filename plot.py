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

for k in range(len(P)):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.contourf(N,M,res[:,:,k])
    plt.title("Period = %s years" % P[k])
    plt.xlabel("Planetary Mass $(M_E)$")
    plt.ylabel("Stellar Mass $(M_\odot)$")
    cbar = plt.colorbar()
    cbar.set_label("Seconds", rotation=270)
    plt.show()
    #savefig("P=%s" % P[k])