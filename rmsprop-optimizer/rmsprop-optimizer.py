import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    #update running avg
    g = np.array(g)
    s = np.array(s)

    
    new_s = beta * s + (1 - beta) * g**2

    #param update
    new_w = w - ((lr / (new_s + eps)**0.5) * g)
    
    return(new_w, new_s)