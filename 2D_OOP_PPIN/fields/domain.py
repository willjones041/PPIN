# here is the domain class where we store info on domains attributes and behaviours
from fields.grid import Grid
import random
from constants import *
from parcels.precip_parcels import *
class Domain:
    def __init__(self,x_extent,y_extent,origin,num_parcels):# Initiating attributes
        self.x_extent = x_extent
        self.y_extent = y_extent
        self.origin = origin #(x,y) tuple
        self.num_parcels = num_parcels
    #Now defining methods of a domain object
    def create_grid(self,num_x,num_y):
        """Creates a grid based on this domain"""
        return Grid(self, num_x, num_y)
    
    def create_parcels(self):
        """Creates parcels based on this domain"""
        for i in range(num_parcels):
            x = random.random()*self.x_extent + self.origin[0]
            y = random.gauss(init_y_parcels, std_dev_y_parcels) 
            qr = qr0
            nr = nr0
            PrecipParcel(x,y,qr=qr,nr=nr)

    