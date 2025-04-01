import matplotlib.pyplot as plt
from parcels.parcels import *
from parcels.precip_parcels import *    
from constants import *
from fields.domain import Domain
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def display_nodes(nodes):
    """Prints the generated nodes in a readable format."""
    for node in nodes:
        print(node)

def plot_nodes(nodes):
    """Visualizes the nodes in a scatter plot with node.temp and node.ro on twin x axes."""
    x_values = [node.y for node in nodes]
    temp_values = [node.temp for node in nodes]
    ro_values = [node.ro for node in nodes]
    

    fig, ax1 = plt.subplots()
    ax1.scatter(x_values, temp_values, marker="x", color="blue")
    ax1.set_xlabel("Y Coordinate")
    ax1.set_ylabel("Temperature")
    ax1.set_title("Grid Nodes Visualization")
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.scatter(x_values, ro_values, marker="o", color="red")
    ax2.set_ylabel("Density")

    plt.show()

def display_parcels(parcels):
    """Displays the positions of all parcels in the domain on a graph."""
    x_values = [parcel.x for parcel in parcels]
    y_values = [parcel.y for parcel in parcels]
    plt.scatter(x_values, y_values, marker="o", color="red")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Parcels Position Visualization")
    plt.grid(True)
    plt.show()

def plot_nodes_and_parcels(nodes, parcels,time):
    """Visualizes the nodes and parcels on the same plot."""
    node_x_values = [node.x for node in nodes]
    node_y_values = [node.y for node in nodes]
    parcel_x_values = [parcel.x for parcel in parcels]
    parcel_y_values = [parcel.y for parcel in parcels]
        
    fig, ax = plt.subplots()
    ax.scatter(node_x_values, node_y_values, marker="x", color="blue", label="Nodes")
    ax.scatter(parcel_x_values, parcel_y_values, marker="o", color="red", label="Parcels")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title(f"Nodes and Parcels Visualization at {time} seconds")
    plt.grid(True)
    plt.legend()
    plt.show()
    plt.close(fig)
        
    return fig

   
def fill_container(ax, parcels):
    xdata = [parcel.x for parcel in parcels]
    ydata = [parcel.y for parcel in parcels]
    areadata = [1/parcel.nr*10000 for parcel in parcels]
    container = [ax.scatter(xdata, ydata,areadata, color='blue')]
    return container

def set_pos_figure():
    fig, ax = plt.subplots()
    ax.set_xlim(0, x_extent)
    ax.set_ylim(0, y_extent)
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")   
    ax.set_title("Parcels Position Visualization")
    ax.grid(True)
    artists = []
    return fig, ax, artists

    
def plot_variables_with_height(x1_values,x2_values, height):
    fig, ax1 = plt.subplots()
    ax1.scatter(height, x1_values, marker="x", color="blue")
    ax1.set_xlabel("Depth m")
    ax1.set_ylabel("First Variable")
    ax1.set_title("Variables Visualization")
    ax1.grid(True)
    ax2 = ax1.twinx()
    ax2.plot(height, x2_values, color="red")
    ax2.set_ylabel("Second variable")
   
    plt.show()
    