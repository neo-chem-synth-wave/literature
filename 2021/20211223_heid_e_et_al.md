# Overview
**Title:**
Influence of Template Size, Canonicalization, and Exclusivity for Retrosynthesis and Reaction Prediction Applications

**Authors:**
Heid, E., Liu, J., Aude, A., and Green, W.H.

**Publication Date:**
2021/12/23

**Publication Link:**
[ACS JCIM](https://pubs.acs.org/doi/10.1021/acs.jcim.1c01192)

**Alternative Publication Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/6153848aef08e609921c1707) |
[Official GitHub Repository](https://github.com/hesther/templatecorr)


# Abstract
Heuristic and machine learning models for rank-ordering reaction templates comprise an important basis for computer-aided organic synthesis regarding both product prediction and retrosynthetic pathway planning. Their viability relies heavily on the quality and characteristics of the underlying template database. 
With the advent of automated reaction and template extraction software and consequently the creation of template databases too large for manual curation, a data-driven approach to assess and improve the quality of template sets is needed. 
We therefore systematically studied the influence of template generality, canonicalization, and exclusivity on the performance of different template ranking models. 
We find that duplicate and nonexclusive templates, i.e., templates which describe the same chemical transformation on identical or overlapping sets of molecules, decrease both the accuracy of the ranking algorithm and the applicability of the respective top-ranked templates significantly. 
To remedy the negative effects of nonexclusivity, we developed a general and computationally efficient framework to deduplicate and hierarchically correct templates. 
As a result, performance improved considerably for both heuristic and machine learning template ranking models, as well as multistep retrosynthetic planning models. 
The canonicalization and correction code is made freely available.


# Citation
```
@article {heid2021,
  author       = { Esther Heid and Jiannan Liu and Andrea Aude and William H. Green },
  title        = { Influence of Template Size, Canonicalization, and Exclusivity for Retrosynthesis and Reaction Prediction Applications },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2022 },
  note         = { PMID: 34939786 },
  pages        = { 16-26 },
  volume       = { 62 },
  number       = { 1 },
  doi          = { 10.1021/acs.jcim.1c01192 },
  url          = { https://doi.org/10.1021/acs.jcim.1c01192 },
  eprint       = { https://doi.org/10.1021/acs.jcim.1c01192 }
}
```
