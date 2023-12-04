import numpy as np
from MFDFA import MFDFA
import matplotlib.pyplot as plt

def calculate_mfdfa(eeg_data, lag, q, channels):
    """
    Calculate the Multifractal Detrended Fluctuation Analysis for EEG data.

    Parameters:
    eeg_data : np.ndarray
        The EEG data array.
    lag : np.ndarray
        Array of lags.
    q : np.ndarray
        Array of q-values.
    channels : list
        List of channel names.
    
    Returns:
    List of tuples containing (scale, fluctuation) for each channel.
    """

    num_channels = eeg_data.shape[0]
    mfdfa_results = []

    for ch in range(num_channels):
        eeg_data_filtered = eeg_data[ch, :]
        scale, fluct = MFDFA(eeg_data_filtered, lag=lag, q=q)
        mfdfa_results.append((scale, fluct))

    return mfdfa_results

def plot_mfdfa_results(mfdfa_results, channels):
    """
    Plot the MFDFA results for each EEG channel.

    Parameters:
    mfdfa_results : list
        List of tuples containing (scale, fluctuation) for each channel.
    channels : list
        List of channel names.
    """
    for ch, (scale, fluct) in enumerate(mfdfa_results):
        plt.figure(figsize=(12, 4))
        
        plt.subplot(1, 2, 1)
        plt.plot(eeg_data[ch, :])
        plt.title(f"Channel {ch+1}: {channels[ch]}")
        
        plt.subplot(1, 2, 2)
        plt.loglog(scale, fluct)
        plt.title(f"Channel {ch+1}: Multifractal DFA")
        
        plt.tight_layout()
        plt.show()
