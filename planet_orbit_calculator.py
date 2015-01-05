#! /usr/bin/env python

from math import pi

# Constants
G = 6.67259e-8 #Gravitational constant (cm^2 g^-1 s^-2)
c = 2.99792458e10 #Speed of light (cm s^-1)
Msun = 1.99e33 #Solar mass (g)
Mearth = 5.976e27 #Earth mass (g)
Yearinsecs = 365.*86400. #length of Earth year (s)

def stellarreflextime(M,N,P, i=True):
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
    a = (((P**2)*G*T)/(4*(pi**2)))**(1./3)
    
    # Consider the relationship M * r = a * N. We find the radius of the star's wobble around the center of mass in centimeters.
    r = a * N / M

    # Changes the units of meters to light travel time.
    l = r / c

    # Return result
    return l

if __name__ == "__main__":
    # Give value for the stellar mass, planet mass, and orbital period.
    M = int(input("Stellar mass in Solar masses:"))
    N = int(input("Planet mass in Earth masses:"))
    P = int(input("Orbital period in years:"))
    l = stellarreflextime(M,N,P, i=True)
    r = l * c
    print "The radius of the star's wobble around the center of mass is", r, "centimeters or", l, "lightseconds."
    
# Consider taking a list of times and each time has been perturbed by an orbital time delay.
times = []
for x in times:
    y = P + sin(x)
    z = r + sin(x)
    # Plot the perturbed times with respect to the original times.
    plt.figure(1)
    plt.xlabel('Time (sec)')
    plt.subplot(211)
    plt.plot(x, y)
    plt.subplot(212)
    plt.plot(x, z)
    plt.subplot(213)
    plt.plot(x, sin(x))
    plt.show()



