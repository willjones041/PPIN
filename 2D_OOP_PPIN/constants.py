import numpy as np

# Simulated user input
x_extent = 10#float(input("Enter X extent of domain: "))
y_extent = 10#float(input("Enter Y extent of domain: "))
origin_x = 0#float(input("Enter X coordinate of origin: "))
origin_y = 0#float(input("Enter Y coordinate of origin: "))
num_x = 11#int(input("Enter number of nodes along X: "))
num_y = 11#int(input("Enter number of nodes along Y: "))
gridbox_x = x_extent/(num_x-1)
gridbox_y = y_extent/(num_y-1)

num_parcels = 100#int(input("Enter parcel number: "))
qr0 = 0.0001#float(input("Enter initial mass mixing ratio:"))
nr0 = 100000##float(input("Enter initial number concentration:"))
rainfall = 0
ro_air_p = 1.225
#Abel and Shipway rain
a1 = 4854
b1 = 1
a2 =-446
b2 = 0.782
g1 = 195
g2 = 4085.35
f = 0.5
D=0.001
#Runge kutta coefficients
ca =  np.array([0,-567301805773/1357537059087,-2404267990393/2016746695238,\
                    -3550918686646/2091501179385,-1275806237668/842570457699])
cb = np.array([1432997174477/9575080441755,5161836677717/13612068292357,\
          1720146321549/2090206949498,3134564353537/4481467310338,\
          2277821191437/14882151754819,-1275806237668/842570457699])
cc = np.array([0,1432997174477/9575080441755,2526269341429/6820363962896,\
                   2006345519317/3224310063776,2802321613138/2924317926251])
#rainfall rate initial value
rainfall = 0

#Size distribution constants
shape = 2.5

#physical constants
ro_r = 1000
visc = 1.14*10**-5
#diffusivity of water on air
diffus = 2.42*10**-5
Sc = visc/diffus
#Assuming T is constant at 24.85 degrees C
#Latent heat of vapourisation
Lv = 2.442*10**6
#Thermal conductivity of air
Ka = 0.02623
cp = 1005.7
#gas constant for water vapour
Rv = 461.52
ro0 = 1.2256
homog = True

#time constants
runtime = 100
delt = 0.05

#parcel initialisations
init_y_parcels = (2/3)*y_extent
std_dev_y_parcels = 0.1*y_extent

