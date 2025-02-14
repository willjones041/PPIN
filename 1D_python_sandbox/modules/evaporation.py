#Not complete all this does is step through the equations! Needs a grid2par function 
# and a call to the grid2par function to evolve the qr and Nr values

import numpy as np
import math
from constants import *
from grid2par import *
#Define constants

def evaporation(parcel,noded_values):
#Slope calculation

    slope = ((math.pi*parcel['Nr']*ro_r*math.gamma(4+shape))/(6*parcel['qr']*math.gamma(1+shape)))**(1/3)
    #Ventilation coefficient
    vent_r = 2*math.pi*parcel['Nr']*noded_values['ro_air_p']* \
        (0.78*((1+shape)/(slope)) \
                +  0.31*((a1*noded_values['ro_air_p']/visc)**(0.5))*(Sc**(1/3))*((ro0/noded_values['ro_air_p'])**(1/4))  \
                * (math.gamma((0.5*b1 +shape +2.5))/math.gamma((1+shape))) \
                *((1 + (0.5*f)/slope)**(-(0.5*b1 + shape + 2.5))) \
                *((slope)**(-0.5*b1 -1.5)))
    #This will be a call to get the grid temperatures and humidities!! Call 2 par2grid
    ABliq = ((Lv**2)/(Ka*Rv* (noded_values['temp_p']**2))) + (1/(noded_values['ro_air_p']*noded_values['ws_p']*diffus))
    
    
    qr_dot = (((noded_values['qv_p']/noded_values['ws_p'])-1)/(noded_values['ro_air_p']*ABliq))*vent_r
    
    nr_dot = 0#qr_dot*(parcel['Nr']/parcel['qr'])
    if homog == True:
       nr_dot = qr_dot*(parcel['Nr']/parcel['qr']) 
    elif homog == False:
        nr_dot = 0   
    return qr_dot,nr_dot