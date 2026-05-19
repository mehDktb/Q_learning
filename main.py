from map_builder import map_builder
from transition import *

import numpy as np
import random

#configuration
states = [4,4]
actions = [0,1,2,3] #0->up 1->right 2->down 3->left
epsilon = 0.1

#map
# road=0, joungle=1, swamp=2, mountain=3, desert=4
costs = [-1, -3, -8, -5, -6]
start = [0,0]
goal = [3,3]

Q_table = np.zeros(((states[0]*states[1]),(len(actions))))
map = map_builder(states)

#agent
current_state = start
round = 0

while current_state != goal:
    action = select_action(current_state=current_state, epsilon=epsilon, Q_table=Q_table, map=map)
    current_state, score, valid_action = apply_transotion(current_state=current_state, action=action, map=map, costs=costs)

#TODO call the transition
#TODO update the score
#TODO update Q_table

