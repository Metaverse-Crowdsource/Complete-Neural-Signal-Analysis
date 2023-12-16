# Neural Signal Analysis Library

The `neural_signal_analysis` library is a comprehensive Python package for EEG data analysis. It encompasses a wide range of functionalities including FFT (Fast Fourier Transform), Higuchi Fractal Dimension, Transfer Entropy, Welch's Power Spectral Density, and more, providing a toolkit for researchers and developers working with neural signal data.

## Installation

To install `neural_signal_analysis`, simply run:

```bash
pip install neural_signal_analysis
```

Ensure you have Python 3.7 or later installed.

Modules:
FFT (Fast Fourier Transform)
frequency_maximum_power
higuchi_fractal_dimension
MFDFA_neural (Multifractal Detrended Fluctuation Analysis)
phase_space_2d
phase_space_3d
spectral_centroids
spectral_edge_density
spectral_entropy_signals
STFTsignal (Short-Time Fourier Transform)
transfer_entropy_all_signals
transfer_entropy_Hemispheric
transfer_entropy_regional
welchsPSD (Power Spectral Density)


Example usage:
```bash
from neural_signal_analysis import welchsPSD
```

Contributing

Contributions to neural_signal_analysis are welcome! If you have suggestions for improvements or encounter any issues, please feel free to open an issue or submit a pull request on our

License

This project is licensed under the CC BY-SA 4.0 License - see the LICENSE file for details.



Fast Fourier Transform (FFT) Module:
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



Frequency Maximum Power Module:
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



Higuchi Fractal Dimension Module:
Example Usage:
--------------
import numpy as np
from higuchi_fractal import higuchi_fd, higuchi_fd_multichannel

# For single-channel data
single_channel_data = np.random.rand(1000)
hfd_single = higuchi_fd(single_channel_data, k_max=10)

# For multi-channel data
multi_channel_data = np.random.rand(1000, 3)
hfd_multi = higuchi_fd_multichannel(multi_channel_data, k_max=10)


Multifractal Detrended Fluctuation Analysis (MFDFA) Module:
Example Usage:
---------------
import numpy as np
from mfdfa_neural import calculate_mfdfa, plot_mfdfa_results

# Sample EEG data (5 channels x 1000 data points)
eeg_data = np.random.rand(5, 1000)
lags = np.linspace(1, 100, 100)
qs = np.linspace(-5, 5, 100)
channel_names = ['Frontal', 'Parietal', 'Temporal', 'Occipital', 'Central']


Phase Space Analysis Module:
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


3D Phase Space Analysis Module:
Example Usage:
---------------
import numpy as np
from phase_space_3d import delay_embedding, create_3d_phase_space_plots

# Sample EEG data (3 channels x 1000 data points)
eeg_data = np.random.rand(3, 1000)
emb_dim = 3
delay = 20


Spectral Centroids Analysis Module:
Example Usage:
---------------
import numpy as np
from spectral_centroids import process_eeg_data

# Sample EEG data (3 channels x 1000 data points)
eeg_data = np.random.rand(3, 1000)
fs = 250  # Sampling frequency in Hz

# Process EEG data and plot spectral centroids
process_eeg_data(eeg_data, fs)


Spectral Edge Density Analysis Module:
Example Usage:
---------------
import numpy as np
from spectral_edge_density import process_eeg_data

# Sample EEG data (3 channels x 1000 data points)
eeg_data = np.random.rand(3, 1000)
fs = 250  # Sampling frequency in Hz
percentage = 90  # Percentage threshold for spectral edge

# Process EEG data and plot spectral edge frequencies
process_eeg_data(eeg_data, fs, percentage)


Spectral Entropy Analysis Module:
Example Usage:
---------------
import numpy as np
from spectral_entropy_signals import process_eeg_data

# Sample EEG data (3 channels x 1000 data points)
eeg_data = np.random.rand(3, 1000)
fs = 250  # Sampling frequency in Hz
nperseg = 128  # Segment length for Welch's method

# Process EEG data and plot spectral entropy
process_eeg_data(eeg_data, fs, nperseg)


Short-Time Fourier Transform (STFT) Module:
Example Usage:
---------------
import numpy as np
from STFT_signal import process_eeg_data

# Sample EEG data (3 channels x 1000 data points)
eeg_data = np.random.rand(3, 1000)
fs = 250  # Sampling frequency in Hz
window_size = 128  # Segment length for STFT in samples

# Process EEG data and plot STFT
process_eeg_data(eeg_data, fs, window_size)


Transfer Entropy Regional Analysis Module:
Example Usage:
---------------
import numpy as np
from transfer_entropy_regional import process_granular_eeg_data

# Sample EEG data (multiple channels)
eeg_data = np.random.rand(5, 1000)  # Example with 5 channels
eeg_channels = ['Ch1', 'Ch2', 'Ch3', 'Ch4', 'Ch5']
channel_groups = {"Group1": ['Ch1', 'Ch2'], "Group2": ['Ch3', 'Ch4']}

# Compute transfer entropy
te_results = process_granular_eeg_data(eeg_data, fs=1000, num_bins=10, k=1, l=1, eeg_channels=eeg_channels, channel_groups=channel_groups)
print(te_results)


Transfer Entropy Hemispheric Analysis Module:
Example Usage:
---------------
import numpy as np
from transfer_entropy_hemispheric import process_eeg_data

# Sample EEG data (multiple channels)
eeg_data = np.random.rand(10, 1000)  # Example with 10 channels
eeg_channels = ['Ch1', 'Ch2', ..., 'Ch10']
left_channels = ['Ch1', 'Ch2', 'Ch3', 'Ch4', 'Ch5']
right_channels = ['Ch6', 'Ch7', 'Ch8', 'Ch9', 'Ch10']

# Compute transfer entropy between hemispheres
te_left_to_right, te_right_to_left = process_eeg_data(eeg_data, fs=1000, num_bins=10, k=1, l=1, eeg_channels=eeg_channels, left_channels=left_channels, right_channels=right_channels)
print(f"Transfer Entropy from Left to Right: {te_left_to_right}")
print(f"Transfer Entropy from Right to Left: {te_right_to_left}")


Transfer Entropy Regional Analysis Module:
Example Usage:
---------------
import numpy as np
from transfer_entropy_regional import process_eeg_data

# Example EEG data with multiple channels
eeg_data = np.random.rand(10, 1000)  # Assume 10 channels
eeg_channels = ['Channel 1', 'Channel 2', ..., 'Channel 10']
regions = {
    "Frontal": ['Channel 1', 'Channel 2'],
    "Temporal": ['Channel 3', 'Channel 4']
    # Add other regions as needed
}

# Compute transfer entropy between regions
te_results = process_eeg_data(eeg_data, fs=1000, num_bins=10, k=1, l=1, eeg_channels=eeg_channels, regions=regions)
print(te_results)


Welch's Power Spectral Density Analysis Module:
Example Usage:
---------------
import numpy as np
from welchsPSD import process_eeg_data

# Sample EEG data (3 channels x 1000 data points)
eeg_data = np.random.rand(3, 1000)
fs = 250  # Sampling frequency in Hz

# Process EEG data and plot Power Spectral Density
process_eeg_data(eeg_data, fs)

