from empty_arrays import rainfall

def remover(parcel,parcel_array,impinged):
    if parcel['z_pos'] <=0:
        impinged.append(parcel)
        rainfall += 522*parcel['D']**(3)
        print(rainfall)
        for i in range(len(parcel_array) - 1, -1, -1):  # Iterate in reverse
            if parcel_array[i].get("z_pos") <=0:  # Condition to remove
                del parcel_array[i]

    return impinged, parcel_array, rainfall