# Overview
**Title:**
Substructure-Based Neural Machine Translation for Retrosynthetic Prediction

**Authors:**
Ucak, U.V., Kang, T., Ko, J., and Lee, J. |
Ucak, U.V. et al.

**Publication Date:**
2021/01/11

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00482-z)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c74ea0f96a00c432287b14) |
[GitHub](https://github.com/knu-chem-lcbc/fragment_based_retrosynthesis) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC7802345) |
[ResearchGate](https://www.researchgate.net/publication/348399059_Substructure-based_neural_machine_translation_for_retrosynthetic_prediction)

**Tags:**
single-step-retrosynthesis, template-free


# Abstract
With the rapid improvement of machine translation approaches, neural machine translation has started to play an important role in retrosynthesis planning, which finds reasonable synthetic pathways for a target molecule.
Previous studies showed that utilizing the sequence-to-sequence frameworks of neural machine translation is a promising approach to tackle the retrosynthetic planning problem.
In this work, we recast the retrosynthetic planning problem as a language translation problem using a template-free sequence-to-sequence model.
The model is trained in an end-to-end and a fully data-driven fashion.
Unlike previous models translating the SMILES strings of reactants and products, we introduced a new way of representing a chemical reaction based on molecular fragments.
It is demonstrated that the new approach yields better prediction results than current state-of-the-art computational methods.
The new approach resolves the major drawbacks of existing retrosynthetic methods such as generating invalid SMILES strings.
Specifically, our approach predicts highly similar reactant molecules with an accuracy of 57.7%.
In addition, our method yields more robust predictions than existing methods.


# Citation
```
@article {20210111_ucak_u_v_et_al,
  author       = { Umit V. Ucak and Taek Kang and Junsu Ko and Juyong Lee },
  title        = { Substructure-based neural machine translation for retrosynthetic prediction },
  journal      = { Journal of Cheminformatics },
  year         = { 2021 },
  pages        = { 4 },
  month        = { Jan },
  volume       = { 13 },
  number       = { 1 },
  day          = { 11 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-020-00482-z },
  url          = { https://doi.org/10.1186/s13321-020-00482-z }
}
```
