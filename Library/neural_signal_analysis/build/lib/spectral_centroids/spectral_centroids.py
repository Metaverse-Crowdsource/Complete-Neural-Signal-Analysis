"""
Spectral Centroids Analysis Module

This module provides functions to compute and plot the spectral centroids of EEG data. It is designed to work with both single-channel and multi-channel EEG data.

Functions:
- compute_spectral_centroid(data, fs): Computes the spectral centroid of the provided data.
- plot_spectral_centroids(centroids, channel_names): Plots the spectral centroids for each channel.
- process_eeg_data(eeg_data, fs): Processes EEG data to calculate and plot spectral centroids for each channel.

Example Usage:
---------------
import numpy as np
from spectral_centroids import process_eeg_data

# Sample EEG data (3 channels x 1000 data points)
eeg_data = np.random.rand(3, 1000)
fs = 250  # Sampling frequency in Hz

# Process EEG data and plot spectral centroids
process_eeg_data(eeg_data, fs)

Note:
-----
The spectral centroid is a measure that indicates the center of mass of the spectrum. It is commonly used in audio signal processing and can be applied to EEG data for feature extraction.
"""

import numpy as np
import scipy.fft
import matplotlib.pyplot as plt

def compute_spectral_centroid(data, fs):
    """
    Compute the spectral centroid of the provided time series data.

    Parameters:
    data : array_like
        One-dimensional time series data.
    fs : float
        Sampling frequency of the data.

    Returns:
    spectral_centroid : float
        Spectral centroid of the data.
    """
    fft_result = scipy.fft.fft(data)
    frequencies = scipy.fft.fftfreq(len(data), 1.0/fs)
    magnitude = np.abs(fft_result)
    spectral_centroid = np.sum(frequencies * magnitude) / np.sum(magnitude)
    return spectral_centroid

def plot_spectral_centroids(centroids, channel_names):
    """
    Plot the spectral centroids for each channel.

    Parameters:
    centroids : list or ndarray
        List or array of spectral centroid values.
    channel_names : list
        List of channel names.
    """
    plt.bar(channel_names, centroids)
    plt.xlabel('Channel')
    plt.ylabel('Spectral Centroid')
    plt.title('Spectral Centroids across Channels')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def process_eeg_data(eeg_data, fs):
    """
    Process EEG data to calculate and plot spectral centroids for each channel.

    Parameters:
    eeg_data : ndarray
        EEG data array (channels x time series data).
    fs : float
        Sampling frequency of the EEG data.
    """
    centroids = [compute_spectral_centroid(channel_data, fs) for channel_data in eeg_data]
    channel_names = [f'Channel {i+1}' for i in range(eeg_data.shape[0])]
    plot_spectral_centroids(centroids, channel_names)

