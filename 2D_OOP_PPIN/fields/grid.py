# Here is where the grid class is defined 
from fields.node import Node
import numpy as np
from constants import *
import math 
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
    #   defining the temperature profile from the top down
        for i in range(self.num_x):
            for j in range(self.num_y):
                x = self.domain.origin[0] + i * x_spacing
                y = self.domain.origin[1] + j * y_spacing
                
                temp,ws,qv,ro,diffus,visc,Lv = self.domain.atmospheric_profile(x=x,y=y)

                
                self.nodes.append(Node(x=x, y=y, temp=temp, qv=qv, ro=ro, ws=ws,diffus=diffus,visc=visc,Lv=Lv))
                
    
    def grid2par(self, x, y):
        """Interpolates the values of the grid to the parcel position."""
        # Find the closest nodes to the parcel
        nodes = Node.get_all_instances()
        closest_nodes = []
        for node in nodes:
            if abs(x - node.x) <= gridbox_x and abs(y - node.y) <= gridbox_y:
                closest_nodes.append(node)
            elif x == node.x and y == node.y:
                closest_nodes.append(node)
        # Sort the closest nodes based on their distance to the parcel
        closest_nodes.sort(key=lambda node: (node.x, node.y))
        

        if len(closest_nodes) < 3:
            raise ValueError(f"Not enough closest nodes found for coordinates ({x}, {y}). Found: {closest_nodes}")

        BL = closest_nodes[0]
        TL = closest_nodes[1]
        BR = closest_nodes[2]
        TR = closest_nodes[3]
        x1 = BL.x
        x2 = BR.x
        y1 = BL.y
        y2 = TL.y
       
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
        diffus = ((((x2-x)*(y2-y))/((x2-x1)*(y2-y1)))*BL.diffus 
            + (((x-x1)*(y2-y))/((x2-x1)*(y2-y1)))*BR.diffus
            + (((x2-x)*(y-y1))/((x2-x1)*(y2-y1)))*TL.diffus
            + (((x-x1)*(y-y1))/((x2-x1)*(y2-y1)))*TR.diffus)
        visc =  ((((x2-x)*(y2-y))/((x2-x1)*(y2-y1)))*BL.visc 
            + (((x-x1)*(y2-y))/((x2-x1)*(y2-y1)))*BR.visc
            + (((x2-x)*(y-y1))/((x2-x1)*(y2-y1)))*TL.visc
            + (((x-x1)*(y-y1))/((x2-x1)*(y2-y1)))*TR.visc)
        Lv = ((((x2-x)*(y2-y))/((x2-x1)*(y2-y1)))*BL.Lv 
            + (((x-x1)*(y2-y))/((x2-x1)*(y2-y1)))*BR.Lv
            + (((x2-x)*(y-y1))/((x2-x1)*(y2-y1)))*TL.Lv
            + (((x-x1)*(y-y1))/((x2-x1)*(y2-y1)))*TR.Lv)




        # Return the interpolated thermodynamic variables
        return temp, qv, ro, ws,diffus,visc,Lv
        
    
    