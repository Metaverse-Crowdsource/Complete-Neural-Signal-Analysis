![Image](Images/00092.png)
<h1 align="center">EEG Prediction from Transcranial Electrical Stimulation(tES) using Chaos Theory, Dynamical Systems Theory, a Recurrent Neural Net(RNN), and a Convolutional Neural Net(CNN)</h1>


<div align="center">
  <a href="https://discord.gg/HBHGvDxDmt">
    <img src="https://img.shields.io/static/v1?label=Metaverse%20Crowdsource&message=450%20Members&color=7289DA&logo=discord&style=for-the-badge" alt="Discord server">
  </a>
</div>


<div align="center">
  <a href="https://www.tiktok.com/@metaversecrowdsourcebr">
    <img src="https://img.shields.io/badge/TikTok-%40metaversecrowdsourcebr-ff0080?style=for-the-badge&logo=tiktok&logoColor=white&labelColor=000000" alt="TikTok Profile">
  </a>
</div>


<br>
<br>
<h1 align="center">Purpose</h1>

We want to take the necessary steps towards connecting the human brain to a silicon computer or hybrid bio-silicon computer, via a biomatter brain-computer-interface. Part of this process includes the input of information directly into the human brain. Immediate readings of EEG data during the inputting of information into the human brain will need to be compared to a baseline of the real experience. An example of this is the [initial state EEG data of a human], the [EEG data state during, and immediately after, viewing a sequence of events in VR], and the [initial state EEG data of that same human], the [EEG data state during, and immediately after, having the visual data input into their brain].

<h1 align="center">Explanation</h1>

The central aim of this research project is to predict the electroencephalographic (EEG) effects of transcranial electrical stimulation (tES) by integrating chaos theory, dynamical systems theory, and a neural net stack. This is due to the importance of nonlinear dynamics in understanding brain activity.

This research has significant potential implications for the field of brain-computer interfaces, particularly for the novel area of connecting a human brain to a biohybrid silicon/biological computer[1] through a biological neural interface[2].

Accurately predicting the brain's reactions to tES could enable us to fine-tune the stimulation parameters, optimizing the quality of communication between the human brain and the hybrid computer. This could pave the way for developing protocols that ensure efficient and reliable transmission of information along the biomatter cable, essentially turning thoughts and brain activity into actionable commands for the hybrid computer.

This research could potentially contribute to the ambitious goal of directly stimulating sensorial perceptions in the human brain[3][4], a feat which, if achieved, would revolutionize neuroprosthetics and human-computer interfaces. The brain's sensorial system is intricate, involving a complex network of interconnected regions responsible for processing and interpreting different aspects of sensory information. The endeavor to predict EEG effects of tES using a multidisciplinary approach could shed light on how this complex system responds to external stimulation, and could possibly inform targeted, controlled stimulation techniques. While the research is not directly aimed at inducing visual perceptions, the insights and methodologies derived from the work could serve as a stepping stone towards understanding how to interface with the brain's sensory nervous system more effectively. It's crucial to note that this potential application would need to address substantial scientific, technical, and ethical challenges. Despite these hurdles, the promise of such a breakthrough underscores the broad-reaching implications of our research and its potential to catalyze advances in several areas of neuroscience and neurotechnology.

This research could contribute significantly to the field of decoding and encoding sensory perceptions in the human brain. The proposed model, which integrates chaos theory, dynamical systems theory, and a neural network stack, could provide a robust and comprehensive tool for understanding how the brain responds to tES. Such an understanding is critical for decoding brain activity associated with sensual perception. Specifically, the proposed use of transfer entropy to measure causal relationships within the brain could provide unique insights into how different sensory regions interact and coordinate to produce perceptions. Once these perceptions are decoded[5], it becomes theoretically possible to encode similar patterns back into the brain. The development of a predictive model capable of accurately capturing these dynamics would be a pivotal step towards this goal. Thus, while the immediate focus of the research is predicting EEG effects of tES, the methodologies and insights derived from the work have broader implications and could be foundational for future efforts aimed at decoding and encoding sensual perceptions in the brain.

<h1 align="center">References</h1>

[1]: L. Smirnova et al, "Organoid intelligence (OI): the new frontier in biocomputing and intelligence-in-a-dish," Frontiers in Science, pp. 0, 2023.

[2]: A. E. Rochford et al, "Functional neurological restoration of amputated peripheral nerve using biohybrid regenerative bioelectronics," Science Advances, vol. 9, (12), pp. eadd8162, 2023.

[3]: E. H. Holbrook et al, "Induction of smell through transethmoid electrical stimulation of the olfactory bulb," in International Forum of Allergy & Rhinology, 2019.

[4]: X. Chen et al, "Restoring vision via electrical stimulation through a 1024-channel microelectrode array implanted in visual cortex," Brain Stimulation: Basic, Translational, and Clinical Research in Neuromodulation, vol. 16, (1), pp. 181-182, 2023.

[5]: Y. Takagi and S. Nishimoto, "High-resolution image reconstruction with latent diffusion models from human brain activity," in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2023.

<br>
<br>
<h1 align="center">Data Source and Article</h1>

Data include within participant application of nine High-Definition tES (HD-tES) types, targeting three cortical regions (frontal, motor, parietal) with three stimulation waveforms (DC, 5 Hz, 30 Hz); more than 783 total stimulation trials over 62 sessions with EEG, physiological (ECG, EOG), and continuous behavioral vigilance/alertness metrics. Experiment 1 and 2 consisted of participants performing a continuous vigilance/alertness task over three 70-minute and two 70.5-minute sessions, respectively. Demographic data were collected, as well as self-reported wellness questionnaires before and after each session. Participants received all 9 stimulation types in Experiment 1, with each session including three stimulation types, with 4 trials per type. Participants received 2 stimulation types in Experiment 2, with 20 trials of a given stimulation type per session. Within-participant reliability was tested by repeating select sessions. This unique dataset supports a range of hypothesis testing including interactions of tDCS/tACS location and frequency, brain-state, physiology, fatigue, and cognitive performance.

Participants maintained a ball at the center of the screen and were periodically stimulated (with low-intensity noninvasive brain stimulation) for 30 secs with combinations of 9 stimulation montages.

**Dataset Article:** [https://doi.org/10.1038/s41597-021-01046-y](https://doi.org/10.1038/s41597-021-01046-y)

**Dataset:** [https://zenodo.org/record/3840615#.ZK2hJdLMKRQ](https://zenodo.org/record/3840615#.ZK2hJdLMKRQ)

**Table of stimulation condition and stimulation intensity:** [https://www.nature.com/articles/s41597-021-01046-y/tables/2](https://www.nature.com/articles/s41597-021-01046-y/tables/2)
<br>
<br>
<h1 align="center">Variables</h1>
<br>
<br>

| Variable       | Description                                                         |
|----------------|---------------------------------------------------------------------|
| triggers       | These are all the labeled EEG/Stimulation start/stop triggers       |
| EEGdata        | Contains the downsampled EEG/ECG/EOG voltage data dims: 35 channels X ~4E6 samples |
| fs             | The downsampled sampling frequency of the data: 1000 Hz             |
| fsOld          | The original sampling frequency of the data                         |
| time           | Time vector for the data. Should be 1 X ~4E6                        |
| label          | Contains the channel label information. BIP1= ECG, BIP2=EOG, RESP1= N/A |
| nchan          | The number of channels in the data                                  |
| rate           | Redundant to fs, sampling rate of data                              |
| npt            | Number of data points ~4E6                                          |
| Subj           | Subject and session that data


| Stim Type | Dominant Frequency (Hz) | Stim Amplitude (mA) |
|-----------|-------------------------|--------------------|
| F0 (Frontal DC)     | 0                       | 0.5                |
| F5 (Frontal 5 Hz)   | 5                       | 0.5                |
| F30 (Frontal 30 Hz) | 30                      | 0.5                |
| M0 (Motor DC)       | 0                       | 0.5                |
| M5 (Motor 5 Hz)     | 5                       | 0.5                |
| M30 (Motor 30 Hz)   | 30                      | 0.5                |
| P0 (Parietal DC)    | 0                       | 0.5                |
| P5 (Parietal 5 Hz)  | 5                       | 0.5                |
| P30 (Parietal 30 Hz)| 30                      | 0.5                |

    
    Trigger Code | Description
------------ | ---------------
02           | Start of the CTT
16           | Start of each stimulation trial
32           | Stimulation stop (end of 30 secs stimulation)


| Sub# | Session | File Num | F0 | M0 | P0 | F5 | M5 | P5 | F30 | M30 | P30 | StimTypeBlock1 | StimTypeBlock2 | StimTypeBlock3 | StimAmplitude_mA_block1 | StimAmplitude_mA_block2 | StimAmplitude_mA_block3 |
|------|---------|----------|----|----|----|----|----|----|-----|-----|-----|----------------|----------------|----------------|-------------------------|-------------------------|-------------------------|
| 1    | 1       | 101      | 1  |    |    |    |    |    | 7   | 8   |     | M30            | F30            | F0♦            | 1                       | 1                       | 1                       |
| 1    | 2       | 102      | 1  |    |    |    |    |    | 7   | 8   |     | M30            | F30            | F0♦            | 0.5                     | 0.5                     | 0.5                     |
| 1    | 3       | 103      |    |    | 3  |    |    |    | 6   |     |     | 9              | P30            | P0             | 0.5                     | 0.5                     | 0.5                     |
| 1    | 4       | 104      |    | 2  |    | 4  | 5  |    |     |     |     | F5             | M5             | M0             | 0.5                     | 0.5                     | 0.5                     |
| 1    | 5       | 105      |    | 2  |    | 4  | 5  |    |     |     |     | F5             | M5             | M0             | 1                       | 1                       | 1                       |
| 1    | 6       | 106      |    |    | 3  |    |    |    | 6   |     |     | 9              | P30            | P0             | 1                       | 1                       | 1                       |
| 2    | 1       | 201      |    |    |    | 4  |    |    | 7   |     | 9   | F30♦          | F5             | P30            | 0.5                     | 0.5                     | 0.5                     |
| 2    | 2       | 202      |    |    | 3  |    | 5  |    |     | 8   |     | P0             | M5             | M30            | 0.5                     | 0.5                     | 0.5                     |
| 3    | 1       | 301      |    | 2  | 3  |    |    |    | 7   |     |     | M0             | P0             | F30            | 0.5                     | 0.5                     | 0.5                     |
| 3    | 2       | 302      |    |    |    | 4  |    | 6  |     |     |     | F5             | P5             | P30            | 0.5                     | 0.5                     | 0.5                     |
| 3    | 3       | 303      | 1  |    |    |    | 5  |    |     |     | 8   | M5             | F0             | M30            | 0.5                     | 0.5                     | 0.5                     |
| 4    | 1       | 401      |    |    |    | 4  |    |    |     | 8   | 9   | P30            | M30            | F5             | 0.5                     | 0.5                     | 0.5                     |
| 4    | 2       | 402      | 1  | 2  | 3  |    |    |    |     |     |     | P0             | F0             | M0             | 1                       | 1                       | 1                       |
| 4    | 3       | 403      |    |    |    |    | 5  | 6  | 7   |     |     | F30            | M5             | P5             | 1                       | 1                       | 1                       |
| 5    | 1       | 501      |    |    | 3  |    | 5  | 6  |     |     |     | M5             | P0             | P5             | 0.5                     | 1                       | 1                       |
| 5    | 4       | 504      |    | 2  |    |    |    |    |     | 8   | 9   | P30            | M30            | M0             | 1                       | 1                       | 1                       |
| 5    | 5       | 505      | 1  |    |    | 4  |    |    | 7   |     |     | F30            | F0             | F5             | 1                       | 1                       | 0.5                     |
| 6    | 1       | 601      | 1  |    |    | 4  |    | 6  |     |     |     | F0             | F5             | P5             | 1                       | 0.5                     | 1                       |
| 6    | 2       | 602      |    |    |    |    |    |    | 7   | 8   | 9   | F30            | M30            | P30            | 0.5                     | 1                       | 1                       |
| 6    | 3       | 603      |    | 2  | 3  |    | 5  |    |     |     |     | P0             | M5             | M0             | 1                       | 1                       | 1                       |
| 7    | 1       | 701      |    |    |    | 4  | 5  | 6  |     |     |     | P5             | F5             | M5             | 0.5                     | 0.5                     | 0.5                     |
| 7    | 2       | 702      | 1  | 2  | 3  |    |    |    |     |     |     | M0             | P0             | F0             | 0.5                     | 0.5                     |


