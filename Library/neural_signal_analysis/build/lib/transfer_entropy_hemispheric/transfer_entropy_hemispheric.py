"""
Transfer Entropy Hemispheric Analysis Module

This module provides functions to compute transfer entropy between the left and right hemispheres of EEG data. It is capable of handling multiple channels and is particularly useful for studying interhemispheric interactions in EEG data.

Functions:
- compute_transfer_entropy(source_data, target_data, k, l): Computes transfer entropy between two sets of data.
- process_eeg_data(eeg_data, fs, num_bins, k, l, eeg_channels, left_channels, right_channels): Processes EEG data to calculate transfer entropy between two hemispheres.

Example Usage:
---------------
import numpy as np
from transfer_entropy_hemispheric import process_eeg_data

# Sample EEG data (multiple channels)
eeg_data = np.random.rand(10, 1000)  # Example with 10 channels
eeg_channels = ['Ch1', 'Ch2', ..., 'Ch10']
left_channels = ['Ch1', 'Ch2', 'Ch3', 'Ch4', 'Ch5']
right_channels = ['Ch6', 'Ch7', 'Ch8', 'Ch9', 'Ch10']

# Compute transfer entropy between hemispheres
te_left_to_right, te_right_to_left = process_eeg_data(eeg_data, fs=1000, num_bins=10, k=1, l=1, eeg_channels=eeg_channels, left_channels=left_channels, right_channels=right_channels)
print(f"Transfer Entropy from Left to Right: {te_left_to_right}")
print(f"Transfer Entropy from Right to Left: {te_right_to_left}")

Note:
-----
Transfer entropy is a measure of the directional flow of information between signals and is useful in EEG data analysis for understanding the interactions between different brain regions.
"""

import numpy as np
import multiprocessing
from minepy import MINE
from pyinform import transferentropy

def mutual_info_worker(args):
    data1, data2 = args
    mine = MINE()
    mine.compute_score(data1, data2)
    return mine.mic()

def determine_delay(data, max_delay=100, subsample_factor=10):
    subsampled_data = data[::subsample_factor]
    with multiprocessing.Pool() as pool:
        args_list = [(subsampled_data[:-i], subsampled_data[i:]) for i in range(1, max_delay + 1)]
        mi_values = pool.map(mutual_info_worker, args_list)
    min_index = np.argmin(mi_values)
    return min_index + 1

def delay_embedding(data, emb_dim, delay):
    N = len(data)
    embedded_data = np.zeros((N - (emb_dim - 1) * delay, emb_dim))
    for i in range(N - (emb_dim - 1) * delay):
        embedded_data[i] = [data[i + j * delay] for j in range(emb_dim)]
    return embedded_data

def bin_data(data, num_bins):
    hist, bins = np.histogram(data, bins=num_bins)
    binned_data = np.digitize(data, bins[:-1]) - 1
    return binned_data

def compute_transfer_entropy(source_data, target_data, k, l):
    try:
        te_value = transferentropy.transferentropy(source_data, target_data, k, l)
        return te_value
    except Exception as e:
        print(f"Error computing Transfer Entropy: {e}")
        return None

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

    embedded_data = []
    for channel_data in eeg_data:
        optimal_delay = determine_delay(channel_data, max_delay=100, subsample_factor=10)
        emb_dim = 2
        embedded_channel_data = delay_embedding(channel_data, emb_dim=emb_dim, delay=optimal_delay)
        embedded_data.append(embedded_channel_data[:, 0])

    binned_data = [bin_data(data, num_bins) for data in embedded_data]

    left_hemisphere_indices = [eeg_channels.index(ch) for ch in left_channels]
    right_hemisphere_indices = [eeg_channels.index(ch) for ch in right_channels]

    left_avg = np.mean([binned_data[i] for i in left_hemisphere_indices], axis=0)
    right_avg = np.mean([binned_data[i] for i in right_hemisphere_indices], axis=0)

    TE_left_to_right = compute_transfer_entropy(left_avg, right_avg, k, l)
    TE_right_to_left = compute_transfer_entropy(right_avg, left_avg, k, l)

    return TE_left_to_right, TE_right_to_left

# Example usage
if __name__ == "__main__":
    # Assume EEG data is loaded here
    eeg_data = ...
    eeg_channels = ...
    left_channels = ...
    right_channels = ...

    # Compute transfer entropy
    te_left_to_right, te_right_to_left = process_eeg_data(eeg_data, fs=1000, num_bins=10, k=1, l=1, eeg_channels=eeg_channels, left_channels=left_channels, right_channels=right_channels)
    print(f"Transfer Entropy from Left to Right: {te_left_to_right}")
    print(f"Transfer Entropy from Right to Left: {te_right_to_left}")
