# Here is where the grid class is defined 
from fields.nodes import Node
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
                self.nodes.append(Node(x, y))
    
    def get_nodes(self):
        """Returns a list of nodes."""
        return self.nodes