import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x)

    tan = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

    # tan = np.tanh(np.asarray(x))

    return(tan)
    pass