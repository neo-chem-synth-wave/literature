# (20190830, Schwaller, P. et al.) Molecular Transformer: A Model for Uncertainty-calibrated Chemical Reaction Prediction

Tags: single-step-synthesis, template-free

## Publication Overview

| **Title:**  | Molecular Transformer: A Model for Uncertainty-calibrated Chemical Reaction Prediction |
| --- | --- |
| **Authors:**  | Philippe Schwaller, Teodoro Laino, Théophile Gaudin, Peter Bolgar, Christopher A. Hunter,
Costas Bekas, Alpha A. Lee |
| Publication Date**:**  | 2019/08/30 |
| Publication Links: | [**ACS Central Science**](https://pubs.acs.org/doi/full/10.1021/acscentsci.9b00576) |
| Alternative Links: | [**arXiv](https://arxiv.org/abs/1811.02633) | [ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c74238702a9b56bc18a3fb)** |
| Code Links: | [**Official GitHub Repository**](https://github.com/pschwllr/MolecularTransformer) |

## Publication Abstract

<aside>
ℹ️ Organic synthesis is one of the key stumbling blocks in medicinal chemistry. A necessary yet unsolved step in planning synthesis is solving the forward problem: Given reactants and reagents, predict the products. Similar to other work, we treat reaction prediction as a machine translation problem between simplified molecular-input line-entry system (SMILES) strings (a text-based representation) of reactants, reagents, and the products. We show that a multihead attention Molecular Transformer model outperforms all algorithms in the literature, achieving a top-1 accuracy above 90% on a common benchmark data set. Molecular Transformer makes predictions by inferring the correlations between the presence and absence of chemical motifs in the reactant, reagent, and product present in the data set. Our model requires no handcrafted rules and accurately predicts subtle chemical transformations. Crucially, our model can accurately estimate its own uncertainty, with an uncertainty score that is 89% accurate in terms of classifying whether a prediction is correct. Furthermore, we show that the model is able to handle inputs without a reactant–reagent split and including stereochemistry, which makes our method universally applicable.

</aside>