# Overview
**Title:**
Molecular Transformer: A Model for Uncertainty-calibrated Chemical Reaction Prediction

**Authors:**
Schwaller, P., Laino, T., Gaudin, T., Bolgar, P., Hunter, C.A., Bekas, C., and Lee, A.A.

**Publication Date:**
2019/08/30

**Publication Link:**
[ACS Central Science](https://pubs.acs.org/doi/full/10.1021/acscentsci.9b00576)

**Alternative Publication Links:**
[arXiv](https://arxiv.org/abs/1811.02633) |
[Official GitHub Repository](https://github.com/pschwllr/MolecularTransformer)


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
@article{schwaller2019,
    author = "Schwaller, Philippe and Laino, Teodoro and Gaudin, Th{\'e}ophile and Bolgar, Peter and Hunter, Christopher A. and Bekas, Costas and Lee, Alpha A.",
    title = "Molecular Transformer: A Model for Uncertainty-Calibrated Chemical Reaction Prediction",
    journal = "ACS Central Science",
    volume = "5",
    number = "9",
    pages = "1572-1583",
    year = "2019",
    doi = "10.1021/acscentsci.9b00576",
    note = "PMID: 31572784",
    URL = "https://doi.org/10.1021/acscentsci.9b00576",
    eprint = "https://doi.org/10.1021/acscentsci.9b00576"
}
```
