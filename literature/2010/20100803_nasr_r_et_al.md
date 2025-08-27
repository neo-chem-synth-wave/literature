# Overview
**Title:**
Hashing Algorithms and Data Structures for Rapid Searches of Fingerprint Vectors

**Authors:**
Nasr, R., Hirschberg, D.S., and Baldi, P. |
Nasr, R. et al.

**Publication Date:**
2010/08/03

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/ci100132g)

**Alternative Links:**
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC2926297/)

**Starred:**
False

**Tags:**
compound-descriptor, fingerprint


# Abstract
In many large chemoinformatics database systems, molecules are represented by long binary fingerprint vectors whose components record the presence or absence of particular functional groups or combinatorial features.
To speed up database searches, we propose to add to each fingerprint a short signature integer vector of length M.
For a given fingerprint, the i component of the signature vector counts the number of 1-bits in the fingerprint that fall on components congruent to i modulo M.
Given two signatures, we show how one can rapidly compute a bound on the Jaccard−Tanimoto similarity measure of the two corresponding fingerprints, using the intersection bound.
Thus, these signatures allow one to significantly prune the search space by discarding molecules associated with unfavorable bounds.
Analytical methods are developed to predict the resulting amount of pruning as a function of M.
Data structures combining different values of M are also developed together with methods for predicting the optimal values of M for a given implementation.
Simulations using a particular implementation show that the proposed approach leads to a 1 order of magnitude speedup over a linear search and a 3-fold speedup over a previous implementation.
All theoretical results and predictions are corroborated by large-scale simulations using molecules from the ChemDB.
Several possible algorithmic extensions are discussed.


# Citation
```
@article {nasr2010a,
  author       = { Ramzi Nasr and Daniel S. Hirschberg and Pierre Baldi },
  title        = { Hashing Algorithms and Data Structures for Rapid Searches of Fingerprint Vectors },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2010 },
  note         = { PMID: 20681581 },
  pages        = { 1358-1368 },
  volume       = { 50 },
  number       = { 8 },
  doi          = { 10.1021/ci100132g },
  url          = { https://doi.org/10.1021/ci100132g },
  eprint       = { https://doi.org/10.1021/ci100132g }
}
```
