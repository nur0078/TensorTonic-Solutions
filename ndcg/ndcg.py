import math
import numpy as np

def ndcg(relevance_scores, k):
    
    """
    Compute NDCG@k.
    """
    # Write code here
    og = relevance_scores.copy()
    (relevance_scores).sort(reverse=True)
    rel = relevance_scores

    
    
    def dcg(k, rel):
        dcg_val = []

        if k > len(rel):
            iter = len(rel)
        else:
            iter = k
            
        for i in range(iter):
            c = i+1 #counting index from 1
            upper = float((2**rel[i]) - 1)
            lower = float(np.log2(c + 1))
            # print(rel[i], upper, lower)
    
            if lower==0:
                dcg_val.append(0)
            else:
                val = upper/lower
                dcg_val.append(val)
        return dcg_val


    idcg = sum(dcg(k, rel))   

    
    if og == rel:
        my_dcg=idcg
    else:
        my_dcg=sum(dcg(k, og))



    if idcg == 0:
        return 0
    else:
        return (my_dcg / idcg)