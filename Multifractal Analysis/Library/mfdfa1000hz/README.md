<div style="font-size: 14px; font-family: 'Times New Roman', Times, serif; background-color: #181818; color: #D0D0D0; padding: 20px; border-radius: 8px; margin: 10px; display: flex; flex-wrap: nowrap; justify-content: space-between;">
    <!-- Column 1 -->
    <div style="flex: 1; margin-right: 10px;">
        <h2>Introduction</h2>
        <p>The examination of multifractal properties of EEG data is essential for understanding the underlying complex dynamics. A popular technique for such analysis is Multifractal Detrended Fluctuation Analysis (MFDFA), which is employed here to delineate the multifractal spectrum of EEG data across various channels. The MFDFA technique facilitates the discernment of self-affine properties of signals across multiple scales.</p>
        <h2>Mathematical Foundations</h2>
        <p>MFDFA is grounded on the calculation of fluctuation functions \( F_q(s) \) for different segments of the time series, followed by a scaling analysis. The fluctuation function is given by:</p>
        \[ F_q(s) = \left[ \frac{1}{2N_s} \sum_{v=1}^{2N_s} F^2(v, s) \right]^{1/q} \]
        <p>where \( s \) is the scale, \( N_s \) is the number of segments, \( v \) is the segment index, and \( F(v, s) \) is the fluctuation in segment \( v \) at scale \( s \). The exponent \( q \) allows us to investigate multifractal properties; for \( q=2 \), this reduces to traditional DFA.</p>
        <p>The scaling behavior is then analyzed by fitting a straight line to the log-log plot of \( F_q(s) \) versus \( s \), which reveals the Hurst exponents \( h(q) \), and consequently, the multifractal spectrum \( f(\alpha) \).</p>
        <h2>MFDFA Process</h2>
        <p>The MFDFA begins with the integration of the time series, followed by dividing the integrated series into segments. A local trend is removed from each segment, and the variance of the residual series is computed. This process is performed across multiple scales to obtain the fluctuation function \( F_q(s) \).</p>
    </div>
    <!-- Column 2 -->
    <div style="flex: 1; margin-left: 10px;">
        <h2>Implementation Synopsis</h2>
        <p>The EEG data is loaded, followed by the configuration of the scale and \( q \) values for the MFDFA. The scale range and \( q \) values are chosen to cover a broad range, encapsulating various fractal properties.</p>
        <p>A loop iterates through each EEG channel, invoking the MFDFA function to calculate the scale and fluctuation functions. These results are stored for further analysis, and a visual representation is generated for each channel, showcasing the raw EEG data alongside its multifractal spectrum.</p>
        <h2>Data Visualization</h2>
        <p>Each channel's data is plotted in time domain, and its corresponding multifractal spectrum is exhibited in a log-log plot. This juxtaposition elucidates the multifractal nature of the EEG data and its manifestation across different channels.</p>
        <h2>Conclusion</h2>
        <p>The exercise unveils the multifractal characteristics of EEG data, furnishing crucial insights into the underlying dynamics. The visual representation augments comprehension of the multifractal behavior inherent in EEG data across different channels, forming a foundation for further explorations into the complex dynamics of brain signals.</p>
    </div>
</div>
