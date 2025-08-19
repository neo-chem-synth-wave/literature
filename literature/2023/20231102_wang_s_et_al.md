# Overview
**Title:**
DeepSA: A Deep-Learning Driven Predictor of Compound Synthesis Accessibility

**Authors:**
Wang, S., Wang, L., Li, F., and Bai, F. |
Wang, S. et al.

**Publication Date:**
2023/11/02

**Link:**
[BMC Journal of Chemoinformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-023-00771-3)

**Alternative Links:**
[GitHub](https://github.com/Shihang-Wang-58/DeepSA) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC10621138) |
[ResearchGate](https://www.researchgate.net/publication/375235649_DeepSA_a_deep-learning_driven_predictor_of_compound_synthesis_accessibility)

**Starred:**
False

**Tags:**
synthesizability, synthetic-accessibility, deep-sa


# Abstract
With the continuous development of artificial intelligence technology, more and more computational models for generating new molecules are being developed.
However, we are often confronted with the question of whether these compounds are easy or difficult to synthesize, which refers to synthetic accessibility of compounds.
In this study, a deep learning based computational model called DeepSA, was proposed to predict the synthesis accessibility of compounds, which provides a useful tool to choose molecules.
DeepSA is a chemical language model that was developed by training on a dataset of 3,593,053 molecules using various natural language processing (NLP) algorithms, offering advantages over state-of-the-art methods and having a much higher area under the receiver operating characteristic curve (AUROC), i.e., 89.6%, in discriminating those molecules that are difficult to synthesize.
This helps users select less expensive molecules for synthesis, reducing the time and cost required for drug discovery and development.
Interestingly, a comparison of DeepSA with a Graph Attention-based method shows that using SMILES alone can also efficiently visualize and extract compound’s informative features.
DeepSA is available online on the below web server (https://bailab.siais.shanghaitech.edu.cn/services/deepsa/) of our group, and the code is available at https://github.com/Shihang-Wang-58/DeepSA.


# Citation
```
@article {wang2023b,
  author       = { Shihang Wang and Lin Wang and Fenglei Li and Fang Bai },
  title        = { DeepSA: a deep-learning driven predictor of compound synthesis accessibility },
  journal      = { Journal of Cheminformatics },
  year         = { 2023 },
  pages        = { 103 },
  month        = { Nov },
  volume       = { 15 },
  number       = { 1 },
  day          = { 02 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-023-00771-3 },
  url          = { https://doi.org/10.1186/s13321-023-00771-3 }
}
```
