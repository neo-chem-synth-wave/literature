# Overview
**Title:**
Deep Retrosynthetic Reaction Prediction Using Local Reactivity and Global Attention

**Authors:**
Chen, S. and Jung, Y.

**Publication Date:**
2021/08/05

**Link:**
[ACS JACS Au](https://pubs.acs.org/doi/10.1021/jacsau.1c00246)

**Alternative Links:**
[GitHub](https://github.com/kaist-amsg/LocalRetro) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC8549044) |
[ResearchGate](https://www.researchgate.net/publication/353723283_Deep_Retrosynthetic_Reaction_Prediction_using_Local_Reactivity_and_Global_Attention)

**Starred:**
False

**Tags:**
single-step-retrosynthesis, template-based, graph, local-retro


# Abstract
As a fundamental problem in chemistry, retrosynthesis aims at designing reaction pathways and intermediates for a target compound.
The goal of artificial intelligence (AI)-aided retrosynthesis is to automate this process by learning from the previous chemical reactions to make new predictions.
Although several models have demonstrated their potentials for automated retrosynthesis, there is still a significant need to further enhance the prediction accuracy to a more practical level.
Here we propose a local retrosynthesis framework called LocalRetro, motivated by the chemical intuition that the molecular changes occur mostly locally during the chemical reactions.
This differs from nearly all existing retrosynthesis methods that suggest reactants based on the global structures of the molecules, often containing fine details not directly relevant to the reactions.
This local concept yields local reaction templates involving the atom and bond edits.
Because the remote functional groups can also affect the overall reaction path as a secondary aspect, the proposed locally encoded retrosynthesis model is then further refined to account for the nonlocal effects of chemical reaction through a global attention mechanism.
Our model shows a promising 89.5 and 99.2% round-trip accuracy at top-1 and top-5 predictions for the USPTO-50K dataset containing 50,016 reactions.
We further demonstrate the validity of LocalRetro on a large dataset containing 479,035 reactions (USPTO-MIT) with comparable round-trip top-1 and top-5 accuracy of 87.0 and 97.4%, respectively.
The practical application of the model is also demonstrated by correctly predicting the synthesis pathways of five drug candidate molecules from various literature.


# Citation
```
@article {chen2021a,
  author       = { Shuan Chen and Yousung Jung },
  title        = { Deep Retrosynthetic Reaction Prediction using Local Reactivity and Global Attention },
  journal      = { JACS Au },
  year         = { 2021 },
  note         = { PMID: 34723264 },
  pages        = { 1612-1620 },
  volume       = { 1 },
  number       = { 10 },
  doi          = { 10.1021/jacsau.1c00246 },
  url          = { https://doi.org/10.1021/jacsau.1c00246 },
  eprint       = { https://doi.org/10.1021/jacsau.1c00246 }
}
```
