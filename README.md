# Cooperative-Imitation-Learning-CIL
Dynamic Treatment Regimes (DTRs) are sets of sequential decision rules that can be adapted over time to treat patients with a specific pathology. DTR consists of alternative treatment paths and any of these treatments can be adapted depending on the patient’s characteristics. Reinforcement Learning (RL) and Imitation Learning (IL) approaches have been deployed for obtaining optimal treatment for a patient but, these approaches rely only on positive trajectories (i.e., treatments that concluded with positive responses of the patient). In contrast, negative trajectories (i.e., samples of non-responding treatments) are discarded, although these have valuable information content.
We propose a Cooperative Imitation Learning (CIL) method that exploits information from both negative and positive trajectories to learn the optimal DTR. The proposed method reduces the chance of selecting any treatment which results in a negative outcome (negative response of the patient) during the medical examination.
To validate our approach, we have considered a well-known DTR which is defined for the treatment of patients with alcohol addiction. Results show that our approach outperforms those that rely only on positive trajectories.

## Installation 
The Code is written in MATLAB R2015b. If you don't have MATLAB installed you can find it [here](https://se.mathworks.com/store/?ef_id=Cj0KCQjwof6WBhD4ARIsAOi65ahm5EmvYkeZrBV4inHO6ap_WU7FS2A51nQBeZsW1OREpax5dJAnWJQaAmRcEALw_wcB:G:s&s_kwcid=AL!8664!3!552213010978!p!!g!!get%20matlab&s_eid=ppc_69452703753&q=get%20matlab&gclid=Cj0KCQjwof6WBhD4ARIsAOi65ahm5EmvYkeZrBV4inHO6ap_WU7FS2A51nQBeZsW1OREpax5dJAnWJQaAmRcEALw_wcB). If you are using an updated version of MATLAB you may need to modify the code accordingly. ## Disscussion
### (i) System Model

The AMC module consists of three stages: \
(i) Feature Extractor, \
(ii) Heuristic Optimizer \
(iii) ELM Classifier \
 A random signal x (n)  is generated on the transmission side; after modulation, it is passed through some pre-defined channel (AWGN/ Rayleigh) with some pre-specified SNR value. The signal sensed on the receiving side represented as r(n).   
 The transmitter encodes sequences of randomly generated bits into continuous signal patterns by selecting the appropriate symbol glossaries. Through transmission from the considered channel at some pre-specified SNR values, signal is corrupted due to noise.  At the receiver side, noise components from the received signal are removed at the first step in the pre-processing stage; then the signal is fed to the AMC module for further processing. 

![Prediction](Images/AMC_System_model.png)

The first stage in the AMC module is feature extraction where Gabor filter is used to extract the different features for classification of considered digitally modulated schemes. \
The Gabor features extracted in the previous step is further optimized through Cuckoo Search Algorithm (CSA). \
In the final step Extreme Learing Machine is used to classify the the modulation schemes. 
### (ii) Flow Chart
![Prediction](Images/FlowChart%20Diagram.png.png)

The flow diagram in above figure depicts the step-wise methodology of the algorithm. The working of three core modules, i.e., Gabor, CSA, and ELM of the proposed system can be seen in parallel to each other. Gabor feature extraction module extracts Gabor features ( c , σ , f , w) from randomly generated signal passed through either of the two channels. \
The extracted Gabor features are distinct but to achieve better classification accuracy, they are further optimized using CSA using the fitness function. The best solution having max fitness is then fed to ELM classifier. The ELM classifier (already trained according to reference values) then makes a decision using about the modulation classification.
### (iii) Results

![Prediction](Images/Table.png)

Table displays the percentage classification accuracy (PCA) of our proposed CSA-ELM classifier for different variants of PSK, FSK and QAM 
considering samples sizes (512, 1024) at 0 dB SNR for Rayleigh channel. Here we have considered the 
1000 trails of ELM, and calculated results have been shown in the respective tables. Almost all the modulations schemes are classified with an accuracy of ~99 % at 512 samples, which becomes ~ 100% for 1024 sample size. 




## Future Scope

- Other features such as Cyclostationary and Spectral features can further be explored. 
- Similarly, Deep learning approach instead of ELM can be used 
- New bio-inspired heuristic techniques such as Cat swarm optimization, Bat optimization, firefly optimization can also be utilized to enhance the accuracy at low snr values.


## Deployment

To deploy this project run

```bash
   install MATLAB
```
## Acknowledgements

 - [Article](https://ieeexplore.ieee.org/abstract/document/8754798)
