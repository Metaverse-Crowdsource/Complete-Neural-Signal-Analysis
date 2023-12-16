"""
Frequency Maximum Power Module for Data Analysis

This module provides functions to compute and plot the peak frequency with the maximum power in EEG (electroencephalogram) data. It supports both single-channel and multi-channel EEG data analysis.

Functions:
- compute_peak_frequency(data, fs): Computes the peak frequency in the provided data.
- plot_frequency_spectrum(data, fs, channel_name): Plots the frequency spectrum with peak frequency marked.
- process_eeg_data(eeg_data, fs): Processes EEG data to calculate and plot peak frequencies for each channel.

Example Usage:
---------------
import numpy as np
from frequency_maximum_power import compute_peak_frequency, plot_frequency_spectrum, process_eeg_data

# Example for single-channel data
single_channel_data = np.random.rand(1000)  # Example data
fs = 250  # Example sampling frequency
peak_frequency = compute_peak_frequency(single_channel_data, fs)
plot_frequency_spectrum(single_channel_data, fs, channel_name='Channel 1')

# Example for multi-channel data
multi_channel_data = np.random.rand(5, 1000)  # 5 channels, example data
process_eeg_data(multi_channel_data, fs)

Note:
-----
While designed for EEG data, this module can be used for analyzing peak frequencies in other types of time series data as well. Ensure the sampling frequency (fs) is set appropriately for your specific data.
"""

import numpy as np
import scipy.fft
import matplotlib.pyplot as plt

def compute_peak_frequency(data, fs):
    """
    Compute the peak frequency of the provided time series data.

    Parameters:
    data : array_like
        One-dimensional time series data.
    fs : float
        Sampling frequency of the data.

    Returns:
    peak_frequency : float
        Peak frequency with maximum power in the data.
    """
    fft_result = scipy.fft.fft(data)
    frequencies = scipy.fft.fftfreq(len(data), 1.0/fs)
    positive_frequencies = frequencies[frequencies >= 0]
    positive_fft_result = fft_result[frequencies >= 0]
    peak_frequency = positive_frequencies[np.argmax(np.abs(positive_fft_result))]
    return peak_frequency

def plot_frequency_spectrum(data, fs, channel_name=None):
    """
    Plot the frequency spectrum of the data with peak frequency marked.

    Parameters:
    data : array_like
        Time series data.
    fs : float
        Sampling frequency of the data.
    channel_name : str, optional
        Name of the channel (for title).
    """
    fft_result = scipy.fft.fft(data)
    frequencies = scipy.fft.fftfreq(len(data), 1.0/fs)
    positive_frequencies = frequencies[frequencies >= 0]
    positive_fft_result = fft_result[frequencies >= 0]

    peak_frequency = positive_frequencies[np.argmax(np.abs(positive_fft_result))]

    plt.figure()
    plt.plot(positive_frequencies, np.abs(positive_fft_result), label='Power Spectral Density')
    plt.axvline(peak_frequency, color='r', linestyle='--', label=f'Peak Frequency = {peak_frequency} Hz')
    plt.xscale('log')
    plt.yscale('log')
    plt.title(f'Frequency Spectrum {" - " + channel_name if channel_name else ""}')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Power Spectral Density')
    plt.legend()
    plt.grid(True)
    plt.show()


# Example usage of the library functions
def process_eeg_data(eeg_data, fs):
    """
    Process EEG data to calculate and plot peak frequencies for each channel.

    Parameters:
    eeg_data : ndarray
        EEG data array (channels x time series data).
    fs : float
        Sampling frequency of the EEG data.
    """
    for i in range(eeg_data.shape[0]):
        channel_data = eeg_data[i, :]
        plot_frequency_spectrum(channel_data, fs, channel_name=f'Channel {i+1}')
