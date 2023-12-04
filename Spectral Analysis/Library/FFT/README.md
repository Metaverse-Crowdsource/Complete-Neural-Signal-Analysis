<div style="font-size: 13px; font-family: 'Times New Roman', Times, serif; background-color: #181818; color: #D0D0D0; padding: 20px; border-radius: 8px; margin: 10px; display: flex; flex-wrap: nowrap; justify-content: space-between;">
    <!-- Column 1 -->
    <div style="flex: 1; margin-right: 10px;">
        <h2>Introduction</h2>
        <p>This analysis is focused on computing the Power Spectral Density (PSD) of electroencephalogram (EEG) data via Fast Fourier Transform (FFT). Understanding the frequency composition of EEG signals has critical applications in neuroscience research and diagnostics.</p>
        <h2>Objectives</h2>
        <ul>
            <li>Data Selection: Extract the EEG data for individual channels.</li>
            <li>Fourier Analysis: Compute the PSD using FFT.</li>
            <li>Data Visualization: Render the computed PSD values.</li>
        </ul>
        <h2>Mathematical Formulations</h2>
        <h3>Data Selection and Parameter Definition</h3>
        <p>The EEG data, represented by the array \( \text{eeg\_data\_array} \), is segregated into individual channels. The sampling frequency \( f_s \) is defined to establish the time intervals between successive samples.</p>
       <h3>FFT-based PSD Computation</h3>
        <p>For each EEG channel, the FFT is computed as per the following formula:</p>
        \[ \text{FFT}(x) = \sum_{n=0}^{N-1} x[n] \cdot e^{-j \cdot 2 \pi \cdot f \cdot n / N} \]
        <p>Subsequently, PSD is derived from the FFT values using:</p>
        \[ \text{PSD} = |\text{FFT}(x)|^2 \]
    </div>
    <!-- Column 2 -->
    <div style="flex: 1; margin-left: 10px;">
        <h2>Computational Steps</h2>
        <p>A Python loop enumerates through each EEG channel, extracts the corresponding EEG data, and computes the PSD using FFT. The PSD values for each channel are stored in a Python dictionary, \( \text{fft\_psd\_data} \).</p>
        <h2>Data Visualization</h2>
        <p>The frequency components of the PSD are plotted using Matplotlib. The frequency axis is determined by the function \( \text{fftfreq} \), which takes into account the length of the PSD and the sampling frequency. Each subplot corresponds to a specific EEG channel, and the y-axis employs a logarithmic scale to improve clarity.</p>
        <h2>Data Storage</h2>
        <p>The computed PSD values are saved as a single NumPy file for further analysis or scientific research. The saved path is specified, and the data is serialized in the .npy format.</p>
        <h2>Scientific Relevance</h2>
        <p>The FFT-based approach to PSD analysis serves as a robust technique for investigating neural oscillations, brain connectivity, and other physiological phenomena of interest. The method is computationally efficient and widely applicable in both research and clinical settings.</p>
    </div>
</div>