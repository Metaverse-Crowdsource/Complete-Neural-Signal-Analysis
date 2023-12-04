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
    frequencies, peak_frequency = compute_peak_frequency(data, fs)
    plt.figure()
    plt.plot(frequencies, np.abs(fft_result), label='Power Spectral Density')
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
