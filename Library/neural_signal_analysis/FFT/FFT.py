"""
Fast Fourier Transform (FFT) Module 

This module provides functions to compute the Fast Fourier Transform (FFT) and
Power Spectral Density (PSD) of signal data. It can handle
both single-channel and multi-channel data.

Functions:
- compute_fft(data, fs): Computes the FFT and PSD of the provided data.
- plot_psd(frequencies, psd, channel_name): Plots the Power Spectral Density.
- process_eeg_data(eeg_data, fs): Processes data to calculate and plot FFT PSD for each channel.

Example Usage:
---------------
import numpy as np
from FFT import compute_fft, plot_psd, process_eeg_data

# Example for single-channel data
single_channel_data = np.random.rand(1000)  # Example data
fs = 250  # Example sampling frequency
frequencies, psd = compute_fft(single_channel_data, fs)
plot_psd(frequencies, psd, channel_name='Channel 1')

# Example for multi-channel data
multi_channel_data = np.random.rand(5, 1000)  # 5 channels, example data
process_eeg_data(multi_channel_data, fs)

Note:
-----
The module is designed with EEG data analysis in mind but can be used for other
types of time series data as well. Ensure that the sampling frequency (fs) is
appropriately set for your specific data.
"""

import numpy as np
import matplotlib.pyplot as plt


def compute_fft(data, fs):
    """
    Compute the FFT and PSD of the provided data.

    Parameters:
    data : array_like
        One-dimensional time series data.
    fs : float
        Sampling frequency of the data.

    Returns:
    frequencies : ndarray
        Frequencies corresponding to the FFT result.
    psd : ndarray
        Power spectral density of the data.
    """
    fft_result = np.fft.fft(data)
    psd = np.abs(fft_result) ** 2
    frequencies = np.fft.fftfreq(len(psd), d=1/fs)
    return frequencies, psd

def plot_psd(frequencies, psd, channel_name=None):
    """
    Plot the Power Spectral Density.

    Parameters:
    frequencies : ndarray
        Frequencies corresponding to the PSD.
    psd : ndarray
        Power spectral density of the data.
    channel_name : str, optional
        Name of the channel (for title).
    """
    plt.figure()
    plt.semilogy(frequencies, psd)
    if channel_name:
        plt.title(f'PSD for Channel {channel_name}')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('PSD [V**2]')
    plt.grid(True)
    plt.show()

# Example usage of the library functions
def process_eeg_data(eeg_data, fs):
    """
    Process EEG data to calculate and plot FFT PSD for each channel.

    Parameters:
    eeg_data : ndarray
        EEG data array. Can be either one-dimensional (single-channel)
        or two-dimensional (multi-channel, with channels as rows).
    fs : float
        Sampling frequency of the EEG data.
    """
    if eeg_data.ndim == 1:
        eeg_data = np.expand_dims(eeg_data, axis=0)  # Convert 1D to 2D for consistency

    num_channels = eeg_data.shape[0]

    for i in range(num_channels):
        channel_data = eeg_data[i, :]
        frequencies, psd = compute_fft(channel_data, fs)
        plot_psd(frequencies, psd, channel_name=f'Channel {i+1}')

