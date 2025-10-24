# Overview
**Title:**
Quantum Mechanics and Machine Learning Synergies: Graph Attention Neural Networks to Predict Chemical Reactivity

**Authors:**
Tavakoli, M., Mood, A., Vranken, D.V., and Baldi, P. |
Tavakoli, M. et al.

**Publication Date:**
2022/01/12

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.1c01400)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2103.14536) |
[ResearchGate](https://www.researchgate.net/publication/350457036_Quantum_Mechanics_and_Machine_Learning_Synergies_Graph_Attention_Neural_Networks_to_Predict_Chemical_Reactivity)

**Tags:**
single-step-synthesis


# Abstract
There is a lack of scalable quantitative measures of reactivity that cover the full range of functional groups in organic chemistry, ranging from highly unreactive C–C bonds to highly reactive naked ions.
Measuring reactivity experimentally is costly and time-consuming, and no single method has sufficient dynamic range to cover the astronomical size of chemical reactivity space.
In previous quantum chemistry studies, we have introduced Methyl Cation Affinities (MCA*) and Methyl Anion Affinities (MAA*), using a solvation model, as quantitative measures of reactivity for organic functional groups over the broadest range.
Although MCA* and MAA* offer good estimates of reactivity parameters, their calculation through Density Functional Theory (DFT) simulations is time-consuming.
To circumvent this problem, we first use DFT to calculate MCA* and MAA* for more than 2,400 organic molecules thereby establishing a large data set of chemical reactivity scores.
We then design deep learning methods to predict the reactivity of molecular structures and train them using this curated data set in combination with different representations of molecular structures.
Using 10-fold cross-validation, we show that graph attention neural networks applied to a relational model of molecular structures produce the most accurate estimates of reactivity, achieving over 91% test accuracy for predicting the MCA* ± 3.0 or MAA* ± 3.0, over 50 orders of magnitude.
Finally, we demonstrate the application of these reactivity scores to two tasks: (1) chemical reaction prediction and (2) combinatorial generation of reaction mechanisms.
The curated data sets of MCA* and MAA* scores is available through the ChemDB chemoinformatics web portal at cdb.ics.uci.edu under Chemical Reactivities data sets.


# Citation
```
@article {20220112_tavakoli_m_et_al,
  author       = { Mohammadamin Tavakoli and Aaron Mood and David Van Vranken and Pierre Baldi },
  title        = { Quantum Mechanics and Machine Learning Synergies: Graph Attention Neural Networks to Predict Chemical Reactivity },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2022 },
  note         = { PMID: 35020394 },
  pages        = { 2121-2132 },
  volume       = { 62 },
  number       = { 9 },
  doi          = { 10.1021/acs.jcim.1c01400 },
  url          = { https://doi.org/10.1021/acs.jcim.1c01400 },
  eprint       = { https://doi.org/10.1021/acs.jcim.1c01400 }
}
```
