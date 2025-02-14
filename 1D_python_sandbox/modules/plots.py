# ===================================================
#              This is where I keep my plotting functions
# ===================================================

def plot_z_pos(parcel_array):
    import matplotlib.pyplot as plt
    parcel_no = [parcel['parcel_no'] for parcel in parcel_array]
    z_pos = [parcel['z_pos'] for parcel in parcel_array]

    plt.figure(figsize=(10, 6))
    plt.plot(parcel_no, z_pos, marker='o', linestyle='', color='b', label='z_pos')
    plt.title('Parcel Number vs z_pos')
    plt.xlabel('Parcel Number')
    plt.ylabel('z_pos')
    plt.grid(True)
    plt.legend()
    plt.show()