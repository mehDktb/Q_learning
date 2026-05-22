import numpy as np
import random

def map_builder(states, goal, wall_percentage):
    rows, cols = states
    num_walls = rows * cols * wall_percentage
    grid_map = np.random.randint(0, 5, size=(rows, cols))
    grid_map[goal[0]][goal[1]] = 6
    placed = 0
    while placed < num_walls:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)

        if [r, c] != goal and grid_map[r][c] != 5:
            grid_map[r][c] = 5
            placed += 1
    return grid_map
