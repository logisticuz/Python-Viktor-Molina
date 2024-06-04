import matplotlib.pyplot as plt
from main import Circle, Rectangle, GeometryShapes
import numpy as np

class ShapeVisualizer:

    @staticmethod
    def draw_shapes_on_same_plot(*shapes):
        fig, ax = plt.subplots()
        for shape in shapes:
            if isinstance(shape, Circle):
                # Using attributes from the Circle class to draw it
                circle = plt.Circle((shape.x, shape.y), shape.radius, color='blue', fill=False, linewidth=2)
                ax.add_patch(circle)
            elif isinstance(shape, Rectangle):
                # Using attributes from the Rectangle class to draw it
                rectangle = plt.Rectangle((shape.x, shape.y), shape.width, shape.height, color='red', fill=False, linewidth=2)
                ax.add_patch(rectangle)

    # Set the limits for the axes
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)

    # Reinforce the origin
        ax.axhline(y=0, color='black', linewidth=2)
        ax.axvline(x=0, color='black', linewidth=2)

    # Adjust the grid
        ax.grid(True, linestyle='-', color='gray', linewidth=0.5, alpha=0.5)
        ax.set_aspect('equal', adjustable='box')
        
    # Set smaller steps for the x-axis and y-axis
        ax.set_xticks(np.arange(-15, 16, 2))  # Smaller steps for x-axis
        ax.set_yticks(np.arange(-15, 16, 2))  # Smaller steps for y-axis

        plt.show()
