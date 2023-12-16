<div style="font-size: 13px; font-family: 'Times New Roman', Times, serif; background-color: #181818; color: #D0D0D0; padding: 20px; border-radius: 8px; margin: 10px; display: flex; flex-wrap: nowrap; justify-content: space-between;">
    <!-- Column 1 -->
    <div style="flex: 1; margin-right: 10px;">
        <h2>Introduction</h2>
        <p>This analysis adopts the Short-Time Fourier Transform (STFT) approach to break down Electroencephalogram (EEG) signals across multiple channels into their constituent frequencies. The objective is to represent these signals in both the time and frequency domain.</p>
        <h2>Objectives</h2>
        <ul>
            <li>Perform STFT on EEG data for each channel.</li>
            <li>Convert the magnitude spectrum to decibels (dB).</li>
            <li>Visualize the resulting spectrograms for various EEG channels.</li>
        </ul>
        <h2>Mathematical Foundations</h2>
        <h3>Short-Time Fourier Transform (STFT)</h3>
        \[ \text{STFT}(x(t)) = X(f, \tau) = \int_{-\infty}^{\infty} x(t) w(t-\tau) e^{-j 2\pi f t} dt \]
        <p>Where \( X(f, \tau) \) is the STFT, \( x(t) \) is the time-domain EEG signal, \( w(t) \) is the window function, \( \tau \) is the time shift, and \( f \) is the frequency.</p>        
        <h3>Conversion to Decibels</h3>
        \[ \text{STFT}_{\text{dB}} = 10 \log_{10} \left| \text{STFT}(x(t)) \right| \]
        <p>This conversion allows for a logarithmic representation of the amplitude, enhancing the visibility of lower amplitude spectral components.</p>
    </div>
    <!-- Column 2 -->
    <div style="flex: 1; margin-left: 10px;">
        <h2>Methodology</h2>
        <ul>
            <li>EEG data from each channel is isolated for analysis.</li>
            <li>The window size for STFT is set to 2 seconds, given the sampling frequency.</li>
            <li>STFT is performed using the Scipy library's <code>stft</code> function.</li>
            <li>The resulting STFT data is converted to dB for better interpretability.</li>
            <li>The STFT data for each channel is stored in a Python dictionary.</li>
        </ul>
        <h2>Data Serialization</h2>
        <p>The processed STFT data for each EEG channel is serialized and stored as a single NumPy file for later retrieval and analysis.</p>
        <h2>Scientific and Clinical Relevance</h2>
        <p>The derived spectrograms can serve as valuable diagnostic tools in clinical neuroscience to assess brain functions. They may facilitate the diagnosis and monitoring of various neurological disorders, thereby providing key insights for therapeutic strategies.</p>       
        <h2>Conclusion</h2>
        <p>The STFT approach offers a robust methodology for EEG data analysis, enabling the time-frequency representation of electrical activity in the brain. This holds significant potential for enhancing our comprehension of neural oscillations and for the clinical interpretation of EEG data.</p>
    </div>
</div>
