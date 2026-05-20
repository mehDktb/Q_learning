from unittest import case
import random
import numpy as np

def select_action(current_state, Q_table, epsilon, rows, cols):
    row, col = current_state

    state_flatten = row * cols + col

    valid_actions = get_valid_actions(current_state, rows, cols)

    # ε-greedy decision
    if random.uniform(0, 1) < epsilon:
        # exploration (ONLY valid actions)
        action = random.choice(valid_actions)

    else:
        # exploitation (ONLY valid actions)
        q_values = Q_table[state_flatten]

        # filter Q-values for valid actions only
        valid_q_values = [(a, q_values[a]) for a in valid_actions]

        max_q = max(valid_q_values, key=lambda x: x[1])[1]

        best_actions = [a for a, q in valid_q_values if q == max_q]

        action = random.choice(best_actions)

    return action


def get_valid_actions(current_state, rows, cols):
    row, col = current_state

    valid_actions = []

    # up
    if row > 0:
        valid_actions.append(0)

    # right
    if col < cols - 1:
        valid_actions.append(1)

    # down
    if row < rows - 1:
        valid_actions.append(2)

    # left
    if col > 0:
        valid_actions.append(3)

    return valid_actions



def apply_transition(current_state, action, map, score, rewards):
    row, col = current_state
    new_row, new_col = row, col
    match action:
        case 0:
            new_row, new_col = row - 1, col
        case 1:
            new_row, new_col = row, col + 1
        case 2:
            new_row, new_col = row + 1, col
        case 3:
            new_row, new_col = row, col - 1

    if new_row < 0 or new_row >= len(map) or new_col < 0 or new_col >= len(map[0]):
        return current_state, score, 0  # invalid move → no change

    current_state = [new_row, new_col]

    rewards = rewards[(map[new_row][new_col])]
    score += rewards
    return current_state, score, rewards








