from fields.domain import Domain
from utils import *
from parcels.parcels import *
from parcels.precip_parcels import *
from fields.grid import Grid
from fields.node import Node
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

##Next job is to create realistic atmospheric profile
def main():
    
    
    # Create domain
    domain = Domain(x_extent, y_extent, (origin_x, origin_y),num_parcels)

    # Create grid with structured nodes
    grid = domain.create_grid(num_x, num_y)
   
   #create parcels
    domain.create_parcels()

    

    #Run Loop
    t=0
    rainfall = 0
    

    #prime figure for animation
    fig, ax, artists= set_pos_figure()

    while t < runtime and len(PrecipParcel.instances) > 0:
        
        for parcel in PrecipParcel.instances:
            #This is the remover function
            if parcel.y < 0:
                parcel.clear_parcel()
                rainfall += 522*D**(3)
                continue
            elif parcel.nr < 1:
                parcel.clear_parcel()
                continue
            #this is the fucntion that does periodic boundary conditions
            parcel.x_teleport()
            #this is the function that moves the parcels and updates attributes
            parcel.move(grid=grid,t=t,delt=delt)
        
        t=t+delt
        container = fill_container(ax, PrecipParcel.instances)
        artists.append(container)
    
    ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=10)
    plt.show()
        
            
        
       
        
    
        
        
    



if __name__ == "__main__":
    main()


