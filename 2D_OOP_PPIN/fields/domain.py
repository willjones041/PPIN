# here is the domain class where we store info on domains attributes and behaviours
from fields.grid import Grid
class Domain:
    def __init__(self,x_extent,y_extent,origin):# Initiating attributes
        self.x_extent = x_extent
        self.y_extent = y_extent
        self.origin = origin #(x,y) tuple
    
    #Now defining methods of a domain object
    def create_grid(self,num_x,num_y):
        """Creates a grid based on this domain"""
        return Grid(self, num_x, num_y)