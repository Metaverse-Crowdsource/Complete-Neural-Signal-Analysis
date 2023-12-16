"""
Short-Time Fourier Transform (STFT) Module

This module provides functions for computing and visualizing the Short-Time Fourier Transform (STFT) of EEG data. It is capable of processing both single-channel and multi-channel EEG data.

Functions:
- compute_stft(data, fs, window_size): Computes the STFT of the provided data.
- plot_stft(frequencies, time_intervals, stft_data, channel_name): Plots the STFT as a heatmap for a given channel.
- process_eeg_data(eeg_data, fs, window_size): Processes EEG data to calculate and plot STFT for each channel.

Example Usage:
---------------
import numpy as np
from STFT_signal import process_eeg_data

# Sample EEG data (3 channels x 1000 data points)
eeg_data = np.random.rand(3, 1000)
fs = 250  # Sampling frequency in Hz
window_size = 128  # Segment length for STFT in samples

# Process EEG data and plot STFT
process_eeg_data(eeg_data, fs, window_size)

Note:
-----
STFT is a powerful method for analyzing the frequency content of signals over time, making it highly suitable for EEG signal analysis.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft

def compute_stft(data, fs, window_size):
    """
    Compute the Short-Time Fourier Transform (STFT) of the provided data.

    Parameters:
    data : array_like
        One-dimensional time series data.
    fs : float
        Sampling frequency of the data.
    window_size : int
        Size of each segment for STFT in samples.

    Returns:
    frequencies : ndarray
        Frequencies corresponding to the STFT.
    time_intervals : ndarray
        Time intervals of the STFT.
    stft_data : ndarray
        STFT of the data.
    """
    frequencies, time_intervals, stft_data = stft(data, fs=fs, nperseg=window_size)
    return frequencies, time_intervals, stft_data

def plot_stft(frequencies, time_intervals, stft_data, channel_name=None):
    """
    Plot the STFT as a heatmap.

    Parameters:
    frequencies : ndarray
        Frequencies corresponding to the STFT.
    time_intervals : ndarray
        Time intervals of the STFT.
    stft_data : ndarray
        STFT of the data.
    channel_name : str, optional
        Name of the channel (for title).
    """
    plt.figure()
    plt.imshow(10 * np.log10(np.abs(stft_data)), aspect='auto', cmap='inferno', extent=[time_intervals[0], time_intervals[-1], frequencies[-1], frequencies[0]])
    if channel_name:
        plt.title(f'STFT for Channel {channel_name}')
    plt.xlabel('Time [s]')
    plt.ylabel('Frequency [Hz]')
    plt.colorbar(label='Power/Frequency [dB/Hz]')
    plt.show()

def process_eeg_data(eeg_data, fs, window_size):
    """
    Process EEG data to calculate and plot STFT for each channel.

    Parameters:
    eeg_data : ndarray
        EEG data array (channels x time series data).
    fs : float
        Sampling frequency of the EEG data.
    window_size : int
        Size of each segment for STFT in samples.
    """
    for i in range(eeg_data.shape[0]):
        channel_data = eeg_data[i, :]
        frequencies, time_intervals, stft_data = compute_stft(channel_data, fs, window_size)
        plot_stft(frequencies, time_intervals, stft_data, channel_name=f'Channel {i+1}')
