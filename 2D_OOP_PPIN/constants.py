import numpy as np
import math
# User input
x_extent = 10000#float(input("Enter X extent of domain: "))
y_extent = 10000#float(input("Enter Y extent of domain: "))
origin_x = 0#float(input("Enter X coordinate of origin: "))
origin_y = 0#float(input("Enter Y coordinate of origin: "))
num_x = 100#int(input("Enter number of nodes along X: "))
num_y = 100#int(input("Enter number of nodes along Y: "))
gridbox_x = x_extent/(num_x-1)
gridbox_y = y_extent/(num_y-1)
num_parcels = 1#int(input("Enter parcel number: "))

#use these for a range of drop size dsitributions 
nrlower = 1e3
nrupper =(3/5)*10**5
#use nr0 for fixed DSD in each parcel i.e fixed diameter
nr0 = 1e5##float(input("Enter initial number concentration:"))

#mass mixing ratio
#qr0 = 0.001#float(input("Enter initial mass mixing ratio:"))

#Abel and Shipway rain constants
a1 = 4854
b1 = 1
a2 =-446
b2 = 0.782
g1 = 195
g2 = -4085.35
f = 0.5


#Runge kutta coefficients
ca =  np.array([0,-567301805773/1357537059087,-2404267990393/2016746695238,\
                    -3550918686646/2091501179385,-1275806237668/842570457699])
cb = np.array([1432997174477/9575080441755,5161836677717/13612068292357,\
          1720146321549/2090206949498,3134564353537/4481467310338,\
          2277821191437/14882151754819,-1275806237668/842570457699])
cc = np.array([0,1432997174477/9575080441755,2526269341429/6820363962896,\
                   2006345519317/3224310063776,2802321613138/2924317926251])



#Size distribution constants
shape = 2.5

#physical constants
ro_r = 1000



#Thermal conductivity of air
Ka = 0.02623
cp = 1005.7
#gas constant for water vapour
Rv = 461.52
ro0 = 1.2256
inhomog = False
isothermal = True

#time constants
runtime = 10000
delt = 1

#parcel initialisations
init_y_parcels = 1000
std_dev_y_parcels = 0

#environmental constants
#isotropic

##
T0 = 280
lapse_rate = 0.009
P0 = 100000
Rd = 287
g = 9.81
RHenv = 0.8

##I went down a rappid hole on the dependence of these with temperature and density 
##Gave these a temperature and density dependence, could just use constants for shallow cases

##Got these from smithsoinian meteorological tables
#for diffusivity
diffus_standard = 2.26e-5
T_standard = 273.15
P_standard = 100000

#for viscocity
suth_const = 110.4
dyn_visc_standard = 1.718e-5

#for latent heat of vapourisation
Lv_standard = 2.257*10**6
T_critical = 647.1
T_boil = 373.15

D = 0.00005
rostart = ro0*math.e**(-(g*init_y_parcels)/(Rd*T0))

qr0 = (ro_r*nr0*(D**3))/rostart