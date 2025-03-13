from fields.domain import Domain
from utils import *
from parcels.parcels import *
from parcels.precip_parcels import *
from fields.grid import Grid
from fields.node import Node
def main():
    
    
    # Create domain
    domain = Domain(x_extent, y_extent, (origin_x, origin_y),num_parcels)

    # Create grid with structured nodes
    grid = domain.create_grid(num_x, num_y)
   
   #create parcels
    domain.create_parcels()

    

    # #PLOT PARCELS
    plot_nodes_and_parcels(Node.get_all_instances(),PrecipParcel.get_all())
    print(grid.grid2par(0.5,0.5))

    # #Run Loop
    # t=0
    # t_plot = 0
    # while t < runtime:
    #     for parcel in PrecipParcel.get_all():

    #         parcel.move(grid=grid,t=t,delt=delt)
    #     t=t+delt
    



if __name__ == "__main__":
    main()


