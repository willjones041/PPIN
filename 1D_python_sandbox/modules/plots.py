# ===================================================
#              This is where I keep my plotting functions
# ===================================================
import matplotlib.pyplot as plt
def plot_z_pos(noded_field):
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Example data structure (replace with your actual data)

    # Set professional style
    sns.set_style("whitegrid")
    plt.rcParams.update({'font.size': 12})

    fig, axes = plt.subplot_mosaic([
        ['temp', 'qv', 'p']
    ], sharey=True, figsize=(9, 6))

    # Temperature Plot
    axes['temp'].plot(noded_field['temp_node'], noded_field['z_node'], color='red', linewidth=2)
    axes['temp'].set_xlabel('Temperature (K)')
    axes['temp'].set_ylabel('Height (m)')
    axes['temp'].set_title('Temperature Profile')
    axes['temp'].set_xlim(min(noded_field['temp_node']) - 1, max(noded_field['temp_node']) + 1)

    # Humidity Plot
    axes['qv'].plot(noded_field['qv_node'], noded_field['z_node'], color='blue', linewidth=2)
    axes['qv'].set_xlabel('Specific Humidity (g/kg)')
    axes['qv'].set_title('Humidity Profile')
    
    # Pressure Plot
    axes['p'].plot(noded_field['p_node'], noded_field['z_node'], color='green', linewidth=2)
    axes['p'].set_xlabel('Pressure (hPa)')
    axes['p'].set_title('Pressure Profile')
    axes['p'].set_xlim(min(noded_field['p_node']) - 25, max(noded_field['p_node']) + 25)

    # Adjust layout and add grid
    plt.tight_layout()
    plt.show()

        



def plot_arrays_vs_t(t, nr_array, qr_array,  z_array):
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
    #D=[D*1000 for D in D]
    # Create a 2x2 grid of subplots (2 rows, 2 columns)
    # superscripts
    base = "m"
    power= "\u207B"  # Superscript 2
    power2 = "\u00b3"
    smolr = "\u1D63"
    sentance = f'N{smolr} ({base}{power}{power2})'
 
    fig, axs = plt.subplot_mosaic("ADB;ADB",sharex=True)
    fig.set_layout_engine('compressed')
    # Plot nr_array on the first subplot (top-left)
    axs['A'].plot(t, nr_array, label='Nr', color='b')
    axs['A'].set_ylabel(f'Rainwater number concentration {sentance}')
    axs['A'].tick_params(axis='y')
    axs['A'].set_title(f'N{smolr} Vs time')

    # Plot qr_array on the second subplot (top-right)
    axs['B'].plot(t, qr_array, label='LWC kg/kg', color='g')
    axs['B'].set_ylabel(f'Rainwater mixing ratio q{smolr}')
    axs['B'].tick_params(axis='y')
    axs['B'].set_title(f'q{smolr} vs time')

    # # Plot D on the third subplot (bottom-left)
    # axs['C'].plot(t, D, label='D', color='r')
    # axs['C'].set_xlabel('time (s)')
    # axs['C'].set_ylabel('Diameter (mm)', color='r')
    # axs['C'].tick_params(axis='y', labelcolor='r')
    # axs['C'].set_title('D vs t')

    # Plot z_array on the fourth subplot (bottom-right)
    axs['D'].plot(t, z_array, label='Height', color='purple')
    axs['D'].set_xlabel('Time (s)')
    axs['D'].set_ylabel('Height (m)')
    axs['D'].tick_params(axis='y')
    axs['D'].set_title('Height vs time')

    #add a title for whole figure
    #fig.suptitle('Homogeneous evaporation of parcel_no 1',fontsize=16)
    # Adjust the layout to prevent overlap
    plt.tight_layout()
    
    # Show the plot
    plt.show()





