# ===================================================
#               These functions will create a prescribe atmospheric 
#               profile to the node_array
# ===================================================
# This function prexcribes a height value to each node
import math 
from constants import *

 # give each node a z_value
def z_profile(noded_field):
    for index in reversed(range(n_nodes)):
        if index == 0:
            z = domain_floor
        elif index == n_nodes-1:
            z = domain_height
        else:
            z = (index+1)*node_gap
        noded_field['z_node'].append(z)
    return noded_field

# This function prescribes a temperature value to each node
# Would be a good idea to call some function here that makes a temperature profile
def atmos_profile(noded_field):
    noded_field = z_profile(noded_field)
    for z in noded_field['z_node']:
        # This is where the temperature and humidity profile is initialised in the domain and prescribed to the nodes
        # I got this profile from the bomex setup case
        # Use lapse rate of 6.5 degrees per kilometre
        #Giving it a pressure and stuff as well
        p_node = P0*math.e**(-z/PSH)
        exn = (p_node/P0)**(Rd/cp)
        temp_node = theta0*exn 
        p_node = P0*math.e**(-z/PSH)
        ws_node = 3.8/(p_node*math.e**(-17.2693882*(temp_node-273.15)/(temp_node-35.86))-6.109)
        qv_node = RH*ws_node
        Tv_node = temp_node*(1+ 0.61*qv_node)
        ro_node = p_node/(Rd*Tv_node)
        noded_field['p_node'].append(p_node)
        noded_field['ws_node'].append(ws_node)
        noded_field['temp_node'].append(temp_node)
        noded_field['qv_node'].append(qv_node)
        noded_field['ro_node'].append(ro_node)
        
    return noded_field



