import numpy as np
def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    #top-k as a set
    top_k = set(recommended[:k])
    #relevant sets so we get O(1) lookup time
    rel_items = set(relevant)

    #top_k in relevant set
    intersection = (top_k & rel_items)

    #number of hits - common items
    hits = len(intersection)
    
    precision = hits / k
    recall = hits / len(relevant)

    return([precision, recall])

    