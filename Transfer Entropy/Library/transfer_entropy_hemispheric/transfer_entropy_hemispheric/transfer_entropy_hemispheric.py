import numpy as np
import multiprocessing
from minepy import MINE
from pyinform import transferentropy

# Function to calculate mutual information
def mutual_info_worker(args):
    data1, data2 = args
    mine = MINE()
    mine.compute_score(data1, data2)
    return mine.mic()

# Function to determine the optimal delay using mutual information
def determine_delay(data, max_delay=100, subsample_factor=10):
    subsampled_data = data[::subsample_factor]
    with multiprocessing.Pool() as pool:
        args_list = [(subsampled_data[:-i], subsampled_data[i:]) for i in range(1, max_delay + 1)]
        mi_values = pool.map(mutual_info_worker, args_list)
    min_index = np.argmin(mi_values)
    return min_index + 1

# Function to perform delay embedding
def delay_embedding(data, emb_dim, delay):
    N = len(data)
    embedded_data = np.zeros((N - (emb_dim - 1) * delay, emb_dim))
    for i in range(N - (emb_dim - 1) * delay):
        embedded_data[i] = [data[i + j * delay] for j in range(emb_dim)]
    return embedded_data

# Function to bin data for transfer entropy calculation
def bin_data(data, num_bins):
    hist, bins = np.histogram(data, bins=num_bins)
    binned_data = np.digitize(data, bins[:-1]) - 1
    return binned_data

# Function to compute transfer entropy
def compute_transfer_entropy(source_data, target_data, k, l):
    try:
        te_value = transferentropy.transferentropy(source_data, target_data, k, l)
        return te_value
    except Exception as e:
        print(f"Error computing Transfer Entropy: {e}")
        return None

# Example usage of the library functions
def process_eeg_data(eeg_data, fs, num_bins, k, l, eeg_channels, left_channels, right_channels):
    """
    Process EEG data to calculate transfer entropy between two hemispheres.
    
    Parameters:
    eeg_data : ndarray
        EEG data array (channels x time series data).
    fs : float
        Sampling frequency of the EEG data.
    num_bins : int
        Number of bins for data binning.
    k, l : int
        Parameters for transfer entropy calculation.
    eeg_channels : list
        List of EEG channel names.
    left_channels : list
        List of left hemisphere channel names.
    right_channels : list
        List of right hemisphere channel names.
    """


    # Perform 2D delay embedding on the data
    embedded_data = []
    for channel_data in eeg_data:
        # Determine the optimal delay using mutual information
        optimal_delay = determine_delay(channel_data, fs=fs)
        
        # Perform 2D delay embedding with determined optimal delay
        emb_dim = 2  # Since we are doing 2D embedding
        embedded_channel_data = delay_embedding(channel_data, emb_dim=emb_dim, delay=optimal_delay)
        
        # Choose one of the embedding dimensions for transfer entropy calculation
        # For example, using the first dimension
        embedded_data.append(embedded_channel_data[:, 0])  # or [:, 1] for the second dimension
    
    # Calculate Transfer Entropy using binned embedded data
    # Assuming we calculate transfer entropy between two sets of channels
    # Example: between left and right hemispheres
    
    # Bin the embedded data
    num_bins = 1000  # Choose an appropriate number of bins
    binned_data = [bin_data(data, num_bins) for data in embedded_data]
    
    # Now, compute transfer entropy between pairs of binned data
    # Example: between the average of left hemisphere channels and right hemisphere channels
    left_hemisphere_indices = [eeg_channels.index(ch) for ch in left_channels]
    right_hemisphere_indices = [eeg_channels.index(ch) for ch in right_channels]
    
    # Average the binned data for each hemisphere
    left_avg = np.mean([binned_data[i] for i in left_hemisphere_indices], axis=0)
    right_avg = np.mean([binned_data[i] for i in right_hemisphere_indices], axis=0)
    
    # Compute transfer entropy
    TE_left_to_right = compute_transfer_entropy(left_avg, right_avg, k, l)
    TE_right_to_left = compute_transfer_entropy(right_avg, left_avg, k, l)
    
    print(f"Transfer Entropy from Left to Right: {TE_left_to_right}")
    print(f"Transfer Entropy from Right to Left: {TE_right_to_left}")
