import numpy as np

GRID_SIZE = 5
NUM_ACTIONS = 4  # Up, Down, Left, Right
NUM_STATES = GRID_SIZE * GRID_SIZE
ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']

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
        for action in ACTIONS:
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

# Initialize Q-values
Q_values = np.zeros((NUM_STATES, NUM_ACTIONS))

# Q-learning algorithm
for episode in range(NUM_EPISODES):
    state = 0  # Starting state
    while state != NUM_STATES - 1:  # Continue until reaching the goal state
        # Epsilon-greedy policy
        if np.random.uniform(0, 1) < EPSILON:
            action = np.random.randint(NUM_ACTIONS)  # Explore
        else:
            action = np.argmax(Q_values[state])  # Exploit

        next_state = TRANSITIONS[state][ACTIONS[action]]
        reward = REWARDS[next_state // GRID_SIZE, next_state % GRID_SIZE]
        max_next_action = np.argmax(Q_values[next_state])
        Q_values[state, action] += LEARNING_RATE * (
                reward + DISCOUNT_FACTOR * Q_values[next_state, max_next_action] - Q_values[state, action])
        state = next_state

# Define policy based on Q-values
policy = np.argmax(Q_values, axis=1)

# Simulate agent's movement using policy
current_state = 0
while current_state != NUM_STATES - 1:  # Continue until reaching the goal state
    print("Agent at state:", current_state)
    action = policy[current_state]
    current_state = TRANSITIONS[current_state][ACTIONS[action]]
