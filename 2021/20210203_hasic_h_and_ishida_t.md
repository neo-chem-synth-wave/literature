# Overview
**Title:**
Single-step Retrosynthesis Prediction based on the Identification of Potential Disconnection Sites using Molecular Substructure Fingerprints

**Authors:**
Hasic, H. and Ishida, T.

**Publication Date:**
2021/02/03

**Publication Link:**
[ACS JCIM](https://pubs.acs.org/doi/10.1021/acs.jcim.0c01100)

**Alternative Publication Links:**
[ResearchGate](https://www.researchgate.net/publication/349040662_Single-Step_Retrosynthesis_Prediction_Based_on_the_Identification_of_Potential_Disconnection_Sites_Using_Molecular_Substructure_Fingerprints) |
[Official GitHub Repository](https://github.com/hasic-haris/one_step_retrosynth_ai)


# Abstract
The proper application of retrosynthesis to identify possible transformations for a given target compound requires a lot of chemistry knowledge and experience. 
However, because the complexity of this technique scales together with the complexity of the target, efficient application on compounds with intricate molecular structures becomes almost impossible for human chemists. 
The idea of using computers in such situations has existed for a long time, but the accuracy was not sufficient for practical applications. 
Nevertheless, with the steady improvement of machine learning and artificial intelligence in recent years, computer-assisted retrosynthesis has been gaining research attention again. 
Because of the overall lack of chemical reaction data, the main challenge for the recent retrosynthesis methods is low exploration ability during the analysis of target and intermediate compounds. 
The main goal of this research is to develop a novel, template-free approach to address this issue. 
Only individual molecular substructures of the target are used to determine potential disconnection sites, without relying on additional information such as chemical reaction class. 
The model for the identification of potential disconnection sites is trained on novel molecular substructure fingerprint representations. 
For each of the disconnections suggested using the model, a simple structural similarity-based reactant retrieval and scoring method is applied, and the suggestions are completed. 
This method achieves 47.2% top-1 accuracy for the single-step retrosynthesis task on the processed United States Patent Office dataset. 
Furthermore, if the predicted reaction class is used to narrow down the reactant candidate search space, the performance is improved to 61.4% top-1 accuracy.


# Citation
```
@article {hasic2021,
  author       = { Haris Hasic and Takashi Ishida },
  title        = { Single-step retrosynthesis prediction based on the identification of potential disconnection sites using molecular substructure fingerprints },
  journal      = { J. Chem. Inf. Model. },
  year         = 2021,
  pages        = { 641--652 },
  month        = feb,
  volume       = 61,
  number       = 2,
  publisher    = { American Chemical Society (ACS) },
  copyright    = { https://creativecommons.org/licenses/by-nc-nd/4.0/ },
  language     = { en }
}
```
