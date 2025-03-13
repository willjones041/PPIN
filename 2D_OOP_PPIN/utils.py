import matplotlib.pyplot as plt
from parcels.parcels import *
from parcels.precip_parcels import *    
from constants import *
from fields.domain import Domain
def display_nodes(nodes):
    """Prints the generated nodes in a readable format."""
    for node in nodes:
        print(node)

def plot_nodes(nodes):
    """Visualizes the nodes in a scatter plot."""
    x_values = [node.x for node in nodes]
    y_values = [node.y for node in nodes]

    plt.scatter(x_values, y_values, marker="x", color="blue")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Grid Nodes Visualization")
    plt.grid(True)
    plt.show()

def impinge_check():
    for parcel in PrecipParcel.get_all():
        if parcel.y <=0:
            rainfall += 522*D**(3)
            parcel.clear_parcel()
    return rainfall

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

def plot_nodes_and_parcels(nodes, parcels):
    """Visualizes the nodes and parcels on the same plot."""
    node_x_values = [node.x for node in nodes]
    node_y_values = [node.y for node in nodes]
    parcel_x_values = [parcel.x for parcel in parcels]
    parcel_y_values = [parcel.y for parcel in parcels]
        
    plt.scatter(node_x_values, node_y_values, marker="x", color="blue", label="Nodes")
    plt.scatter(parcel_x_values, parcel_y_values, marker="o", color="red", label="Parcels")
        
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Nodes and Parcels Visualization")
    plt.grid(True)
    plt.legend()
    plt.show()