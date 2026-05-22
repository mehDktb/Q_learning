import random

random.seed(42)

def random_state(start ,random_rate, rows, cols):
    if random.uniform(0, 1) < random_rate:
        state = [random.randint(0, rows - 1), random.randint(0, cols - 1)]
    else:
        state = start.copy()

    return state