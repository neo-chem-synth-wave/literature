# Overview
**Title:**
Quantitative Interpretation Explains Machine Learning Models for Chemical Reaction Prediction and Uncovers Bias

**Authors:**
Kovács, D.P., McCorkindale, W., and Lee, A.A. |
Kovács, D.P. et al.

**Publication Date:**
2021/03/16

**Link:**
[Nature Communications](https://www.nature.com/articles/s41467-021-21895-w)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c7509f567dfe0f14ec58cb) |
[GitHub](https://github.com/davkovacs/MTExplainer) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC7966799) |
[ResearchGate](https://www.researchgate.net/publication/350097666_Quantitative_interpretation_explains_machine_learning_models_for_chemical_reaction_prediction_and_uncovers_bias) |
[University of Cambridge Apollo Repository](https://www.repository.cam.ac.uk/items/e1934cf3-341b-434a-9106-3d95d1a48139)

**Starred:**
False

**Tags:**
single-step-synthesis, analysis


# Abstract
Organic synthesis remains a major challenge in drug discovery.
Although a plethora of machine learning models have been proposed as solutions in the literature, they suffer from being opaque black-boxes.
It is neither clear if the models are making correct predictions because they inferred the salient chemistry, nor is it clear which training data they are relying on to reach a prediction.
This opaqueness hinders both model developers and users.
In this paper, we quantitatively interpret the Molecular Transformer, the state-of-the-art model for reaction prediction.
We develop a framework to attribute predicted reaction outcomes both to specific parts of reactants, and to reactions in the training set.
Furthermore, we demonstrate how to retrieve evidence for predicted reaction outcomes, and understand counterintuitive predictions by scrutinising the data.
Additionally, we identify Clever Hans predictions where the correct prediction is reached for the wrong reason due to dataset bias.
We present a new debiased dataset that provides a more realistic assessment of model performance, which we propose as the new standard benchmark for comparing reaction prediction models.


# Citation
```
@article {kovacs2021a,
  author       = { Dávid Péter Kovács and William McCorkindale and Alpha A. Lee },
  title        = { Quantitative interpretation explains machine learning models for chemical reaction prediction and uncovers bias },
  journal      = { Nature Communications },
  year         = { 2021 },
  pages        = { 1695 },
  month        = { Mar },
  volume       = { 12 },
  number       = { 1 },
  day          = { 16 },
  issn         = { 2041-1723 },
  doi          = { 10.1038/s41467-021-21895-w },
  url          = { https://doi.org/10.1038/s41467-021-21895-w }
}
```
