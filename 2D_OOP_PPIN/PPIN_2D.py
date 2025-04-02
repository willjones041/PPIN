from fields.domain import Domain
from utils import set_pos_figure, fill_container,plot_nodes
from parcels.parcels import Parcel
from parcels.precip_parcels import PrecipParcel
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from constants import x_extent, y_extent, origin_x, origin_y, num_x, num_y, num_parcels, runtime, delt,ro0

##Next job is to create realistic atmospheric profile
def main():
    
    
    # Create domain
    domain = Domain(x_extent, y_extent, (origin_x, origin_y),num_parcels)

    # Create grid with structured nodes
    grid = domain.create_grid(num_x, num_y)

    plot_nodes()
   
   #create parcels
    domain.create_parcels()
    
    #Run Loop
    t=0
    rainfall = 0
    y_track = []
    qr_track = []

    #prime figure for animation
    #fig, ax, artists= set_pos_figure()

    while t < runtime and len(PrecipParcel.instances) > 0:
        
        for parcel in PrecipParcel.instances:

            #These 7 lines check if the parcel is outside the domain and if so, removes it
            if parcel.y < 0:
                rainfall+=parcel.impinge(ro0)
                rainfall_rate = rainfall/t
                print(f'Ping! Rainfall rate = {rainfall_rate} ')
                print(f'Parcel y position = {parcel.y}m ')
                parcel.clear_parcel()
                continue
                
            #These 3 lines clear a parcel if its number concentration is less than 1
            elif parcel.qr < 0:
                parcel.clear_parcel()
                print(f'Poof! Raindrop evaporated at height {parcel.y}m ')
                continue
                
            #this is the function that enforces periodic boundary conditions
            parcel.x_teleport()

            #this is the function that moves the parcels and updates attributes
            parcel.move(grid=grid,t=t,delt=delt)
        #Timer
        t=t+delt
        print(t)
        #This is the function that updates the plot
        #container = fill_container(ax, PrecipParcel.instances)
        #artists.append(container)
        y_track.append(parcel.y)
        qr_track.append(parcel.qr)
    #This is the animation method
    #ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=10)
    #plt.show()
    
    #ani.save('rainfall')
    fig,ax = plt.subplots()
    ax.plot(y_track, qr_track)
    plt.xlabel('y')
    plt.ylabel('qr')
    plt.title('y_track vs qr_track')
    plt.show()

if __name__ == "__main__":
    main()


