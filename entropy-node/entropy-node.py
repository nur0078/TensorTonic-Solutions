import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here

    total_count = len(y)
    _, occurrence_count = np.unique(y, return_counts=True)

    p = occurrence_count / total_count
    return -np.sum(p * np.log2(p))