# Here is where the grid class is defined 
from fields.node import Node
import numpy as np
from constants import *
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
                if x == 1:
                    temp = 1
                elif x == 0:
                    temp = 0
                else: temp = 100
                # if y <=100:
                #     temp = 300
                # elif y > 100 and y <= 200:
                #     temp = 250
                # else:
                #     temp = 200
                qv = 0.01
                ro = 1.225
                ws = 0.0001
                Node(x, y, temp, qv, ro, ws)
  
    
    def grid2par(self, x, y):
        """Interpolates the values of the grid to the parcel position."""
        # Find the closest nodes to the parcel
        nodes = Node.get_all_instances()
        closest_nodes = []
        for node in nodes:
            if abs(x -node.x) <= gridbox_x and abs(y-node.y) <= gridbox_y:
                closest_nodes.append(node)
        
        # Sort the closest nodes based on their distance to the parcel
        closest_nodes.sort(key=lambda node: ((node.x - x) ** 2 + (node.y - y) ** 2))
        
        # Extract the temperature, qv, ro, and ws values from the closest nodes

        BL = closest_nodes[0]
        TL = closest_nodes[1]
        BR = closest_nodes[2]
        TR = closest_nodes[3]
        x1 = BL.x
        x2 = BR.x
        y1 = BL.y
        y2 = TL.y
        print(f'BL = {BL}, BR = {BR}, TL = {TL}, TR = {TR}')
        print(f'x1 = {x1}, x2 = {x2}, y1 = {y1}, y2 = {y2}')
        temp = ((((x2-x)*(y2-y))/((x2-x1)*(y2-y1)))*BL.temp 
            + (((x-x1)*(y2-y))/((x2-x1)*(y2-y1)))*BR.temp 
            + (((x2-x)*(y-y1))/((x2-x1)*(y2-y1)))*TL.temp 
            + (((x-x1)*(y-y1))/((x2-x1)*(y2-y1)))*TR.temp)
        qv = ((((x2-x)*(y2-y))/((x2-x1)*(y2-y1)))*BL.qv 
            + (((x-x1)*(y2-y))/((x2-x1)*(y2-y1)))*BR.qv 
            + (((x2-x)*(y-y1))/((x2-x1)*(y2-y1)))*TL.qv 
            + (((x-x1)*(y-y1))/((x2-x1)*(y2-y1)))*TR.qv)
        ro = ((((x2-x)*(y2-y))/((x2-x1)*(y2-y1)))*BL.ro 
            + (((x-x1)*(y2-y))/((x2-x1)*(y2-y1)))*BR.ro 
            + (((x2-x)*(y-y1))/((x2-x1)*(y2-y1)))*TL.ro 
            + (((x-x1)*(y-y1))/((x2-x1)*(y2-y1)))*TR.ro)
        ws = ((((x2-x)*(y2-y))/((x2-x1)*(y2-y1)))*BL.ws 
            + (((x-x1)*(y2-y))/((x2-x1)*(y2-y1)))*BR.ws 
            + (((x2-x)*(y-y1))/((x2-x1)*(y2-y1)))*TL.ws 
            + (((x-x1)*(y-y1))/((x2-x1)*(y2-y1)))*TR.ws)    




        # Return the interpolated temperature
        return temp, qv, ro, ws
        
    
    