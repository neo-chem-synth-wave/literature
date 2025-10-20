# Overview
**Title:**
Learning Retrosynthetic Planning Through Simulated Experience

**Authors:**
Schreck, J.S., Coley, C.W., and Bishop, K.J.M. |
Schreck, J.S. et al.

**Publication Date:**
2019/05/31

**Link:**
[ACS Central Science](https://pubs.acs.org/doi/10.1021/acscentsci.9b00055)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/1901.06569) |
[GitHub](https://github.com/jsschreck/retroRL) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC6598174) |
[ResearchGate](https://www.researchgate.net/publication/333529497_Learning_Retrosynthetic_Planning_through_Simulated_Experience)

**Tags:**
multi-step-synthesis


# Abstract
The problem of retrosynthetic planning can be framed as a one-player game, in which the chemist (or a computer program) works backward from a molecular target to simpler starting materials through a series of choices regarding which reactions to perform.
This game is challenging as the combinatorial space of possible choices is astronomical, and the value of each choice remains uncertain until the synthesis plan is completed and its cost evaluated.
Here, we address this search problem using deep reinforcement learning to identify policies that make (near) optimal reaction choices during each step of retrosynthetic planning according to a user-defined cost metric.
Using a simulated experience, we train a neural network to estimate the expected synthesis cost or value of any given molecule based on a representation of its molecular structure.
We show that learned policies based on this value network can outperform a heuristic approach that favors symmetric disconnections when synthesizing unfamiliar molecules from available starting materials using the fewest number of reactions.
We discuss how the learned policies described here can be incorporated into existing synthesis planning tools and how they can be adapted to changes in the synthesis cost objective or material availability.


# Citation
```
@article {20190531_schreck_j_s_et_al,
  author       = { John S. Schreck and Connor W. Coley and Kyle J. M. Bishop },
  title        = { Learning Retrosynthetic Planning through Simulated Experience },
  journal      = { ACS Central Science },
  year         = { 2019 },
  note         = { PMID: 31263756 },
  pages        = { 970-981 },
  volume       = { 5 },
  number       = { 6 },
  doi          = { 10.1021/acscentsci.9b00055 },
  url          = { https://doi.org/10.1021/acscentsci.9b00055 },
  eprint       = { https://doi.org/10.1021/acscentsci.9b00055 }
}
```
