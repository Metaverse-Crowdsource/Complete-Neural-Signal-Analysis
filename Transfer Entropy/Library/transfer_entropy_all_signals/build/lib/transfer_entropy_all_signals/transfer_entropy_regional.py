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

def process_granular_eeg_data(eeg_data, fs, num_bins, k, l, eeg_channels, channel_groups=None):
    """
    Process EEG data to calculate transfer entropy at a granular level between channels or channel groups.
    
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
    channel_groups : dict (optional)
        Dictionary mapping group names to lists of channel names or indices.
    """

    # Perform 2D delay embedding on the data
    embedded_data = []
    for channel_data in eeg_data:
        optimal_delay = determine_delay(channel_data, fs=fs)
        emb_dim = 2
        embedded_channel_data = delay_embedding(channel_data, emb_dim=emb_dim, delay=optimal_delay)
        embedded_data.append(embedded_channel_data[:, 0])  # Using the first dimension

    # Prepare channel pairs for TE calculation
    if channel_groups:
        # Use defined channel groups for TE calculation
        pairs = [(group, source, target) for group, channels in channel_groups.items()
                 for source in channels for target in channels if source != target]
    else:
        # Use all individual channels for TE calculation
        pairs = [(ch1, ch2) for i, ch1 in enumerate(eeg_channels)
                 for j, ch2 in enumerate(eeg_channels) if i != j]

    # Calculate Transfer Entropy for each pair
    te_results = {}
    for pair in pairs:
        source_idx = eeg_channels.index(pair[0])
        target_idx = eeg_channels.index(pair[1])
        source_data = bin_data(embedded_data[source_idx], num_bins)
        target_data = bin_data(embedded_data[target_idx], num_bins)
        te_value = compute_transfer_entropy(source_data, target_data, k, l)
        te_key = f"{pair[0]}_to_{pair[1]}"
        te_results[te_key] = te_value

    return te_results

# Example usage
if __name__ == "__main__":
    # Load and preprocess EEG data
    # eeg_data = ...

    # Optionally define channel groups for granular TE calculation
    # channel_groups = {
    #     "Group1": ['Fp1', 'Fp2'],
    #     "Group2": ['F7', 'F8'],
    #     # Define other groups...
    # }

    # Compute granular transfer entropy
    te_results = process_granular_eeg_data(eeg_data, fs=1000, num_bins=1000, k=1, l=1, eeg_channels, channel_groups=None)
    print(te_results)