import math

def ndcg(relevance_scores, k):
    """Compute NDCG@k."""
    
    def dcg(scores, k):
        return sum(
            (2 ** scores[i] - 1) / math.log2(i + 2)
            for i in range(min(k, len(scores)))
        )
    
    ideal = sorted(relevance_scores, reverse=True)
    idcg = dcg(ideal, k)
    
    if idcg == 0:
        return 0
    
    return dcg(relevance_scores, k) / idcg