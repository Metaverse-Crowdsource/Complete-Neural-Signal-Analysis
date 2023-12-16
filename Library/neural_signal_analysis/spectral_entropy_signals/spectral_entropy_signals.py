"""
Spectral Entropy Analysis Module

This module provides functions to compute and plot the spectral entropy of EEG data. It can process both single-channel and multi-channel EEG data, making it suitable for a variety of EEG analysis tasks.

Functions:
- compute_spectral_entropy(data, fs, nperseg): Computes the spectral entropy of the provided data.
- plot_spectral_entropy(channels, entropy_values): Plots the spectral entropy values for each channel.
- process_eeg_data(eeg_data, fs, nperseg): Processes EEG data to calculate and plot spectral entropy for each channel.

Example Usage:
---------------
import numpy as np
from spectral_entropy_signals import process_eeg_data

# Sample EEG data (3 channels x 1000 data points)
eeg_data = np.random.rand(3, 1000)
fs = 250  # Sampling frequency in Hz
nperseg = 128  # Segment length for Welch's method

# Process EEG data and plot spectral entropy
process_eeg_data(eeg_data, fs, nperseg)

Note:
-----
Spectral entropy is a measure used in signal processing, often applied to EEG data to assess the complexity or regularity of the signal across different frequency bands.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

def compute_spectral_entropy(data, fs, nperseg):
    """
    Compute the spectral entropy of the provided data.

    Parameters:
    data : array_like
        One-dimensional time series data.
    fs : float
        Sampling frequency of the data.
    nperseg : int
        Length of each segment for Welch's method.

    Returns:
    spectral_entropy : float
        Spectral entropy of the data.
    """
    frequencies, Pxx = welch(data, fs=fs, nperseg=nperseg)
    normalized_Pxx = Pxx / np.sum(Pxx)
    spectral_entropy = -np.sum(normalized_Pxx * np.log2(normalized_Pxx))
    return spectral_entropy

def plot_spectral_entropy(channels, entropy_values):
    """
    Plot the spectral entropy values for each channel.

    Parameters:
    channels : list
        List of channel names.
    entropy_values : list
        List of spectral entropy values.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(channels, entropy_values, color='b')
    plt.xlabel('Channel')
    plt.ylabel('Spectral Entropy')
    plt.title('Spectral Entropy across Channels')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def process_eeg_data(eeg_data, fs, nperseg):
    """
    Process EEG data to calculate and plot spectral entropy for each channel.

    Parameters:
    eeg_data : ndarray
        EEG data array (channels x time series data).
    fs : float
        Sampling frequency of the EEG data.
    nperseg : int
        Length of each segment for Welch's method.
    """
    entropy_values = [compute_spectral_entropy(channel_data, fs, nperseg) for channel_data in eeg_data]
    channels = [f'Channel {i+1}' for i in range(len(eeg_data))]
    plot_spectral_entropy(channels, entropy_values)

