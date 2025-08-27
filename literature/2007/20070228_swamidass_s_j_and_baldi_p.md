# Overview
**Title:**
Bounds and Algorithms for Fast Exact Searches of Chemical Fingerprints in Linear and Sublinear Time

**Authors:**
Swamidass, S.J. and Baldi, P.

**Publication Date:**
2007/02/28

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/ci600358f)

**Alternative Links:**
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC2527184) |
[ResearchGate](https://www.researchgate.net/publication/6479186_Bounds_and_Algorithms_for_Fast_Exact_Searches_of_Chemical_Fingerprints_in_Linear_and_Sub-Linear_Time)

**Starred:**
False

**Tags:**
compound-descriptor, fingerprint


# Abstract
Chemical fingerprints are used to represent chemical molecules by recording the presence or absence, or by counting the number of occurrences, of particular features or substructures, such as labeled paths in the 2D graph of bonds, of the corresponding molecule.
These fingerprint vectors are used to search large databases of small molecules, currently containing millions of entries, using various similarity measures, such as the Tanimoto or Tversky's measures and their variants.
Here, we derive simple bounds on these similarity measures and show how these bounds can be used to considerably reduce the subset of molecules that need to be searched.
We consider both the case of single-molecule and multiple-molecule queries, as well as queries based on fixed similarity thresholds or aimed at retrieving the top K hits.
We study the speedup as a function of query size and distribution, fingerprint length, similarity threshold, and database size |D| and derive analytical formulas that are in excellent agreement with empirical values.
The theoretical considerations and experiments show that this approach can provide linear speedups of one or more orders of magnitude in the case of searches with a fixed threshold, and achieve sublinear speedups in the range of O(|D|0.6) for the top K hits in current large databases.
This pruning approach yields subsecond search times across the 5 million compounds in the ChemDB database, without any loss of accuracy.


# Citation
```
@article {swamidass2007a,
  author       = { S. Joshua Swamidass and Pierre Baldi },
  title        = { Bounds and Algorithms for Fast Exact Searches of Chemical Fingerprints in Linear and Sublinear Time },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2007 },
  note         = { PMID: 17326616 },
  pages        = { 302-317 },
  volume       = { 47 },
  number       = { 2 },
  doi          = { 10.1021/ci600358f },
  url          = { https://doi.org/10.1021/ci600358f },
  eprint       = { https://doi.org/10.1021/ci600358f }
}
```
