# Overview
**Title:**
RLSynC: Offline-Online Reinforcement Learning for Synthon Completion

**Authors:**
Baker, F.N., Chen, Z., Adu-Ampratwum, D., and Ning, X. |
Baker, F.N. et al.

**Publication Date:**
2024/08/18

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.4c00554)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2309.02671) |
[GitHub](https://github.com/ninglab/RLSynC) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC11388466/) |
[ResearchGate](https://www.researchgate.net/publication/383214478_RLSynC_Offline-Online_Reinforcement_Learning_for_Synthon_Completion)

**Starred:**
False

**Tags:**
single-step-retrosynthesis, semi-template-based, rl-sync


# Abstract
Retrosynthesis is the process of determining the set of reactant molecules that can react to form a desired product.
Semitemplate-based retrosynthesis methods, which imitate the reverse logic of synthesis reactions, first predict the reaction centers in the products and then complete the resulting synthons back into reactants.
We develop a new offline–online reinforcement learning method RLSynC for synthon completion in semitemplate-based methods.
RLSynC assigns one agent to each synthon, all of which complete the synthons by conducting actions step by step in a synchronized fashion.
RLSynC learns the policy from both offline training episodes and online interactions, which allows RLSynC to explore new reaction spaces.
RLSynC uses a standalone forward synthesis model to evaluate the likelihood of the predicted reactants in synthesizing a product and thus guides the action search.
Our results demonstrate that RLSynC can outperform state-of-the-art synthon completion methods with improvements as high as 14.9%, highlighting its potential in synthesis planning.


# Citation
```
@article {baker2024a,
  author       = { Frazier N. Baker and Ziqi Chen and Daniel Adu-Ampratwum and Xia Ning },
  title        = { RLSynC: Offline–Online Reinforcement Learning for Synthon Completion },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2024 },
  note         = { PMID: 39154287 },
  pages        = { 6723-6735 },
  volume       = { 64 },
  number       = { 17 },
  doi          = { 10.1021/acs.jcim.4c00554 },
  url          = { https://doi.org/10.1021/acs.jcim.4c00554 },
  eprint       = { https://doi.org/10.1021/acs.jcim.4c00554 }
}
```
