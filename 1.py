import numpy as np
import matplotlib.pyplot as plt

# Create a 20x20 grid
grid_size = 20
grid = np.zeros((grid_size, grid_size))

# Generate 3-5 random indices for red cells
num_red_cells = np.random.randint(3, 6)
red_indices = np.random.choice(range(grid_size * grid_size), num_red_cells, replace=False)

# Convert indices to grid coordinates
red_cells = [(index // grid_size, index % grid_size) for index in red_indices]

# Color the random cells red and others white
for i in range(grid_size):
    for j in range(grid_size):
        if (i, j) in red_cells:
            grid[i][j] = 2  # Representing red cells with 2
        else:
            grid[i][j] = 0

# Spread lava to adjacent cells
for i, j in red_cells:
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            new_i, new_j = i + dx, j + dy
            if 0 <= new_i < grid_size and 0 <= new_j < grid_size and grid[new_i][new_j] == 0:
                grid[new_i][new_j] = 1  # Representing yellow cells with 1

# Plot the grid with colors
plt.imshow(grid, cmap='YlOrRd', interpolation='nearest', vmin=0, vmax=2)
plt.title('2D Grid with Lava Flows')
plt.show()
