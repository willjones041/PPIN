# ===================================================
#               These functions initialise the parcel array 
#               and array of domian nodes
# ===================================================
import numpy as np
def create_parcel_array(num_parcels):
    parcel_array = []
    # Each parcel will have the attributes number, rainwater number concentration
    # rainwater mixing ratio, volume, z_position and dz, and for now a D, although this can be diagnosed from Nr and qr 
    for i in range(num_parcels):
        parcel = {
            'parcel_no' : i,
            'Nr' : 3*10**5,
            'dNr': 1,
            'qr' : 0.005,
            'dqr': 1,
            'z_pos': np.random.normal(1000,2),
            'dz':1,
            'D':0.0001
        }
        parcel_array.append(parcel)
    return parcel_array


def create_noded_field(n_nodes):
    node_no = []
    z_node = []
    temp_node = []
    qv_node = []
    p_node = []
    ro_node = []
    ws_node = []
    noded_field ={'node_no':node_no,'z_node':z_node,'temp_node':temp_node,'qv_node':qv_node,'p_node':p_node,'ro_node':ro_node,'ws_node':ws_node}
    
    for index in reversed(range(n_nodes)):
        # Each node will be a fixed point within a prescribed 
        # atmoshperic profile
        node_no.append(index)
        
    return noded_field

