from fields.domain import Domain
from utils import display_nodes, plot_nodes
def main():
    # Simulated user input
    x_extent = float(input("Enter X extent of domain: "))
    y_extent = float(input("Enter Y extent of domain: "))
    origin_x = float(input("Enter X coordinate of origin: "))
    origin_y = float(input("Enter Y coordinate of origin: "))
    num_x = int(input("Enter number of nodes along X: "))
    num_y = int(input("Enter number of nodes along Y: "))

    # Create domain
    domain = Domain(x_extent, y_extent, (origin_x, origin_y))

    # Create grid with structured nodes
    grid = domain.create_grid(num_x, num_y)

    # Display nodes
    print("\nGenerated Nodes (Evenly Spaced):")
    display_nodes(grid.get_nodes())

    # Plot nodes (optional)
    plot_nodes(grid.get_nodes())


if __name__ == "__main__":
    main()

