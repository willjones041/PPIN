from fields.domain import Domain
from utils import *
from parcels.parcels import *
from parcels.precip_parcels import *
from fields.grid import Grid
def main():
    
    
    # Create domain
    domain = Domain(x_extent, y_extent, (origin_x, origin_y),num_parcels)

    # Create grid with structured nodes
    grid = domain.create_grid(num_x, num_y)
   #create parcels
    for i in range(num_parcels):
        x = random.randint(1, 30)
        y = random.random(0, domain.y_extent)
        qr = qr0
        nr = nr0
        PrecipParcel(x,y,qr=qr,nr=nr)

    #Run Loop
    t=0
    while t < runtime:
        for parcel in PrecipParcel.get_all():

            parcel.move(grid=grid,t=t,delt=delt)
        t=t+delt
        print(t)
    



if __name__ == "__main__":
    main()


