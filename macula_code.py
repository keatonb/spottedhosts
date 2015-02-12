# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 23:21:55 2015

@author: supernova
"""

import pymacula
import math
import numpy as np
import matplotlib.pyplot as plt

time = int(raw_input("Number of time points: "))
times = np.arange(time)
derivatives == True
temporal == True
tdeltav == True
theta_star = matrix()
theta_spot = matrix()
theta_inst = matrix()
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