#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from planet_orbit_calculator import timeoffset, stellarreflextime
from pymacula import MaculaModel, Spot
#import plot.py

#Reference: https://github.com/timothydmorton/pymacula

#Here are the default settings:
#pymacula.MaculaModel(self, t=None, fobs=None, tmin=0, tmax=500, t_start=None, t_end=None, star=None, 
#  spots=None, nspots=3, inst_offsets=None, blend_factors=None)

#Spot(self, lon=None, lat=None, alpha_max=5.0, contrast=0.3, tmax=None, lifetime=None, ingress=None, egress=None)
#ingress, egress, lon, lat, tmax all have random generators

#Star(self, incl=1.5707963267948966, Peq=30.0, kappa2=0.3, kappa4=0.3, c1=0.3999, c2=0.4269, c3=-0.0227, c4=-0.839, 
#   d1=0.3999, d2=0.4269, d3=-0.0227, d4=-0.839)

testspot = Spot(lon=0, lat=0, alpha_max=5.0, contrast=0.3)
testspot.tmax = 0.2
testspot.lifetime = 1.
testspot.ingress = 0.7
testspot.egress = 0.5

model = MaculaModel(spots=[testspot],nspots=1)
ts = np.arange(0,500,0.05)
plt.plot(ts, model(ts))

M = np.arange(0.2,5.1,0.1)
N = np.arange(0.5,3000,10)
P = np.arange(0.1,10.1,0.1)

res = np.zeros((len(M),len(N),len(P),len(ts)))
for i in range(len(M)):
    for j in range(len(N)):
        for k in range(len(P)):
            for l in range(len(ts)):
                res[i,j,k,l] = (model(ts)-model(timeoffset(ts[l],stellarreflextime(M[i],N[j],P[k]),P[k],0)))**2
                #res[i,j,k] = stellarreflextime(M[i],N[j],P[k])
                #t = timeoffset(ts,stellarreflextime(M[i],N[j],P[k]),P[k],0)
                #u = (model(ts) - model(t))**2
            
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
