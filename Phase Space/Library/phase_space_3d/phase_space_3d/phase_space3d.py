import numpy as np
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
from minepy import MINE
import multiprocessing
import os

def delay_embedding(data, emb_dim, delay):
    """
    Perform delay embedding on the provided data.
    
    Parameters:
    data : array_like
        One-dimensional time series data.
    emb_dim : int
        Embedding dimension.
    delay : int
        Delay time steps.
        
    Returns:
    embedded_data : ndarray
        The delay-embedded data.
    """
    N = len(data)
    embedded_data = np.zeros((N - (emb_dim - 1) * delay, emb_dim))
    for i in range(N - (emb_dim - 1) * delay):
        embedded_data[i] = [data[i + j * delay] for j in range(emb_dim)]
    return embedded_data

embedded_data_dict = {}

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


def create_3d_phase_space_plot(embedded_data, title, show_plot=True, save_path=None):
    """
    Create and optionally save a 3D phase space plot.
    
    Parameters:
    embedded_data : ndarray
        Data to be plotted, should be 3D embedded.
    title : str
        Title of the plot.
    show_plot : bool, optional
        Whether to display the plot.
    save_path : str, optional
        Path to save the plot image.
    """
    fig = plt.figure(figsize=(10, 8), facecolor='black')
    ax = fig.add_subplot(111, projection='3d', frame_on=False)
    ax.scatter(embedded_data[:, 0], embedded_data[:, 1], embedded_data[:, 2], color='red', s=0.2)
    ax.set_facecolor('black')
    ax.set_title(title, color='white')
    # Set other axes properties and labels...
    if save_path:
        plt.savefig(save_path, facecolor='black', dpi=300)
    if show_plot:
        plt.show()
    plt.close()
