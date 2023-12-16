"""
Phase Space Analysis Module

This module provides functions for performing phase space analysis on EEG data. It includes delay embedding, false nearest neighbors, and mutual information analysis for determining optimal delays. The module is capable of handling both single-channel and multi-channel EEG data.

Functions:
- delay_embedding(data, emb_dim, delay): Performs delay embedding for each channel.
- false_nearest_neighbors(data, emb_dim, delay, R): Computes False Nearest Neighbors for each channel.
- determine_delay(data, max_delay, subsample_factor): Determines optimal delays for each channel using mutual information.
- process_phase_space_analysis(eeg_data, emb_dim, max_delay, subsample_factor): Processes EEG data for phase space analysis, including delay determination and embedding.
- create_phase_space_plot(embedded_data_list, titles, output_dir): Creates and saves 2D phase space plots for each channel.

Example Usage:
---------------
import numpy as np
from phase_space import process_phase_space_analysis

# Sample EEG data (3 channels x 1000 data points)
eeg_data = np.random.rand(3, 1000)
emb_dim = 3
max_delay = 20

# Process phase space analysis
phase_space_results = process_phase_space_analysis(eeg_data, emb_dim, max_delay)

# Assuming phase_space_results contains the embedded data for 3 channels
titles = ['Channel 1', 'Channel 2', 'Channel 3']
output_dir = '/path/to/save/plots'
create_phase_space_plot(phase_space_results, titles, output_dir)

Note:
-----
Ensure the EEG data is properly preprocessed. The embedding dimension and delay should be chosen based on the specific characteristics of your data.
"""

import numpy as np
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
from minepy import MINE
import multiprocessing
import os

def delay_embedding(data, emb_dim, delay):
    """
    Perform delay embedding on the provided data for each channel.
    
    Parameters:
    data : 2D array_like
        Multi-dimensional time series data where each row is a channel.
    emb_dim : int
        Embedding dimension.
    delay : int
        Delay time steps.
        
    Returns:
    embedded_data : list of ndarrays
        The delay-embedded data for each channel.
    """
    num_channels = data.shape[0]
    embedded_data = []
    for ch in range(num_channels):
        channel_data = data[ch, :]
        N = len(channel_data)
        embedded_channel_data = np.array([channel_data[i:i+emb_dim*delay:delay].flatten() 
                                          for i in range(N - emb_dim * delay + 1)])
        embedded_data.append(embedded_channel_data)
    return embedded_data

def false_nearest_neighbors(data, emb_dim, delay, R=10):
    """
    Compute False Nearest Neighbors for different embedding dimensions.
    
    Parameters:
    data : array_like
        One-dimensional time series data.
    max_emb_dim : int
        Maximum embedding dimension to consider.
    delay : int
        Delay time steps.
    R : float
        Threshold for determining false neighbors.
        
    Returns:
    false_neighbors : ndarray
        Array of false nearest neighbor fractions for each embedding dimension.
    """
    N = len(data)
    false_neighbors = np.zeros(emb_dim)

    for d in range(1, emb_dim + 1):
        emb_data = delay_embedding(data, d, delay)
        nbrs = NearestNeighbors(n_neighbors=2).fit(emb_data[:-delay])
        distances, indices = nbrs.kneighbors(emb_data[:-delay])
        neighbor_index = indices[:, 1]
        neighbor_distance = np.abs(data[neighbor_index + delay] - data[np.arange(N - d * delay) + delay])
        false_neighbors[d - 1] = np.mean((neighbor_distance / distances[:, 1]) > R)

    return false_neighbors

def mutual_info_worker(args):
    """
    Worker function for multiprocessing in mutual information calculation.
    """
    data1, data2 = args
    mine = MINE()
    mine.compute_score(data1, data2)
    return mine.mic()

def determine_delay(data, max_delay=100, subsample_factor=10):
    """
    Determine the optimal delay using mutual information with subsampling.
    
    Parameters:
    data : array_like
        One-dimensional time series data.
    max_delay : int
        Maximum delay to consider.
    subsample_factor : int
        Factor by which to subsample the data for efficiency.
        
    Returns:
    optimal_delay : int
        The determined optimal delay.
    """
    subsampled_data = data[::subsample_factor]
    with multiprocessing.Pool() as pool:
        args_list = [(subsampled_data[:-i], subsampled_data[i:]) for i in range(1, max_delay+1)]
        mi_values = pool.map(mutual_info_worker, args_list)
    min_index = np.argmin(mi_values)
    return min_index + 1
    
def process_phase_space_analysis(eeg_data, emb_dim, max_delay, subsample_factor=10):
    """
    Process EEG data for phase space analysis.
    
    Parameters:
    eeg_data : 2D ndarray
        EEG data array (channels x time series data).
    emb_dim : int
        Embedding dimension.
    max_delay : int
        Maximum delay to consider.
    subsample_factor : int, optional
        Factor for subsampling in delay determination.
        
    Returns:
    results : list
        Results of phase space analysis for each channel.
    """
    results = []
    for ch in range(eeg_data.shape[0]):
        channel_data = eeg_data[ch, :]
        optimal_delay = determine_delay(channel_data, max_delay, subsample_factor)
        embedded_data = delay_embedding(channel_data, emb_dim, optimal_delay)
        # Additional analysis can be added here
        results.append(embedded_data)
    return results

def create_phase_space_plot(embedded_data_list, titles, output_dir):
    """
    Create and save 2D phase space plots for each channel.

    Parameters:
    embedded_data_list : list of ndarrays
        List of delay-embedded data for each channel.
    titles : list of str
        List of titles for each plot corresponding to each channel.
    output_dir : str
        Directory to save the plots.
    """
    for i, embedded_data in enumerate(embedded_data_list):
        plt.figure(figsize=(8, 6), facecolor='black')
        plt.scatter(embedded_data[:, 0], embedded_data[:, 1], color='red', s=0.5)
        plt.title(titles[i], color='white')
        plt.xlabel('Embedding Dimension 1', color='grey')
        plt.ylabel('Embedding Dimension 2', color='grey')
        plt.xticks(color='grey')
        plt.yticks(color='grey')
        plt.gca().spines['left'].set_color('grey')
        plt.gca().spines['right'].set_color('grey')
        plt.gca().spines['bottom'].set_color('grey')
        plt.gca().spines['top'].set_color('grey')
        
        output_path = os.path.join(output_dir, f"phase_space_channel_{i+1}.png")
        plt.savefig(output_path, facecolor='black', dpi=300)
        plt.close()

