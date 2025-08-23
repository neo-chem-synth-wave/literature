# Overview
**Title:**
Enhancing Monte Carlo Tree Search for Retrosynthesis

**Authors:**
Blackshaw, T.M., Davies, J.C., Spoerer, K.T., and Hirst, J.D. |
Blackshaw, T.M. et al.

**Publication Date:**
2025/06/13

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.5c00417)

**Alternative Links:**
[AI4Green](https://ai4green.app) |
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/67b879d4fa469535b94e1ae5) |
[GitHub](https://github.com/AI4Green/AI4Green) |
[GitHub (API)](https://github.com/AI4Green/retrosynthesis-api)

**Starred:**
False

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, duct, ai4green


# Abstract
Computer-Assisted Synthesis Programs are increasingly employed by organic chemists.
Often, these tools combine neural networks for policy prediction with heuristic search algorithms.
We propose two novel enhancements, which we call eUCT and dUCT, to the Monte Carlo tree search (MCTS) algorithm.
The enhancements were deployed in AiZynthFinder and have been integrated into the open-source electronic lab notebook, AI4Green, available at https://ai4green.app.
A memory-efficient stock file was used to reduce the computational carbon footprint.
Both enhancements significantly reduced, by up to 50%, the computational clock-time to solve 1500 heavy (500–800 Da) molecules.
The dUCT enhancement increased the number of routes found per molecule for the 1500 heavy molecules and a 50,000-molecule set from ChEMBL.
eUCT and dUCT-v2 solved between 600 and 900 more molecules than the unenhanced MCTS algorithm across the 50,000 molecules.
When limited to a 150 s time constraint, dUCT-v1 solved ∼5 million more routes to the 50,000 targets than the unenhanced algorithm.


# Citation
```
@article {blackshaw2025a,
  author       = { Ton M. Blackshaw and Joseph C. Davies and Kristian T. Spoerer and Jonathan D. Hirst },
  title        = { Enhancing Monte Carlo Tree Search for Retrosynthesis },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2025 },
  note         = { PMID: 40512567 },
  pages        = { 6537-6546 },
  volume       = { 65 },
  number       = { 13 },
  doi          = { 10.1021/acs.jcim.5c00417 },
  url          = { https://doi.org/10.1021/acs.jcim.5c00417 },
  eprint       = { https://doi.org/10.1021/acs.jcim.5c00417 }
}
```
