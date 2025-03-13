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
    while t < runtime and len(PrecipParcel.instances) > 0:
        
        for parcel in PrecipParcel.instances:
            #This is the remover function
            if parcel.y < 0:
                parcel.clear_parcel()
                rainfall += 522*D**(3)
                continue
            parcel.move(grid=grid,t=t,delt=delt)
        t=t+delt
        print(t)
        print(rainfall)
    plot_nodes_and_parcels(Node.instances,PrecipParcel.instances)
        
        
        
        
       
        
        
    



if __name__ == "__main__":
    main()


