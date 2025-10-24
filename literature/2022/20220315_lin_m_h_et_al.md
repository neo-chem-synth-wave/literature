# Overview
**Title:**
Improving the Performance of Models for One-Step Retrosynthesis Through Re-Ranking

**Authors:**
Lin, M.H., Tu, Z., and Coley, C.W. |
Lin, M.H. et al.

**Publication Date:**
2022/03/15

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-022-00594-8)

**Alternative Links:**
[DSpace@MIT](https://dspace.mit.edu/handle/1721.1/141316) |
[GitHub](https://github.com/coleygroup/rxn-ebm) |
[ResearchGate](https://www.researchgate.net/publication/359248622_Improving_the_performance_of_models_for_one-step_retrosynthesis_through_re-ranking)

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, template-based, optimization


# Abstract
Retrosynthesis is at the core of organic chemistry.
Recently, the rapid growth of artificial intelligence (AI) has spurred a variety of novel machine learning approaches for data-driven synthesis planning.
These methods learn complex patterns from reaction databases in order to predict, for a given product, sets of reactants that can be used to synthesise that product.
However, their performance as measured by the top-N accuracy in matching published reaction precedents still leaves room for improvement.
This work aims to enhance these models by learning to re-rank their reactant predictions.
Specifically, we design and train an energy-based model to re-rank, for each product, the published reaction as the top suggestion and the remaining reactant predictions as lower-ranked.
We show that re-ranking can improve one-step models significantly using the standard USPTO-50k benchmark dataset, such as RetroSim, a similarity-based method, from 35.7 to 51.8% top-1 accuracy and NeuralSym, a deep learning method, from 45.7 to 51.3%, and also that re-ranking the union of two models' suggestions can lead to better performance than either alone.
However, the state-of-the-art top-1 accuracy is not improved by this method.


# Citation
```
@article {20220315_lin_m_h_et_al,
  author       = { Min Htoo Lin and Zhengkai Tu and Connor W. Coley },
  title        = { Improving the performance of models for one-step retrosynthesis through re-ranking },
  journal      = { Journal of Cheminformatics },
  year         = { 2022 },
  pages        = { 15 },
  month        = { Mar },
  volume       = { 14 },
  number       = { 1 },
  day          = { 15 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-022-00594-8 },
  url          = { https://doi.org/10.1186/s13321-022-00594-8 }
}
```
