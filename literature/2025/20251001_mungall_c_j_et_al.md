# Overview
**Title:**
Chemical Classification Program Synthesis Using Generative Artificial Intelligence

**Authors:**
Mungall, C.J., Malik, A., Korn, D.R., Reese, J.T., O'Boyle, N.M., and Hastings, J. |
Mungall, C.J. et al.

**Publication Date:**
2025/10/01

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-025-01092-3)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2505.18470) |
[C3PO: CHEBI Classification Programs Ontology](https://chemkg.github.io/c3p) |
[GitHub](https://github.com/chemkg/c3p) |
[ResearchGate](https://www.researchgate.net/publication/396085932_Chemical_classification_program_synthesis_using_generative_artificial_intelligence)

**Tags:**
reaction-classification, c3po


# Abstract
Accurately classifying chemical structures is essential for cheminformatics and bioinformatics, including tasks such as identifying bioactive compounds of interest, screening molecules for toxicity to humans, finding non-organic compounds with desirable material properties, or organizing large chemical libraries for drug discovery or environmental monitoring.
However, manual classification is labor-intensive and difficult to scale to large chemical databases.
Existing automated approaches either rely on manually constructed classification rules, or are deep learning methods that lack explainability.
This work presents an approach that uses generative artificial intelligence to automatically write chemical classifier programs for classes in the Chemical Entities of Biological Interest (ChEBI) database.
These programs can be used for efficient deterministic run-time classification of SMILES structures, with natural language explanations.
The programs themselves constitute an explainable computable ontological model of chemical class nomenclature, which we call the ChEBI Chemical Class Program Ontology (C3PO).
We validated our approach against the ChEBI database, and compared our results against deep learning models and a naive SMARTS pattern based classifier.
C3PO outperforms the naive classifier, but does not reach the performance of state-of-the-art deep learning methods.
However, C3PO has a number of strengths that complement deep learning methods, including explainability and reduced data dependence.
C3PO can be used alongside deep learning classifiers to provide an explanation of the classification, where both methods agree.
The programs can be used as part of the ontology development process, and iteratively refined by expert human curators.


# Citation
```
@article {20251001_mungall_c_j_et_al,
  author       = { Christopher J. Mungall and Adnan Malik and Daniel R. Korn and Justin T. Reese and Noel M. O'Boyle and Janna Hastings },
  title        = { Chemical classification program synthesis using generative artificial intelligence },
  journal      = { Journal of Cheminformatics },
  year         = { 2025 },
  pages        = { 152 },
  month        = { Oct },
  volume       = { 17 },
  number       = { 1 },
  day          = { 01 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-025-01092-3 },
  url          = { https://doi.org/10.1186/s13321-025-01092-3 }
}
```
