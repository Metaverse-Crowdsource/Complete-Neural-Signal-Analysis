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

# Example usage of the library functions
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
