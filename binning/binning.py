import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    values = np.asarray(values)
    max_val = np.max(values)
    min_val = np.min(values)
    
    if min_val == max_val:
        return [0] * len(values)
    
    bin_wid = (max_val - min_val) / num_bins
    bins = []
    
    for value in values:
        binx = (value - min_val) / bin_wid
        bins.append(int(np.minimum(binx, num_bins - 1)))
    
    return bins

    