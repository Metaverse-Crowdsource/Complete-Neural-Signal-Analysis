<div style="font-size: 13px; font-family: 'Times New Roman', Times, serif; background-color: #181818; color: #D0D0D0; padding: 20px; border-radius: 8px; margin: 10px; display: flex; flex-wrap: nowrap; justify-content: space-between;">
    <!-- Column 1 -->
    <div style="flex: 1; margin-right: 10px;">
        <h2>Introduction</h2>
        <p>
            This script performs analysis on EEG data using the concept of Transfer Entropy (TE). Specifically, it investigates the directionality of information flow between different EEG channels based on their 2D embeddings.
        </p>
        <h2>Data Preparation</h2>
        <p>
            Initially, the code unzips a dataset of 2D embedded EEG data for multiple channels. The embedded data is then loaded into Python, trimmed to a desired length, and grouped by hemisphere (left and right).
        </p>
    </div>
    <!-- Column 2 -->
    <div style="flex: 1; margin-left: 10px;">
        <h2>Analysis</h2>
        <p>
            Transfer Entropy calculations are conducted to quantify the amount of information flowing from one EEG channel to another. This is done after binning the data and applying the PyInform library’s TE function.
        </p>
        <p>
            The TE formula is represented as:
            \[
            TE_{X \rightarrow Y} = \sum_{y_{t+1}, y_t, x_t} p(y_{t+1}, y_t, x_t) \log \frac{p(y_{t+1} | y_t, x_t)}{p(y_{t+1} | y_t)}
            \]
            Here \(X\) and \(Y\) are random variables, \(p(y_{t+1}, y_t, x_t)\) is the joint probability distribution function, and \(p(y_{t+1} | y_t, x_t)\) and \(p(y_{t+1} | y_t)\) are conditional probability distribution functions.
        </p>
        </p>
    </div>
</div>