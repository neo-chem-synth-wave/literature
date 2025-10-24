# Overview
**Title:**
Molecule Edit Graph Attention Network: Modeling Chemical Reactions as Sequences of Graph Edits

**Authors:**
Sacha, M., Błaż, M., Byrski, P., Dąbrowski-Tumański, P., Chromiński, M., Loska, R., Włodarczyk-Pruszyński, P., and Jastrzębski, S. |
Sacha, M. et al.

**Publication Date:**
2021/07/12

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.1c00537)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2006.15426v2) |
[GitHub](https://github.com/molecule-one/megan)

**Tags:**
single-step-retrosynthesis, template-free, graph, megan


# Abstract
The central challenge in automated synthesis planning is to be able to generate and predict outcomes of a diverse set of chemical reactions.
In particular, in many cases, the most likely synthesis pathway cannot be applied due to additional constraints, which requires proposing alternative chemical reactions.
With this in mind, we present Molecule Edit Graph Attention Network (MEGAN), an end-to-end encoder–decoder neural model.
MEGAN is inspired by models that express a chemical reaction as a sequence of graph edits, akin to the arrow pushing formalism.
We extend this model to retrosynthesis prediction (predicting substrates given the product of a chemical reaction) and scale it up to large data sets.
We argue that representing the reaction as a sequence of edits enables MEGAN to efficiently explore the space of plausible chemical reactions, maintaining the flexibility of modeling the reaction in an end-to-end fashion and achieving state-of-the-art accuracy in standard benchmarks.
Code and trained models are made available online at https://github.com/molecule-one/megan.


# Citation
```
@article {20210712_sacha_m_et_al,
  author       = { Mikołaj Sacha and Mikołaj Błaż and Piotr Byrski and Paweł Dąbrowski-Tumański and Mikołaj Chromiński and Rafał Loska and Paweł Włodarczyk-Pruszyński and Stanisław Jastrzębski },
  title        = { Molecule Edit Graph Attention Network: Modeling Chemical Reactions as Sequences of Graph Edits },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2021 },
  note         = { PMID: 34251814 },
  pages        = { 3273-3284 },
  volume       = { 61 },
  number       = { 7 },
  doi          = { 10.1021/acs.jcim.1c00537 },
  url          = { https://doi.org/10.1021/acs.jcim.1c00537 },
  eprint       = { https://doi.org/10.1021/acs.jcim.1c00537 }
}
```
