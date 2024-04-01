import numpy as np
import pygame
import sys

GRID_SIZE = 5
CELL_SIZE = 50
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define rewards
REWARDS = np.zeros((GRID_SIZE, GRID_SIZE))
REWARDS[GRID_SIZE - 1, GRID_SIZE - 1] = 1  # Reward at the goal state

# Define transition probabilities
# For simplicity, assume deterministic transitions
TRANSITIONS = {}
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        state = i * GRID_SIZE + j
        next_states = {}
        for action in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            if action == 'UP':
                next_i, next_j = max(0, i - 1), j
            elif action == 'DOWN':
                next_i, next_j = min(GRID_SIZE - 1, i + 1), j
            elif action == 'LEFT':
                next_i, next_j = i, max(0, j - 1)
            elif action == 'RIGHT':
                next_i, next_j = i, min(GRID_SIZE - 1, j + 1)
            next_state = next_i * GRID_SIZE + next_j
            next_states[action] = next_state
        TRANSITIONS[state] = next_states

# Q-learning parameters
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9
EPSILON = 0.1
NUM_EPISODES = 1000

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pygame.time.Clock()

# Font for rendering text
font = pygame.font.SysFont(None, 30)

# Initialize Q-values
Q_values = np.zeros((GRID_SIZE * GRID_SIZE, 4))

# Q-learning algorithm
for episode in range(NUM_EPISODES):
    print("hayee")
    state = 0  # Starting state
    while state != GRID_SIZE * GRID_SIZE - 1:  # Continue until reaching the goal state
        # Epsilon-greedy policy
        print("here")
        if np.random.uniform(0, 1) < EPSILON:
            action = np.random.randint(4)  # Explore
        else:
            action = np.argmax(Q_values[state])  # Exploit

        next_state = TRANSITIONS[state][['UP', 'DOWN', 'LEFT', 'RIGHT'][action]]
        reward = REWARDS[next_state // GRID_SIZE, next_state % GRID_SIZE]
        max_next_action = np.argmax(Q_values[next_state])
        Q_values[state, action] += LEARNING_RATE * (
                reward + DISCOUNT_FACTOR * Q_values[next_state, max_next_action] - Q_values[state, action])
        state = next_state

# Define policy based on Q-values
policy = np.argmax(Q_values, axis=1)

# Function to draw grid and agent
def draw_grid(agent_pos):
    screen.fill(WHITE)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = RED if (i, j) == (GRID_SIZE - 1, GRID_SIZE - 1) else BLACK
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    agent_rect = pygame.Rect(agent_pos[1] * CELL_SIZE, agent_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, BLUE, agent_rect)
    pygame.display.flip()

# Simulate agent's movement using policy
agent_pos = [0, 0]
running = True
while running:
    for event in pygame.event.get():
        print("oyo")
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    action = policy[agent_pos[0] * GRID_SIZE + agent_pos[1]]
    if action == 0:  # UP
        agent_pos[0] = max(0, agent_pos[0] - 1)
    elif action == 1:  # DOWN
        agent_pos[0] = min(GRID_SIZE - 1, agent_pos[0] + 1)
    elif action == 2:  # LEFT
        agent_pos[1] = max(0, agent_pos[1] - 1)
    elif action == 3:  # RIGHT
        agent_pos[1] = min(GRID_SIZE - 1, agent_pos[1] + 1)

    draw_grid(agent_pos)
    clock.tick(5)  # Adjust the speed of movement
