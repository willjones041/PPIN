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
    """Visualizes the nodes in a scatter plot."""
    x_values = [node.x for node in nodes]
    y_values = [node.y for node in nodes]

    plt.scatter(x_values, y_values, marker="x", color="blue")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Grid Nodes Visualization")
    plt.grid(True)
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

def animate_parcel_histories(parcel_histories):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Set the limits of the plot
    ax.set_xlim(0, x_extent)
    ax.set_ylim(0, y_extent)

    # Create an empty plot
    scatter = ax.scatter([], [])

    # Function to update the plot for each frame
    def update(frame):
        x_values = [history[frame][0] for history in parcel_histories]
        y_values = [history[frame][1] for history in parcel_histories]
        scatter.set_offsets(np.column_stack((x_values, y_values)))
        return scatter,

    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=len(parcel_histories[0]), interval=1000, blit=True)

    # Show the animation
    plt.show()
   
    