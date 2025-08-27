# Overview
**Title:**
Lossless Compression of Chemical Fingerprints Using Integer Entropy Codes Improves Storage and Retrieval

**Authors:**
Baldi, P., Benz, R.W., Hirschberg, D.S., and Swamidass, S.J. |
Baldi, P. et al.

**Publication Date:**
2007/10/30

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/ci700200n)

**Alternative Links:**
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC2536658) |
[ResearchGate](https://www.researchgate.net/publication/5879191_Lossless_Compression_of_Chemical_Fingerprints_Using_Integer_Entropy_Codes_Improves_Storage_and_Retrieval)

**Starred:**
False

**Tags:**
compound-descriptor, fingerprint


# Abstract
Many modern chemoinformatics systems for small molecules rely on large fingerprint vector representations, where the components of the vector record the presence or number of occurrences in the molecular graphs of particular combinatorial features, such as labeled paths or labeled trees.
These large fingerprint vectors are often compressed to much shorter fingerprint vectors using a lossy compression scheme based on a simple modulo procedure.
Here, we combine statistical models of fingerprints with integer entropy codes, such as Golomb and Elias codes, to encode the indices or the run lengths of the fingerprints.
After reordering the fingerprint components by decreasing frequency order, the indices are monotone-increasing and the run lengths are quasi-monotone-increasing, and both exhibit power-law distribution trends.
We take advantage of these statistical properties to derive new efficient, lossless, compression algorithms for monotone integer sequences: monotone value (MOV) coding and monotone length (MOL) coding.
In contrast to lossy systems that use 1024 or more bits of storage per molecule, we can achieve lossless compression of long chemical fingerprints based on circular substructures in slightly over 300 bits per molecule, close to the Shannon entropy limit, using a MOL Elias Gamma code for run lengths.
The improvement in storage comes at a modest computational cost.
Furthermore, because the compression is lossless, uncompressed similarity (e.g., Tanimoto) between molecules can be computed exactly from their compressed representations, leading to significant improvements in retrival performance, as shown on six benchmark data sets of druglike molecules.


# Citation
```
@article {baldi2007a,
  author       = { Pierre Baldi and Ryan W. Benz and Daniel S. Hirschberg and S. Joshua Swamidass },
  title        = { Lossless Compression of Chemical Fingerprints Using Integer Entropy Codes Improves Storage and Retrieval },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2007 },
  note         = { PMID: 17967006 },
  pages        = { 2098-2109 },
  volume       = { 47 },
  number       = { 6 },
  doi          = { 10.1021/ci700200n },
  url          = { https://doi.org/10.1021/ci700200n },
  eprint       = { https://doi.org/10.1021/ci700200n }
}
```
