<div style="font-size: 13px; font-family: 'Times New Roman', Times, serif; background-color: #181818; color: #D0D0D0; padding: 20px; border-radius: 8px; margin: 10px; display: flex; flex-wrap: nowrap; justify-content: space-between;">
    <!-- Column 1 -->
    <div style="flex: 1; margin-right: 10px;">
        <h2>Introduction</h2>
        <p>The core objective of the discussed methodology was to ascertain an optimal embedding dimension for the phase space reconstruction of EEG data. This step is paramount for accurate dynamical analysis of time-series data. The False Nearest Neighbors (FNN) algorithm was employed to this end, providing a metric that gauges the fraction of false neighbors across varying dimensions, thus hinting at the dimension where the data unfolds into a sufficiently unambiguous geometric structure.</p>
        <h2>Mathematical Foundations</h2>
        <p>The process initiates with a <strong>delay embedding</strong> transformation, which maps the one-dimensional time-series data into a higher-dimensional phase space, aiding in the exploration of its geometric and topological properties. The delay embedding of a time series \( x(t) \) is given by:</p>
        \[ X(t) = [ x(t), x(t-\tau), x(t-2\tau), \ldots, x(t-(m-1)\tau) ] \]
        <p>where \( m \) is the embedding dimension, and \( \tau \) is the delay parameter. This transformation is pivotal as it facilitates the unveiling of the underlying dynamical structure of the EEG data, which is ostensibly concealed in its one-dimensional time-series representation.</p>
        <p>The chosen delay \( \tau \) and embedding dimension \( m \) significantly impact the resultant phase space structure. A judicious choice of these parameters is essential to ensure an accurate reconstruction that mirrors the intrinsic dynamics of the system.</p>
        <h2>False Nearest Neighbors Analysis</h2>
        <p>The crux of the FNN methodology lies in the identification of false neighbors. A point is deemed a false neighbor if the distance between the points increases significantly when the dimension of the embedding space is increased. Mathematically, the condition for a false neighbor is given by:</p>
        \[ \frac{|x(t + \tau) - x(u + \tau)|}{\|X(t) - X(u)\|} > R \]
        <p>where \( X(t) \) and \( X(u) \) are neighboring points in the \( m \)-dimensional space, \( x(t + \tau) \) and \( x(u + \tau) \) are the corresponding points in the next higher dimension, and \( R \) is a threshold value. The threshold \( R \) is crucial in distinguishing between true and false neighbors, thus aiding in identifying the dimension where the system's dynamics are sufficiently unfolded.</p>
        <p>The FNN analysis provides a quantitative measure to ascertain the embedding dimension where the structure of the attractor is adequately revealed, thereby avoiding the misinterpretations that could arise from a spurious, lower-dimensional representation.</p>
    </div>
    <!-- Column 2 -->
    <div style="flex: 1; margin-left: 10px;">
        <h2>Implementation Synopsis</h2>
        <p>Initially, the EEG data along with channel names were loaded. A predefined maximum embedding dimension was set to guide the exploration. The delay embedding transformation was then applied to the data, post which the FNN algorithm was engaged to calculate the fraction of false neighbors for each embedding dimension, per EEG channel.</p>
        <h2>Data Visualization</h2>
        <p>The results were illustrated in a plot depicting the fraction of false neighbors as a function of embedding dimensions for each EEG channel. This visual representation is instrumental in discerning the embedding dimension at which the fraction of false neighbors plunges, indicating a suitable unfolding of the attractor.</p>
        <h2>Conclusion</h2>
        <p>The elucidated method furnishes a robust mechanism for identifying an appropriate embedding dimension, a critical precursor for any profound analysis of time-series EEG data. The graphical insight, alongside the saved data, serves as a substantial asset for ongoing and future explorations into the complex dynamical systems represented by EEG recordings.</p>
    </div>
</div>

<div style="font-size: 14px; font-family: 'Times New Roman', Times, serif; background-color: #181818; color: #D0D0D0; padding: 20px; border-radius: 8px; margin: 10px; display: flex; flex-wrap: nowrap; justify-content: space-between;">
    <!-- Column 1 -->
    <div style="flex: 1; margin-right: 10px;">
        <h2>Introduction</h2>
        <p>Building upon the foundational exploration of optimal embedding dimensions using the False Nearest Neighbors (FNN) algorithm, the methodology now shifts towards fine-tuning the delay parameter for phase space reconstruction of EEG data. This critical step aims to ensure that the temporal structure of the data is preserved in the phase space, thus enabling an accurate reflection of the underlying dynamical systems. The method employed for delay determination utilizes the concept of Mutual Information (MI), offering a quantitative measure of statistical dependencies between the time-lagged versions of the time-series data.</p>
        <h2>Mathematical Foundations</h2>
        <p>The first pivotal step in the analysis is the calculation of mutual information between the original time series \( x(t) \) and its delayed version \( x(t+\tau) \), which is defined as:</p>
        \[ \text{MI}(x(t); x(t+\tau)) = \sum_{x,x'} p(x, x') \log\left(\frac{p(x, x')}{p(x)p(x')}\right) \]
        <p>where \( p(x, x') \) is the joint probability distribution of \( x(t) \) and \( x(t+\tau) \), and \( p(x) \) and \( p(x') \) are the marginal distributions. The MI quantifies the amount of information shared between the original and delayed time series, with a minimization of MI indicating a suitable choice of delay, as it implies a reduction in redundancy.</p>
        <p>Following the determination of the optimal delay, a <strong>delay embedding</strong> is carried out, transforming the one-dimensional time-series data into a higher-dimensional phase space. The delay embedding formula is given by:</p>
        \[ X(t) = [ x(t), x(t-\tau), x(t-2\tau), \ldots, x(t-(m-1)\tau) ] \]
        <p>where \( m \) is the embedding dimension, and \( \tau \) is the delay parameter. This transformation unveils the geometric and topological properties of the dynamical system underlying the EEG data, subsequently allowing for a nuanced exploration of its phase space structure.</p>
        <h2>Implementation of Mutual Information for Delay Determination</h2>
        <p>Employing the Maximal Information Coefficient (MIC) as a robust measure for mutual information, the process navigates through a range of delay values to identify the one that minimizes the MIC, thus pinpointing the delay that affords a decorrelation in the time-lagged data. This step is crucial as it sets the stage for an accurate phase space reconstruction, which is indispensable for any subsequent dynamical analysis.</p>
    </div>
    <!-- Column 2 -->
    <div style="flex: 1; margin-left: 10px;">
        <h2>Implementation Synopsis</h2>
        <p>The EEG data, along with the specified channel names, were initially loaded, followed by a loop through each EEG channel to perform the analysis individually. For each channel, the mutual information was calculated for a range of delay values, with a subsampling factor employed to manage the computational load. The delay that minimized the mutual information was then selected as the optimal delay for that particular channel.</p>
        <p>Post delay determination, a delay embedding was performed using the optimal delay and a fixed embedding dimension of 2. The embedded data was saved for further analysis, and a 2D scatter plot was generated to visualize the phase space structure for each channel. The visual representation serves as a qualitative validation of the delay embedding, offering insight into the unfolding of the EEG data in the phase space.</p>
        <h2>Data Visualization</h2>
        <p>The phase space plots provide a visual validation of the delay embedding, illustrating the unfolding of the EEG data in a 2D phase space. Each plot showcases the dynamical structure inherent in the data, offering a spatial representation of the time-series data that unveils its complex behavior over time.</p>
        <h2>Conclusion</h2>
        <p>The described methodology offers a meticulous approach towards the crucial step of delay determination and embedding for phase space reconstruction. By leveraging mutual information as a metric for delay selection, the method ensures a robust foundation for unveiling the intrinsic dynamical systems represented by the EEG data. The subsequent visualization and preservation of the embedded data underscore the potential for deeper exploration into the complex dynamics of neurological signals, setting the stage for advanced analytical endeavors.</p>
    </div>
</div>
