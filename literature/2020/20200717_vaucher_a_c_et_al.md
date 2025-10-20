# Overview
**Title:**
Automated Extraction of Chemical Synthesis Actions From Experimental Procedures

**Authors:**
Vaucher, A.C., Zipoli, F., Geluykens, J., Nair, V.H., Schwaller, P., and Laino, T. |
Vaucher, A.C. et al.

**Publication Date:**
2020/07/17

**Link:**
[Nature Communications](https://www.nature.com/articles/s41467-020-17266-6)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c749fbee301c10e1c79b75) |
[GitHub (Training of the Models)](https://github.com/rxn4chemistry/paragraph2actions) |
[GitHub (Trained Models)](https://github.com/rxn4chemistry/rxn4chemistry) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC7367864)

**Tags:**
reaction-extraction


# Abstract
Experimental procedures for chemical synthesis are commonly reported in prose in patents or in the scientific literature.
The extraction of the details necessary to reproduce and validate a synthesis in a chemical laboratory is often a tedious task requiring extensive human intervention.
We present a method to convert unstructured experimental procedures written in English to structured synthetic steps (action sequences) reflecting all the operations needed to successfully conduct the corresponding chemical reactions.
To achieve this, we design a set of synthesis actions with predefined properties and a deep-learning sequence to sequence model based on the transformer architecture to convert experimental procedures to action sequences.
The model is pretrained on vast amounts of data generated automatically with a custom rule-based natural language processing approach and refined on manually annotated samples.
Predictions on our test set result in a perfect (100%) match of the action sequence for 60.8% of sentences, a 90% match for 71.3% of sentences, and a 75% match for 82.4% of sentences.


# Citation
```
@article {20200717_vaucher_a_c_et_al,
  author       = { Alain C. Vaucher and Federico Zipoli and Joppe Geluykens and Vishnu H. Nair and Philippe Schwaller and Teodoro Laino },
  title        = { Automated extraction of chemical synthesis actions from experimental procedures },
  journal      = { Nature Communications },
  year         = { 2020,
  pages        = { 3601 },
  month        = { Jul },
  volume       = { 11 },
  number       = { 1 },
  day          = { 17 },
  issn         = { 2041-1723 },
  doi          = { 10.1038/s41467-020-17266-6 },
  url          = { https://doi.org/10.1038/s41467-020-17266-6 }
}
```
