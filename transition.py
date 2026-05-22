import random




def select_action(current_state, Q_table, epsilon, states):
    rows, cols = states
    row, col = current_state

    state_flatten = row * cols + col

    valid_actions = get_valid_actions(current_state, states)

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


def get_valid_actions(current_state, states):
    rows, cols = states
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



def apply_transition(current_state, action, grid_map, states, score, rewards, loop_penalty):
    rows, cols = states
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

    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
        return current_state, score, 0  # invalid move → no change
    if grid_map[new_row][new_col] == 5:
        return current_state, score, 0

    current_state = [new_row, new_col]
    reward = rewards[(grid_map[new_row][new_col])]
    score += reward
    return current_state, score, reward


def get_best_path(Q_table, grid_map, start, goal, states, rewards, loop_penalty, visited_tuple,max_steps):
    state = start
    path = [state.copy()]

    score = 0
    for _ in range(max_steps):

        visited_tuple.add(tuple(state))
        action = select_action(state, Q_table, epsilon=0, states=states)

        state, score, _ = apply_transition(current_state=state, action=action, grid_map=grid_map, states=states, score=score, rewards=rewards, loop_penalty=loop_penalty)
        path.append(state.copy())

        if state == goal:
            break

    return path




