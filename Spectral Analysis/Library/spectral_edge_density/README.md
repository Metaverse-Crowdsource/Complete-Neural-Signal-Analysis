<div style="font-size: 13px; font-family: 'Times New Roman', Times, serif; background-color: #181818; color: #D0D0D0; padding: 20px; border-radius: 8px; margin: 10px; display: flex; flex-wrap: nowrap; justify-content: space-between;">
    <!-- Column 1 -->
    <div style="flex: 1; margin-right: 10px;">
        <h2>Introduction</h2>
        <p>This code calculates the spectral edge density for multiple EEG channels. Spectral edge density is a feature commonly used in EEG analysis to locate the frequency below which a certain percentage of the total power in the spectrum resides. This is especially helpful for identifying the dominant frequency components in brain activity.</p>
    </div>
    <!-- Column 2 -->
    <div style="flex: 1; margin-left: 10px;">
        <p>The Fourier Transform is used to transition from the time domain to the frequency domain. The spectral edge density is computed by first finding the total power in the spectrum:</p>
        \[
        P_{\text{total}} = \sum_{f \geq 0} |F(f)|^2
        \]
        <p>We then set a threshold, based on a given percentage (in this code, 95% is used), of the total power:</p>
        \[
        P_{\text{threshold}} = P_{\text{total}} \times \frac{\text{percentage}}{100}
        \]
        <p>We sum the power in descending order of magnitude and identify the frequency at which this sum first exceeds \( P_{\text{threshold}} \). This frequency is the spectral edge density:</p>
        \[
        f_{\text{edge}} = \text{argmax}_{f \geq 0} \left( \text{cumulative sum}(|F(f)|^2) \geq P_{\text{threshold}} \right)
        \]
        <p>The calculated spectral edge density for each EEG channel is stored in a dictionary named <code>spectral_edge_densities</code>.</p>
        <p>The bar chart plots the spectral edge densities across the EEG channels, providing a quick graphical summary. The calculated values are also saved as a numpy array for further analysis.</p>
    </div>
</div>