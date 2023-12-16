"""
Transfer Entropy Regional Analysis Module

This module provides functionality to compute transfer entropy between predefined regions in EEG data. It's designed to handle multiple EEG channels and analyze the directional information flow between different brain regions.

Functions:
- compute_transfer_entropy(source_data, target_data, k, l): Computes the transfer entropy between two data series.
- process_eeg_data(eeg_data, fs, num_bins, k, l, eeg_channels, regions): Processes EEG data to calculate transfer entropy between specified regions.

Example Usage:
---------------
import numpy as np
from transfer_entropy_regional import process_eeg_data

# Example EEG data with multiple channels
eeg_data = np.random.rand(10, 1000)  # Assume 10 channels
eeg_channels = ['Channel 1', 'Channel 2', ..., 'Channel 10']
regions = {
    "Frontal": ['Channel 1', 'Channel 2'],
    "Temporal": ['Channel 3', 'Channel 4']
    # Add other regions as needed
}

# Compute transfer entropy between regions
te_results = process_eeg_data(eeg_data, fs=1000, num_bins=10, k=1, l=1, eeg_channels=eeg_channels, regions=regions)
print(te_results)

Note:
-----
Transfer entropy is a useful measure in EEG analysis for exploring the connectivity and information flow between different brain regions.
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
    return np.argmin(mi_values) + 1

def delay_embedding(data, emb_dim, delay):
    N = len(data)
    return np.array([data[i:i + emb_dim * delay:delay] for i in range(N - (emb_dim - 1) * delay)])

def bin_data(data, num_bins):
    bins = np.linspace(np.min(data), np.max(data), num_bins + 1)
    return np.digitize(data, bins[:-1]) - 1

def compute_transfer_entropy(source_data, target_data, k, l):
    try:
        return transferentropy.transferentropy(source_data, target_data, k, l)
    except Exception as e:
        print(f"Error computing Transfer Entropy: {e}")
        return None

def process_eeg_data(eeg_data, fs, num_bins, k, l, eeg_channels, regions):
    """
    Process EEG data to calculate transfer entropy between defined regions.

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
    regions : dict
        Dictionary mapping region names to lists of channel names or indices.
    """

    # Prepare data for each region
    region_data = {}
    for region_name, channels in regions.items():
        region_indices = [eeg_channels.index(channel) for channel in channels]
        region_eeg = np.mean(eeg_data[region_indices, :], axis=0)
        optimal_delay = determine_delay(region_eeg, max_delay=100, subsample_factor=10)
        embedded_region_eeg = delay_embedding(region_eeg, emb_dim=2, delay=optimal_delay)
        region_data[region_name] = bin_data(embedded_region_eeg[:, 0], num_bins)

    # Calculate Transfer Entropy between regions
    te_results = {}
    for source_region, source_data in region_data.items():
        for target_region, target_data in region_data.items():
            if source_region != target_region:
                te_value = compute_transfer_entropy(source_data, target_data, k, l)
                te_key = f"{source_region}_to_{target_region}"
                te_results[te_key] = te_value

    return te_results

# Example usage
if __name__ == "__main__":
    # Load and preprocess EEG data
    eeg_data = ... # Assume EEG data is loaded here
    eeg_channels = ... # List of EEG channel names

    # Define regions and channels
    regions = {
        "Frontal": ['Fp1', 'Fpz', 'Fp2', 'F7', 'F3', 'Fz', 'F4', 'F8'],
        "Temporal": ['T7', 'T8'],
        # Define other regions...
    }

    # Compute regional transfer entropy
    te_results = process_eeg_data(eeg_data, fs=1000, num_bins=10, k=1, l=1, eeg_channels=eeg_channels, regions=regions)
    print(te_results)

