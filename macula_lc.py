#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from planet_orbit_calculator import timeoffset
from pymacula import MaculaModel, Spot, Star

#Reference: https://github.com/timothydmorton/pymacula

#Here are the default settings:
#pymacula.MaculaModel(self, t=None, fobs=None, tmin=0, tmax=500, t_start=None, t_end=None, star=None, 
#  spots=None, nspots=3, inst_offsets=None, blend_factors=None)

#Spot(self, lon=None, lat=None, alpha_max=5.0, contrast=0.3, tmax=None, lifetime=None, ingress=None, egress=None)
#ingress, egress, lon, lat, tmax all have random generators

#Star(self, incl=1.5707963267948966, Peq=30.0, kappa2=0.3, kappa4=0.3, c1=0.3999, c2=0.4269, c3=-0.0227, c4=-0.839, 
#   d1=0.3999, d2=0.4269, d3=-0.0227, d4=-0.839)

#Keep inst_offsets = None and blend_factors = None


testspot = Spot(lon=0, lat=0, alpha_max=5.0, contrast=0.3, tmax=1, lifetime=1, ingress=1, egress=1)
teststar = Star()

model = MaculaModel(spots=[testspot],star=[teststar]) #default, no randomness
ts = np.arange(0,500,0.05)
plt.plot(ts, model(ts))

t = timeoffset(ts,5.,50.,0)
plt.plot(ts, model(t))
plt.title("LCs Comparing Time vs Perturbed Time Models")
plt.xlabel("Time (s)")
plt.ylabel("Flux")
plt.show()

print np.sum((model(ts) - model(t))**2) #difference