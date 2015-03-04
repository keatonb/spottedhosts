#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from planet_orbit_calculator import timeoffset
from pymacula import MaculaModel, Spot

testspot = Spot(lon=0, lat=0, alpha_max=5.0, contrast=0.3, tmax=1, lifetime=1, ingress=1, egress=1)

model = MaculaModel(spots=[testspot]) # default
ts = np.arange(0,500,0.05)
plt.plot(ts, model(ts))

t = timeoffset(ts,5.,50.,0)
plt.plot(ts, model(t))
plt.show()

print np.sum((model(ts) - model(t))**2) #difference