import numpy as np
import matplotlib.pyplot as plt

# Create a 20x20 grid
grid_size = 20
grid = np.zeros((grid_size, grid_size))

# Generate random indices for red cells
center_x, center_y = np.random.randint(3, grid_size - 3), np.random.randint(3, grid_size - 3)

# Color the center cell red
grid[center_x, center_y] = 2  # Representing red cells with 2

# Make surrounding cells yellow
for dx in range(-1, 2):
    for dy in range(-1, 2):
        new_x, new_y = center_x + dx, center_y + dy
        if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
            grid[new_x, new_y] = 1  # Representing yellow cells with 1

# Define possible directions of lava flow
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Spread lava to adjacent cells randomly
for i in range(grid_size):
    for j in range(grid_size):
        if grid[i][j] == 1:  # If cell is yellow
            num_spread = np.random.randint(1, 6)  # Random number of adjacent cells to turn yellow
            spread_directions = np.random.choice(len(directions), min(num_spread, len(directions)), replace=False)  # Randomly choose directions
            for direction in spread_directions:
                dx, dy = directions[direction]
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < grid_size and 0 <= new_j < grid_size and grid[new_i][new_j] == 0:
                    grid[new_i][new_j] = 1  # Representing yellow cells with 1

# Plot the grid with colors
plt.imshow(grid, cmap='YlOrRd', interpolation='nearest', vmin=0, vmax=2)
plt.title('2D Grid with Random Lava Flows')
plt.show()
