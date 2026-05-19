import numpy as np

import numpy as np

def map_builder(states):
    rows, cols = states
    map = np.random.randint(0, 5, size=(rows, cols))
    return map