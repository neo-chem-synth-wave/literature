# Overview
**Title:**
Comparing Structural Fingerprints using a Literature-based Similarity Benchmark

**Authors:**
O’Boyle, N.M., and Sayle, R.A.

**Publication Date:**
2016/07/05

**Publication Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-016-0148-0)

**Alternative Publication Links:**
[ResearchGate](https://www.researchgate.net/publication/304914634_Comparing_structural_fingerprints_using_a_literature-based_similarity_benchmark) |
[GitHub Repository](https://github.com/nextmovesoftware/similaritybenchmark)


# Abstract
Background 

The concept of molecular similarity is one of the central ideas in cheminformatics, despite the fact that it is ill-defined and rather difficult to assess objectively. 
Here we propose a practical definition of molecular similarity in the context of drug discovery: molecules A and B are similar if a medicinal chemist would be likely to synthesise and test them around the same time as part of the same medicinal chemistry program. 
The attraction of such a definition is that it matches one of the key uses of similarity measures in early-stage drug discovery. 
If we make the assumption that molecules in the same compound activity table in a medicinal chemistry paper were considered similar by the authors of the paper, we can create a dataset of similar molecules from the medicinal chemistry literature. 
Furthermore, molecules with decreasing levels of similarity to a reference can be found by either ordering molecules in an activity table by their activity, or by considering activity tables in different papers which have at least one molecule in common.
Results 

Using this procedure with activity data from ChEMBL, we have created two benchmark datasets for structural similarity that can be used to guide the development of improved measures. 
Compared to similar results from a virtual screen, these benchmarks are an order of magnitude more sensitive to differences between fingerprints both because of their size and because they avoid loss of statistical power due to the use of mean scores or ranks. 
We measure the performance of 28 different fingerprints on the benchmark sets and compare the results to those from the Riniker and Landrum (J Cheminf 5:26, 2013. doi:10.1186/1758-2946-5-26) ligand-based virtual screening benchmark.
Conclusions 

Extended-connectivity fingerprints of diameter 4 and 6 are among the best performing fingerprints when ranking diverse structures by similarity, as is the topological torsion fingerprint. 
However, when ranking very close analogues, the atom pair fingerprint outperforms the others tested. 
When ranking diverse structures or carrying out a virtual screen, we find that the performance of the ECFP fingerprints significantly improves if the bit-vector length is increased from 1024 to 16,384.
# Citation
```
@article{o’boyle2016,
author="O'Boyle, Noel M. and Sayle, Roger A.",
title="Comparing structural fingerprints using a literature-based similarity benchmark",
journal="Journal of Cheminformatics",
year="2016",
month="Jul",
day="05",
volume="8",
number="1",
pages="36",
issn="1758-2946",
doi="10.1186/s13321-016-0148-0",
url="https://doi.org/10.1186/s13321-016-0148-0"
}
```

