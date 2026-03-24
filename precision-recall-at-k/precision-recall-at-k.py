
import numpy as np
def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = recommended[:k]

    #top_k in relevant set
    intersection = np.intersect1d(top_k, relevant)

    #number of relevant items    
    num_of_rel = len(relevant)
    #number of hits - common items
    hits = len(intersection)

    
    precision = hits / k
    recall = hits / num_of_rel

    return([precision, recall])