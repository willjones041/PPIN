from init_arrays import *
from init_domain import *
from plots import *
from RK3 import *
from grid2par import *
import matplotlib.pyplot as plt
import math

#Initialise the parcel array
parcel_array = create_parcel_array(num_parcels)
#Initialise the noded field
noded_field = atmos_profile(create_noded_field(n_nodes))
#Here is the runtime script

while t < runtime:
    move_parcels(parcel_array,t,delt,noded_field=noded_field)
    
    t = t+delt

#plot_arrays_vs_t(t=t_array,nr_array=nr_array,qr_array=qr_array,z_array=z_array)
#plot_z_pos(noded_field)
