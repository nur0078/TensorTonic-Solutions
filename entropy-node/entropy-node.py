import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here

    #length of the given array
    total_count = len(y)
    
    #unique vals, their occurence count
    y = np.unique(y, return_counts=True)

    #first element is unique values, second is as class_frequencies
    y_array = y[0]
    occurence_count = y[1]

    #length of unique values
    length = len(y_array)

    #init entropy for float
    entropy = float(0)
    
    #sum of all entropy 
    for i in range(length):
        #portion of the sample
        p =  occurence_count[i] / total_count

        #by convention, 0log2(0) = 0 
        if p == 0:
            entropy += 0
        else:           
            entropy += -( p * np.log2(p) )
     
    return entropy