# Overview
**Title:**
SynTemp: Efficient Extraction of Graph-Based Reaction Rules From Large-Scale Reaction Databases

**Authors:**
Phan, T., Weinbauer, K., Laffitte, M.E.G., Pan, Y., Merkle, D., Andersen, J.L., Fagerberg, R., Flamm, C., and Stadler, P.F. |
Phan, T. et al.

**Publication Date:**
2025/02/28

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.4c01795)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/66f677b751558a15ef4cf5f7) |
[GitHub](https://github.com/TieuLongPhan/SynTemp) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC11938280) |

**Tags:**
reaction-template-extraction, syn-temp


# Abstract
Reaction templates are graphs that represent the reaction center as well as the surrounding context in order to specify salient features of chemical reactions.
They are subgraphs of imaginary transition states, which are equivalent to double pushout graph rewriting rules and thus can be applied directly to predict reaction outcomes at the structural formula level.
We introduce here SynTemp, a framework designed to extract and hierarchically cluster reaction templates from large-scale reaction data repositories.
Rule inference is implemented as a robust graph-theoretic approach, which first computes an atom–atom mapping (AAM) as a consensus over partial predictions from multiple state-of-the-art tools and then augments the raw AAM by mechanistically relevant hydrogen atoms and extracts the reactions center extended by relevant context.
SynTemp achieves an exceptional accuracy of 99.5% and a success rate of 71.23% in obtaining AAMs on the chemical reaction dataset.
Hierarchical clustering of the extended reaction centers based on topological features results in a library of 311 transformation rules explaining 86% of the reaction dataset.


# Citation
```
@article {20250228_phan_t_et_al,
  author       = { Tieu-Long Phan and Klaus Weinbauer and Marcos E. González Laffitte and Yingjie Pan and Daniel Merkle and Jakob L. Andersen and Rolf Fagerberg and Christoph Flamm and Peter F. Stadler },
  title        = { SynTemp: Efficient Extraction of Graph-Based Reaction Rules from Large-Scale Reaction Databases },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2025 },
  note         = { PMID: 40019281 },
  pages        = { 2882-2896 },
  volume       = { 65 },
  number       = { 6 },
  doi          = { 10.1021/acs.jcim.4c01795 },
  url          = { https://doi.org/10.1021/acs.jcim.4c01795 },
  eprint       = { https://doi.org/10.1021/acs.jcim.4c01795 }
}
```
