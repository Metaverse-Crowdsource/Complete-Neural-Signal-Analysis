"""
3D Phase Space Analysis Module

This module provides functions for performing 3D phase space analysis on EEG data. It includes delay embedding and phase space reconstruction techniques, suitable for both single-channel and multi-channel EEG data.

Functions:
- delay_embedding(data, emb_dim, delay): Performs delay embedding for each channel.
- false_nearest_neighbors(data, emb_dim, delay, R): Computes False Nearest Neighbors for each channel.
- determine_delay(data, max_delay, subsample_factor): Determines optimal delays for each channel using mutual information.
- create_3d_phase_space_plots(embedded_data_list, titles, show_plots, output_dir): Creates and optionally saves 3D phase space plots for each channel.

Example Usage:
---------------
import numpy as np
from phase_space_3d import delay_embedding, create_3d_phase_space_plots

# Sample EEG data (3 channels x 1000 data points)
eeg_data = np.random.rand(3, 1000)
emb_dim = 3
delay = 20

# Perform delay embedding
embedded_data = delay_embedding(eeg_data, emb_dim, delay)

# Create 3D phase space plots
titles = ['Channel 1', 'Channel 2', 'Channel 3']
output_dir = '/path/to/save/plots'
create_3d_phase_space_plots(embedded_data, titles, output_dir=output_dir)

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
        embedded_channel_data = np.zeros((N - (emb_dim - 1) * delay, emb_dim))
        for i in range(N - (emb_dim - 1) * delay):
            embedded_channel_data[i] = [channel_data[i + j * delay] for j in range(emb_dim)]
        embedded_data.append(embedded_channel_data)
    return embedded_data

def false_nearest_neighbors(data, emb_dim, delay, R=10):
    """
    Compute False Nearest Neighbors for different embedding dimensions for each channel.
    
    Parameters:
    data : 2D array_like
        Multi-dimensional time series data where each row is a channel.
    emb_dim : int
        Embedding dimension.
    delay : int
        Delay time steps.
    R : float
        Threshold for determining false neighbors.
        
    Returns:
    false_neighbors : list of ndarrays
        Array of false nearest neighbor fractions for each embedding dimension for each channel.
    """
    num_channels = data.shape[0]
    false_neighbors_all = []
    for ch in range(num_channels):
        channel_data = data[ch, :]
        N = len(channel_data)
        false_neighbors = np.zeros(emb_dim)
        for d in range(1, emb_dim + 1):
            emb_data = delay_embedding(np.array([channel_data]), d, delay)[0]
            nbrs = NearestNeighbors(n_neighbors=2).fit(emb_data[:-delay])
            distances, indices = nbrs.kneighbors(emb_data[:-delay])
            neighbor_index = indices[:, 1]
            neighbor_distance = np.abs(channel_data[neighbor_index + delay] - channel_data[np.arange(N - d * delay) + delay])
            false_neighbors[d - 1] = np.mean((neighbor_distance / distances[:, 1]) > R)
        false_neighbors_all.append(false_neighbors)
    return false_neighbors_all

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
    Determine the optimal delay using mutual information with subsampling for each channel.
    
    Parameters:
    data : 2D array_like
        Multi-dimensional time series data where each row is a channel.
    max_delay : int
        Maximum delay to consider.
    subsample_factor : int
        Factor by which to subsample the data for efficiency.
        
    Returns:
    optimal_delays : list of ints
        The determined optimal delays for each channel.
    """
    num_channels = data.shape[0]
    optimal_delays = []
    for ch in range(num_channels):
        channel_data = data[ch, :]
        subsampled_data = channel_data[::subsample_factor]
        with multiprocessing.Pool() as pool:
            args_list = [(subsampled_data[:-i], subsampled_data[i:]) for i in range(1, max_delay+1)]
            mi_values = pool.map(mutual_info_worker, args_list)
        min_index = np.argmin(mi_values)
        optimal_delays.append(min_index + 1)
    return optimal_delays

def create_3d_phase_space_plots(embedded_data_list, titles, show_plots=True, output_dir=None):
    """
    Create and optionally save 3D phase space plots for each channel.
    
    Parameters:
    embedded_data_list : list of ndarrays
        List of delay-embedded data for each channel.
    titles : list of str
        List of titles for each plot corresponding to each channel.
    show_plots : bool, optional
        Whether to display the plots.
    output_dir : str, optional
        Directory to save the plot images.
    """
    for i, embedded_data in enumerate(embedded_data_list):
        fig = plt.figure(figsize=(10, 8), facecolor='black')
        ax = fig.add_subplot(111, projection='3d', frame_on=False)
        ax.scatter(embedded_data[:, 0], embedded_data[:, 1], embedded_data[:, 2], color='red', s=0.2)
        ax.set_facecolor('black')
        ax.set_title(titles[i], color='white')
        # Set other axes properties and labels...

        if output_dir:
            save_path = os.path.join(output_dir, f"3d_phase_space_channel_{i+1}.png")
            plt.savefig(save_path, facecolor='black', dpi=300)
        if show_plots:
            plt.show()
        plt.close()


