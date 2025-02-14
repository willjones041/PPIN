import math
import decimal
import numpy as np
from constants import *
# This is a function to relate terminal velocity to droplet size,
# if by evaporation the droplet size changes the terminal velocity would change
def vel_func(parcel,ro_air_p):
    #These constants are from Shipway and Abel (2007) based on the observational work of Beard (1978)
    #The same as used in CASIM
    
    
    #Abel and Shipway rain
    xdot = -((a1*(parcel['D']**b1)*(math.e**(g1*parcel['D'])))\
           + (a2*(parcel['D']**b2)*(math.e**(g2*parcel['D']))))\
            *(ro0/ro_air_p)**(f)
    if parcel['parcel_no']==1:
        print(xdot)

    return xdot

