<div style="font-size: 13px; font-family: 'Times New Roman', Times, serif; background-color: #181818; color: #D0D0D0; padding: 20px; border-radius: 8px; margin: 10px; display: flex; flex-wrap: nowrap; justify-content: space-between;">
    <!-- Column 1 -->
    <div style="flex: 1; margin-right: 10px;">
        <h2>Introduction</h2>
        <p>Utilising Welch's method, an adaptation of Fourier Transform designed for reducing noise and improving spectral estimate accuracy, the EEG data is transposed from the time to the frequency domain. This is achieved using the `welch` function from the `scipy.signal` library with a sampling frequency \( f_s \) of 1000 Hz and a segment length \( n_{\text{perseg}} \) of 2000 samples. The output is a power spectral density (PSD), \( P_{xx} \), which is then normalised to serve as a probability density function (PDF). Mathematically, the Shannon spectral entropy \( H \) is calculated as:</p>
        <p>
        \[
        H = -\sum_{i} p(x_i) \log_2 p(x_i)
        \]
        </p>
        <p>Where \( p(x_i) \) are the probabilities corresponding to the power at each frequency bin in \( P_{xx} \). Shannon's entropy serves as an apt measure to gauge the complexity and variability inherent in neural signals. </p>
    </div>
    <!-- Column 2 -->
    <div style="flex: 1; margin-left: 10px;">
        <p>In the neuroscientific sphere, the algorithm interrogates EEG channels that span strategic cortical regions, thereby permitting an enriched understanding of different cognitive and motor functions. Spectral entropy functions as an incisive index for assessing neural complexity and has found applications in delineating various mental states such as relaxation, attention, and cognitive load, as well as pathological states including epilepsy and Alzheimer's disease. </p>
        <p>The code is structured to iterate through each EEG channel, calculate its power spectral density, normalise this density, and derive its spectral entropy. These entropy values are meticulously stored in a Python dictionary, which dovetails with the code's modular architecture. Finally, the spectral entropy values are visualised through a bar graph, offering an intuitive medium for channel-wise comparisons. This is enabled through Python libraries like `numpy`, `matplotlib`, and `scipy`, thus amalgamating computational efficacy with rigorous mathematical and neuroscientific reasoning.</p>
    </div>
</div>