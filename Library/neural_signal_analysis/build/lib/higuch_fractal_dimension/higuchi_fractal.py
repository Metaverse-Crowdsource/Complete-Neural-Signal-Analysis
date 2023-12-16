"""
Higuchi Fractal Dimension Module

This library provides functions to compute the Higuchi Fractal Dimension (HFD)
of time series data. It supports both single-channel and multi-channel data inputs.

Dependencies:
- NumPy

Installation:
- Install via pip: pip install higuchi_fractal

Example Usage:
--------------
import numpy as np
from higuchi_fractal import higuchi_fd, higuchi_fd_multichannel

# For single-channel data
single_channel_data = np.random.rand(1000)
hfd_single = higuchi_fd(single_channel_data, k_max=10)

# For multi-channel data
multi_channel_data = np.random.rand(1000, 3)
hfd_multi = higuchi_fd_multichannel(multi_channel_data, k_max=10)
"""

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


def higuchi_fd_multichannel(data, k_max):
    """
    Compute Higuchi Fractal Dimension of a multi-channel time series.
    
    Parameters:
    data : 2D np.array
        Multi-dimensional time series where each column represents a channel
    k_max : int
        Maximum delay (time offset)
        
    Returns:
    hfd_list : list
        List of Higuchi Fractal Dimensions for each channel
    
    Example:
    --------
    data = np.random.rand(1000, 3)
    hfd_list = higuchi_fd_multichannel(data, k_max=10)
    """
    if data.ndim == 1:
        data = np.expand_dims(data, axis=1)  # Convert 1D to 2D for consistency

    num_channels = data.shape[1]
    hfd_list = []

    for channel in range(num_channels):
        channel_data = data[:, channel]
        N = len(channel_data)
        L = []

        for k in range(1, k_max):
            Lk = []

            for m in range(0, k):
                Lkm = 0
                for i in range(1, int((N-m)/k)):
                    Lkm += abs(channel_data[m+i*k] - channel_data[m+i*k-k])
                Lkm = Lkm*(N - 1)/(((N - m)/k)*k)
                Lk.append(Lkm)

            L.append(np.log(np.mean(Lk)))

        hfd = np.polyfit(np.log(range(1, k_max)), L, 1)[0]
        hfd_list.append(hfd)

    return hfd_list
