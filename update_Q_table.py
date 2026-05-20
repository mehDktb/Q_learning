import numpy as np

def update_Q_table(previous_state, current_state, Q_table, action, reward, learning_rate, discount_factor, states):
    rows, cols = states
    previous_row, previous_col = previous_state
    current_row, current_col = current_state
    previous_state_flatten = previous_row * cols + previous_col
    current_state_flatten = current_row * cols + current_col
    # print("Q_table[previous_state_flatten][action]", Q_table[previous_state_flatten][action])
    # print("reward", reward)
    # print("np.max(Q_table[current_state_flatten])", np.max(Q_table[current_state_flatten]))
    new_Q_value = Q_table[previous_state_flatten][action] + learning_rate*(reward + discount_factor * np.max(Q_table[current_state_flatten]) - Q_table[previous_state_flatten][action])
    # print("new_Q_value:", new_Q_value)
    Q_table[previous_state_flatten][action] = new_Q_value
    return Q_table