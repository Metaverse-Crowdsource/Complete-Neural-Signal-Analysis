"""
Multifractal Detrended Fluctuation Analysis (MFDFA) Module for EEG Data

This module provides functions to perform MFDFA on EEG data, suitable for both single-channel and multi-channel analysis.

Functions:
- calculate_mfdfa(eeg_data, lag, q, channels): Calculates MFDFA for each EEG channel.
- plot_mfdfa_results(eeg_data, mfdfa_results): Plots EEG signals and their MFDFA results.

Example Usage:
---------------
import numpy as np
from mfdfa_neural import calculate_mfdfa, plot_mfdfa_results

# Sample EEG data (5 channels x 1000 data points)
eeg_data = np.random.rand(5, 1000)
lags = np.linspace(1, 100, 100)
qs = np.linspace(-5, 5, 100)
channel_names = ['Frontal', 'Parietal', 'Temporal', 'Occipital', 'Central']

# Calculate MFDFA
mfdfa_results = calculate_mfdfa(eeg_data, lags, qs, channel_names)

# Plot results
plot_mfdfa_results(eeg_data, mfdfa_results)

Note:
-----
Ensure the EEG data is properly preprocessed and the 'lags' and 'qs' parameters are appropriately chosen for your analysis.
"""

import numpy as np
from MFDFA import MFDFA
import matplotlib.pyplot as plt

def calculate_mfdfa(eeg_data, lag, q, channels=None):
    """
    Calculate the Multifractal Detrended Fluctuation Analysis (MFDFA) for EEG data.

    Parameters:
    eeg_data : np.ndarray
        The EEG data array (channels x time series data).
    lag : np.ndarray
        Array of lags.
    q : np.ndarray
        Array of q-values.
    channels : list, optional
        List of channel names.

    Returns:
    List of tuples containing (channel_name, scale, fluctuation) for each channel.
    """

    num_channels = eeg_data.shape[0]
    mfdfa_results = []

    for ch in range(num_channels):
        eeg_data_filtered = eeg_data[ch, :]
        scale, fluct = MFDFA(eeg_data_filtered, lag=lag, q=q)
        channel_name = channels[ch] if channels else f"Channel {ch+1}"
        mfdfa_results.append((channel_name, scale, fluct))

    return mfdfa_results

def plot_mfdfa_results(eeg_data, mfdfa_results):
    """
    Plot the MFDFA results for each EEG channel.

    Parameters:
    eeg_data : np.ndarray
        The EEG data array (channels x time series data).
    mfdfa_results : list
        List of tuples containing (channel_name, scale, fluctuation) for each channel.
    """
    for ch, (channel_name, scale, fluct) in enumerate(mfdfa_results):
        plt.figure(figsize=(12, 4))
        
        plt.subplot(1, 2, 1)
        plt.plot(eeg_data[ch, :])
        plt.title(f"{channel_name} - EEG Signal")
        
        plt.subplot(1, 2, 2)
        plt.loglog(scale, fluct)
        plt.title(f"{channel_name} - Multifractal DFA")
        
        plt.tight_layout()
        plt.show()

