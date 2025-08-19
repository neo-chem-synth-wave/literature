# Overview
**Title:**
ORDerly: Data Sets and Benchmarks for Chemical Reaction Data

**Authors:**
Wigh, D.S., Arrowsmith, J., Pomberger, A., Felton, K.C., and Lapkin, A.A. |
Wigh, D.S. et al.

**Publication Date:**
2024/04/22

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/full/10.1021/acs.jcim.4c00292)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/64ca5d3e4a3f7d0c0d78ca42) |
[GitHub](https://github.com/sustainable-processes/orderly) |
[PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11094788) |
[ResearchGate](https://www.researchgate.net/publication/372903934_ORDerly_Datasets_and_benchmarks_for_chemical_reaction_data)

**Starred:**
False

**Tags:**
data-source, orderly


# Abstract
Machine learning has the potential to provide tremendous value to life sciences by providing models that aid in the discovery of new molecules and reduce the time for new products to come to market.
Chemical reactions play a significant role in these fields, but there is a lack of high-quality open-source chemical reaction data sets for training machine learning models.
Herein, we present ORDerly, an open-source Python package for the customizable and reproducible preparation of reaction data stored in accordance with the increasingly popular Open Reaction Database (ORD) schema.
We use ORDerly to clean United States patent data stored in ORD and generate data sets for forward prediction, retrosynthesis, as well as the first benchmark for reaction condition prediction.
We train neural networks on data sets generated with ORDerly for condition prediction and show that data sets missing key cleaning steps can lead to silently overinflated performance metrics.
Additionally, we train transformers for forward and retrosynthesis prediction and demonstrate how non-patent data can be used to evaluate model generalization.
By providing a customizable open-source solution for cleaning and preparing large chemical reaction data, ORDerly is poised to push forward the boundaries of machine learning applications in chemistry.


# Citation
```
@article {wigh2024a,
  author       = { Daniel S. Wigh and Joe Arrowsmith and Alexander Pomberger and Kobi C. Felton and Alexei A. Lapkin },
  title        = { ORDerly: Data Sets and Benchmarks for Chemical Reaction Data },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2024 },
  note         = { PMID: 38648077 },
  pages        = { 3790-3798 },
  volume       = { 64 },
  number       = { 9 },
  doi          = { 10.1021/acs.jcim.4c00292 },
  url          = { https://doi.org/10.1021/acs.jcim.4c00292 },
  eprint       = { https://doi.org/10.1021/acs.jcim.4c00292 }
}
```
