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

