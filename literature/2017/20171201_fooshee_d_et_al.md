# Overview
**Title:**
Deep Learning for Chemical Reaction Prediction

**Authors:**
Fooshee, D., Mood, A., Gutman, E., Tavakoli, M., Urban, G., Liu, F., Huynh, N., Vranken, D.V., and Baldi, P. |
Fooshee, D. et al.

**Publication Date:**
2017/12/01

**Link:**
[RSC Molecular Systems Design & Engineering](https://pubs.rsc.org/en/content/articlelanding/2018/me/c7me00107j)

**Alternative Links:**
None

**Tags:**
single-step-synthesis


# Abstract
Reaction predictor is an application for predicting chemical reactions and reaction pathways.
It uses deep learning to predict and rank elementary reactions by first identifying electron sources and sinks, pairing those sources and sinks to propose elementary reactions, and finally ranking the reactions by favorability.
Global reactions can be identified by chaining together these elementary reaction predictions.
We carefully curated a data set consisting of over 11,000 elementary reactions, covering a broad range of advanced organic chemistry.
Using this data for training, we demonstrate an 80% top-5 recovery rate on a separate, challenging benchmark set of reactions drawn from modern organic chemistry literature.
A fundamental problem of synthetic chemistry is the identification of unknown products observed via mass spectrometry.
Reaction predictor includes a pathway search feature that can help identify such products through multi-target mass search.
Finally, we discuss an alternative approach to predicting electron sources and sinks using recurrent neural networks, specifically long short-term memory (LSTM) architectures, operating directly on SMILES strings.
This approach has shown promising preliminary results.


# Citation
```
@article {20171201_fooshee_d_et_al,
  author       = { David Fooshee and Aaron Mood and Eugene Gutman and Mohammadamin Tavakoli and Gregor Urban and Frances Liu and Nancy Huynh and David Van Vranken and Pierre Baldi },
  title        = { Deep learning for chemical reaction prediction },
  journal      = { Mol. Syst. Des. Eng. },
  year         = { 2018 },
  pages        = { 442-452 },
  volume       = { 3 },
  issue        = { 3 },
  publisher    = { The Royal Society of Chemistry },
  doi          = { 10.1039/C7ME00107J },
  url          = { https://dx.doi.org/10.1039/C7ME00107J }}
```
