# Overview
**Title:**
Molecular Transformer: A Model for Uncertainty-Calibrated Chemical Reaction Prediction

**Authors:**
Schwaller, P., Laino, T., Gaudin, T., Bolgar, P., Hunter, C.A., Bekas, C., and Lee, A.A. |
Schwaller, P. et al.

**Publication Date:**
2019/08/30

**Link:**
[ACS Central Science](https://pubs.acs.org/doi/full/10.1021/acscentsci.9b00576)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/1811.02633) |
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c74238702a9b56bc18a3fb) |
[GitHub](https://github.com/pschwllr/MolecularTransformer) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC6764164) |
[ResearchGate](https://www.researchgate.net/publication/328800945_Molecular_Transformer_for_Chemical_Reaction_Prediction_and_Uncertainty_Estimation)

**Tags:**
single-step-synthesis, template-free


# Abstract
Organic synthesis is one of the key stumbling blocks in medicinal chemistry.
A necessary yet unsolved step in planning synthesis is solving the forward problem: Given reactants and reagents, predict the products.
Similar to other work, we treat reaction prediction as a machine translation problem between simplified molecular-input line-entry system (SMILES) strings (a text-based representation) of reactants, reagents, and the products.
We show that a multihead attention Molecular Transformer model outperforms all algorithms in the literature, achieving a top-1 accuracy above 90% on a common benchmark data set.
Molecular Transformer makes predictions by inferring the correlations between the presence and absence of chemical motifs in the reactant, reagent, and product present in the data set.
Our model requires no handcrafted rules and accurately predicts subtle chemical transformations.
Crucially, our model can accurately estimate its own uncertainty, with an uncertainty score that is 89% accurate in terms of classifying whether a prediction is correct.
Furthermore, we show that the model is able to handle inputs without a reactant–reagent split and including stereochemistry, which makes our method universally applicable.


# Citation
```
@article {20190830_schwaller_p_et_al,
  author       = { Philippe Schwaller and Teodoro Laino and Théophile Gaudin and Peter Bolgar and Christopher A. Hunter and Costas Bekas and Alpha A. Lee },
  title        = { Molecular Transformer: A Model for Uncertainty-Calibrated Chemical Reaction Prediction },
  journal      = { ACS Central Science },
  year         = { 2019 },
  note         = { PMID: 31572784 },
  pages        = { 1572-1583 },
  volume       = { 5 },
  number       = { 9 },
  doi          = { 10.1021/acscentsci.9b00576 },
  url          = { https://doi.org/10.1021/acscentsci.9b00576 },
  eprint       = { https://doi.org/10.1021/acscentsci.9b00576 }
}
```
