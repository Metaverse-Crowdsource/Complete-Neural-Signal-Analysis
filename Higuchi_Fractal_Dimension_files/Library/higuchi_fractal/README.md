<div style="font-size: 13px; font-family: 'Times New Roman', Times, serif; background-color: #181818; color: #D0D0D0; padding: 20px; border-radius: 8px; margin: 10px; display: flex; flex-wrap: nowrap; justify-content: space-between;">
    <!-- Column 1 -->
    <div style="flex: 1; margin-right: 10px;">
        <h2>Introduction</h2>
        <p>
            This code calculates the Higuchi Fractal Dimension (HFD) of EEG signals for multiple channels.
            Fractal dimensions are used to quantify the complexity of a data series, which is particularly useful in neuroscience for understanding the complexity of brain activity.
        </p>
    </div>
    <!-- Column 2 -->
    <div style="flex: 1; margin-left: 10px;">
        <p>
            The code uses the Higuchi Fractal Dimension algorithm, which is computationally efficient and particularly useful for analyzing time series data. It works by evaluating the length of the curve created by the data points at different scales.
        </p>
        \[
        L_k = \frac{N-1}{\left\lfloor \frac{N-m}{k} \right\rfloor k} \sum_{m=0}^{k-1} \left[ \sum_{i=1}^{\left\lfloor \frac{N-m}{k} \right\rfloor} \left| x[m+i \cdot k] - x[m+i \cdot k - k] \right| \right]
        \]
        \[
        HFD = \frac{\log(L_{k2}/L_{k1})}{\log(k2/k1)}
        \]
        <p>
            Here, \( L_k \) is the length of the curve for a given \( k \) (delay or time offset). \( N \) is the length of the data, \( x \) is the time series data, and \( m \) is the initial time point for each \( k \).
        </p>
        <p>
            Finally, the HFD values for each channel are stored in the list <code>hfd_values</code>.
        </p>
    </div>
</div>