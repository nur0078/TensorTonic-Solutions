import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    # Write code here
    w = np.array(w)
    g = np.array(g)
    G = np.array(G)

    acg = G + g**2
    w_new = w - (lr / (acg + eps)**0.5) * g
    return (w_new, acg)