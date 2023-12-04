<div style="font-size: 13px; font-family: 'Times New Roman', Times, serif; background-color: #181818; color: #D0D0D0; padding: 20px; border-radius: 8px; margin: 10px; display: flex; flex-wrap: nowrap; justify-content: space-between;">
    <!-- Column 1 -->
    <div style="flex: 1; margin-right: 10px;">
        <h2>Introduction</h2>
        <p>This code calculates and visualizes the frequency at which maximum power occurs in the spectrum of EEG signals for multiple channels. By identifying these peak frequencies, one can understand which frequency components dominate the EEG signals for each channel, providing valuable insights into brain activity.</p>
            <div style="flex: 1; margin-left: 10px;">
        <p>Similar to the spectral centroid, the Fourier Transform is used here to move from the time-domain to the frequency domain. The formula for the Fourier Transform remains the same:</p>
        \[
        F(f) = \int_{-\infty}^{\infty} x(t) e^{-2\pi ift} dt
        \]
        <p>In this case, however, the focus is on identifying the frequency at which the power spectral density (PSD) peaks. The power spectral density for each frequency \( f \) is given by \( |F(f)|^2 \).</p>
    </div>
    <!-- Column 2 -->
        <p>The frequency \( f_{\text{peak}} \) at which the power is maximum can be mathematically expressed as:</p>
        \[
        f_{\text{peak}} = \text{argmax}_{f \geq 0} \left( |F(f)|^2 \right)
        \]
        <p>In the code, this peak frequency is computed using NumPy's <code>argmax</code> function on the absolute value of the positive half of the Fourier spectrum. It is stored in a dictionary called <code>peak_frequencies</code>, one for each EEG channel.</p>
        <p>Each channel's power spectral density is also plotted in log-log scale, and the peak frequency is marked on the graph. This allows for better visualization of the power-law distribution commonly seen in natural signals like EEG.</p>
    </div>
</div>