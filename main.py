from map_builder import map_builder
from transition import *
from update_Q_table import update_Q_table
import numpy as np
import random



#configuration
states = [4,4]
actions = [0,1,2,3] #0->up 1->right 2->down 3->left
epsilon = 0.1
learning_rate = 0.1
discount_factor = 0.1

#map
# road=0, joungle=1, swamp=2, mountain=3, desert=4
rewards = [-1, -3, -8, -5, -6]
start = [0,0]
goal = [3,3]

Q_table = np.zeros(((states[0]*states[1]),(len(actions))))
map = map_builder(states)

#agent
current_state = start
round = 0
score = 0

rows, cols = states
while current_state != goal:
    previous_state = current_state
    action = select_action(current_state=current_state, epsilon=epsilon, Q_table=Q_table, rows=rows, cols=cols)
    current_state, score, reward = apply_transition(current_state=current_state, action=action, map=map, rewards=rewards, score=score)
    Q_table = update_Q_table(

        Q_table=Q_table,
        previous_state=previous_state,
        current_state=current_state,
        rows=rows,
        cols=cols,
        action=action,
        reward=reward,
        learning_rate=learning_rate,
        discount_factor=discount_factor
    )
    round += 1



