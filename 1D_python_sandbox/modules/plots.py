# ===================================================
#              This is where I keep my plotting functions
# ===================================================

def plot_z_pos(z_array,t):
    

    plt.figure(figsize=(10, 6))
    plt.plot(t, z_array, marker='o', linestyle='', color='b', label='z_pos')
    plt.title('Parcel Number vs z_pos')
    plt.xlabel('Parcel Number')
    plt.ylabel('z_pos')
    plt.grid(True)
    plt.legend()
    plt.show()

import matplotlib.pyplot as plt



def plot_arrays_vs_t(t, nr_array, qr_array, D, z_array):
    """
    Plots nr_array, qr_array, D, and z_array on separate axes within the same 4x4 grid figure.

    Parameters:
    t (array-like): The x-axis values.
    nr_array (array-like): The y-values for the nr_array plot.
    qr_array (array-like): The y-values for the qr_array plot.
    D (array-like): The y-values for the D plot.
    z_array (array-like): The y-values for the z_array plot.
    """
    plt.style.use(style='bmh')
    #Convert m into mm
    D=[D*1000 for D in D]
    # Create a 2x2 grid of subplots (2 rows, 2 columns)
    
    fig, axs = plt.subplot_mosaic("ABD;CCD",sharex=True)
    fig.set_layout_engine('compressed')
    # Plot nr_array on the first subplot (top-left)
    axs['A'].plot(t, nr_array, label='Nr', color='b')
    axs['A'].set_ylabel('Nr m^-3', color='b')
    axs['A'].tick_params(axis='y', labelcolor='b')
    axs['A'].set_title('Nr Vs time')

    # Plot qr_array on the second subplot (top-right)
    axs['B'].plot(t, qr_array, label='LWC kg/kg', color='g')
    axs['B'].set_ylabel('qr', color='g')
    axs['B'].tick_params(axis='y', labelcolor='g')
    axs['B'].set_title('LWC vs t')

    # Plot D on the third subplot (bottom-left)
    axs['C'].plot(t, D, label='D', color='r')
    axs['C'].set_xlabel('time (s)')
    axs['C'].set_ylabel('Diameter (mm)', color='r')
    axs['C'].tick_params(axis='y', labelcolor='r')
    axs['C'].set_title('D vs t')

    # Plot z_array on the fourth subplot (bottom-right)
    axs['D'].plot(t, z_array, label='Height', color='purple')
    axs['D'].set_xlabel('time (s)')
    axs['D'].set_ylabel('Height', color='purple')
    axs['D'].tick_params(axis='y', labelcolor='purple')
    axs['D'].set_title('Height vs t')

    #add a title for whole figure
    fig.suptitle('Homogeneous evaporation of parcel_no 1',fontsize=16)
    # Adjust the layout to prevent overlap
    plt.tight_layout()
    
    # Show the plot
    plt.show()





