<div style="font-size: 13px; font-family: 'Times New Roman', Times, serif; background-color: #181818; color: #D0D0D0; padding: 20px; border-radius: 8px; margin: 10px; display: flex; flex-wrap: nowrap; justify-content: space-between;">
    <!-- Column 1 -->
    <div style="flex: 1; margin-right: 10px;">
        <h2>Introduction</h2>
        <p>This section aims to elaborate on the computational methodology for the estimation of Power Spectral Density (PSD) in electroencephalogram (EEG) data. By employing Welch's method, we convert the time-domain EEG signals into their frequency domain representation, which is pivotal for neurological diagnosis and research.</p>        
        <h2>Objectives</h2>
        <ul>
            <li>Data Importation: Load EEG data from a .npy file.</li>
            <li>Frequency Analysis: Compute PSD for each EEG channel using Welch's method.</li>
            <li>Data Visualization: Plot the PSD data for each channel.</li>
        </ul>        
        <h2>Mathematical Formulations</h2>
        <h3>Data Importation and Pre-Processing</h3>
        <p>The EEG data, represented as a NumPy array \( \text{eeg\_data\_array} \), is imported. Each column in this array corresponds to different EEG channels. A scalar \( f_s \) specifies the sampling frequency, providing the temporal resolution of the EEG data.</p>
        <h3>Welch's Method</h3>
        <p>Welch's method for computing PSD involves partitioning the time series into overlapping segments and then averaging the Fourier Transforms. Mathematically, the PSD \( P(f) \) is given by:</p>
        \[ P(f) = \frac{1}{N}\sum_{i=1}^{N}|\text{FFT}(x_{i})|^{2} \]
        <p>Here, \( N \) is the number of segments, \( x_i \) is the \( i \)-th segment, and FFT refers to the Fast Fourier Transform.</p>
    </div>
    <!-- Column 2 -->
    <div style="flex: 1; margin-left: 10px;">
        <h2>Computational Steps</h2>
        <p>A Python loop iterates through each channel to extract the EEG data, upon which Welch's method is applied to calculate the PSD. A dictionary \( \text{psd\_data} \) is initialized to store the computed PSD values.</p>        
        <h2>Data Storage</h2>
        <p>The computed PSD is saved as a NumPy array for future analyses, serving as a dataset for downstream scientific applications like spectral clustering or machine learning-based neurological diagnosis.</p>
        <h2>Visualization</h2>
        <p>The calculated PSD values are visualized using Matplotlib. A subplot is created for each channel, and a logarithmic scale is employed on the y-axis to highlight variations in the spectral density.</p>
        <h2>Scientific Relevance</h2>
        <p>This methodology serves as a cornerstone for both neuroscientific research and clinical applications. Spectral analysis of EEG is invaluable for understanding abnormal neural patterns, sleep cycles, or even the neural basis of consciousness.</p>
        <h2>Summary</h2>
        <p>The computation of PSD using Welch's method and its subsequent visualization provides an in-depth spectral analysis of EEG data. This is integral for scientific research endeavors that focus on understanding brain functionalities and abnormalities.</p>
    </div>
</div>