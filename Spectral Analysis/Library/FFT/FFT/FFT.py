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
        EEG data array (channels x time series data).
    fs : float
        Sampling frequency of the EEG data.
    """
    for i in range(eeg_data.shape[0]):
        channel_data = eeg_data[i, :]
        frequencies, psd = compute_fft(channel_data, fs)
        plot_psd(frequencies, psd, channel_name=f'Channel {i+1}')
