# Overview
**Title:**
Substructure-based Neural Machine Translation for Retrosynthetic Prediction

**Authors:**
Ucak, U.V., Kang, T., Ko, J., and Lee, J.

**Publication Date:**
2021/01/11

**Publication Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00482-z)

**Alternative Publication Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c74ea0f96a00c432287b14) |
[Official GitHub Repository](https://github.com/knu-chem-lcbc/fragment_based_retrosynthesis)


# Abstract
With the rapid improvement of machine translation approaches, neural machine translation has started to play an important role in retrosynthesis planning, which finds reasonable synthetic pathways for a target molecule. 
Previous studies showed that utilizing the sequence-to-sequence frameworks of neural machine translation is a promising approach to tackle the retrosynthetic planning problem. 
In this work, we recast the retrosynthetic planning problem as a language translation problem using a template-free sequence-to-sequence model. 
The model is trained in an end-to-end and a fully data-driven fashion. 
Unlike previous models translating the SMILES strings of reactants and products, we introduced a new way of representing a chemical reaction based on molecular fragments. 
It is demonstrated that the new approach yields better prediction results than current state-of-the-art computational methods. 
The new approach resolves the major drawbacks of existing retrosynthetic methods such as generating invalid SMILES strings. 
Specifically, our approach predicts highly similar reactant molecules with an accuracy of 57.7%. In addition, our method yields more robust predictions than existing methods.


# Citation
```
@article {ucak2021,
  author       = { Umit V Ucak and Taek Kang and Junsu Ko and Juyong Lee },
  title        = { Substructure-based neural machine translation for retrosynthetic prediction },
  journal      = { J. Cheminform. },
  year         = { 2021 },
  pages        = { 4 },
  month        = { jan },
  volume       = { 13 },
  number       = { 1 },
  publisher    = { Springer Science and Business Media LLC },
  keywords     = { Attention; Neural machine translation; Retrosynthesis planning;
               Seq-to-seq },
  copyright    = { http://creativecommons.org/licenses/by/4.0/ },
  language     = { en }
}
```
