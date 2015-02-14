# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 23:21:55 2015

@author: supernova
"""

import pymacula
#import planet_orbit_calculator
import numpy as np
import matplotlib.pyplot as plt

time = int(raw_input("Number of time points: "))
times = np.arange(time)
derivatives = True
temporal = True
tdeltav = True
theta_star = np.matrix(1,2)
theta_spot = np.matrix(1,2)
theta_inst = np.matrix(1,2)
t_start = times[0]
t_stop = times[-1] 

output = pymacula.maculamod.macula(times,derivatives,temporal,tdeltav,theta_star,theta_spot,theta_inst,t_start,t_stop)

Fmod = output[0]
dFmod_star = output[1]
dFmod_spot = output[2]
dFmod_inst = output[3]
dFmoddt = output[4]
deltaratio = output[5]

plt.plot(dFmod_star,dFmod_spot)
plt.show()

for star_mass in np.arange(1,10,0.1):
    for planet_mass in np.arange(1,10,0.1):
        #plt.plot(star_mass,planet_mass)        
        hist2d(star_mass,planet_mass)
        print '(%d,%d)' % (star_mass,planet_mass)

        
        
        
        