# Here is where the grid class is defined 
from fields.node import Node
class Grid:
    def __init__(self,domain, num_x, num_y):
        self.domain = domain #Tying the grid to the domain
        self.nodes = [] # we store the nodes in the grid!
        self.num_x = num_x  # Number of nodes along x-axis
        self.num_y = num_y  # Number of nodes along y-axis
        self.generate_nodes()  # Automatically generate nodes on creation

    def generate_nodes(self):
        """Creates nodes inside the grid based on the specified resolution"""
        x_spacing = self.domain.x_extent / (self.num_x - 1) if self.num_x > 1 else 0
        y_spacing = self.domain.y_extent / (self.num_y - 1) if self.num_y > 1 else 0

        for i in range(self.num_x):
            for j in range(self.num_y):
                x = self.domain.origin[0] + i * x_spacing
                y = self.domain.origin[1] + j * y_spacing
                if y <=100:
                    temp = 300
                elif y > 100 and y <= 200:
                    temp = 250
                else:
                    temp = 200
                qv = 0.01
                ro = 1.225
                ws = 0.0001
                self.nodes.append(Node(x, y, temp, qv, ro, ws))
    
    def get_nodes(self):
        """Returns a list of nodes."""
        return self.nodes
    

    def grid2par(self, x, y):
        """Interpolates the values of the grid to the parcel position."""
        x_min = self.domain.origin[0]
        y_min = self.domain.origin[1]
        x_max = self.domain.origin[0] + self.domain.x_extent
        y_max = self.domain.origin[1] + self.domain.y_extent

        # Find the indices of the nodes that form the grid box
        i_min = int((x - x_min) / (x_max - x_min) * (self.num_x - 1))
        j_min = int((y - y_min) / (y_max - y_min) * (self.num_y - 1))
        i_max = i_min + 1
        j_max = j_min + 1

        # Debug information
        print(f"i_min: {i_min}, j_min: {j_min}, i_max: {i_max}, j_max: {j_max}")
        print(x_min)
        print(y_min)
    # Boundary check
        if i_min < 0 or j_min < 0 or i_min * self.num_y + j_min >= len(self.nodes):
            raise IndexError("Calculated index is out of range")
    



        # Get the nodes at the vertices of the grid box
        node1 = self.nodes[i_min * self.num_y + j_min]
        node2 = self.nodes[i_min * self.num_y + j_max]
        node3 = self.nodes[i_max * self.num_y + j_min]
        node4 = self.nodes[i_max * self.num_y + j_max]
        x1,y1 = node1.x,node1.y
        x2,y2 = node4.x, node4.y
        # Interpolate the temperature based on the parcel position
        temp = ((((x2-x)*(y2-y))/((x2-x1)*(y2-y1)))*node1.temp 
                + (((x-x1)*(y2-y))/((x2-x1)*(y2-y1)))*node2.temp 
                + (((x2-x)*(y-y1))/((x2-x1)*(y2-y1)))*node3.temp 
                + (((x-x1)*(y-y1))/((x2-x1)*(y2-y1)))*node4.temp)
        qv = ((((x2-x)*(y2-y))/((x2-x1)*(y2-y1)))*node1.qv 
                + (((x-x1)*(y2-y))/((x2-x1)*(y2-y1)))*node2.qv 
                + (((x2-x)*(y-y1))/((x2-x1)*(y2-y1)))*node3.qv 
                + (((x-x1)*(y-y1))/((x2-x1)*(y2-y1)))*node4.qv)
        ro = ((((x2-x)*(y2-y))/((x2-x1)*(y2-y1)))*node1.ro 
                + (((x-x1)*(y2-y))/((x2-x1)*(y2-y1)))*node2.ro 
                + (((x2-x)*(y-y1))/((x2-x1)*(y2-y1)))*node3.ro 
                + (((x-x1)*(y-y1))/((x2-x1)*(y2-y1)))*node4.ro)
        ws = ((((x2-x)*(y2-y))/((x2-x1)*(y2-y1)))*node1.ws 
                + (((x-x1)*(y2-y))/((x2-x1)*(y2-y1)))*node2.ws 
                + (((x2-x)*(y-y1))/((x2-x1)*(y2-y1)))*node3.ws 
                + (((x-x1)*(y-y1))/((x2-x1)*(y2-y1)))*node4.ws)    




        # Return the interpolated temperature
        return temp, qv, ro, ws
        
    
    