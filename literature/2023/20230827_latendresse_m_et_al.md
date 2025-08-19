# Overview
**Title:**
SynRoute: A Retrosynthetic Planning Software

**Authors:**
Latendresse, M., Malerich, J.P., Herson, J., Krummenacker, M., Szeto, J., Vu, V., Collins, N., and Madrid, P.B. |
Latendresse, M. et al.

**Publication Date:**
2023/08/27

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.3c00491)

**Alternative Links:**
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC10498441)

**Starred:**
False

**Tags:**
multi-step-retrosynthesis, synroute


# Abstract
Computer-assisted synthetic planning has seen major advancements that stem from the availability of large reaction databases and artificial intelligence methodologies.
SynRoute is a new retrosynthetic planning software tool that uses a relatively small number of general reaction templates, currently 263, along with a literature-based reaction database to find short, practical synthetic routes for target compounds.
For each reaction template, a machine learning classifier is trained using data from the Pistachio reaction database to predict whether new computer-generated reactions based on the template are likely to work experimentally in the laboratory.
This reaction generation methodology is used together with a vectorized Dijkstra-like search of top-scoring routes organized by synthetic strategies for easy browsing by a synthetic chemist.
SynRoute was able to find routes for an average of 83% of compounds based on selection of random subsets of drug-like compounds from the ChEMBL database. Laboratory evaluation of 12 routes produced by SynRoute, to synthesize compounds not from the previous random subsets, demonstrated the ability to produce feasible overall synthetic strategies for all compounds evaluated.


# Citation
```
@article {latendresse2023a,
  author       = { Mario Latendresse and Jeremiah P. Malerich and James Herson and Markus Krummenacker and Judy Szeto and Vi-Anh Vu and Nathan Collins and Peter B. Madrid },
  title        = { SynRoute: A Retrosynthetic Planning Software },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2023 },
  note         = { PMID: 37635298 },
  pages        = { 5484-5495 },
  volume       = { 63 },
  number       = { 17 },
  doi          = { 10.1021/acs.jcim.3c00491 },
  url          = { https://doi.org/10.1021/acs.jcim.3c00491 },
  eprint       = { https://doi.org/10.1021/acs.jcim.3c00491 }
}
```
