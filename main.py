from graphical_interface import draw_grid
from map_builder import map_builder
from transition import *
from update_Q_table import update_Q_table
import numpy as np
import random



#configuration
states = [20,20]
actions = [0,1,2,3] #0->up 1->right 2->down 3->left
epsilon = 0.5
learning_rate = 0.4
discount_factor = 0.9
episodes = 50000
max_steps = 100

#map
# road=0, joungle=1, swamp=2, mountain=3, desert=4
rewards = [-1, -3, -8, -5, -6, 1000]
start = [0,0]
goal = [19,19]
loop_penalty = 2

Q_table = np.zeros(((states[0]*states[1]),(len(actions))))
grid_map = map_builder(states)
grid_map[goal[0]][goal[1]] = 5


for episode in range(episodes):
    current_state = start
    score = 0
    visited_tuple = set()

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

visited_tuple = set()
print(Q_table)
path = get_best_path(Q_table=Q_table, grid_map=grid_map, states=states, rewards=rewards, start=start, goal=goal, loop_penalty=loop_penalty, visited_tuple=visited_tuple)
print(path)
draw_grid(grid_map, path, start, goal)



#TODO fixing ping ponging.
#TODO implementing epsilon decay.
#TODO implementing random start.
#TODO implementing walls.
#TODO implementing traps.
#TODO implementing config file

