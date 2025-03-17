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
    artists = []
    fig, ax = plt.subplots()
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
            parcel.x_teleport()
            parcel.move(grid=grid,t=t,delt=delt)
            if parcel.id == 0:
                pass#print(f'parcel x = {parcel.x}, parcel y = {parcel.y}')  
        t=t+delt
        print(f'time = {t}')
        xdata = [parcel.x for parcel in PrecipParcel.instances]
        ydata = [parcel.y for parcel in PrecipParcel.instances]
        container = plt.scatter(xdata, ydata, color='blue')
        artists.append(container)
    print(len(artists))
    ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=1000)
    plt.show()
        
            
        
       
        
    
        
        
    



if __name__ == "__main__":
    main()


