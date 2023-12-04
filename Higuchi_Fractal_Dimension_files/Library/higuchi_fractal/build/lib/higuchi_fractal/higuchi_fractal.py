import numpy as np

def higuchi_fd(data, k_max):
    """
    Compute Higuchi Fractal Dimension of a time series.
    
    Parameters:
    data : list or np.array
        One-dimensional time series
    k_max : int
        Maximum delay (time offset)
        
    Returns:
    hfd : float
        Higuchi Fractal Dimension
    """
    N = len(data)
    L = []
    
    x = np.asarray(data)
    
    for k in range(1, k_max):
        Lk = []
        
        for m in range(0, k):
            Lkm = 0
            for i in range(1, int((N-m)/k)):
                Lkm += abs(x[m+i*k] - x[m+i*k-k])
            Lkm = Lkm*(N - 1)/(((N - m)/k)*k)
            Lk.append(Lkm)
            
        L.append(np.log(np.mean(Lk)))
    
    hfd = np.polyfit(np.log(range(1, k_max)), L, 1)[0]
    
    return hfd
