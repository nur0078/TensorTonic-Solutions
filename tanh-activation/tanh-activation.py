import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x)

    tan = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

    return(tan)
    pass