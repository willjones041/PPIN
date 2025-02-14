# Here i get the values from the nodes to use in ther evolution of the parcel attributes
def grid2par(parcel,noded_field):
    i,iplus = find_upper_lower_indices(z=parcel['z_pos'],L=noded_field['z_node'])
    z_i,z_iplus = noded_field['z_node'][i],noded_field['z_node'][iplus]
    #temp
    temp_iplus,temp_i = noded_field['temp_node'][iplus],noded_field['temp_node'][i]
    #humidity
    qv_iplus,qv_i = noded_field['qv_node'][iplus],noded_field['qv_node'][i]
    # density
    ro_iplus,ro_i = noded_field['ro_node'][iplus],noded_field['ro_node'][i]
    # saturation specific humidity
    ws_iplus,ws_i = noded_field['ws_node'][iplus],noded_field['ws_node'][i]
    #field values at parcel z coordinate
    temp_p = temp_i+((parcel['z_pos']-z_i)*(temp_iplus-temp_i))/(z_iplus-z_i)
    qv_p = qv_i+((parcel['z_pos']-z_i)*(qv_iplus-qv_i))/(z_iplus-z_i)
    ro_air_p = ro_i+((parcel['z_pos']-z_i)*(ro_iplus-ro_i))/(z_iplus-z_i)
    ws_p = ws_i+((parcel['z_pos']-z_i)*(ws_iplus-ws_i))/(z_iplus-z_i)
    return {'temp_p':temp_p,'qv_p':qv_p,'ro_air_p':ro_air_p,'ws_p':ws_p}

def find_upper_lower_indices(z, L):
    # Sort the list along with the original indices
    L_sorted_with_indices = sorted(enumerate(L), key=lambda x: x[1])
    
    # Initialize variables for lower and upper
    lower_index = None
    upper_index = None
    
    for i, value in L_sorted_with_indices:
        if value < z:
            lower_index = i  # index of closest value below z
        elif value > z and upper_index is None:
            upper_index = i  # index of closest value above z
            break
    
    return lower_index, upper_index

