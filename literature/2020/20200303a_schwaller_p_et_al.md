# Overview
**Title:**
Predicting Retrosynthetic Pathways Using Transformer-Based Models and a Hyper-Graph Exploration Strategy

**Authors:**
Schwaller, P., Petraglia, R., Zullo, V., Nair, V.H., Haeuselmann, R.A., Pisoni, R., Bekas, C., Iuliano, A., and Laino, T. |
Schwaller, P. et al.

**Publication Date:**
2020/03/03

**Publication Link:**
[RSC Chemical Science](https://pubs.rsc.org/en/content/articlelanding/2020/sc/c9sc05704h)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/1910.08036) |
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c7453df96a0026a5286b6a) |
[GitHub](https://github.com/pschwllr/MolecularTransformer) |
[ResearchGate](https://www.researchgate.net/publication/339673653_Predicting_Retrosynthetic_Pathways_using_Transformer-Based_Models_and_a_Hyper-Graph_Exploration_Strategy)

**Tags:**
single-step-retrosynthesis, template-free


# Abstract
We present an extension of our Molecular Transformer model combined with a hyper-graph exploration strategy for automatic retrosynthesis route planning without human intervention.
The single-step retrosynthetic model sets a new state of the art for predicting reactants as well as reagents, solvents and catalysts for each retrosynthetic step.
We introduce four metrics (coverage, class diversity, round-trip accuracy and Jensen–Shannon divergence) to evaluate the single-step retrosynthetic models, using the forward prediction and a reaction classification model always based on the transformer architecture.
The hypergraph is constructed on the fly, and the nodes are filtered and further expanded based on a Bayesian-like probability.
We critically assessed the end-to-end framework with several retrosynthesis examples from literature and academic exams.
Overall, the frameworks have an excellent performance with few weaknesses related to the training data.
The use of the introduced metrics opens up the possibility to optimize entire retrosynthetic frameworks by focusing on the performance of the single-step model only.


# Citation
```
@article {20200303a_schwaller_p_et_al,
  author       = { Philippe Schwaller and Riccardo Petraglia and Valerio Zullo and Vishnu H. Nair and Rico Andreas Haeuselmann and Riccardo Pisoni and Costas Bekas and Anna Iuliano and Teodoro Laino },
  title        = { Predicting retrosynthetic pathways using transformer-based models and a hyper-graph exploration strategy },
  journal      = { Chem. Sci. },
  year         = { 2020 },
  pages        = { 3316-3325 },
  volume       = { 11 },
  issue        = { 12 },
  publisher    = { The Royal Society of Chemistry },
  doi          = { 10.1039/C9SC05704H },
  url          = { https://dx.doi.org/10.1039/C9SC05704H }
}
```
