<h1 align="center">EEG Prediction from Transcranial Electrical Stimulation(tES) using Chaos Theory, Dynamical Systems Theory, a Recurrent Neural Net(RNN), and a Convolutional Neural Net(CNN)</h1>
---
<a href="https://discord.gg/HBHGvDxDmt">
  <img src="https://logodownload.org/wp-content/uploads/2017/11/discord-logo-0.png" alt="Discord logo" width="20" height="20">
  Join our Discord server
</a>


---
<h1 align="center">Purpose</h1>
---
We want to take the necessary steps towards connecting the human brain to a silicon computer or hybrid bio-silicon computer, via a biomatter brain-computer-interface. Part of this process includes the input of information directly into the human brain. Immediate readings of EEG data during the inputting of information into the human brain will need to be compared to a baseline of the real experience. An example of this is the [initial state EEG data of a human], the [EEG data state during, and immediately after, viewing a sequence of events in VR], and the [initial state EEG data of that same human], the [EEG data state during, and immediately after, having the visual data input into their brain].
---
<h1 align="center">Explanation</h1>
---
The central aim of this research project is to predict the electroencephalographic (EEG) effects of transcranial electrical stimulation (tES) by integrating chaos theory, dynamical systems theory, and a neural net stack. This is due to the importance of nonlinear dynamics in understanding brain activity.

This research has significant potential implications for the field of brain-computer interfaces, particularly for the novel area of connecting a human brain to a biohybrid silicon/biological computer[21] through a biological neural interface[22].

Accurately predicting the brain's reactions to tES could enable us to fine-tune the stimulation parameters, optimizing the quality of communication between the human brain and the hybrid computer. This could pave the way for developing protocols that ensure efficient and reliable transmission of information along the biomatter cable, essentially turning thoughts and brain activity into actionable commands for the hybrid computer.

This research could potentially contribute to the ambitious goal of directly stimulating sensorial perceptions in the human brain[23][24], a feat which, if achieved, would revolutionize neuroprosthetics and human-computer interfaces. The brain's sensorial system is intricate, involving a complex network of interconnected regions responsible for processing and interpreting different aspects of sensory information. The endeavor to predict EEG effects of tES using a multidisciplinary approach could shed light on how this complex system responds to external stimulation, and could possibly inform targeted, controlled stimulation techniques. While the research is not directly aimed at inducing visual perceptions, the insights and methodologies derived from the work could serve as a stepping stone towards understanding how to interface with the brain's sensory nervous system more effectively. It's crucial to note that this potential application would need to address substantial scientific, technical, and ethical challenges. Despite these hurdles, the promise of such a breakthrough underscores the broad-reaching implications of our research and its potential to catalyze advances in several areas of neuroscience and neurotechnology.

This research could contribute significantly to the field of decoding and encoding sensory perceptions in the human brain. The proposed model, which integrates chaos theory, dynamical systems theory and a neural network stack, could provide a robust and comprehensive tool for understanding how the brain responds to tES. Such an understanding is critical for decoding brain activity associated with sensual perception. Specifically, the proposed use of transfer entropy to measure causal relationships within the brain could provide unique insights into how different sensory regions interact and coordinate to produce perceptions. Once these perceptions are decoded[25], it becomes theoretically possible to encode similar patterns back into the brain. The development of a predictive model capable of accurately capturing these dynamics would be a pivotal step towards this goal. Thus, while the immediate focus of the research is predicting EEG effects of tES, the methodologies and insights derived from the work have broader implications and could be foundational for future efforts aimed at decoding and encoding sensual perceptions in the brain.
---
<h1 align="center">Data Source and Article</h1>
---
Data include within participant application of nine High-Definition tES (HD-tES) types, targeting three cortical regions (frontal, motor, parietal) with three stimulation waveforms (DC, 5 Hz, 30 Hz); more than 783 total stimulation trials over 62 sessions with EEG, physiological (ECG, EOG), and continuous behavioral vigilance/alertness metrics. Experiment 1 and 2 consisted of participants performing a continuous vigilance/alertness task over three 70-minute and two 70.5-minute sessions, respectively. Demographic data were collected, as well as self-reported wellness questionnaires before and after each session. Participants received all 9 stimulation types in Experiment 1, with each session including three stimulation types, with 4 trials per type. Participants received 2 stimulation types in Experiment 2, with 20 trials of a given stimulation type per session. Within-participant reliability was tested by repeating select sessions. This unique dataset supports a range of hypothesis testing including interactions of tDCS/tACS location and frequency, brain-state, physiology, fatigue, and cognitive performance.

Participants maintained a ball at the center of the screen and were periodically stimulated (with low-intensity noninvasive brain stimulation) for 30 secs with combinations of 9 stimulation montages.
---
**Article:** <a href="https://doi.org/10.1038/s41597-021-01046-y" style="color: red;">https://doi.org/10.1038/s41597-021-01046-y</a>
---
**Dataset:** <a href="https://zenodo.org/record/3840615#.ZK2hJdLMKRQ" style="color: red;">https://zenodo.org/record/3840615#.ZK2hJdLMKRQ</a>
---
**Table of stimulation condition and stimulation intensity:** <a href="https://www.nature.com/articles/s41597-021-01046-y/tables/2" style="color: red;">https://www.nature.com/articles/s41597-021-01046-y/tables/2</a>
---
<h1 align="center">Variables</h1>
---
| Variable       | Description                                                         |
|----------------|---------------------------------------------------------------------|
| DSamp          |                                                                     |
| triggers       | These are all the labeled EEG/Stimulation start/stop triggers       |
| EEGdata        | Contains the downsampled EEG/ECG/EOG voltage data dims: 35 channels X ~4E6 samples |
| fs             | The downsampled sampling frequency of the data: 1000 Hz             |
| fsOld          | The original sampling frequency of the data                         |
| time           | Time vector for the data. Should be 1 X ~4E6                        |
| label          | Contains the channel label information. BIP1= ECG, BIP2=EOG, RESP1= N/A |
| nchan          | The number of channels in the data                                  |
| rate           | Redundant to fs, sampling rate of data                              |
| npt            | Number of data points ~4E6                                          |
| Subj           | Subject and session that data belong to. I.e. 0302 - Subject 03 session 03 |
| ptrackerPerf   | The CTT data deviation/ the behavioral data                         |
| ptrackerTime   | Time vector for the CTT data                                        |
| ptrackerfs     | The sampling frequency for the CTT data: 100 Hz                     |

