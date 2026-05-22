from graphical_interface import draw_grid
from map_builder import map_builder
from transition import *
from update_Q_table import update_Q_table
from random_start import random_state
import numpy as np
import random



#configuration
states = [40,40]
actions = [0,1,2,3] #0->up 1->right 2->down 3->left
epsilon = 1.0
epsilon_min = 0.05
decay_rate = 0.995
learning_rate = 0.3
discount_factor = 0.9
episodes = 50000
max_steps = 200
random_start = True


#map
# road=0, joungle=1, swamp=2, mountain=3, desert=4
rewards = [-1, -3, -8, -5, -6, 1000]
rows, cols = states
if random_start:
    start = [random.randint(0, rows-1), random.randint(0, cols-1)]
else:
    start = [0, 0]

goal = [rows-1, cols-1]
loop_penalty = 10

Q_table = np.zeros(((states[0]*states[1]),(len(actions))))
grid_map = map_builder(states)
grid_map[goal[0]][goal[1]] = 5


for episode in range(episodes):
    episode_random_start_rate = max(0.1, 0.5 * (0.9995 ** episode))
    current_state = random_state(start=start, random_rate=episode_random_start_rate, rows=rows, cols=cols)
    print("start from : ", current_state)
    epsilon = max(epsilon_min, epsilon * decay_rate)
    visited_tuple = set()
    score = 0

    for step in range(max_steps):

        if current_state == goal:
            break

        previous_state = current_state.copy()
        action = select_action(current_state=current_state, epsilon=epsilon, Q_table=Q_table, states=states)
        current_state, score, reward = apply_transition(current_state=current_state, action=action, grid_map=grid_map, states=states, rewards=rewards, score=score, loop_penalty=loop_penalty)

        if tuple(current_state) in visited_tuple:
            reward -= loop_penalty
        visited_tuple.add(tuple(current_state))

        Q_table = update_Q_table(

            Q_table=Q_table,
            previous_state=previous_state,
            current_state=current_state,
            states=states,
            action=action,
            reward=reward,
            learning_rate=learning_rate,
            discount_factor=discount_factor
        )
    epsilon = max(epsilon_min, epsilon * decay_rate)

visited_tuple = set()
print(Q_table)
path = get_best_path(Q_table=Q_table, grid_map=grid_map, states=states, rewards=rewards, start=start, goal=goal, loop_penalty=loop_penalty, visited_tuple=visited_tuple, max_steps=max_steps)
print(path)
draw_grid(grid_map, path, start, goal)



#TODO implementing walls.
#TODO implementing traps.
#TODO implementing config file

