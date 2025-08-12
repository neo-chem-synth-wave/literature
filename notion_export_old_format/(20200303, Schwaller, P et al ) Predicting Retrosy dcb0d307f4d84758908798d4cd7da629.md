# (20200303, Schwaller, P. et al.) Predicting Retrosynthetic Pathways using Transformer-based Models and a Hyper-graph Exploration Strategy

Tags: single-step-retrosynthesis, synthesis-route-planning, template-free

## Publication Overview

| **Title:**  | Predicting Retrosynthetic Pathways using Transformer-based Models and a Hyper-graph
Exploration Strategy |
| --- | --- |
| **Authors:**  | Philippe Schwaller, Riccardo Petraglia, Valerio Zullo, Vishnu H. Nair, Rico A. Haeuselmann,
Riccardo Pisoni, Costas Bekas, Anna Iuliano, Teodoro Laino |
| Publication Date**:**  | 2020/03/03 |
| Publication Links: | [**RSC Chemical Science**](https://pubs.rsc.org/en/content/articlelanding/2020/sc/c9sc05704h) |
| Alternative Links: | [**arXiv](https://arxiv.org/abs/1910.08036) | [ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c7453df96a0026a5286b6a)** |
| Code Links: | [**Official GitHub Repository**](https://github.com/pschwllr/MolecularTransformer) |

## Publication Abstract

<aside>
ℹ️ We present an extension of our Molecular Transformer model combined with a hyper-graph exploration strategy for automatic retrosynthesis route planning without human intervention. The single-step retrosynthetic model sets a new state of the art for predicting reactants as well as reagents, solvents and catalysts for each retrosynthetic step. We introduce four metrics (coverage, class diversity, round-trip accuracy and Jensen-Shannon divergence) to evaluate the single-step retrosynthetic models, using the forward prediction and a reaction classification model always based on the transformer architecture. The hypergraph is constructed on the fly, and the nodes are filtered and further expanded based on a Bayesian-like probability. We critically assessed the end-to-end framework with several retrosynthesis examples from literature and academic exams. Overall, the frameworks have an excellent performance with few weaknesses related to the training data. The use of the introduced metrics opens up the possibility to optimize entire retrosynthetic frameworks by focusing on the performance of the single-step model only.

</aside>