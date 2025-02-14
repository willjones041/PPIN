#Use Uplinger constants from Abel and Shipway (2007) paper in the ventilation coefficient
#Using the Abel and shipway constants for terminal velocity
# this is an inconsistency in the treatment of the particles! Fix
#
a1 = 4854
b1 = 1
a2 =-446
b2 = 0.782
g1 = 195
g2 = 4085.35
f = 0.5
ro0 = 1.2256
ro_r = 1000
visc = 1.14*10**-5
#diffusivity of water on air
diffus = 2.42*10**-5
Sc = visc/diffus
shape = 2.5
n_nodes = 10
num_parcels = 100
domain_height = 3200
domain_floor = 0
T0 = 298
P0 = 10**5
RH = 0.7
Rd = 287.05
homog = False
#Assuming T is constant at 24.85 degrees C
#Latent heat of vapourisation
Lv = 2.442*10**6
#Thermal conductivity of air
Ka = 0.02623
#gas constant for water vapour
Rv = 461.52
Lapse = 0.00065
node_gap = abs(domain_height - domain_floor)/n_nodes
PSH = 8619
#mass to diameter constants from CASIM
c = 522
d = 3
#Initialise time
t = 0
# How long to run for
runtime = 500
# Fixed timestep (for now)
delt = 0.05