# Overview
**Title:**
Accelerating the Inference of String Generation-Based Chemical Reaction Models for Industrial Applications

**Authors:**
Andronov, M., Andronova, N., Wand, M., Schmidhuber, J., and Clevert, D. |
Andronov, M. et al.

**Publication Date:**
2025/03/10

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-025-00974-w)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2407.09685) |
[GitHub](https://github.com/Academich/translation-transformer) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC11895308)

**Tags:**
optimization


# Abstract
Transformer-based, template-free SMILES-to-SMILES translation models for reaction prediction and single-step retrosynthesis are of interest to computer-aided synthesis planning systems, as they offer state-of-the-art accuracy.
However, their slow inference speed limits their practical utility in such applications.
To address this challenge, we propose speculative decoding with a simple chemically specific drafting strategy and apply it to the Molecular Transformer, an encoder-decoder transformer for conditional SMILES generation.
Our approach achieves over 3X faster inference in reaction product prediction and single-step retrosynthesis with no loss in accuracy, increasing the potential of the transformer as the backbone of synthesis planning systems.
To accelerate the simultaneous generation of multiple precursor SMILES for a given query SMILES in single-step retrosynthesis, we introduce Speculative Beam Search, a novel algorithm tackling the challenge of beam search acceleration with speculative decoding.
Our methods aim to improve transformer-based models’ scalability and industrial applicability in synthesis planning.


# Citation
```
@article {20250310_andronov_m_et_al,
  author       = { Mikhail Andronov and Natalia Andronova and Michael Wand and Jürgen Schmidhuber and Djork-Arné Clevert },
  title        = { Accelerating the inference of string generation-based chemical reaction models for industrial applications },
  journal      = { Journal of Cheminformatics },
  year         = { 2025 },
  pages        = { 31 },
  month        = { Mar },
  volume       = { 17 },
  number       = { 1 },
  day          = { 10 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-025-00974-w },
  url          = { https://doi.org/10.1186/s13321-025-00974-w }
}
```
