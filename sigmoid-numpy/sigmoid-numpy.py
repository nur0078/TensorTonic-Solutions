import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    val = np.asarray(x, dtype=float)
    #np.exp(-x)
    ex = np.exp(-val)
    sig = 1 / (1 + ex)

    return sig
    pass