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

# Example usage of the library functions
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
    entropy_values = []
    for channel_data in eeg_data:
        entropy = compute_spectral_entropy(channel_data, fs, nperseg)
        entropy_values.append(entropy)
    
    # Assuming channel names are provided or known
    channels = [f'Channel {i+1}' for i in range(len(eeg_data))]
    plot_spectral_entropy(channels, entropy_values)
