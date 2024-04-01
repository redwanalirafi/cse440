import numpy as np
import pygame
import sys

# Constants
GRID_SIZE = 30
CELL_SIZE = 20
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
AGENT_COLOR = (0, 0, 255)

# Create the grid
grid = np.zeros((GRID_SIZE, GRID_SIZE))

# Generate random red cells
num_red_cells = np.random.randint(4, 8)
red_indices = np.random.choice(range(GRID_SIZE * GRID_SIZE), num_red_cells, replace=False)
red_cells = [(index // GRID_SIZE, index % GRID_SIZE) for index in red_indices]

# Spread lava from red cells
for i, j in red_cells:
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            new_i, new_j = i + dx, j + dy
            if 0 <= new_i < GRID_SIZE and 0 <= new_j < GRID_SIZE and grid[new_i][new_j] == 0:
                grid[new_i][new_j] = 1  # Representing yellow cells with 1

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pygame.time.Clock()

# Load the agent character
agent_image = pygame.Surface((CELL_SIZE, CELL_SIZE))
agent_image.fill(AGENT_COLOR)

# Function to draw the grid and agent
def draw_grid(agent_pos):
    screen.fill(WHITE)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = YELLOW if grid[i][j] == 1 else RED if grid[i][j] == 2 else WHITE
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    screen.blit(agent_image, (agent_pos[1] * CELL_SIZE, agent_pos[0] * CELL_SIZE))
    pygame.display.flip()

# Main loop
def main():
    agent_pos = [0, 0]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        # Agent logic (random exploration for demonstration)
        next_i = agent_pos[0] + np.random.choice([-1, 0, 1])
        next_j = agent_pos[1] + np.random.choice([-1, 0, 1])
        if 0 <= next_i < GRID_SIZE and 0 <= next_j < GRID_SIZE:
            agent_pos = [next_i, next_j]

        draw_grid(agent_pos)
        clock.tick(5)  # Adjust the speed of movement

# Run the main function
if __name__ == "__main__":
    main()
