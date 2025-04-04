import numpy as np
import math
#time constants
runtime = 100
delt = 0.01

# Number of parcels to be seeded in the domain
num_parcels = 1 

# Height at which to seed the parcels
init_y_parcels = 1000

# Number concentration in each parcel
nr0 = 100000

# Mean droplet diameter in each parcel 
D = 0.0001

#Bounds of the domain
x_extent = 10000
y_extent = 10000

#Coordinates of the origin (don't change)
origin_x = 0
origin_y = 0

#Resolution of the grid (number of nodes)
num_y = 100
num_x = 100

#Grid spacing in x and y
gridbox_x = x_extent/(num_x-1)
gridbox_y = y_extent/(num_y-1)

#Boolean switches for 1. Abel and shipway rain (changes terminal velocity equation) 
# # 2. Inhomogeneous evaporation 
# # # 3. Isothermal atmosphere (if False then lapse rate is used)
abel_shipway = False
inhomog = True
isothermal = True

#Terminal velocity constants from Abel and Shipway (2012)
a1 = 362
b1 = 0.65
a2 =446
b2 = 0.782
g1 = 0
g2 = 4085.35
f = 0.5

#Runge kutta coefficients
ca =  np.array([0,-567301805773/1357537059087,-2404267990393/2016746695238,\
                    -3550918686646/2091501179385,-1275806237668/842570457699])
cb = np.array([1432997174477/9575080441755,5161836677717/13612068292357,\
          1720146321549/2090206949498,3134564353537/4481467310338,\
          2277821191437/14882151754819,-1275806237668/842570457699])
cc = np.array([0,1432997174477/9575080441755,2526269341429/6820363962896,\
                   2006345519317/3224310063776,2802321613138/2924317926251])


#Size distribution constants (shape parameter mu)
shape = 2.5

## physical constants
#density of liquid water
ro_r = 1000


#Thermal conductivity of air
Ka = 0.02623

#Specific heat capacity at constant pressure
cp = 1005.7

#gas constant for water vapour
Rv = 461.52

#density of air at sea levl
ro0 = 1.2256
#Gas constant for dry air (can use as no saturation)
Rd = 287
g = 9.81

#environmental constants
#isotropic

#Surface temperature
T0 = 280
# environmental lapse rate
lapse_rate = 0.009
#surface pressure
P0 = 100000
# Enviornmental relative humidity
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

## Here we use the values given for the starting point thermodynamic variables and the size distribution to calculate
## the mixing ratio of rainwater in the starting parcels
rostart = ro0*math.e**(-(g*init_y_parcels)/(Rd*T0))

qr0 = (ro_r*nr0*(D**3))/rostart