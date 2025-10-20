# Overview
**Title:**
Prediction of Chemical Reaction Yields Using Deep Learning

**Authors:**
Schwaller, P., Vaucher, A.C., Laino, T., Reymond, J. |
Schwaller, P. et al.

**Publication Date:**
2021/08/31

**Link:**
[IOPScience Machine Learning: Science and Technology](https://iopscience.iop.org/article/10.1088/2632-2153/abc81d)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c750f2ee301c70b1c7a973) |
[GitHub](https://rxn4chemistry.github.io/rxn_yields) |
[ResearchGate](https://www.researchgate.net/publication/351320365_Prediction_of_chemical_reaction_yields_using_deep_learning)

**Tags:**
reaction-yield


# Abstract
Artificial intelligence is driving one of the most important revolutions in organic chemistry.
Multiple platforms, including tools for reaction prediction and synthesis planning based on machine learning, have successfully become part of the organic chemists’ daily laboratory, assisting in domain-specific synthetic problems.
Unlike reaction prediction and retrosynthetic models, the prediction of reaction yields has received less attention in spite of the enormous potential of accurately predicting reaction conversion rates.
Reaction yields models, describing the percentage of the reactants converted to the desired products, could guide chemists and help them select high-yielding reactions and score synthesis routes, reducing the number of attempts.
So far, yield predictions have been predominantly performed for high-throughput experiments using a categorical (one-hot) encoding of reactants, concatenated molecular fingerprints, or computed chemical descriptors.
Here, we extend the application of natural language processing architectures to predict reaction properties given a text-based representation of the reaction, using an encoder transformer model combined with a regression layer.
We demonstrate outstanding prediction performance on two high-throughput experiment reactions sets.
An analysis of the yields reported in the open-source USPTO data set shows that their distribution differs depending on the mass scale, limiting the data set applicability in reaction yields predictions.


# Citation
```
@article {20210831_schwaller_p_et_al,
  author       = { Philippe Schwaller and Alain C Vaucher and Teodoro Laino and Jean-Louis Reymond },
  title        = { Prediction of chemical reaction yields using deep learning },
  journal      = { Machine Learning: Science and Technology },
  year         = { 2021 },
  pages        = { 015016 },
  month        = { Mar },
  volume       = { 2 },
  number       = { 1 },
  doi          = { 10.1088/2632-2153/abc81d },
  url          = { https://doi.org/10.1088/2632-2153/abc81d },
  publisher    = { IOP Publishing }
}
```
