import numpy as np
import matplotlib.pyplot as plt
from vel_func import *
from grid2par import *
from evaporation import *
from empty_arrays import *
from remover import *
def RK3_step(parcel,t,xdot,qr_dot,nr_dot,delt):
    ca =  np.array([0,-567301805773/1357537059087,-2404267990393/2016746695238,\
                    -3550918686646/2091501179385,-1275806237668/842570457699])
    cb = np.array([1432997174477/9575080441755,5161836677717/13612068292357,\
          1720146321549/2090206949498,3134564353537/4481467310338,\
          2277821191437/14882151754819,-1275806237668/842570457699])
    cc = np.array([0,1432997174477/9575080441755,2526269341429/6820363962896,\
                   2006345519317/3224310063776,2802321613138/2924317926251])
    
    for j in range(5):
        
        if j ==0:
            #postition
            parcel['dz']= xdot
            parcel['z_pos']=parcel['z_pos'] + cb[j]*parcel['dz']*delt
            #number concentration
            parcel['dNr']= nr_dot
            parcel['Nr']=parcel['Nr'] + cb[j]*parcel['dNr']*delt
            # mixing ratio
            parcel['dqr']= qr_dot
            parcel['qr']=parcel['qr'] + cb[j]*parcel['dqr']*delt
        else:
            t= t + cc[j]*delt
            #position
            parcel['dz']= ca[j]*parcel['dz'] + xdot 
            parcel['z_pos']= parcel['z_pos'] + cb[j]*parcel['dz']*delt
            #number concentration
            parcel['dNr']= ca[j]*parcel['dNr'] + nr_dot 
            parcel['Nr']= parcel['Nr'] + cb[j]*parcel['dNr']*delt
            #mixing ratio
            parcel['dqr']= ca[j]*parcel['dqr'] + qr_dot
            parcel['qr']= parcel['qr'] + cb[j]*parcel['dqr']*delt



    return parcel
def move_parcels(parcel_array,t,delt,noded_field):
    for parcel in parcel_array:
        noded_values = grid2par(parcel,noded_field)
        xdot = vel_func(parcel,noded_values['ro_air_p'])
        qr_dot,nr_dot = evaporation(parcel,noded_values)
        RK3_step(parcel,t=t,xdot=xdot,qr_dot=qr_dot,nr_dot=nr_dot,delt=delt)
        #Calculate average rain mass and then calculate average rain diameter
        parcel['D']=((parcel['qr']/parcel['Nr'])/c)**(1/d)
        if parcel['z_pos']<=0:
            remover(parcel=parcel,parcel_array=parcel_array,impinged=impinged)
        if parcel['parcel_no']==1:
            print(parcel['z_pos'])
    return parcel_array

