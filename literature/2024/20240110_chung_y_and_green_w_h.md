# Overview
**Title:**
Machine Learning From Quantum Chemistry to Predict Experimental Solvent Effects on Reaction Rates

**Authors:**
Chung, Y. and Green, W.H.

**Publication Date:**
2024/01/10

**Link:**
[RSC Chemical Science](https://pubs.rsc.org/en/content/articlelanding/2024/sc/d3sc05353a)

**Alternative Links:**
[DSpace@MIT](https://dspace.mit.edu/handle/1721.1/156713) |
[GitHub](https://github.com/yunsiechung/chemprop/tree/RxnSolvKSE_ML) |
[ResearchGate](https://www.researchgate.net/publication/377314920_Machine_learning_from_quantum_chemistry_to_predict_experimental_solvent_effects_on_reaction_rates)

**Tags:**
reaction-solvent-effects


# Abstract
Fast and accurate prediction of solvent effects on reaction rates are crucial for kinetic modeling, chemical process design, and high-throughput solvent screening.
Despite the recent advance in machine learning, a scarcity of reliable data has hindered the development of predictive models that are generalizable for diverse reactions and solvents.
In this work, we generate a large set of data with the COSMO-RS method for over 28,000 neutral reactions and 295 solvents and train a machine learning model to predict the solvation free energy and solvation enthalpy of activation (ΔΔG‡solv, ΔΔH‡solv) for a solution phase reaction.
On unseen reactions, the model achieves mean absolute errors of 0.71 and 1.03 kcal mol−1 for ΔΔG‡solv and ΔΔH‡solv, respectively, relative to the COSMO-RS calculations.
The model also provides reliable predictions of relative rate constants within a factor of 4 when tested on experimental data.
The presented model can provide nearly instantaneous predictions of kinetic solvent effects or relative rate constants for a broad range of neutral closed-shell or free radical reactions and solvents only based on atom-mapped reaction SMILES and solvent SMILES strings.


# Citation
```
@article {20240110_chung_y_and_green_w_h,
  author       = { Yunsie Chung and William H. Green },
  title        = { Machine learning from quantum chemistry to predict experimental solvent effects on reaction rates },
  journal      = { Chem. Sci. },
  year         = { 2024 },
  pages        = { 2410-2424 },
  volume       = { 15 },
  issue        = { 7 },
  publisher    = { The Royal Society of Chemistry },
  doi          = { 10.1039/D3SC05353A },
  url          = { https://dx.doi.org/10.1039/D3SC05353A }
}
```
