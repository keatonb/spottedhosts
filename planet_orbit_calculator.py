#! /usr/bin/env python

import math

# Constants
G = 6.67259e-8 #Gravitational constant (cm^2 g^-1 s^-2)
c = 2.99792458e10 #Speed of light (cm s^-1)
Msun = 1.99e33 #Solar mass (g)
Mearth = 5.976e27 #Earth mass (g)
Yearinsecs = 365.*86400. #length of Earth year (s)

def stellarreflextime(M,N,P,i=0):
    """Returns stellar reflex time in seconds

    inputs:
    M = Stellar mass in Solar masses
    N = Planet mass in Earth masses
    P = Orbital period in years
    i = Inclination in radians
    """
    
    # Convert to CGS units
    M = M * Msun
    N = N * Mearth
    P = P * Yearinsecs
    
    # Total mass
    T = M + N
    
    # Using the input values, we find the semimajor axis given by Kepler's 3rd Law.
    a = (((P**2)*G*T)/(4*(math.pi**2)))**(1./3)
    
    # Consider the relationship M * r = a * N. We find the radius of the star's wobble around the center of mass in centimeters.
    r = a * N / M

    # Changes the units of meters to light travel time.
    l = r / c
    
    # Include effect of inclination
    l = l * math.cos(i)

    # Return result
    return l

if __name__ == "__main__":
    # Give value for the stellar mass, planet mass, orbital period, and inclination.
    M = float(raw_input("Stellar mass in Solar masses: "))
    N = float(raw_input("Planet mass in Earth masses: "))
    P = float(raw_input("Orbital period in years: "))
    i = float(raw_input("Inclination in radians [0]: ") or "0")
    l = stellarreflextime(M,N,P,i=i)
    r = l * c
    print "The radius of the star's wobble around the center of mass is", r, "centimeters or", l, "lightseconds."
    
def timeoffset(t,o,p=0)
    """Returns stellar reflex time in seconds

    inputs:
    t = time
    o = offset
    p = phase
    """
    t = np.arange()
    o = t + np.sin(t)
